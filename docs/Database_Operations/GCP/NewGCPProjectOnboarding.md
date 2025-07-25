---
author: "Justin West"
date: "2025-02-06"
description: "Process"
tags: ["DBops", "Database Operations", "GCP", "Google Cloud Platform"]
---

# Onboard DBOps into new or existing GCP Project

## Prerequisites
1. Case to Cloud to add Database Operations Google group to GCP Project requesting project & IAP Access
2. Request to Cloud or 3rd Party company to create gcs storage bucket for database backups ([ProjectName]-db-backups-gcs
3. Request new AD group in appropriate domain ([DOMAIN]\[DOMAIN]-UserRole-TS-DatabaseOperations) - DBOps already has groups created in LENDSOLNLV & JHCLOUD.LOCAL
4. Request AD group to be included as local admin via manual update or ansible push
5. Request DBops core project team to have user accounts created to be added to group (jhNow case to IDM)
6. Request GCP storage object admin for gcs buckets created above.
7. Send jhNow request to IDM to create a service account/gmsa for the SQL Engine.  Reference Instance ID's and purpose.

*NOTES:* 
* ServiceNow "Access" requests likely won't have the domain as an option. Choose "Other" domain.
* AD User requests are 1 request for each user.
* If no Managed AD in the GCP project, request ability to generate new credentials upon connection.


## Server Environment Config 
Kerberos Delegation Resolution

* Ensure both app tier machine and sql machine has  "Network security: Configure encryption types allowed for Kerberos" set to allow AES128_HMAC_SHA1, AES256_HMAC_SHA1 and Future Encryption types
* Ensure sql server instance svc account was assigned the following SPNs per sql machine
    - MSSQLSvc/{sql machine}.domain
    - MSSQLSvc/{sql machine}.domain:SQLPort
    - MSSQLSvc/{sql machine}:SQLPort
    - MSSQLSvc/{sql machine}
* Configure the msds-supportedencryptiontypes ad account attribute on both the service account running the sql server instance and the service account running the IIS application pool that is running the .NET service to 24 for AES128+AES256.
* Wait for replication and then restart the SQL Server instance.

## GCS Bucket Config
### Set Object Lifecycle Policy to 15 day retention (BU can specficy others)
{Brandon, can you document here}

## Installation of SQL (Reference Standard SQL Install Process)
1. IAP to target
2. Follow standard install process
3. Configure backups to write to gcs bucket "s3:\"
   
## Validation
* Configure SQLCare to write backups to write to GCS bucket.
* Test restore to SQL Server 

## Documentation
* Navigate to revelio.jackhenry.com -> Database Operations -> GCP -> GCP Overview.md
* Add a the new "service" to the table in the Summary and link to it's Service Level Documentation
* Save, Create/complete Pull Request
* Navigate to Service Level Documentation page for service in question
* In the environment section, create a new section for GCP.
    * Add General Info, specific GCP Project Info, table summarizing the environments.
* Document any non-standard configs.
* Document the Cloud RACI link.
* Save, Create/complete Pull Request


