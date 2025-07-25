---
author: "Justin West"
date: "2024-12-20"
description: "Template"
tags: ["DBops", "Database Operations", "TS-DBOps", "YHB", "YHF", "YHS", "jhahosting", "BSA", "Yellow Hammer"]
---
# Yellow Hammer (BSA, Fraud, SAR)

## Service Description

Yellow Hammer is a suite of products utilized by FI's to meet Bank Secrecy Act regulations as well as reduce Fraud.  The product is slowly being replaced by Defender. 
> [**!WARNING**] 
> Yellow Hammer supports at least one Regional Banking Office customer.  When making changes, ensure you know what customer you're impacting.  

### Key Contacts
* BU Support - Tracye Johnson
* SO - Adam Gantman
* DBA - Jeffrey Hillier
* Service Abbreviation - YHB, YHF, YHS
* HPS SLA - Gold

## Environments

### Yellow Hammer BSA (YHB)

#### Description
Yellow Hammer BSA fully automates and centralizes compliance with the FI
Secrecy Act (BSA). This data monitoring, recordkeeping, and reporting
solution eliminates the time-consuming and error-prone manual
compliance process and mitigates the risks associated with BSA
compliance. Batch or near-real-time customer and transaction data can
be imported from JHA’s core processing platforms, wire transfer and teller
systems, and brokerage/trust databases and stored in a centralized
database for ongoing access and analysis. Yellow Hammer BSA automates
the customer due diligence required during the account opening process,
assigns risk ratings based on responses to specific questions, and supports
the accurate evaluation of risk based on proven metrics. The capabilities to
profile existing customers, perform peer group analyses, maintain research
analyst notes and actions, and generate management, board, and auditor
reports are also provided.

#### SQL Overview

Yellow Hammer BSA (Bank Secrecy Act) is a single tenant solution for external customers. Most servers are 2 node partners with a mix of mirroring and availability groups.  SQL Server Engine and SSRS are used and SSRS keys frequently are issues during site transitions. YHB largely follows DBOps standard practices; however, as of 12/31/24 the BU has an active finding to ensure db encryption is in place by 3/30/25.  


### Yellow Hammer Fraud (YHF)
#### Description
Yellow Hammer Fraud Detective automatically monitors account activity
from multiple touch points to identify potentially fraudulent transactions
and accounts with the highest probability of fraudulent activities.
Innovative data storage technology generates extremely accurate
representations of normal and abnormal account activity and spending
behavior, enabling suspicious transactions to be immediately identified
and researched online. This real-time system effectively and efficiently
reduces fraud related to checking and deposit transactions with the ability
to detect kiting, duplicate or out-of-sequence checks, checks with out-of-
range dollar amounts, suspicious check writing activities or signatures, and
multiple daily transactions. Yellow Hammer Fraud Detective helps FIs to
proactively protect themselves and their customers from fraud and the
related financial.

#### SQL Overview
Yellow Hammer Fraud is a multi-tenant solution for external customers.  This also houses Regional Banking Customers therefore caution should be exercised before making changes to any production server.

#### Critical Customers
Both Banner (Server Set 1) and Simmons (Server Set 27) are Regional Banks with non-standard recovery times.  In the event of a DRE or actual DR, priority should be given to these to FI's unless otherwise noted. 

### Yellow Hammer SAR (YHS)
#### Description
ipsom lorem

#### SQL Overview
ipsom lorem

### Non-standard Configs
Collation, non-standard sqlcare jobs, named instances, non-standard port, additional sqlcare jobs, ha/dr, etc

### Additional Links
* [HPS Business Partner Portal - YHB](https://jackhenry.sharepoint.com/sites/hpsyhbsa)
* [HPS Business Partner Portal - YHF](https://jackhenry.sharepoint.com/sites/hpsyhf)
* [HPS Business Partner Portal - YHS](https://jackhenry.sharepoint.com/sites/hpsyhsar)

* [RACI](Link) - 







