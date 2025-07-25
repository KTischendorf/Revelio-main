---
author: "Vance Stokes"
date: "2024-12-16"
description: "Troubleshooting with Panorama"
tags: ["network","Panorama", "Palo Alto", "Troubleshooting", "Network Security"]
---
# Panorama Basic Troubleshooting 

### Panorama Documentation

I am not an expert in this software; I am still learning.

#### Boundary Devices

We use two different platforms here: ASA and Palo Alto.

#### Accessibility

How to access these devices:
- CLI
- ASDM
- Panorama

This document will focus primarily on Palo Alto and Panorama.

#### Login

- [BMO Panorama](https://10.204.249.5/)
- [ATX Panorama](https://10.225.35.111/)

#### Dashboard

This section contains general information.

#### Monitor

- Ensure you switch to the correct device group when performing any tasks.
- Traffic: This feature is similar to Splunk in its query functionality.
- URL Filtering: Useful when the developer looks past the IP address.

#### Device Groups

Policies have configured rules for access and NAT, which can be helpful during troubleshooting.
- In the lower bar, you'll see a `Test Policy Match` option, similar to the packet tracer on the ASA appliance. You can use this for both Security and NAT.

#### CLI

You can also `ssh` directly to the devices to validate configurations specific to each device.
