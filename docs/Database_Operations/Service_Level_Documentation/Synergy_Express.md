---
author: “Justin West”
date: "2025-MM-DD”
description: “Service Level Documentation Template”
tags: ["DBops", "Database Operations", "TS-DBOps”, “Banking, “GCP", "On-prem", “Synergy Express”, “SYN”, "SYNEX", "SYN-EX"]
---
# Synergy Express

## Service Description
What is the product and what does it do for JH or customers?

### Key Contacts
* BU Support - Clarke Headen
* BU Development - 
* SO - 
* DBA - Temidayo Babatunde
* Service Abbreviation - SYN


## Environments


### General Info
[SAMPLE} LoanVantage is configured as a 4 node AG with automatic zonal failover.  Regional failover must be performed manually due to application and networking dependencies.  It's expected that all customers will be migrated to GCP by 3/1/25.

Lending Solutions, specifically LoanVantage, is working to modernize its application stack.  As part of that effort, their GCP projects are broken up in to modern and legacy projects.  The intent is that resources in the legacy projects have an end of life date published and will be sunset.  While dba support doesn't change between the two environments, both modern and legacy exist in all environments.  Legacy projects house SSIS/SSRS servers used in their processing.  Modern projects house database engine servers that will persist.

LoanVantage also heavily utilizes an off-shore development team in Bulgaria.  The work overnight hours but are usually available for meetings first thing in the morning.

### On Prem
Supplemental information about on-prem environments

* Domain(s)
* HA/DR Form:  Mirror, AG, SRM, Others

### GCP
Synergy Express is currently working a plan to ingress into GCP.  More documentation will be available as the project takes shape.

#### GCP Project Info
- Domain: 
- DBOps Google Group: JH-GCP-Glb-ETS-DBOps@jackhenry.com
- DBOps Security Group: 
- SQL Server OU: 

| Environment | Project Name | Backup GCS Bucket | Backup Retention |
| ----------- | -------------------- | ------------- | ------------ |
| PROD  | [prod-lendsoln-lv-leg](https://console.cloud.google.com/compute/instances?project=prod-lendsoln-lv-leg), [prod-lendsoln-lv-mod](https://console.cloud.google.com/compute/instances?project=prod-lendsoln-lv-mod) | [prd-lendsoln-lv-mod-db-backups-gcs](https://console.cloud.google.com/storage/browser/prd-lendsoln-lv-mod-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=prod-lendsoln-lv-mod) | 30 Days |
| STAGE |  |  | x Days |
| DEV |  |  | x Days |

### Non-standard Configs
Collation, non-standard sqlcare jobs, named instances, non-standard port, additional sqlcare jobs, ha/dr, etc

### Additional Links
* [RACI](Link) - 
