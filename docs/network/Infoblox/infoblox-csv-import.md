---
author: "Vance Stokes"
date: "2024-12-05"
description: "Infoblox Import Procedures"
tags: ["network", "infoblox", "procedures", "import"]
---

# Infoblox CSV Import Procedures

## Overview

This document provides detailed procedures for importing data into Infoblox using CSV files. The import process allows you to quickly add or update records in Infoblox without manual data entry. By following these steps, you can streamline the management of your IP address and DNS records.

## Prerequisites

Before you begin the import process, ensure you have the following:

- Access to the Infoblox GUI.
- A valid CSV file containing the data to import.
- Knowledge of the required fields and data format for the import.

### CSV File Format

The CSV file should be formatted correctly to match the fields in Infoblox. Each row in the CSV file represents a record to be imported, and each column corresponds to a field in Infoblox. Make sure the CSV file follows the required format to avoid errors during the import process.

#### Sample CSV File Format

```csv
HEADER-Type, configure_for_dns, FQDN, ADDRESSES, comment, network_view
HostRecord, FALSE, test.infoblox.lab.com, 10.1.1.1, test, Jack Henry Enterprise
```

#### Required Fields

| Header Value | Required | Description |
|---|---|---|
|**HEADER-Type** | Yes | The type of record to import (e.g., HostRecord, Network, etc.). |
| **configure_for_dns** | No | Indicates whether the record is configured for DNS (TRUE or FALSE). |
| **FQDN** | Yes | The Fully Qualified Domain Name of the record. |
| **ADDRESSES** | Yes | The IP address associated with the record. |
| **comment** | No | Additional comments or notes for the record. |
| **network_view** | Yes | View the record will be inserted to, *blank will go to the default view* |

### Infoblox Access

Ensure you have the necessary access to the Infoblox GUI to perform the import.

### Permissions

Verify that you have the appropriate permissions to import data into Infoblox.

## Import Process

### Steps

1. Log in to the [Infoblox GUI](https://jhaddi.jkhy.com).
2. Navigate to the **Data Management** tab.
3. Click on **Import**.
4. Select the **CSV File** to import.
5. Choose the **Import Type** (Add or Update).
6. Map the **CSV Columns** to Infoblox Fields.
7. Review the **Import Summary**.
8. Click **Import** to start the import process.
9. Monitor the import progress.
10. Verify the imported records in Infoblox.

### Additional Information

- It is recommended to test the import process with a small dataset before importing large files.
- Backup your data before performing any imports to avoid data loss.
- Use csv validation tools to ensure the file is formatted correctly.
- If the `network view` isn't a configured column, it will default to the default view.
- Make sure the CSV file is formatted correctly to avoid errors during the import.
- If you encounter any issues during the import, check the logs for error messages.
  - This file can also be used to re-import as long as the first column is deleted.

## Conclusion

The CSV import feature in Infoblox provides a convenient way to manage IP address and DNS records efficiently. By following the steps outlined in this document and ensuring data accuracy, you can maintain a reliable and up-to-date IP address management system. If you have any questions or need assistance with the import process, contact Infoblox Support for help.
