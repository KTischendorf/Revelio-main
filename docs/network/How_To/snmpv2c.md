---
author: "Vance Stokes"
date: "2024-10-17"
description: "SNMPv2c NX-OS non-ACI"
tags: ["network", "configs", "snmp"]
---
# SNMPv2c Nexus (non-ACI)

## 1. Enable SNMP

`switch(config)# feature snmp`

---

## 2. Configure the SNMP community string

`switch(config)# snmp-server community <community-string> group network-operator`

!!! note "FYI"
    `<community-string>`should be replaced with the correct value available in Secret Server.

- Below is the current grolup used across our nexus platforms.  This could also be change to `ro` for readability. `ro` is also a built-group.

```
Role: network-operator
Description: Predefined network operator role has access to all read
commands on the switch
-------------------------------------------------------------------
Rule Perm Type Scope Entity 
-------------------------------------------------------------------
1 permit read 
```

---

### Associate ACL to SNMP (secure SNMP)

`switch(config)# snmp-server community <community-string> use-ipv4acl SNMP-ACL`

---

## 3. Configure SNMP Server host (Trap Destination)

I need to get the IPs for this...

```nx-os
snmp-server host [ScienceLogic-IP] traps version 2c <community-string>
snmp-server host [ScienceLogic-IP] use-vrf management
```

---

## 4. Configure Traps

```
snmp-server enable traps config ccmCLIRunningConfigChanged
snmp-server enable traps snmp authentication
```

- On the lab devices these were the only traps enabled.  So, if the running configs changes or an auth against snmp happens, this device will fire off a trap to ScienceLogic.
- Configure trap types...look into this more

```
rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 log trap public description ERROR(3) owner PMON@ERROR
rmon event 4 log trap public description WARNING(4) owner PMON@WARNING
rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO
```

---

## SNMP Locations

```
snmp-server contact TECHOPS NETWORK ENGINEERING
```

---

## SNMP Contact

```
snmp-server location GC-MN
```

---

## Example Configuration/Template

```
snmp-server contact TechOps Network Engineering
snmp-server location <location>
snmp-server host <TRAP VIP> traps version 2c <SNMP Community String>
snmp-server host <TRAP VIP> use-vrf <VRF NAME>
rmon event 1 log trap public description FATAL(1) owner PMON@FATAL
rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 log trap public description ERROR(3) owner PMON@ERROR
rmon event 4 log trap public description WARNING(4) owner PMON@WARNING
rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO
snmp-server enable traps config ccmCLIRunningConfigChanged
snmp-server enable traps snmp authentication
snmp-server community <SNMP Community String> group network-operator
snmp-server community <SNMP Community String> use-ipv4acl <ACL NAME>
```

### Variables Needed

- `<TRAP VIP>`
- `<VRF NAME>`

---

## Validation Commands

- `show run snmp`
- `show snmp community`
- `show snmp host`

## Validation (Dangerous)

!!! danger "DANGER"
    This command could cause the device to become unresponsive, especially if multiple devices are polling the device being troubleshot.  If you believe this is needed, please reach out to a couple of engineers and discuss it

`debug snmp packets`
