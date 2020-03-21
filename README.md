# Packet sniffer

- Sniff all the packet on the choosen interface

# Tech part

This script uses a number of open source projects to work properly:

- scapy
- argparse
- scapy.layers
- python

### Installation

```
pip install scapy 
pip install argparse
pip install scapylayers
```

### Usage

```
usage: main.py [-h] [-i INTERFACE]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --ip INTERFACE
                        Interface of the network (ex: enO / ethO)
```

```
python main.py -i en0
```

### Pictures

[![N|Solid](https://i.imgur.com/4VXFkQn.png)](https://i.imgur.com/4VXFkQn.png)

@LasCC
