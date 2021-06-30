# Configuring Smartwatches over ADB (Android Debug Bridge)
Command line tool to remove packages on a smartwatch according to a list. The connection between host and target (Smartwatch) is established via WLAN.



## Requirements
ADB (Android Debug Bridge) must be present on the host system, it is included in the Android SDK Platform-Tools. The target system (smartwatch) must have activated developer mode and allow debugging via WLAN. During the first connection from the host to the target, a question appears on the target as to whether debugging should be permitted. This must be confirmed with "Yes" or even better "Yes, always from this device".

Since the host and target (Smartwatch) are connected to each other via WLAN, they must both be in the same network.

- [Android SDK Platform-Tools](https://developer.android.com/studio/releases/platform-tools)
- [Python 3.x](https://www.python.org/downloads/)
- [argparse](https://pypi.python.org/pypi/argparse)


## Usage

# Command line arguments






## Roadmap
- [x] Create script with base functions
- [x] Elaborate package list for TicWatch 3
- [ ] Elaborate package list for other watches
- [ ] Pass multiple IP adresses for batch configuration


