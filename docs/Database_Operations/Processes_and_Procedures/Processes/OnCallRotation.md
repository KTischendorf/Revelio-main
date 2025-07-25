---
author: "Justin West"
date: "2025-01-15"
description: "Process Guide"
tags: ["DBops", "Database Operations", "SQL", "Process Guide", "On-Call", "Rotation", "Genesys"]
---

# DBA On-Call Rotation

## Summary
This process guide outlines steps neccessary to prepare to be on-call as well as ensure calls will route to the next DBA in the on-call rotation.  Additionally, it highlights core expectations for the DBA On-Call.

## Description
DBA On-call ensure contiunity of service after hours and weekends.  DBA's are expected to be responsive to calls initiated via the on-call number or via automated system alerts.

## Process
### Week Prior to On-Call
1. Login to each domain that DBOps supports to ensure active credentials.  A list will be available in future iterations of this document.
2. If Credential has expired, utilize [Self-Service Password Reset](https://bupr.jhatechservices.com/my.policy) to reset your password.  Once complete, login to ensure access is functional.
3. If your credential no longer exists, submit a [jhNow Request](https://jhnow.service-now.com/) to Identity Management to have new credentials create.  Manager and/or Business Unit approval may be neccessary to create new credentials, please escalate to your direct report to ensure approval.

### Morning of On-Call

#### Roll Over DBA On-Call Phone Number to your cell phone
1. Login to the [Genesys Cloud Website](https://apps.usw2.pure.cloud/)
2. Login utilizing the "DBA On-Call Genesys" credentials from https://vault.jhatechservices.com/
  >**_NOTE:_** If this is the first time you've logged in you'll need to select "More Login Options" and use the "jackhenry" organization name.

3. If prompted choose "Collaborate/Communicate
4. Click the profile button
5. Choose "Forward My Calls"
6. Ensure "Forward calls is toggled to 'On'"
7. Enter your phone number in the format +1XXXXXXXXX in the Find me at the following numbers section.
8. Click the X at the top right and log out.

Upon completion of rolling over, test the call by using teams to dial out or have a peer dial the on-call number.

#### Test Everbridge Notification
Between 9:30am and 10:00am on Tuesday morning, a test everbridge notification will be sent.  Do not acknoledge the notification until you've confirmed that email, text and phone call have been received. If you do not receive the notification, please contact your direct report to review Everbridge.

### Expectations
On-call available is critical to the health of our services.  Call are expected to be answered/acknowledged within 15 minutes.  If it's an automated Everbridge alert, acknowledgement via the prompts is fine.  If a jh employee leaves a message, please contact them ASAP via Teams or a call back number.  In addition to ad-hoc pages, afterhours work for a variety of services may be required.  These include but aren't limited to DRE's, application upgrade/maintenance, patching, etc. 

**Important:** If you find yourself unavailable to assist with a call (ie.. multiple calls, stuck in traffic, dropping kids off at school, etc.) please reach out to the team or management to ensure timely response.


*Created on: 6/25/19*

*Last Reviewed on: 4/10/25*
