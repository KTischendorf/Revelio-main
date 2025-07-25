---
author: "Vance Stokes"
date: "2024-11-16"
description: "Standard VLANs"
tags: ["network", "vlan", "cheatsheet"]
---

# VLANs

## Introduction

This document provides an overview of the standard VLANs used across our enterprise. VLANs (Virtual Local Area Networks) are used to segment network traffic, improve security, and optimize network performance. By logically separating different types of traffic, VLANs help in managing and securing the network more effectively. The following sections outline the standard VLANs and their respective purposes within our network infrastructure.

### VLANs

| VLAN Number | VLAN Name | Description |
|-------------|-----------|-------------|
| 319         | Netbackup MN | Used for network backup management. |
| 328         | null | Reserved for future use. |
| 329         | ESX Hosts Management | Manages ESX host servers. |
| 446         | Net Admin/Net Management | Used for network administration and management. |
| 327         | Netsec Management | Manages network security devices. |
| 490         | Standard Environment Transport Network | Facilitates transport in the standard environment. |
| 140/141     | Legacy Clean/Dirty Internet | Segregates clean and dirty internet traffic in legacy systems. |
| 454/455     | Internet | Handles general internet traffic. |
| 419         | Corporate | Used for corporate network traffic. |
| 515         | Systems/Storage Management | Manages systems and storage devices. |
| 1024        | Native VLAN | Default VLAN for untagged traffic. |

## Conclusion

This document outlines the standard VLANs used across our enterprise, providing a clear understanding of their purposes and configurations. Proper VLAN management is crucial for maintaining network security and performance. For any questions or further details, please refer to the network engineering team.
