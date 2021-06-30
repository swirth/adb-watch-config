# Configuring Smartwatches over ADB (Android Debug Bridge)
Command line tool to remove packages on a smartwatch according to a list. The connection between host and target (smartwatch) is established via WLAN.



## Requirements
ADB (Android Debug Bridge) must be present on the host system, it is included in the Android SDK Platform-Tools. The target system (smartwatch) must have activated developer mode and allow debugging via WLAN. During the first connection from the host to the target, a question appears on the target as to whether debugging should be permitted. This must be confirmed with "Yes" or even better "Yes, always from this device".

Since the host and target (Smartwatch) are connected to each other via WLAN, they must both be in the same network.

- [Android SDK Platform-Tools](https://developer.android.com/studio/releases/platform-tools)
- [Python 3.x](https://www.python.org/downloads/)
- [argparse](https://pypi.python.org/pypi/argparse)



## Usage
The script and the package list can be copied to a local directory on the host and be executed via the terminal.

`python3 adb-remove-apps.py 192.168.1.127 remove-list-ticwatch-3.txt `


### Command line arguments
```
usage: adb-remove-apps.py [-h] [-v] ip file

positional arguments:
  ip             IP address of the target
  file           File containing list of packages to be uninstalled

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```

### Create custom list
You can also create and use your own package list. In this case it makes sense to export a list of all installed packages on the target device, which can then be adapted.

To do this, a connection to the device must first be established, where `192.168.1.127` is the ip address of the target:

`adb connect 192.168.1.127`

The package list can then be exported:

`adb shell pm list packages | sort > export.txt`

All entries in the list have the prefix package, which must be removed:

`sed -i -e 's/package://g' export.txt `

All packages in the list are going to be uninstalled. Therefor all packages which shall remain on the device have to be removed from the list. The list then has the following exemplary entries:

```
com.google.android.clockwork.flashlight
com.google.android.clockwork.nfc
com.google.android.deskclock
com.google.android.apps.fitness
...
```

### Expected behavior and exceptions
The script exports a list of the remaining packages on the target device into the file `installed_packages.txt`. The script checks whether all packages according to the list have been removed. If so, it will be displayed as a success message:

`All packages cleared and uninstalled`

It is possible that packages cannot be uninstalled correctly. The script recognizes which packages these are and exports them to the file `uninstalled_packages.txt`. A corresponding message will be displayed:

`2 package(s) still installed, check output file 'uninstalled_packages.txt' for details`







## Roadmap
- [x] Create script with base functions
- [x] Elaborate package list for TicWatch 3
- [ ] Make export of installed packages optional/controlled by argument
- [ ] Elaborate package list for other watches
- [ ] Pass multiple IP adresses for batch configuration
- [ ] Create pip installable package


