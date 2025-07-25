---
title: "ACI CLI Helpful Commands"
author: "Krystal Tischendorf"
date: "2025-25-07"
description: "Quick reference for common ACI CLI commands."
tags: ["network", "ACI", "cheatsheet", "commands"]
---

## Introduction

This document provides a quick reference for useful Cisco ACI CLI commands to help with common operational tasks such as searching for VLANs, VPCs, IPs, L3Outs, and switchport configurations.

## Common Commands

- **Find if a VLAN is in use and where:**
    ```
    moquery -c fvIfConn | grep dn | grep vlan-xxx
    ```

- **Find where a VPC is assigned:**
    ```
    moquery -c fvRsPathAtt | grep dn | grep LKSVBNC01H01-VPC
    ```

- **Find IP addresses on leaf switches from APIC:**
    ```
    fabric 1458 show ip interface vrf all | grep 10.225.
    ```

- **Run commands on a specific leaf from APIC:**
    ```
    fabric <node ID> <command>
    ```
    Replace `<node ID>` with the leaf node number and `<command>` with the desired command.

- **Find a specific subnet in all L3Outs:**
    ```
    moquery -c l3extSubnet | grep 10.252.227.0
    ```

- **Check if a switchport is configured as a static port under an EPG:**
    ```
    moquery -c fvIfConn | grep dn | grep stpathatt | grep 153 | grep 1/4
    ```

## Additional Information

- Replace variables (e.g., `vlan-xxx`, `LKSVBNC01H01-VPC`, `10.225.`, `10.252.227.0`, `153`, `1/4`) with your specific values.
- These commands are typically run from the APIC CLI.

## Conclusion

Use this cheatsheet to quickly find information about VLANs, VPCs, IPs, L3Outs, and switchport configurations in your ACI environment.