---
title: "Capturing ACI Interface Flapping"
author: "Krystal Tischendorf"
date: "2024-11-20"
description: "This document provides procedures for capturing ACI interface flapping."
tags: ["network", "ACI", "interface", "flapping", "procedure"]
---

## Introduction

This document provides step-by-step procedures for capturing ACI interface flapping. It aims to help technicians diagnose and resolve interface flapping issues efficiently.

## Procedures

### Step 1: Log into the APIC CLI

1. **Access APIC CLI**: Log into the APIC CLI where the script is loaded.
    - BMO – APIC
    - SMO - APIC
    - LKS - APIC
    - MMO - APIC
    - ATX PNF – APIC3
    - ATX HNS – APIC3

### Step 2: Change Directory

1. **Navigate to Directory**: Change to the following directory.
    ```bash
    cd /data/techsupport/
    ```
2. **Verify Script**: Verify that `collect-dom-data-v8.py` is in the directory.
    ```bash
    ls | grep collect-dom-data-v8.py
    ```

### Step 3: Run the Script

1. **Execute Script**: Run the script.
    ```bash
    python collect-dom-data-v8.py --debug INFO
    ```
    - Note: Missing hyphens and/or spaces may result in errors.
2. **Log in**: Script will request you log in with your TACACS credentials.
3. **Output Files**: Script will generate the following files when done:
    - `ACI_Fabric1-collection-xxxx.tgz`
    - `ACI_Fabric1-formatted-dom-data-xxxx.csv`

### Step 4: Download Files via FileZilla

1. **Launch FileZilla**: Log into the device via FileZilla.
2. **Connect to APIC**: Enter APIC IP address, TACACS credentials, and port 22 in the quick connect.
3. **Navigate to Directory**: Navigate to `/data/techsupport` in the right side pane.
4. **Download Files**: Download both ACI Script files.
    - Right-click on the files and select download.
    - Change download location on the left side pane if necessary.
5. **Copy Files**: Copy files from download location on the jump box and paste them on your computer.
    - Convert the file to `.xls` rather than `.csv` for saving purposes.

### Step 5: Cross Reference and Identify Issues

1. **Cross Reference**: Cross reference the Node with the device name and add device serial number for TAC reference.
    - Leave QSFP serial number, but clearly indicate between the 2 serial numbers.
2. **Identify Interfaces**: Open the `.csv/Excel` file and sort it by “Interface Resets” Z to A.
3. **Verify Neighbor Device**: Log into CLI on the indicated leafs.
    ```bash
    show lldp neighbor interface ethx/y
    ```
    - Verify the neighbor device and interface match the export.
     - The IPN connections will show up from the leaf side but not populate the IPN information into the spreadsheet.
     - Verify the pairs are listeed for review.
       
### Step 6: Capture QSFP Serial Numbers

1. **Log into GUI**: Navigate to Fabric -> Inventory -> Pod -> Leaf/Spine# -> Interfaces -> Physical Interfaces.
2. **Select Interface**: Select the interface in question and scroll to the Transceiver information.
3. **Add Serial Number**: Add the QSFP serial number to the spreadsheet.
    - IPN serial numbers can be seen on the CLI by doing a `show inventory`.

### Step 7: Cross Check for Work

1. **Check for Work**: Cross check for any work that may have caused flapping such as device work, upgrades, crashed devices, etc.

### Step 8: Open TAC Case

1. **Open Case**: Pick one device Serial Number and open a TAC case.
    - Keep tickets separated by fabric (ATX PNF, ATX HNS, BMO, etc.).
2. **Copy Information**: Copy the information into your TAC case and request they review the indicated QSFPs for failure and RMA replacement.
    - Ongoing Field Notice FN70438 issues have been seen, this is a fix on fail field notice.
    - They can review for any additional, non-FN related issues as well.
3. **Request RMA**: This can be created and shipped to appropriate data center.
    
### Step 9: Open Incident for Data Center Engineering

1. **Open Incident**: Open incident for Data Center Engineering to replace QSFPs once RMA is received.
2. **Swap and Clear Interfaces**: Verify with Data Center what order they would like to replace in.
    - Log into ACI GUI and select the node/interface.
    - Click disable and submit.
    - Wait for Data Center to confirm QSFP is replaced.
    - Click enable and submit.
    - Check LLDP neighbor returns in CLI.
    - Refresh interface status on the GUI.
3. **Clear Counters**: After all QSFPs are replaced, clear counters for the interfaces you replaced ONLY.

## Additional Information

Ensure you have the device's manual and any necessary tools before starting the validation process. Keep a record of all findings and actions taken for future reference.

## Conclusion

By following these procedures, technicians can systematically capture and troubleshoot ACI interface flapping issues. This helps in identifying the root cause and implementing appropriate solutions.
