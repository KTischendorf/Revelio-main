---
author: "Vance Stokes"
date: "2024-11-22"
description: "Infoblox Overview"
tags: ["network", "infoblox", "ToC"]
---

# Infoblox Overview

## Table of Contents

## Introduction

- Overview
- High Level Drawings
- Physical Drawings

## Hardware Design Life Cycle

Currently we don't utilize any physical appliances outside of the lab environment and need to be looking at
utilizing a workflowed implementation, a "just in time" solution that will allow us the ability to test the changes
but turn down the lab after research has been completed.  This could be one of the first introduction out of documentation as
code

## Software Design Life Cycle

This will take more work as this is a virtual implementation.  (Place link for upgrade process here).

- How are we following the Infoblox Software Cycles, not to be constantly put in Upgrade out of necessity situation.
  - Which trains should be hook to create a process?
  - **Upgrade groups**, future proofing using other services, i.e. DNS on seperate nodes and not rebooting at the same time.
  - **Upgrade Process**, how are we going to handle this, what is the process for this?

### Licenses

Visit [Infoblox Support Site](https://support.infoblox.com).  Click on the *My Products* tab on the top.

- All licenses Valid through 2027

## Access

JH is currently evolving, jhNow is the central work point across the enterprise.  As we progress to the future, Infoblox
will be the source of truth for all IPs across the enterprise.  With that all users will maintain read rights but GUI based admin rights will be given to a select view to deal with issues on the system and workflows.

### Admin Connectivity

JKHY AD Group will give Admin rights based on group policy

### User Connectivity

- [GUI JKHY](https://jhaddi.jkhy.com) or [GUI JHTechservices](https://jhaddi.jhatechservices.com/ui)
- API, same urls will be used.

Both mechanisms will eventually be *Read-only*

### Support Cases

Support cases can be opened by any user that has been given the rights from the portal page.

- Procedures on how to open a support case.