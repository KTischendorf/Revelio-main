---
author: "Vance Stokes"
date: "2024-10-10"
description: "How to submit exceptions for network devices in Kenna (CVM-Cisco Vulnerability Management)."
tags: ["Kenna", "CVM", "Vulnerability Management", "Network"]
---

# Submitting Security Exceptions for Network Devices

## The Reason

This document outlines how to submit exceptions for network devices that have been identified in Kenna as being vulnerable for CVE(s).

## Kenna (CVM) Overview

Kenna Security is a cloud-based vulnerability management platform that helps organizations prioritize cyber risks. Kenna automates the connection of vulnerability scan data with real-time threat intelligence. Qualys integrates with Kenna to help us know where to prioritize and remediate.

Devices in Kenna are organized by Risk Meters on the Kenna Dashboard. There are nine Risk Meters that represent different networks or a specific CVE (Common Vulnerability Exposures) that has been added by ICS Threat and Vulnerability Management. Our Risk Meter is Technology Services – Infrastructure (Cisco | VMWare). This dashboard helps us to identify the legitimacy of the vulnerability relative to the specific asset.

### Analyzing Vulnerabilities

Below are some questions, provided by ICS Threat and Vulnerability Management, to consider when analyzing a vulnerability:

- Could this vulnerability be exploited from the internet?
- Is there known, published code for this vulnerability?
- What would the impact to the business be if this vulnerability were exploited?
- Are there other security controls in place that reduce the likelihood and/or impact of this vulnerability being exploited?
- How old is this vulnerability?

### Categorizing Vulnerabilities

Upon completion of this assessment, each vulnerability will be categorized as one of the following:

- **False Positive**: The vulnerability is incorrectly identified.
- **Remediation**: The vulnerability needs to be addressed.
- **Service Level Agreement (SLA) Extension Request**: Additional time is needed to address the vulnerability.

## Submitting Exceptions

To submit an exception for a network device in Kenna, follow these steps:

1. **Log into Kenna**: Access the Kenna dashboard using your credentials.
2. **Navigate to the Risk Meter**: Select the appropriate Risk Meter for the device.
3. **Identify the Vulnerability**: Locate the specific CVE(s) for the device.
4. **Analyze the Vulnerability**: Use the questions provided above to assess the vulnerability.
5. **Categorize the Vulnerability**: Determine the appropriate category for the vulnerability.
6. **Submit the Exception**: Follow the process outlined in Kenna to submit the exception, providing all necessary details and justifications.

## Conclusion

Following these steps will help ensure that exceptions for network devices in Kenna are submitted accurately and efficiently. Consistent analysis and categorization of vulnerabilities are crucial for maintaining the security and integrity of our network infrastructure.
