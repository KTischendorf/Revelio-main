---
author: "Brent Bohannon"
date: "2025-4-24"
description: "Python Update"
tags: ["DBops", "Database Operations", "CARE", "SQLCARE", "AZURECARE", "python", "upgrade", "kenna"]
---
# Updating Python on DSMS SQLCare Agent Servers
[Agent Code Repository](https://github.com/jkhy/data-engineering-care-agentp/blob/main/win/README.md)

---

## *Before You Begin*
- Collect the following files in a compressed(.zip) folder
  - [Python Installer for windows](https://www.python.org/downloads/)
  - [Newest versions of the pytz .whl file](https://pypi.org/project/pytz/#files)
  - [Newest version of the pyodbc .whl fle](https://pypi.org/project/pyodbc/#files)
- Place the zip file on the JKHY management server so it can be copied to each Agent server in each Domain
---

## Update Steps
- Log in to the Server
- Copy the zip file containing the installation files to the E:\ drive of the server
- Extract the files to E:\Python
- Stop and Disable the AzureCare - Gather Events Scheduled Task
- Go to Control Panel --> Programs and Features, uninstall the old version of Python
- Delete the old Python folder out of C:\Program Files
- Run the new Python version's Installer
  - Check "Use Admin Priviledges", "Add python.exe to PATH" and Select "Customize Installation" --> NEXT
  - Make Sure "pip" and "for all users" are checked --> NEXT
  - Check "Install Python for all users" and "Add Python to Environment Variables"
  - Change the install directory to C:\Program Files\Python --> INSTALL
- Once the installer is done, open a command window or powershell window
  - change directory to E:\Python\
  - run "pip install pyodbc-XXXXX.whl" *use tab auto-complete to choose the file in the directory* 
  - run "pip install pytz-XXXXX.whl"  *use tab auto-complete to choose the file in the directory* 
  - change directory to E:\PowerShellScripts\AzureCARE\
  - run "python agentp.py" and verify that no errors occur
    - look in console output
    - Check the log file for the agent (E:\PowerShellScripts\Azure\Log\agentpAll)
  - ctrl-c and close the powershell window
- Edit the scheduled task and ensure the targed is pointing to C:\Program Files\Python
- Re-Enable the task and Run it.
- Check the end of the log file in E:\PowerShellScripts\AzureCARE\Logs to make sure there are no errors
  - The ouput should say Gathering Events or Event Gathering Complete
