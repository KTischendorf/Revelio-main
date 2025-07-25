---
author: "Justin West"
date: "2025-04-10"
description: "SQL Server Licensing Chargeback"
tags: ["DBops", "Database Operations", "SQL Server", "Chargeback", "Finance"]
---
 
# SQL Server Licensing Chargeback
 
## MS Contract Info
 JH is currently licensed to use SQL Server under Microsoft Server and Cloud Environment (SCE) agreement #67723779 and extends licensing capabilities using our Enterprise Agreement. 
 
 | Edition | Contracted Licenses | Level C Cost | JH SCE Renewal Pricing |
 | ------- | ------------ | ------------------- | ----------- |
 | Enterprise | 2900 | $312.25 | $236.06 |
 | Standard | 800 | $81.43 | $61.57 | 
 | Developer | N/A | N/A | N/A |
 
## True-up licensing
JH is required to keep a monthly count of licenses used each month.  Currently, that total is captured on the last Monday of the month and reported in SQL licensing.  The procurement team has access to these numbers and uses then to report license counts on JH's behalf. 
 
 
## Licensing rules/Methodology
 1. Is there a need for a SQL Enterprise License? SQL Developer has the same features for free, but cannot be used in a production enviroment.   
 2. If there is a need for SQL Enterprise, can a SQL licensed cluster be used? Licensed clusters share the expenses with others on the cluster using SQL Enterprise.
 3. SQL Standard has limited features compared to Enterprise, and cannot be on a Licensed cluster, if the CPU's are less than 4, the minimum purchase is 2 licenses.
 4. Microsoft licensing is based on the number of cores on your server, consider if the server is overprovisioned, costing more.

### Licensed Host
 A licensed SQL Cluster, shares the cost with other tenants on the cluster.
 Formula used for cost of SQL servers on a host:
                                                           
              1. Logical CPU's divided by VMWare Virtual Cluster CPU's.
              2. VMWare Physical Cluster CPU's divided by 2.
              3. Enterprise rate = $236.02 per license.

### Enterprise Edition
Enterprise Edition of SQL includes all features of SQL. **$236.06** per license
Some included features of SQL Enterprise:
   
              1.Supports maximum available RAM.
              2.Advanced support-Hyper-V integration and more.
              3.AlwaysOn Availability Groups-AG.
              4.Advanced BI tools & In-Memory OLAP.
              5.Granular access control, data encryption, at-rest & in-motion, 
              advanced auditing.

### Standard Edition
Standard Edition offers basic performance capabilities. **$61.57** per license if the CPU's are less than **4**, the minimum purchase is **2** licenses
Some included features of SQL Standard:
   
              1.Limited - capped RAM usage.
              2.Limited disaster recovery options.
              3.Basic reporting and BI tools.
              4.Standard data encryption & access control.

### Developer Edition Limitations
 SQL Developer is a free version with all the features of SQL Enterprise, but cannot be used in a production enviroment.
 
### Cloud Considerations
 
 
## Technical Documentation
Each Monday morning by 7:30am CST, the VROPS and SCCM data is dropped on the server BMOMNDSHOST01P.JKHY.COM. A manual process is executed to bring data into the SQL Licensing database.

Monday morning Process on BMOMNDSHOST01P.JKHY.COM,54277

     •	Connect to BMOMNDSHOST01P.JKHY.COM,54277
     •	E:\DBAProjects\SQLLicensing\Scripts
     •	Make sure two VROPS files are in the “Dropzone” folder. 
     •	The SCCM file will  be in the root “SQLLicensing” folder after 
       running the Exports script.
     •	Run 1_Exports-(Gets SCCM Data)
     •	Run 2_Imports
     •	Run job SQLLICENSING_V2
     •	Check the dbo.vw.Tallies table under SQL Licensing, Views 
       to make sure data pulled in correctly for the current date.




### Data Sources
 Currently pulling data from a static GAMBIT table, SCCM, VROPS & VROPS Clusters. The future plan is to pull SQL Licensing data from jhNow.

### Processing Servers/Database Instances
 Link to more detailed instructions and scripts for the Monday SQL licensing process.
[Monday Process](https://revelio.jackhenry.com/Database_Operations/Documents/SQL_Licensing/MondayMorningProcess/)

### Reporting
 [Tableau](https://corptableau.jackhenry.com/#/views/SQLCostYTDV4/4ChargebackDetail?:iid=1) is an up to date reporting platform pulling the data from the SQL Licensing Table.
 
#### Access
Access to Tableau reporting is granted via Monett\JHA-PSA-SQLSrvLic-DashboardAccess.  Accounting, Finance, Tech Services, all managers and supervisors inherited access via nested security groups membership. A jhNow ticket should be created for access not covered by one of these groups.

## Resources




