---
author: "Justin West"
date: "2024-11-26"
description: "Process Guide"
tags: ["DBops", "Database Operations", "Access", "Security by Service", "SBS"]
---
# Granting User Access to Databases
**Description:**
This document outlines standards and process to add users to an existing database.

## General Info
Access to SQL Servers is granted using the principal of least privilege.  Furthermore, JH has established a "Security by Service" model for granting access to databases.  This model defines security groups that should be added to grant appropriate access.  Security Groups eliminate the need to grant individual users explicit access to the database which is prone to error.


## Process
* Upon receiving a request for user access, TS-Database Operations should consult with the requestor on access needed.
* After determining access requirements, TS-Database Operations should review existing security groups that have access to the server for an appropriate role.
    - If an appropriate role exists, send the group name to the requestor to submit a jhNow "Access" Request.  Identity Management will process the request according to their process.
    - If an apprpriate group doesn't exist, TS-Database Operations will submit a case to Identity Management via jhNow to request a new "Security Group" matching the access needs and naming convention below.
* Once the Security Group has been created, TS-Database Operations will add the Security Group to the SQL instance and map the appropriate security roles.
    - Upon completion, the original requestor will need to submit a case an "Access" request via jhNow to be added to the newly created security group.

## Security By Service Naming Standards

Groups will be named based on the database the user is requesting access to. The format of these group names should be as follows:

JHA-PSA-JCSDBA-DB-[SERVERNAME\CNAME]-[DATABASENAME]-[R,M,O]

The final character designates the level of access being granted:
R - Read (read, execute, view definition)
M - Modify (write, read, execute, view definition)
O - Owner (db_owner)

Examples for MMOESDSQL are listed below:

- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-PAS-M 
     - Grants Modify access to the PAS database on MMOESDSQL
- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-PAS-R 
     - Grants Read access to PAS database on MMOESDSQL
- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-PolicyCenter-M 
- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-PolicyCenter-R 
- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-SurveyData_External-M 
- MONETT\JHA-PSA-JCSDBA-DB-MMOESDSQL-SurveyData_External-R 

## Governance
Identity Management sends "Access Reviews" via Sailpoint to active directory group owners.  Owners have the responsibility to ensure group membership is appropriate for their application and/or database.

TS-Compliance Operations initiates a quarterly access review.  TS-Database Operations is responsibile for delivering a complete list of groups and/or individual users.  Business units have the responsibility to approve access is appropriate.

---

*Created on: 4/11/2016*

*Last Reviewed on: 2/7/25*
