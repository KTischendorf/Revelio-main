---
title: "Naming"
author: "Vance Stokes"
date: "2024-10-30"
description: "A brief history of naming"
tags: ["network", "naming"]
---

## Introduction

There have been many standards and none of them have truly remained intact.  So, I'll try to break it down to the best of my ability.

One of the larger issues is that there isn't a clear standard for all teams in all orgs.  Please refer to Acronym Listing or another engineer if you have questions about a certain acronym.

## ATX-A1-1F-AS-01-MN

| Key  |  Description    |
|------|-----------------|
| ATX  | This is our Enterprise abbreviation notating the location of the device.  This is the first letter of the city's name and the state abbreviation.  There are a couple exceptions with cities that are multiple words. |
| A1   | This represents the building number, when needed. |
| 1F   | This represents the floor, when needed. Mostly in corporate environments. |
| AS   | This represents the function of the device.  This is an access switch. |
| 01   | This represents the device number.  It's usually a 2-digit number [XX] |
| MN   | This represents the business unit or network function.  This is management. |

## H-BMOQAD09-AS03

| Key  |  Description    |
|------|-----------------|
| H    | This device is in the HNS fabric. P represents the production fabric. |
| BMO  | This is the location of the switch. |
| QAD09| This is the rack it's in and location. This helps the data center team but doesn't truly help us that much. |
| AS   | This represents the function of the device. This is an access switch. |
| 03   | This represents the device number. It's usually a 2-digit number [XX] |

## MNATX-R01

| Key  |  Description    |
|------|-----------------|
| MN   | This represents the function of the device. |
| ATX  | This represents the location of the device. |
| R    | This represents the rack. |
| 01   | This represents the device number. It's usually a 2-digit number [XX] |

## COCNC-CS02

| Key  |  Description    |
|------|-----------------|
| CO   | This is a corporate operations switch. |
| CNC  | That is currently located in Charlotte, North Carolina. |
| CS   | This is a core switch. |
| 02   | This is the second core switch. |

## EPSATX-EDGE-FW

| Key  |  Description    |
|------|-----------------|
| EPS  | This represents the business unit this device supports. |
| ATX  | This is the location of the device. |
| EDGE | This is the function of this device. |
| FW   | This represents the type of device, in this instance a firewall. |

## Future Considerations


## Conclusion

It was originally intended for ease of use of identification and using regular expressions to easily sort/filter devices.  
