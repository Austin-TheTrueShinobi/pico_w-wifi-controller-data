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
