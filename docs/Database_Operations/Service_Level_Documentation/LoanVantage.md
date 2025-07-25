---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps","Complimentary", "Lending","GCP", "LoanVantage", "LV"]
---
# LoanVantage

## Service Description
LoanVantage is a digital platform that helps financial institutions manage the loan process.  It is part of the complimentary solutions branch of JH.

#### Key Contacts
* BU Support - Jim Witherow, Philip Sims, Ed Majewski
* BU Development - 
* SO - None
* DBA - Kevin Stutler
* Service Abbreviation - LV

## Environment

#### Azure
As of 4/7/25 all workloads have been migrated to GCP.  There are still two customers accessing full backups via a storage blob, see details below.

#### GCP
##### General Info
LoanVantage is configured as a 4 node AG with automatic zonal failover.  Regional failover must be performed manually due to application and networking dependencies.  It's expected that all customers will be migrated to GCP by 3/1/25.

Lending Solutions, specifically LoanVantage, is working to modernize its application stack.  As part of that effort, their GCP projects are broken up in to modern and legacy projects.  The intent is that resources in the legacy projects have an end of life date published and will be sunset.  While dba support doesn't change between the two environments, both modern and legacy exist in all environments.  Legacy projects house SSIS/SSRS servers used in their processing.  Modern projects house database engine servers that will persist.

LoanVantage also heavily utilizes an off-shore development team in Bulgaria.  They work overnight hours but are usually available for meetings first thing in the morning.

##### GCP Project Info
- Domain: LENDSOLNLV
- DBOps Google Group: JH-GCP-Glb-ETS-DBOps@jackhenry.com
- DBOps Security Group: LENDSOLNLV\LENDSOLNLV-UserRole-TS-DatabaseOperations
- SQL Server OU: 

| Environment | Project Name | Backup GCS Bucket | Backup Retention |
| ----------- | -------------------- | ------------- | ------------ |
| PROD  | [prod-lendsoln-lv-leg](https://console.cloud.google.com/compute/instances?project=prod-lendsoln-lv-leg), [prod-lendsoln-lv-mod](https://console.cloud.google.com/compute/instances?project=prod-lendsoln-lv-mod) | [prd-lendsoln-lv-mod-db-backups-gcs](https://console.cloud.google.com/storage/browser/prd-lendsoln-lv-mod-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=prod-lendsoln-lv-mod) | 30 Days |
| STAGE | [stg-lendsoln-lv-leg](https://console.cloud.google.com/compute/instances?project=stg-lendsoln-lv-leg), [stg-lendsoln-lv-mod](https://console.cloud.google.com/storage/browser/stg-lendsoln-lv-mod-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=stg-lendsoln-lv-mod&prefix=&forceOnObjectsSortingFiltering=false) |[stg-lendsoln-lv-mod-db-backups-gcs](https://console.cloud.google.com/storage/browser?project=stg-lendsoln-lv-mod&prefix=&forceOnBucketsSortingFiltering=true)| 30 Days |
| DEV   | [dev-lendsoln-lv-leg](https://console.cloud.google.com/compute/instances?project=dev-lendsoln-lv-leg), [dev-lendsoln-lv-mod](https://console.cloud.google.com/compute/instances?project=stg-lendsoln-lv-mod) |[dev-lendsoln-lv-mod-db-backups-gcs](https://console.cloud.google.com/storage/browser/dev-lendsoln-lv-mod-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=dev-lendsoln-lv-mod) | 30 Days |

### Non-standard Configs

#### Backups

LoanVantage has 2 scheduled jobs to perform daily full backups.  These are written to the Azure Storage Accounts listed below.  FI's have access to these storage accounts and download full bak's daily.  At some point in the future, these jobs will be dropped and the FI's will move to Data Broker to consume this data. 

This file structure/data can be accessed using Azure Storage Explorer.  Authenticate with jhacorp standard credentials.

- LCEF - [lcefbutransferstorage01](https://portal.azure.com/#resource//subscriptions/02cfec69-01ec-4988-bb30-c725fc113679/resourceGroups/ER-NetworkCore/providers/Microsoft.Storage/storageAccounts/lcefbutransferstorage01)
- Flushing - [fb26017sqlbackup01](https://portal.azure.com/#@jackhenry.onmicrosoft.com/resource/subscriptions/02cfec69-01ec-4988-bb30-c725fc113679/resourceGroups/ER-NetworkCore/providers/Microsoft.Storage/storageAccounts/fb26017sqlbackup01/overview)

#### HA/DR
As of 4/1/25, LoanVantage only has a single production node in service with backups.  After all customers are migrated, db's will begin enrollment into a 4 Node AG cluster.

### Additional Links
RACI - [LoanVantage GCP](https://docs.google.com/spreadsheets/d/1i5Vo28Zz2IksLAppRQGnoLgjiPb5jXxJ/edit?gid=1446979822#gid=1446979822)


