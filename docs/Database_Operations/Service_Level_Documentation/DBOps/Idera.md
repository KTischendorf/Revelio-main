---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps", "Idera", "jhahosting", "jhapps", "synergy express", "jhacorp"]
---
# Idera

## Summary

Idera SQL Diagnostic Manager is used to monitor SQL Server databases.  JH has a limited number of licenses and therefore monitoring is generally limited to multi-tenant servers or servers that support critical customers.  Servers may also be added temporarily to troubleshoot performance issues.

## Versions & License Counts

| Domain | App Version | Total Licenses |
| --- | ---- | --- |
| GLADIATOR | 12.2.0.49 | 18 |
| JHACORP | 12.2.0.49 | 40 |
| JHAHOSTING - EIS | 12.2.0.49 | 50 |
| JHAHOSTING - HPS | 12.2.0.49 | 50 |
| LKSOTLEP | Does this still exist? | | 
| SYNERGY.SASS.LOCAL | 12.2.0.49 | TBD |

## Domains

### JHACORP

#### Overview of Servers
| Purpose | Servers |
| -------------------------------------- | ------- |
| Diagnostic Manager Monitoring Services | MMODBOPDBP01.jhacorp.com |
| SQL Diagnostic Manager Console | MMODBOPSRDP01.jhacorp.com, BMODBOPSRDP01.jhacorp.com, MMODBOPDBP01.jhacorp.com |

#### Idera Connection Details

| Idera SQLdm SQL Connection Details| | 
| --- | --- |
| Server |  MMODBOPDBP01,1433 |
| Database |  SQLdmRepository |

#### Non-Standard Configurations
None

### Gladiator

| Purpose | Servers |
|---------| ------- |
| Diagnostic Manager Monitoring Services | ATXGLDDBAMGT02P.gladtech.net | 
| SQL Diagnostic Manager Console | ATXGLDDBAMGT02P.gladtech.net, BMOGLDDBAMGT02P.gladtech.net |

| | | 
| --- | --- |
| Server | ATXGLDDBAMGT02P,54277 |
| Database | SQLdmRepository |

#### Non-Standard Configurations
While there are no non-standard configurations, the BU also has access to the console servers and SQLdm

### JHAHOSTING - EIS

| Purpose | Servers |
|---------| ------- |
| Diagnostic Manager Monitoring Services | ATXDBOPRDBP02 | 
| SQL Diagnostic Manager Console |  ATXDBOPRDBP01, ATXDBOPRDBP03 |

| | | 
| --- | --- |
| Server | ATXDBOPRDBP01,54277 |
| Database | SQLdmRepository_EIS |

#### Non-Standard Configurations
EIS & HPS share a domain.  In order to limit visibility/confusion between the services, separate SQLdm repositories exist segmenting services.


### JHAHOSTING - HPS

| Purpose | Servers |
|---------| ------- |
| Diagnostic Manager Monitoring Services | ATXDBOPRDBP02 | 
| SQL Diagnostic Manager Console |  ATXDBOPRDBP02, ATXDBOPRDBP03 |

| | | 
| --- | --- |
| Server | ATXDBOPRDBP01,54277 |
| Database | SQLdmRepository_HPS |

#### Non-Standard Configurations
EIS & HPS share a domain.  In order to limit visibility/confusion between the services, separate SQLdm repositories exist segmenting services.  Additionally, HPS and some BU's have access to SQLdm.

### Synergy Express


| Purpose | Servers |
|---------| ------- |
| Diagnostic Manager Monitoring Services | SYNDBOPDBP01.synergy.saas.local | 
| SQL Diagnostic Manager Console | SYNDBOPSRDP01.synergy.saas.local, SYNDBOPDBP01.synergy.saas.local |

#### Non-Standard Configurations
None

| | | 
| --- | --- |
| Server | SYNDBOPDBP01,1433 |
| Database | SQLdmRepository |
