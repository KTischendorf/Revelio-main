---
author: "Justin West"
date: "2024-12-20"
description: "Backup Standards for Services Supported by MSDB Operations"
tags: ["DBops", "Database Operations", "TS-Database Operations", "MSDBOps", "DRE", "Site Transition", "Process Guide"]
---

# Site Transition Process Guide

## Overview
Site transitions are a result of both planned or unplanned efforts to move a services primary production data center to an alternate location.  This guide will outline the steps neccessary to ensure that site transitions are completed successfully with little to no data loss or downtime.

### Unplanned Events

### Planned Events
At the time of notice or 4 weeks prior to site transtion....
--- 
Info about CMS trees, reviewing service level documentation, ha/dr health checks, CPU/Ram Parity between datacenters, mirror backlogs, ag syncs, how to copy logins and jobs, SSRS Keys, Server Lists (if HPS consider using security groups to build CMS) post transition validation, validation of who from BU will test, dates/times, etc.
---

### Consult Service Level Documentation
Review of service level documentation is always advised but must be done for prior to transitioning the following services.
* jX, EES, ODI, CPS EAD or JKW.