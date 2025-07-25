---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps","EI&S", "OCTO","GCP", "jXchange"]
---

# jXchange 
> [!WARNING]  
> jX touches nearly everything at jh.  Proceed with extreme caution.

## Service Description
jXchange serves as middleware from jh customers to jh infrastructure.  It is made up of a suite of products:

- JXAPP
- JXAPP GreenDot
- JXAPP Banno
- JXGTW
- JXLOG
- JXBETA
- JXOFI
- JXSTG
- Anicillary but also must DRE at the same time is Enterprise Event System (EES)

#### Key Contacts
* BU Support: Todd Johnson
* BU Management: Jason Bradshaw/Vance Nall
* BU Development: James Hughes/Duane Kelley
* DBA: Asegid Asegilitew


#### On-Prem
jX deploys their product in what they call farms.  There are farms in jhahosting, citjha and dev.jha that are all considered customer facing production environments.  Additionally, jX writes data to the Usage Billing System which is how JH charges customers for utilizing the middleware stack.  


##### Non-Standard Configurations
NEEDS VALIDATION --- Not all db's are in an HA posture by design (list them out).  

#### GCP
##### General Info
As of 6/30/25, the jX implementation in GCP only support Banno subscribers

##### Project Info
- Domain: jhcloud.local
- DBOps Google Group: JH-GCP-Glb-ETS-DBOps@jackhenry.com
- DBOps Security Group: jhcloud.local\JHCLOUD-UserRole-TS-DatabaseOperations
- SQL Server OU: jhcloud.local\Cloud/Computers/Servers/SQL/jXchange/
- Monitoring - DataDog

| Environment | Project Name | Backup GCS Bucket | Backup Retention |
| ----------- | -------------------- | ------------- | ------------ |
| PROD  | [jh-prd-cto-eis-jxchange](https://console.cloud.google.com/compute/instances?project=jh-prd-cto-eis-jxchange) | TBD | TBD |
| STAGE | [jh-stg-cto-eis-jxchange](https://console.cloud.google.com/compute/instances?project=jh-stg-cto-eis-jxchange) | [stg-officecto-jx-leg-db-backups-gcs](https://console.cloud.google.com/storage/browser/stg-officecto-jx-leg-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=jh-stg-cto-eis-jxchange) | Default |
| DEV   | [jh-dev-cto-eis-jxchange](https://console.cloud.google.com/compute/instances?project=jh-dev-cto-eis-jxchange) |[dev-officecto-jx-leg-db-backups-gcs](https://console.cloud.google.com/storage/browser/dev-officecto-jx-leg-db-backups-gcs;tab=objects?forceOnBucketsSortingFiltering=true&project=jh-dev-cto-eis-jxchange) | Default



[jx GCP RACI Chart](https://docs.google.com/spreadsheets/d/17K2XHkTZ3PomXyKG6EIZZE97qqTjaNPu/edit?usp=sharing&ouid=104625505739318582366&rtpof=true&sd=true)


