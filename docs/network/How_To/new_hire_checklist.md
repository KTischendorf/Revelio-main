---
author: "Krystal Tischendorf"
date: "2024-11-29"
description: "New Hire Checklist"
tags: ["new hire", "checklist", "onboarding"]
---

## Introduction

This document provides a checklist for new hires, detailing the necessary software and tools required for different platforms (PC, Mac, and Multi-Platform).

## Procedures

### PC Specific Items

1. **Microsoft Visio**: Found in Software Center
2. **Observer**
3. **BitLocker to Go Exception**
4. **USB to Serial Drivers for Console Cable**
    - Might want to put the General Access -CORP before this so people can find these easier

### Mac Specific Items

1. **Omnigraffle**
2. [**Draw.io desktop software**:](https://draw.io)
3. **iTerm 2**: Secure CRT also available
4. **Remote Desktop Client 10**

### Multi-Platform Items

1. [**Visual Studio Code with XML Tools Extension**](https://code.visualstudio.com/)
2. [**Notepad++ with Compare add-in or Beyond Compare**:](https://notepad-plus-plus.org/)
3. [**F5 VPN – RA**:](https://ra.jhavpn.com/)
4. [**Postman**:](https://www.getpostman.com/)
5. [**Webex Teams**:](https://www.webex.com/team-collaboration.html)
    - Create a new account with JH email address
6. [**Wireshark**:](https://www.wireshark.org/)
7. **Secure CRT**: If a local install is wanted. Access via Jumpbox preferably.
    - Install found in Network Share - fn
8. **Microsoft Teams**: Found in Software Center
9. [**StructureWare DCIM**:](https://etsatxswdco01p.jkhy.com/web/#/)
10. [**WinSCP or other FTP/SCP Client**:](https://winscp.net/eng/index.php)

### File Shares

1. **User Directory**
    - (PC) `\\jhacorp.com\mmo\Users\[username] H:`
    - (MAC) `smb://jhacopr.com/mmo/users/[username]`
2. **Team Share**
    - (PC) `\\jhacorp.com\mmoco\Groups\Network Admins`
    - (MAC) `SMB://jhacorp.com/mmco/groups/network admins`
3. **CatTools, current configs**
    - (PC) `\\mmonetworkapp\c$\Program Files (x86)\CatTools3\Configs`
    - (MAC)
4. **CatTools, old configs**
    - (PC) `\\mmonetworkapp\c$\Program Files (x86)\CatTools3\Dated Configs`
    - (MAC)
5. **Corporate Office Pics**
    - `\\mmocofs02\groups\CorpOps\OfficePictures\`

### Remote Desktop Sessions

1. **Old List**
    - `ATXTORDSFARM.jkhy.com`
    - `BMOMNRDS01.jkhy.com`
    - `BMOTORDS01.jkhy.com`
    - `ETSMMONETAPP.jkhy.com`
    - `ETSMMONETWORKAPP.jkhy.com`
    - `MMOCONETAPP.jhacorp.com`
    - `MMOCONETAPP2.jhacorp.com`
    - `MMOTORDSFARM.jkhy.com` (reset JKHY creds)
    - `SMOCONETAPP.jhacorp.com`
    - `SMOCONETAPP2.jhacorp.com`
2. **New Remote Desktops**
    - `PEATX3NETWORK.jkhy.com`
    - `PEMMONETAPP.jkhy.com`
    - `PEATX3NETAPP.jkhy.com`

### Jumpbox Installed Apps

1. **Kee Pass**
2. **Easy IP**
3. **Cherwell**
4. **Observer**: Console to review packet captures.
5. **Cat Tools**: mmonetworkapp only.
6. **ASDM**: mmoconetapp2 only
7. **Secure CRT**
    - Configuration file located at `C:\Users\Public\Desktop\SecureCRT\`

### Web Apps

1. [**Akips**: Network device SNMP monitoring](https://akips.jhacorp.com/)
2. **CA Suite**
3. [**Thousand Eyes**](https://app.thousandeyes.com/login)
4. [**Splunk**: Centralized logging](https://jhasvc.splunkcloud.com/en-US/app/ncc) 
5. [**Change Point**: Project time tracking](https://changepoint.jackhenry.com)
6. [**Cloud Vision**: Arista](https://www.cv-prod-us-central1-c.arista.io/cv/devices)
7. [**ACI APIC’s**: ACI APICS Bookmark](https://jackhenry.sharepoint.com/:x:/r/sites/teoantc/_layouts/15/Doc.aspx?sourcedoc=%7BF791EE21-22D9-4D22-93F5-B9573B68278B%7D&file=APIC%20Serial%20Numbers.xlsx&action=default&mobileredirect=true)
8. [**Cisco ACI Network Assurance Engine (Candid)**: Local account – Cword](https://10.225.239.250/#/login?redirect-to=%2523%252F)
9. [**SOC Portal**: Change Management](https://soc.jackhenry.com/)
10. [**SmartNet Total Care Collector**](https://services.cisco.com)
11. **ISE**: wireless
12. [**jSource**: jhaToday > Tools & Info > jSource (CRM)](https://crm.jhacorp.com/psp/CRM92PRD/?cmd=start)
13. **Cisco Prime Infrastructure**
14. [**Cisco DNA Center**](https://10.1.1.64/)
15. **Python (v3)**
16. [**Corporate Account unlock**](https://resetme.jackhenry.com)

### Web Portals

1. **Carrier Portals**
2. **Arista Portal**
3. **Meraki Portal**
4. **Cisco Portals/Contracts**
    - `2541716,3673696,90229886,90278656,92193567,93993469,94427388,95404136.95755779,95732362`
    - `201111220,201126788,200392286.201462547,94588746,95521509,95713932,95907490,96028832`
    - `201296379,201412889,201444051,201471423,201498278,200773387`

### General Access – CORP

1. Mirror AD groups after csegalas
2. **Microsoft Teams Rooms**
3. [**NCC Website**](https://jackhenry.sharepoint.com/sites/ncc)
4. **Network Share**: `\\jhacorp.com\mmoco\Groups\Network Admins\`
5. **Network Share**: `\\jhacorp.com\mmoco\Groups\CorpOps`

### General Access – JKHY

1. Mirror AD groups after Chas – This will take care of TACACS

### Terms to know

1. **ION**: Infrastructure Operations Network (no production traffic)
2. **PNF**: Production Network Fabric
3. **Border Leaf**: Leaf switch connected to something permitting comms beyond the fabric
4. **CR**: Change Request
5. **MOP**: Method of Procedure

### Network and BU Training

1. **Network & BU Training**: Presentations

### Things to know

1. High IP addresses (.254;.253) are firewalls
2. Low IP addresses (.1;.2;.3) are almost always F5 LB or routers

### Cherwell access

1. Open a ticket requesting access
    - **TechOps - Network Services**
    - **Change Management Support**
    - **TechOps - Network Services**
    - **TS-NCC**

### Jsource

1. Go through training on JHU
    - 100, 105, 110

## Conclusion
This checklist provides a comprehensive guide for new hires to ensure they have all the necessary tools and software for their respective platforms. By following this checklist, new hires can quickly set up their work environment and be ready to contribute effectively. If there are any issues or additional requirements, please reach out to the IT support team for assistance.
