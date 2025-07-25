---
author: "Justin West"
date: "2024-12-20"
description: "Backup Standards for Services Supported by MSDB Operations"
tags: ["DBops", "Database Operations", "TS-Database Operations", "MSDBOps", "Audit", "Standards", "Backup"]
---
For Internal Use Only - Official copies of this document can be requested from TS-Compliance Operations.  Official copy also provides graphical overview of standard topography.

# TS – DO – Microsoft SQL Server Database Backup Standards
## Scope
Microsoft SQL Servers managed by Tech Services - Database Operations (TS-DO). The following standards are
applicable to all TS-Database Operations managed services unless specified otherwise in the service-level
documentation provided by the service owner or business unit (BU).

## Purpose
The purpose of this document is to establish the standards for backup and recovery of data managed by TS-
Database Operations. The implementation of the backup and recovery standards discussed in this document is
designed to provide protection against data corruption, natural disasters, and/or accidental data deletion.

### SQL Server Backup Methods
All versions of SQL Server utilize native backups with compression.

### Full Database Backup Guidelines
Full backups are scheduled weekly with a default start time between 7:00 p.m. and 6:00 a.m. CT to limit impact
to business operations.
Full database backup files are written to centralized database backup servers located in the respective domain.
For database backup retention, the database backup servers are backed up daily by the TS - Infra Tech Svcs
team using Commvault. Crash protection backups of the database backup server, and thus the database
backups, are retained for a period of no less than 14 days.

### Transaction Log Backup Guidelines
Transaction logs for all user databases are backed up every 15 minutes at a minimum. Transaction log backup
files are written to a centralized backup server in the respective domain for backup retention to match the
backup option chosen for full database backups of the service. System databases do not require transaction log
backups, as the recovery point of these databases is not production-critical to the service.

### Differential Database Backup Guidelines
Differential backups are optional for all user databases and, if enabled, occur every day except for the day of the
full database backup. Differential backup files are written to a centralized backup server in the respective
domain for backup retention to match the backup option chosen for full database backups of the service.
System databases do not require differential backups, as the recovery point of these databases is not
production-critical to the service.

### Database Backup Execution
Backups are scheduled and initiated through automated SQL Server Agent Jobs, which call a custom, stored
procedure. The parameter passed through the job specifies either FULL, DIFFERENTIAL, or LOG as the backup
type. These custom, stored procedures perform the backup.

### Database Backup Retention
Backups are retained on the backup server for the following periods.
• Full Backup - 8 days
• Differential Backup - A minimum of 1 day, when enabled, with a recommendation of 8 days if possible.
• Transaction Log - 8 days

### Database Backup File Synchronization
Due to the need for disaster recovery, the backup files mentioned in the Full, Transaction, and Differential
guidelines above are replicated to an offsite, disaster recovery location via Windows Distributed File System
Replication (DFSR) or scheduled Robocopy process, as demonstrated in the supplemental diagrams of the PDF
mentioned above.

### Database Backup Monitoring
TS-Database Operations has several monitors to alert for missing backups that have failed to complete within
specific tolerances for the execution standards.
AzureCare Open Events:
• SQL Server Job Failures
• SQL Server Missing Backups
• SQL Agent Job Alerts

### Database Backup Response
TS-Database Operations responds to identified issues in accordance with the service-level documentation
provided by the service owner or BU. Service owners or BUs may require TS-Database Operations to withhold
action due to processing or performance impacts that could occur. Service-specific backups remain scheduled as
normal even if action is withheld at the request of the service owner or BU.

