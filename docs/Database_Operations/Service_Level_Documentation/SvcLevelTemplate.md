---
author: “Justin West”
date: "2025-MM-DD”
description: “Service Level Documentation Template”
tags: ["DBops", "Database Operations", "TS-DBOps”, “[Choose one, remove brackets CORP, PAYMENTS, CREDIT UNION, OR BANKING], “[GCP, AZURE or ON-PREM”], “[ServiceName]”, “[Service”Abbreviation]”
---

# TEMPLATE FOR SERVICE LEVEL DOCUMENTATION.
## Instructions
This .md file is a template for Service Level Documentation.  
* To copy, click the edit icon.
* Copy the entire contents of this to a new .md or an existing service page that needs to be completed.
* Update Front Matter Above:
    * Author, date, and tags (should include division of JH, service name, service abbreviation and at least one tag indicating whether the service is in GCP, Azure or On-prem.  If in multiple, create a new tag.
* Complete the remainder of the template below.
    * If an HPS Service, reference the [HPS Business Partner Portal](https://jackhenry.sharepoint.com/sites/hpsbpp) for SO, Service Abbreviation, SLA.  Also use the HPS Business Partner Portal to get a direct link to the HPS Service documentation and update in the additional links section below.
* Delete sections that don't apply.
* Delete this entire section
* Save, Create pull request

# Service Name

## Service Description
What is the product and what does it do for JH or customers?

### Key Contacts
* BU Support - 
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
Collation, non-standard sqlcare jobs, named instances, non-standard port, additional sqlcare jobs, ha/dr, etc

### Additional Links
* [HPS Business Partner Portal](link) - If HPS, go to [HPS Site](https://jackhenry.sharepoint.com/sites/hpsbpp), scroll to Service, click into service and replace link to HPS Business Partner Portal with service specific link.  Ex: https://jackhenry.sharepoint.com/sites/hpsbpp
* [RACI](Link) - 







