# pico_w-wifi-controller-data
# can dynamically grap first available IPV4: ip4addr_ntoa(netif_ip4_addr(netif_list)), TCP_PORT)
##Bluetooth Directory
This directory contains GATT (Generic Attribute Profile) Bluetooth Low Energy (BLE) support for Pico_W. You can find implementations and examples related to Bluetooth communication in this directory.

##Usage
Provide brief instructions on how to use the Bluetooth features in this directory.

##TCP Directory
This directory includes implementations for TCP server communication with Pico_W. You can find TCP server-related code and examples here.

##Usage
Explain how to set up and use the TCP server functionalities provided in this directory.

##UDP Directory
In this directory, you'll find code related to UDP communication. The UDP broadcaster address can be changed to a static IP and port to send UDP packets to a Raspberry Pi 4 or any other specific destination.

##Usage
Provide instructions on how to modify the broadcaster address and use UDP functionalities in this directory.

##Miscellaneous Files
CMake
Explain the purpose of CMake in your project. CMake is a tool designed to build, test, and package software. It provides a simple syntax to specify build parameters and dependencies. In this project, CMake is used to manage the build process for the Bluetooth, TCP, and UDP directories.

##Makefile
A Makefile is a script used for building and compiling a project. It contains a set of rules and dependencies that describe how the project should be built. In this project, Makefiles are utilized to automate the compilation process, making it easier to build the project without having to remember complex build commands.

Controller wireless access
cmake -DPICO_BOARD=pico_w -DWIFI_SSID="RPcontroller" -DWIFI_PASSWORD="RPcontroller" ..


```makefile
# Makefile for pico_w-wifi-controller-data project

# Directories
BLUETOOTH_DIR = Bluetooth
TCP_DIR = TCP
UDP_DIR = UDP

# Targets
all: bluetooth tcp udp

bluetooth:
	@echo "Building Bluetooth components..."
	@$(MAKE) -C $(BLUETOOTH_DIR)

tcp:
	@echo "Building TCP components..."
	@$(MAKE) -C $(TCP_DIR)

udp:
	@echo "Building UDP components..."
	@$(MAKE) -C $(UDP_DIR)

# Clean
clean:
	@echo "Cleaning Bluetooth components..."
	@$(MAKE) clean -C $(BLUETOOTH_DIR)
	@echo "Cleaning TCP components..."
	@$(MAKE) clean -C $(TCP_DIR)
	@echo "Cleaning UDP components..."
	@$(MAKE) clean -C $(UDP_DIR)

# Usage instructions
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all        - Build Bluetooth, TCP, and UDP components"
	@echo "  bluetooth  - Build Bluetooth components"
	@echo "  tcp        - Build TCP components"
	@echo "  udp        - Build UDP components"
	@echo "  clean      - Clean built components"
```

In this Makefile:

- The `all` target builds Bluetooth, TCP, and UDP components when you run `make`.
- Each component (Bluetooth, TCP, and UDP) has its own target, allowing you to build specific components individually.
- The `clean` target cleans the built components in each directory.
- Added a `help` target to provide usage instructions when you run `make help`.
