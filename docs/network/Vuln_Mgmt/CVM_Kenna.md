---
title: "Cisco Vulnerability Management (CVM) Overview "
author: "Krystal Tischendorf"
date: "2024-11-27"
description: "This document gives a brief overview of the function of CVM."
tags: ["network", "CVM", "Kenna", "Cisco", "Vulnerability"]
---
## Introduction

[Cisco Vulnerability Management (CVM -formerly known as Kenna Security)](https://vm.us.kennasecurity.com/) is a cloud-based vulnerability management platform that helps organizations prioritize cyber risks. CVM automates the connection of vulnerability scan data with real-time threat intelligence. Qualys integrates with CVM to help us know where to prioritize and remediate.

## Overview

Devices in CVM are organized by Risk Meters on the CVM Dashboard. There are nine Risk Meters that represent different networks or a specific CVE (Common Vulnerability Exposures) that has been added by ICS Threat and Vulnerability Management. Our Risk Meter is [Technology Services – Infrastructure (Cisco | VMWare)](https://vm.us.kennasecurity.com/dashboard). This dashboard helps us to identify the legitimacy of the vulnerability relative to the specific asset.

## Details

### Vulnerabilities and Vulnerability Statuses

**Vulnerabilities are weaknesses in a system that can be exploited to compromise the system's security. They can be categorized into different statuses based on their severity and the actions taken to address them. Common statuses include**:

- **Open**: The vulnerability has been identified but not yet addressed. These vulnerabilities are currently being reported within CVM (Kenna) as open, and as long as a score is present, will potentially affect the asset score of its asset.
- **Risk Accepted**: These are vulnerabilities which an organization has taken the decision not to fix. These vulnerabilities do not affect the score of an asset and are not included in the default filters when creating Risk Meters.
- **False Positive**: These are vulnerabilities that were identified but later determined to be incorrect or not applicable. This status is provided for scenarios where a finding is incorrectly detected by the originating scanner. Users can use this status to mark the vulnerability as such, and similar to a risk accepted status, removes it from asset score considerations and default Risk Meter creation filters.
- **Closed**: The vulnerability has been verified as resolved and no longer poses a threat. Closed vulnerabilities have been tracked as remediated by the CVM (Kenna) platform. They no longer contribute in any way to the score of the asset. If Kenna rediscovers these vulnerabilities in new connector runs, they can be reopened. If status was manually set as ‘Closed’, then CVM (Kenna)a will no longer automatically manage the status of that vulnerability.

### **How are Vulnerabilities Uncovered?**

To identify vulnerabilities, use vulnerability scanning and management tools to examine applications for flaws in code and misconfigurations that cause security weaknesses. Most vulnerabilities are categorized through the National Vulnerability Database (NVD) and given unique identifiers through the Common Vulnerabilities & Exposures (CVE) list. Some vulnerability scanning solutions may also identify vulnerabilities not found in the NVD.

### **How many Vulnerabilities do organizations typically have?**

Security vulnerability scans at large organizations can cumulatively identify thousands of security risks on each machine and millions of vulnerabilities across an organization. Research reveals that nearly all assets (95% of assets) enclose at least one highly exploitable vulnerability.

### **How do teams remediate their Vulnerabilities?**

There are often more vulnerabilities than an organization has the capacity to fix. That's why prioritization of vulnerabilities is so important. On average, companies can only remediate about one in 10 vulnerabilities on their systems. This capacity deficit puts enormous pressure on cybersecurity professionals to prioritize vulnerabilities based on which are most dangerous. However, research reveals that a mere 2% to 5% of vulnerabilities are at risk of exploitation, significantly narrowing the vulnerability management scope.

### **How do teams decide which Vulnerabilities to remediate?**

Traditionally, organizations have prioritized vulnerabilities according to a mix of instinct, regulatory and compliance needs, and the theoretical damage a successful attack could do. One common metric, the Common Vulnerability Scoring System (CVSS), scores vulnerabilities according to technical severity, or the damage it would do if exploited. But the truth is, many vulnerabilities with high CVSS scores pose little or no risk of exploitation. In recent years, risk-based prioritization has become the gold standard for managing mounting cyber threats against finite resources. Leading vulnerability management software providers offer data-driven, predictive analytics based on real-world threat intelligence and business context to help define the organization’s riskiest vulnerabilities before exploitation occurs.

## Conclusion

Organizations are striving to lower their risk profile by prioritizing and remediating the vulnerabilities that pose the greatest risk. Effective and efficient risk management programs funnel appropriate remediation resources to the right vulnerabilities, saving teams time and money, with the lowest risk possible. For any questions or further details, please refer to the network engineering team.
