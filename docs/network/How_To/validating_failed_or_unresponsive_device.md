---
title: "Validating a Failed or Unresponsive Device"
author: "Krystal Tischendorf"
date: "2024-11-21"
description: "This document provides procedures for validating a failed or unresponsive device."
tags: ["network", "device", "validation", "procedure", "failed", "unresponsive"]
---

## Introduction

This document provides step-by-step procedures for validating a failed or unresponsive device. It aims to help technicians diagnose and resolve issues efficiently.

## Procedures

### Step 1: Check Physical Connections

1. **Inspect Power Supply**: Ensure the device is properly connected to a power source.
2. **Verify Network Cables**: Check that all network cables are securely connected.
    - Look for any visible damage to the cables.
    - Replace cables if necessary.

### Step 2: Restart the Device

1. **Power Cycle**: Turn off the device, wait for 30 seconds, and then turn it back on.
2. **Check Indicators**: Observe any status lights or indicators on the device.
    - Note any unusual patterns or colors.
    - Refer to the device manual for indicator meanings.

### Step 3: Check Device Logs

1. **Access Logs**: Use the device's interface to access system logs.
2. **Identify Errors**: Look for any error messages or warnings.
    - Document any recurring issues.
    - Research error codes if necessary.

### Step 4: Perform Diagnostic Tests

1. **Run Built-in Diagnostics**: Utilize any built-in diagnostic tools provided by the device.
2. **Use External Tools**: If available, use external diagnostic tools to further analyze the device.
    - Compare results with expected outcomes.
    - Record any discrepancies.

### Step 5: Remotely Verify Device Status

1. **Check SSH Status**: Verify if the device is accessible via SSH.
    - If accessible, follow Cisco's instructions for gathering outputs.
2. **Check Console Access**: Connect to the device via console.
    - Copy any status messages or errors shown on the console to relay to Cisco.
    - If it is a switch stack, ensure you are on the console for the failed switch.
    - Coordinate with Data Center for direct console connection if necessary.

### Step 6: Check ACI APIC GUI Status

1. **Navigate to Fabric -> Inventory**: Locate the node in the Pod listings or Unreachable Nodes section.
    - Hard Down devices will show under Unreachable Nodes.
2. **Check Node Details**: Double-click the node to open the details page.
    - Check "faults" and "history" tabs for any error logs.
    - Check "status" listing for the node.
3. **Export Policies**: Navigate to Admin -> Import/Export -> Export Policies.
    - Check under Core for any core files generated related to the device crash.
    - Check for any On-Demand TechSupport files.

### Step 7: Open Ticket with Data Center in ServiceNow

1. **Classify Ticket**: Classify as "Server / Maintenance / Hardware Component Failure".
    - Include device details: Name, Type/Product ID, Serial Number.
2. **Request Physical Verification**: Request verification of device status.
    - Check power status/power supply lights.
    - Check device status and status light indicators.
    - Request a picture of the device if possible.
    - Request power cycle of the device if hard down (15-minute power cycle).

### Step 8: Escalate to Cisco TAC

1. **Log into Cisco Support Portal**: Open a new case or escalate by phone at 800-553-2447.
    - Gather serial number of the product.
2. **Open New Case**: Select appropriate request type and enter device serial number.
    - Fill out the ticket form with all relevant information.
    - Include details regarding device status and errors.
    - Upload any available technical logs and outputs.
3. **Coordinate with Data Center Technician**: Confirm RMA shipping details and site contact information.

## Additional Information

Ensure you have the device's manual and any necessary tools before starting the validation process. Keep a record of all findings and actions taken for future reference.

## Conclusion

By following these procedures, technicians can systematically validate and troubleshoot failed or unresponsive devices. This helps in identifying the root cause and implementing appropriate solutions.
