---
title: "Carrier Maintenance"
author: "Krystal Tischendorf"
date: "2024-11-25"
description: "Guide for managing carrier maintenance activities, including entering notices, handling updates, sending notifications, and managing scripts."
tags: ["template", "process", "carrier maintenance", "procedures"]
---

# Carrier Maintenance Process

## Introduction

This document outlines the procedures for managing carrier maintenance activities. It provides detailed steps for entering maintenance notices, handling updates on the day of maintenance, sending notifications, and managing maintenance scripts. The goal is to ensure a smooth and efficient process for maintaining carrier services with minimal disruption.

## Procedures

### Step 1: When New Notices Are Received

1. **Enter maintenance into the [maintenance calendar](https://jackhenry.sharepoint.com/sites/teoantc/Lists/Carrier%20Maintenance/calendar.aspx)** 
    - If notice indicates an update to the previous schedule, modify the existing entry based on carrier reference number.
    - If notice indicates an upcoming maintenance was cancelled, you may delete it from the calendar.

### Step 2: On the Day of the Maintenance

1. **Check email for any updates to the carrier maintenance based on carrier reference number provided**.
2. **Send out appropriate notifications**.
3. **If carrier maintenance scripts are in use**:
    - Enter CR for Carrier Maintenance.
    - Coordinate who will put circuit into maintenance mode that evening and who will return it to production the next morning.
    - Place/check maintenance mode status in Monitoring.
    - Send completion notification after maintenance has ended.
    - Revert carrier maintenance script after maintenance is completed.

### Step 3: Entering Carrier Maintenance into the Maintenance Calendar

1. **Log into the [CID Listing](https://jackhenry.sharepoint.com/:x:/r/sites/teoantc/_layouts/15/Doc.aspx?sourcedoc=%7BD857B341-D63D-4F09-874E-4FA7C4099EEE%7D&file=CID%202.0.xlsx&action=default&mobileredirect=true) to determine what actions need to be taken for the circuit**.
2. **Log into the [Carrier Maintenance - Calendar](https://jackhenry.sharepoint.com/sites/teoantc/Lists/Carrier%20Maintenance/calendar.aspx) and enter the carrier maintenance activity**:
    - Locate the date in question and click on “add”.
    - Title will be “Carrier Name (Circuit ID)”.
    - Location can be left blank.
    - Start & End time need to be entered in US Central Time.
    - All carrier notices should be converted accordingly.
    - Description will be a copy of the full emailed notice.
    - Category will be as follows:
        - Script – CID List indicates there is a Maintenance Script and notification.
        - Notification Only – CID list indicates that we are to send notification without a script.
        - No action – No actions are being taken proactively but maintenance is being entered for tracking purposes.

### Step 4: Sending Notifications

1. **Before the maintenance activity begins**:
    - Access the notification templates from the document repository at Maintenance Notification Templates.
    - Open the appropriate notification based on actions needed per the [CID Listing.](https://jackhenry.sharepoint.com/:x:/r/sites/teoantc/_layouts/15/Doc.aspx?sourcedoc=%7BD857B341-D63D-4F09-874E-4FA7C4099EEE%7D&file=CID%202.0.xlsx&action=default&mobileredirect=true)
    - Modify the notification template to reflect the details of the upcoming maintenance activity.
    - Change the “From” line to “Tech Services”.
    - Leave the to & cc lines blank.
    - Default addresses should auto populate in the BCC field.
    - For Notifications to remote sites, you will also need to add the site distribution list from the address book, if one exists.
    - Change the Beginning and Completion dates.
    - Update the body of the email to reflect the appropriate information.
    - Make sure your signature is NOT included at the bottom of the notification.

2. **After maintenance activity has ended**:
    - Access the previously sent email notification.
    - Modify the notification template to reflect the details of the completed maintenance activity.
    - Change the “From” line to “Tech Services”.
    - Make sure the “to” & “cc” lines are blank.
    - Copy the address list from the previous email or from the appropriate template into the BCC field.
    - Change the Beginning and Completion dates.
    - Status will be “Completed”.

### Step 5: Entering a CR for Carrier Maintenance with Maintenance Scripts

1. **Open ServiceNow and select the preapproved change “Layer 3 (routing) - Carrier - Routing | Route Map | Modify | Internet BGP”**.
2. **Fill in the CR required fields**:
    - Include the carrier circuit information in the description.
    - Schedule will start at 8:30 PM CT and end at 8 AM CT the following morning.
    - Assign primary CR to one engineer that will be working on the maintenance.
    - After saving CR, scroll down to the Change Tasks tab.
    - Enter 1 Change Task to put the circuit into maintenance mode that evening and assign to appropriate engineer.
    - Enter 1 Change Task to return the circuit to production mode the following morning and assign to appropriate engineer.

3. **When Implementing**:
    - Each engineer start and close their task for their actual work timing for that portion of the process only.
    - Close Primary CR as follows:
        - Start time will be the time circuit was placed to maintenance mode.
        - End time will be the time the circuit was returned to production mode.
        - Closure information will reflect the carrier maintenance status.
        - Make sure to review for successful carrier completion before closing as successful.

### Step 6: Entering Carrier Maintenance Scripts

1. **Navigate to the Maintenance Scripts folder in the repository**.
2. **Locate the appropriate circuit script as indicated by CID Listing and confirmed by circuit number listed**.
3. **Log into devices indicated by the script**:
    - Prior to returning devices to production mode, confirm that the interface is up after carrier maintenance is complete.
    - Input the indicated routing change details per the script.
    - Log into [AKIPS](https://bmoakips.jhacorp.com/) Network Monitor and select the Interface Dashboard.
    - Locate your device and interface and make sure traffic moves away or returns as expected on the interface.
    - Document in the appropriate change task on your CR.

### Step 7: Placing Monitoring into Maintenance Mode

1. **Log into RestorePoint and locate your device**.
2. **In top right corner, enter your device name into “Device Search” field**.
3. **Navigate to “Interfaces” tab under Component Detail for the device**:
    - Locate the interface being modified per the maintenance script.
    - Right click on the interface you are modifying.
    - Select Utilities -> Schedule Maintenance.
    - Add the maintenance schedule to match the planned carrier maintenance window.
    - If this is a first time schedule:
        - Select the “Create” button under the left section of the popup.
        - Change your start date and select the appropriate start and end times for carrier working window only.
        - Leave recurrence as “none”.
        - Click “OK”.
    - If this schedule has been used previously:
        - Locate the appropriate date & time schedule in the “Available Schedules” window.
        - Click the left arrow between the 2 sections of the schedule popup.
        - Click “OK”.

4. **Repeat for all interfaces & port channels included in your script**:
    - If script does not identify a single interface or interface tab is unavailable:
        - From the “Information” tab on Component Details scroll to “In Maintenance”.
        - Click the “Schedule” button and follow steps above.
        - This will put the entire device in maintenance.
        - This is NOT a first choice as we will lose visibility to all device issues, not just maintenance related issues, during the maintenance window.
        
5. **Interfaces/Device will return to normal monitoring at the end of the indicated maintenance schedule**.

## Conclusion

Following these steps will help ensure that carrier maintenance is handled efficiently and effectively. Consistent communication and coordination are crucial for maintaining the integrity of our network infrastructure.
