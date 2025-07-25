---
title: "Assigning Available Public IP Addresses"
author: "Vance Stokes"
date: "2023-10-05"
description: "How to assign available public IP addresses by checking InfoBlox and internet routers."
tags: ["Public IP", "InfoBlox", "Network"]
---

## Introduction

This document outlines the steps to assign available public IP addresses by checking InfoBlox and internet routers.

## Procedures

### Step 1: Check InfoBlox

Check [Infoblox](https://jhaddi.jkhy.com) to find available public IPs in the requested subnet.

### Step 2: Verify with Internet Routers

You can also run a `sh ip route x.x.x.x` command from any of the internet routers to find the firewall where it translates from.

### Step 3: Check Active Translations

Check the internet routers (e.g., INETBRA-P-CR01/02, INETSMO-R01, etc.) by running the `show arp` command to see the list of public IP addresses that are being actively translated. The `Hardware Addr` field shows "Incomplete" for public IP addresses that have no designation. See the sample output below:

```plaintext
INETSMO-R01-CLINK#show arp

Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  74.200.48.100          14   b0fa.eb97.1829  ARPA   GigabitEthernet0/0/1
Internet  74.200.48.101           6   4c4e.35ea.de85  ARPA   GigabitEthernet0/0/1
Internet  74.200.48.103          10   4c4e.35ea.de85  ARPA   GigabitEthernet0/0/1
Internet  74.200.48.104           6   4c4e.35ea.de85  ARPA   GigabitEthernet0/0/1
Internet  74.200.48.105           0   Incomplete      ARPA    
Internet  74.200.48.106           0   Incomplete      ARPA    
Internet  74.200.48.107           0   Incomplete      ARPA    
Internet  74.200.48.108           0   Incomplete      ARPA    
```

### Step 4: Confirm with Firewall

Check the firewall for further confirmation by running the command `show xlate | i x.x.x.x` (where x.x.x.x is the public IP address) to confirm the IP address is not in use. The sample below shows all translations for public IP addresses starting with 74.200:

```plaintext
ciscoasa/FPBMO-FW-EXT# sh xlate | i 74.200

NAT from 3506:10.234.162.18 to OUTSIDE:74.200.62.69
NAT from 3521:10.234.178.24 to OUTSIDE:74.200.62.70
NAT from 3506:10.234.178.24 to OUTSIDE:74.200.62.70
```

## Conclusion

Following these steps will help ensure that available public IP addresses are correctly identified and assigned. Consistent verification across InfoBlox, internet routers, and firewalls is crucial for maintaining the integrity of our network infrastructure.
