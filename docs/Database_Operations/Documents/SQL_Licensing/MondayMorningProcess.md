---
author: "Darren Cole"
date: "2025-04-17"
description: "SQL Server Licensing Monday Morning Process"
tags: ["DBops", "Database Operations", "SQL Server", "Chargeback", "Finance"]
---

# Monday Morning Process
Monday morning Process on BMOMNDSHOST01P.JKHY.COM,54277

    •	Connect to BMOMNDSHOST01P.JKHY.COM,54277
    •	E:\DBAProjects\SQLLicensing\Scripts
    •	Make sure two VROPS files are in the “Dropzone” folder. 
    •	The SCCM file will  be in the root “SQLLicensing” folder after running the Exports script.
    •	Run 1_Exports-(Gets SCCM Data)
    •	Run 2_Imports
    •	Run job SQLLICENSING_V2
    •	Check the dbo.vw.Tallies table under SQL Licensing, Views to make sure data pulled in correctly for the current date.

1.	Run these scripts first after data is update to current date (no changes to scripts need to be made):

  	    Symitar Solutions to Symitar Member Alerts
        Begin Tran
        update [SQLLicensing].[dbo].[SQLLicensingTrending]
        set ServiceGroupName = 'Symitar Member Alerts',
        ServiceGroupPrimaryContact = 'Jordan Vanderflier',
        ServiceGroupSecondaryContact = ''
        where CostCenter = '149700'
        and ServiceGroupName = 'Symitar Solutions'
        --rollback tran
        --commit tran
 
Direct Line Wires

        Begin Tran
        update [SQLLicensing].[dbo].[SQLLicensingTrending]
        set ServiceGroupName = 'Direct Line Wires',
        CostCenter = '114002',
        ServiceGroupPrimaryContact = 'TS-Enterprise Shared Svcs Ops',
        ServiceGroupSecondaryContact = 'Brent Miller'
        where CostCenter = '114004'
        and ServiceGroupName = 'Direct Line Wires'
        --rollback tran
        --commit tran

3.	Check for NULL cost centers: (Will need to assign cost center and service group if null, in Trending and the Lookup server. I use the Trending and Lookup server scripts below and fill in the information. You will need to find similar servers for the cost center and service group. The data no longer pulls in since Gambit went away.)

Check for Null’s and new servers in Trending:

         SELECT [FQDN]
        ,[Full_Domain_Name]
        ,[CostCenter]
        ,[ServiceGroupName]
        ,[ServiceGroupPrimaryContact]
        ,[ServiceGroupSecondaryContact] 
        ,DateCollected
        from SQLLicensingTrending
        where CostCenter is null
        and fqdn not like 'az%'
 
Check for Nulls and new servers in LookUpServer:

       SELECT [FQDN]
      ,[Server_Name]
      ,[LastCollectionDate]
      ,[InsertDate]
      ,[Cost_Center]
      ,[Domain_Name]
      ,[Service_Group_Name]
      FROM [SQLLicensing].[dbo].[LookUpServer]
      where Cost_Center is null

 

Update Trending Script:

    Begin Tran
    update [SQLLicensing].[dbo].[SQLLicensingTrending]
    set CostCenter = '##server costcenter##',
    ServiceGroupName = ##server servicegroup##,
    where fqdn =’##server FQDN##’
    --rollback tran
    --commit tran

Update Lookup Server Script:
 
    Begin Tran
    update [SQLLicensing].[dbo].[LookUpServer]
    set Cost_Center = '##server cost center##',
    Service_Group_Name = '##server servicegroup##'
    where fqdn = ‘##server fqdn##'
    --rollback tran
    --commit tran
