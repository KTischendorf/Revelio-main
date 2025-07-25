---
author: "Vance Stokes"
date: "2024-10-10"
description: "How to access SecureCRT and locate/connect to network devices within the JH environment."
tags: ["SecureCRT", "Remote Desktop", "Network"]
---

# SecureCRT

## The Reason

This outlines how to access SecureCRT and locate/connect to network devices within the JH environment.

### SecureCRT File Structure
---
Devices in SecureCRT are organized by function, site name, and business unit. Think of SecureCRT as a logical diagram that allows you to quickly and efficiently access multiple network devices at a time, while providing a visualization of our environment from a logical perspective which is incredibly effective when walking a network.

> *If this is your first time*, you'll need to modify the file path in options. I'll need to add a write-up on this.

1. Connect to the corporate network and/or the RA VPN.
2. Connect to a Remote Jumpbox.
3. Using the session list, select something to connect to.
4. Login with your **JKHY** credentials, `jkhy\<username>`

### In the Weeds

### Establish Connectivity

- Make sure you are connected to a VPN device or on the corporate network, either via Wi-Fi or a hard-wired connection.

#### Remote Desktop

There are multiple options that can be used depending on your OS and preferences. Some options are:

- RoyalTSX
- Microsoft Remote Desktop Manager
- Default approved application

#### Steps to Connect

1. Start up the app of your choice.
2. Once you are logged in, open SecureCRT. Here are some hints:
    - If prompted for a passphrase, select the "Just Don't do it" option.
    - If this is the first time opening the app from a particular jumpbox:
        1. Navigate to `Options > Global Options > General > Configuration Path`
            - Corporate Jumpboxes need: `C:\Users\Public\Desktop\SecureCRT`
            - JKHY Jumpboxes need: `E:\JKHY_Replication\SecureCRT`
3. Close and re-open SecureCRT.
`