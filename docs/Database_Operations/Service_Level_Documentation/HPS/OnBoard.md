---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps", "hps", "jhahosting", "iTalk", "itab", "ita", "itc"]
---
# OnBoard

## Service Description
What is the product and what does it do for JH or customers?

### Key Contacts
* BU Support - Peter Amstutz
* BU Development - 
* SO - 
* DBA - 
* Service Abbreviation -
* HPS SLA - Silver, Gold or Platinum -- Delete if not HPS Service

## Environments


### General Info
[SAMPLE} LoanVantage is configured as a 4 node AG with automatic zonal failover.  Regional failover must be performed manually due to application and networking dependencies.  It's expected that all customers will be migrated to GCP by 3/1/25.

Lending Solutions, specifically LoanVantage, is working to modernize its application stack.  As part of that effort, their GCP projects are broken up in to modern and legacy projects.  The intent is that resources in the legacy projects have an end of life date published and will be sunset.  While dba support doesn't change between the two environments, both modern and legacy exist in all environments.  Legacy projects house SSIS/SSRS servers used in their processing.  Modern projects house database engine servers that will persist.

LoanVantage also heavily utilizes an off-shore development team in Bulgaria.  The work overnight hours but are usually available for meetings first thing in the morning.

### OnBoard Deposits
Supplemental information about on-prem environments

* Domain(s)
* HA/DR Form:  Mirror, AG, SRM, Others

### OnBoard Loans
Supplemental information about Azure environments

### WKFS

### Non-standard Configs
Collation, non-standard sqlcare jobs, named instances, non-standard port, additional sqlcare jobs, ha/dr, etc

### Additional Links
* [HPS Business Partner Portal](link) - If HPS, go to [HPS Site](https://jackhenry.sharepoint.com/sites/hpsbpp), scroll to Service, click into service and replace link to HPS Business Partner Portal with service specific link.  Ex: https://jackhenry.sharepoint.com/sites/hpsbpp
* [RACI](Link) - 







