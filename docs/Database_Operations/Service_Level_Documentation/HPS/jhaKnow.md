---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps","Complimentary", "jhaKnow Express","jkw"]
---

# jhaKnow Express Service Level Documentation

## Service Description
What is the product and what does it do for JH or customers?

### Key Contacts
* BU Support - April Hurt
* BU Development - 
* SO - Ty Nighswonger
* DBA - Brent Bohannon
* Service Abbreviation - JKW
* HPS SLA - Silver, Gold or Platinum -- Delete if not HPS Service

## Environments


### General Info
[SAMPLE} LoanVantage is configured as a 4 node AG with automatic zonal failover.  Regional failover must be performed manually due to application and networking dependencies.  It's expected that all customers will be migrated to GCP by 3/1/25.

Lending Solutions, specifically LoanVantage, is working to modernize its application stack.  As part of that effort, their GCP projects are broken up in to modern and legacy projects.  The intent is that resources in the legacy projects have an end of life date published and will be sunset.  While dba support doesn't change between the two environments, both modern and legacy exist in all environments.  Legacy projects house SSIS/SSRS servers used in their processing.  Modern projects house database engine servers that will persist.

LoanVantage also heavily utilizes an off-shore development team in Bulgaria.  The work overnight hours but are usually available for meetings first thing in the morning.

### On Prem
Supplemental information about on-prem environments

* Domain(s)
* HA/DR Form:  Mirror, AG, SRM, Others

### Azure
Supplemental information about Azure environments

#### Azure Subscription Info
General Info about usage of the Azure Sub if not captured in General Info above

- Azure Subscription(s):


### GCP

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

#### SQL Config
* Port 12001
* Non-standard drive mapping
* SSAS in use



#### Site Transitions
* During site transitions, JKW expects sql agent jobs to be transferred.  These are custom created by the customer.  Jobs may need to be dropped and re-added instead of copied.  Confirm with BU.

``` sql
Select * from msdb.dbo.sysjobs 
where category_id not in (0,3,8,100,101,105)
order by category_id
```

* SSRS Keys
* Clean Up Orphaned Users
* Encourage BU to process their cubes



### Additional Links
* [HPS Business Partner Portal](link) - If HPS, go to [HPS Site](https://jackhenry.sharepoint.com/sites/hpsbpp), scroll to Service, click into service and replace link to HPS Business Partner Portal with service specific link.  Ex: https://jackhenry.sharepoint.com/sites/hpsbpp
* [RACI](Link) - 







