---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps", "Payments", "jhapps", "azure", "on-prem"]
---

# Card Payment Services

## Service Description
Card Payments Services is a department in the Payments division providing Debit/Credit card services to FI's.  The service is made up of multiple subcomponents of which the description of each is listed below.

> [:!WARNING:]  
> Due to the wide-reaching nature of Card Payments, services below should be considered handle with care.  Outages that impact the service have the ability to impact over 7,000 ATM's nationwide.

## Key Contacts

* BU Support - Christopher Farrar, Blake Heckman
* BU Development - Paurang Parekh; Erik Lee
* SO - Craig Vandivert
* DBA - Kevin Stutler, Temidayo Babatunde
* Service Abbreviation - CPS
* SLA - Platinum


## Environment

### Enhanced ATM Driving (EAD)
This service allows FI's to manage ATM's.

### Service Oriented Architecture (SOA)
Description...

### jBridge
Azure managed instance.  

### Data Warehouse

### Required Domain Credentials
jkhy, jhapps, jhacorp


## Non-standard Configs

* EAD application DR maintenance windows require databases to be dropped from the AG.


Collation, non-standard sqlcare jobs, named instances, non-standard port, additional sqlcare jobs, ha/dr, etc

## Additional Links
* [RACI](Link)







