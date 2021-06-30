#!/usr/bin/python3
#coding:utf-8

import os
import time
import subprocess
import argparse


# Definition of Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("ip", type=str, help="IP address of the target")
parser.add_argument("file", type=str, help="File containing list of packages to be uninstalled")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()





# Function to check valid IP address
def valid_ip(address):
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False


	


# Start script here

if (valid_ip(args.ip)):
    if args.verbose:
        print("Connect device with IP address {} ".format(args.ip))
else:
    print("IP addresse {} is not valid".format(args.ip))
    exit()

    

# start adb and connect to device
try:
    cmd = "adb connect {}".format(args.ip)
    if args.verbose:
        adb = subprocess.run(cmd, shell=True, timeout=5)
    else:
        adb = subprocess.run(cmd, shell=True, timeout=5, stdout=subprocess.DEVNULL)
        
except subprocess.TimeoutExpired as e:
    print("Timeout: Error connecting to device")
    exit()
    
    
try:
    cmd = "adb -s {} shell getprop ro.serialno".format(args.ip)
    if args.verbose:
        adbdev = subprocess.run(cmd, shell=True, timeout=5)
    else:
        adbdev = subprocess.run(cmd, shell=True, timeout=5, stdout=subprocess.DEVNULL)

except subprocess.TimeoutExpired:
    print("Timeout: Error connecting to device")
    exit()


if adbdev.returncode==0:
    if args.verbose:
        print("Target device is ready")

else:
    print("Error connecting to device")
    exit()
    
    

# check if file is valid	
if (os.path.exists(args.file)):
    if args.verbose:
        print("File {} exists".format(args.file))
else:
    print("File {} not found".format(args.file))
    exit()
    

# clear and uninstall packages
try:
    with open(args.file, 'r') as f:
        for line in f:
            cmd = 'adb shell pm clear %s' % line
            sp = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, timeout=5, text=True)
            if args.verbose:
                print('Clear package', line.rstrip(), '... ', end='')
                print(sp.stdout, end='')
		
            cmd = 'adb shell pm uninstall --user 0 %s' % line
            sp = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, timeout=5, text=True)
            if args.verbose:
                print('Uninstall package', line.rstrip(), '... ', end='')
                print(sp.stdout, end='') 
                print()
                
except subprocess.TimeoutExpired :
    print("Timeout: Error loading package list from device")
    exit()
    
except EnvironmentError:
    print("Error loading file list")
    exit()




# export installed packages as list and compare to uninstall list
try:
    cmd = "adb -s {} shell pm list packages | sort > installed_packages.txt".format(args.ip)
    subprocess.run(cmd, shell=True, timeout=5, stdout=subprocess.DEVNULL)
    cmd = "sed -i -e 's/package://g' installed_packages.txt"
    subprocess.run(cmd, shell=True, timeout=5, stdout=subprocess.DEVNULL)
    if args.verbose:
        print("List of installed packages exported in file \'installed_packages.txt\'")
    
except subprocess.TimeoutExpired :
    print("Timeout: Error loading package list from device")
    exit()
    
except EnvironmentError:
    print("Error loading package list from device")
    exit()


    
    
with open(args.file, 'r') as file1:
    with open('installed_packages.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

if len(same)==0:
    print("All packages cleared and uninstalled")
else:
    print("{} package(s) still installed, check output file \'uninstalled_packages.txt\' for details".format(len(same)))
    with open('unistalled_packages.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)























