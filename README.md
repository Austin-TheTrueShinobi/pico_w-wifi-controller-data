```makefile
# Makefile for pico_w-wifi-controller-data project

# Project Description:
# This Makefile automates the build process for the pico_w-wifi-controller-data project. The project comprises
# three main components: Bluetooth, TCP, and UDP functionalities. The Bluetooth directory contains GATT (Generic
# Attribute Profile) Bluetooth Low Energy (BLE) support for Pico_W, including implementations and examples related
# to Bluetooth communication. The TCP directory includes implementations for TCP server communication with Pico_W,
# providing relevant code and examples. The UDP directory contains code for UDP communication, allowing users to
# modify the broadcaster address to send UDP packets to specific destinations, such as a Raspberry Pi 4.

# Usage Instructions:
# The project provides detailed instructions for each component:
# - Bluetooth: Users can find implementations and examples related to Bluetooth communication in the Bluetooth directory.
# - TCP: Instructions on setting up and using TCP server functionalities are available in the TCP directory.
# - UDP: Users can modify the broadcaster address and utilize UDP functionalities in the UDP directory.

# Miscellaneous Files:
# CMake: CMake is used in this project to manage the build process for the Bluetooth, TCP, and UDP directories. It is
# a versatile tool designed for building, testing, and packaging software, simplifying the specification of build parameters
# and dependencies.
# Makefile: This Makefile serves as a script for building and compiling the project. It contains rules and dependencies
# describing how the project should be built, automating the compilation process and eliminating the need for complex build commands.

# Directory Structure:
BLUETOOTH_DIR = Bluetooth
TCP_DIR = TCP
UDP_DIR = UDP

# Targets:
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

# Clean:
# The clean target allows users to remove built components, ensuring a clean build environment.
clean:
	@echo "Cleaning Bluetooth components..."
	@$(MAKE) clean -C $(BLUETOOTH_DIR)
	@echo "Cleaning TCP components..."
	@$(MAKE) clean -C $(TCP_DIR)
	@echo "Cleaning UDP components..."
	@$(MAKE) clean -C $(UDP_DIR)

# Usage Instructions:
# The help target provides a summary of available make commands and their usage.
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  all        - Build Bluetooth, TCP, and UDP components"
	@echo "  bluetooth  - Build Bluetooth components"
	@echo "  tcp        - Build TCP components"
	@echo "  udp        - Build UDP components"
	@echo "  clean      - Clean built components"
	can dynamically grab first available IPV4: ip4addr_ntoa(netif_ip4_addr(netif_list)), TCP_PORT)
```

Notes:
- Each component (Bluetooth, TCP, and UDP) has its own target, allowing you to build specific components individually.
- Controller wireless access: cmake -DPICO_BOARD=pico_w -DWIFI_SSID="RPcontroller" -DWIFI_PASSWORD="RPcontroller" ..
