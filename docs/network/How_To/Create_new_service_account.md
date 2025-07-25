---
author: "Krystal Tischendorf"
date: "2025-02-18"
description: "How-To Create a New Service account."
tags: ["service account", "active directory", "how-to"]
---

## Introduction

This document provides a step-by-step guide for creating a new service account. It outlines the responsibilities, policies, and procedures to ensure compliance with Directory Services standards.

## Procedures

### Step 1: Ensure Approval

1. **Sub-step 1**: Ensure that specific approval has been given for the creation of the service account.
2. **Sub-step 2**: Directory Services is responsible for the creation, modification, and deletion of all service accounts unless otherwise approved.

### Step 2: Naming Conventions

1. **Sub-step 1**: Use the Full Name field to enter the complete name of the account.
2. **Sub-step 2**: This should include a summarized version of the use of the account, including the system and the process or task for which the account was created. Abbreviations are allowed. When character count allows, the name should include "service account" at the end.

#### Examples for Naming

- `svc-commvault` for a service account that runs all aspects of the Commvault system.
- `svc-f5-ldap` for a service account that performs LDAP queries for the F5 system.
- `svc-jhaknow-devqa` for a service account that runs all aspects of the Dev/QA instance of the jhaKnow system.
- `svc-coredir-auto-qa` for a service account that performs automation testing for the QA instance of the Core Director system.

### Step 3: Request a New Service Account in jhNow

1. **Log into jhNow**: Log into the jhNow system.
2. **Navigate to Access**: Go to the left-hand side of the screen and choose Access.
3. **Submit Request**: Follow the prompts to request a new service account.
4. **Choose "New Service Account"**: Then provide the information requested for each section in the form.
    - **Active Directory Domain**: Please add domain here using the search in the drop-down.
    - **Associated System/Application**: Please add the system or application name here.
    - **Task or Function**: Example: This will be the account that integrates with ____________ but will be used to _________________.
    - **Interactive Login Required?**: Yes or No
    - **Elevated Access Required?**: Yes or No
    - **Group Membership(s) Required?**: Yes or No
    - **Group List**: Please add your requested new account name here.
    - **Account Owner**: Please add the responsible associate’s name here using the search in the drop-down.
5. **Submit the Form**: Once the form is filled out, click on the blue “request” button.

### Step 4: Add the New Account to Secret Server

1. **Log into Secret Server**: Log into the Secret Server system.
2. **Navigate to the appropriate folder**: Go to the folder where you want to store the new service account credentials.
3. **Create a new secret**: Click on the "New Secret" button and choose the appropriate template for a service account.
4. **Enter the account details**: Fill in the details for the new service account, including the username, password, and any other relevant information.
5. **Save the secret**: Once all the information is entered, click on the "Save" button to store the new service account credentials in Secret Server.

## Additional Information

- Ensure that the service account credentials are stored securely and are not shared with unauthorized users.
- Regularly review and update the permissions assigned to the service account to maintain security.
- Monitor the activity of the service account to detect any unusual or unauthorized actions.

## Conclusion

Creating a new service account involves ensuring approval, submitting a request, assigning permissions, verifying compliance, following naming conventions, and adding the account to Secret Server. By following this guide, you can ensure that the service account is created correctly and securely. If you encounter any issues, refer to the additional information section or contact your system administrator for assistance.
