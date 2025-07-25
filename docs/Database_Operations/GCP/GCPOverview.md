---
author: "Justin West"
date: "2025-01-27"
description: "Overview"
tags: ["DBops", "Database Operations", "GCP", "Google Cloud Platform"]
---

## Summary
TS-Database Operations currently supports the following business units that have workloads in GCP.  More specific information about each implementation can be found in their Service Level Documentation.

| [LoanVantage](https://revelio.jackhenry.com/Database_Operations/Service_Level_Documentation/LoanVantage/) | [jXchange](https://revelio.jackhenry.com/Database_Operations/Service_Level_Documentation/EIS/jXchange/) | SynergyExpress |


## Security Access

Access to GCP projects is controlled through multiple layers.

#### Project Access
TS-Database Operations utilizes jh-gcp-glb-ets-dbops<span>@jackhenry.com to control project access.  All members of DB Ops should have this access to view relevant GCP Projects.  Examples of access controlled by this group:

- Ability to list & view projects
- Ability to list & view resources like vm's, gcs buckets
- Ability to use IAP (Identity Aware Proxy)

**_Note_**: After installing IAP using information below, if you can't see projects, you likely aren't part of this group.

#### Virtual Machine Access

As of 2/1/25, all DBOps supported services utilize AD to authenticate to vm's.  See Service Level Documentation for specific on domain requirements

#### SQL Server Access
As of 2/1/25, all DBOps supported services utilize AD for SQL Server Security for jh users.  Some services also utilize local SQL Accounts but these are limited to automation and/or specific application needs.

## Connecting to GCP Servers
GCP VM's are not accessible via normal RDP sessions.  GCP utilizes an application named [IAP Desktop](https://googlecloudplatform.github.io/iap-desktop/) to facilitate connectivity to VM's.  This is available for download for all Windows OS's.  Utilize your standard @jackhenry.com credentials to authenticate.

1. Install IAP Desktop or RDP to MMODBOPSRDP01.JHACORP.COM
2. Launch IAP Desktop
3. Choose Profile -> Add Project to add new GCP Project
4. Once added, you can drill down into the project to see individual VM's.
5. From here you can access to the VM multiple ways:
     - Right click the target vm -> Connect Client Application -> SQL Server Management Studio
     - Double click the target vm to open a RDP like session to the GUI.

#### Backup/Restores
Backups of GCP SQL Servers is configured to go to GCS Storage Buckets.  Updates are forthcoming to SQLCare to natively configure backups. Default retention of backups is 15 days; however, service level documentation should be consulted for deviations.

#### Server Changes
The Banno Atlas team manages most infrastructure changes in GCP.  Machine configurations are facilitated via Terraform scripts in the Banno GitHub org. In order to make a change, the Terraform code needs to be updated and a pull request created for Atlas to approve.  Once complete, the merge can occur at the defined maintainance window.
