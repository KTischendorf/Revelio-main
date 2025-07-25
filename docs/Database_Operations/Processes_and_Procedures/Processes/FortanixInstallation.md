---
author: "Justin West"
date: "2025-01-1516"
description: "Process Guide"
tags: ["DBops", "Database Operations", "Process Guide", "Fortanix", "Key Rotation", "TDE"]
---

# Fortanix Installation

## Summary
This process guide outlines steps neccessary to install Fortanix as well as begin the encryption process.  Fortanix is utilized to manage the TDE encryption key so that a DBA is not required know, touch or see the encryption key.

### Prerequisites

1. Request EKM Provider and DSM API Key from Systems Security. 
2. Ensure "GlobalSign Code Signing Root R45.cer" is installed in Trusted Root Certification Authorities (certlm.msc):
3. Run the following on all instances that will have encryption set up. It logs message_id 15466 to the windows application log so scom can detect decryption errors. 
    ``` sql
	exec sp_altermessage 15466, 'WITH_LOG', 'TRUE';
    ```
### Installation
1. Install the client using the SCS [installer v4.31.2462](https://artifactory.jkhy.com/artifactory/scs-systems-security-gen/Fortanix/Scripts/FortanixInstallClientScript_SQL_Bulk_V1.3_client_4.31.2462.ps1]).
   
2. Create the Cryptographic Provider
EKM_Prov refers to the name of the provider defined by the user

    ``` sql 
	CREATE CRYPTOGRAPHIC PROVIDER EKM_Prov
	FROM FILE = 'C:\Program Files\Fortanix\KmsClient\FortanixKmsEkmProvider.dll' ;
	GO
    ```
 
 
3. Run the following commands to create a credential using the API key
>**_NOTE:_** DSM API KEY refers to the generated key provided by Systems Security

   ``` sql
	CREATE CREDENTIAL sa_ekm_tde_cred
	WITH IDENTITY = 'Identity1',
	SECRET = 'DSM API KEY' 
	FOR CRYPTOGRAPHIC PROVIDER EKM_Prov ;
	GO
   ```

 
4\. Add the credential to a high privileged user such as your own domain login in the format [DOMAIN\login]:
>**_NOTE:_** Login should be a sys admin and it can be deleted after rotating or setting up Fortanix
 
 ``` sql 	 
	CREATE LOGIN [MONETT\JCSADM**] FROM WINDOWS 
	ALTER LOGIN MONETT\JCSADM**
	ADD CREDENTIAL "sa_ekm_tde_cred";
	GO
 ```
    
If you are not an administrator and hence unable to alter the login, open the Object Explorer and map the credentials as shown in the following image:
 
	  
5\. Run the following commands to generate a new asymmetric key using the Fortanix External Key Manager (EKM) Provider
>**_NOTE:_**
> * ekm_login_key refers to the master key alias on the MSSQL database.
> * EKM_Prov refers to the Fortanix EKM Provider.
> * SQL_Server_Key_v2 refers to the key created on the Fortanix DSM.

* For Standalone Server or AOAG Primary Replica

    ``` sql
	USE master ;
	GO
	CREATE ASYMMETRIC KEY ekm_login_key_v2
	FROM PROVIDER EKM_Prov
	WITH ALGORITHM = RSA_2048,
	PROVIDER_KEY_NAME = 'SQL_Server_Key_v2' ;
	GO
    ```
    ** Example:

    ``` sql	
	USE master;
	GO
	CREATE ASYMMETRIC KEY sql_jsource_standin_v1
	FROM PROVIDER [EKM_Prov]
	WITH ALGORITHM = RSA_2048,
	PROVIDER_KEY_NAME = sql_jsource_standin_v1
	GO
    ```
* For AOAG Secondary Replicas: 

    ``` sql	 
	USE master ;
	CREATE ASYMMETRIC KEY ekm_login_key
	FROM PROVIDER EKM_Prov
	WITH PROVIDER_KEY_NAME = 'SQL_Server_Key',
	CREATION_DISPOSITION = OPEN_EXISTING;
	GO
    ```
    ** Example: 
 
    ``` sql 
	USE master
	CREATE ASYMMETRIC KEY sql_jsource_standin_v1
	FROM PROVIDER EKM_Prov
	WITH PROVIDER_KEY_NAME=sql_jsource_standin_v1
	CREATION_DISPOSITION = OPEN_EXISTING; 
	GO
    ```
	 
6\. Run the following commands on any standalone and all replicas of an AOAG to create a credential that will be used by the database engine:
>**_NOTE:_**
>* ekm_tde_cred refers to the name of the credentials.
>* EKM_Prov refers to the Fortanix EKM Provider.
>* SECRET refers to the Fortanix DSM API key.

   ``` sql	 
	USE master ;
	GO
	CREATE CREDENTIAL ekm_tde_cred_v2
	WITH IDENTITY = 'Identity_v2',
	SECRET = '{key}'
	FOR CRYPTOGRAPHIC PROVIDER EKM_Prov
   ```	 
	 
7\. Create Login for DB Engine on all SQL nodes
>**_NOTE:_**
>* ekm_login_key refers to the master key alias on the MSSQL database. This key is already created on  step 5  "Creating Asymmetric Keys".
>* EKM_Login refers to the login name.
>* ekm_tde_cred refers to the key created on the Fortanix DSM. This credential is already created on step 6 ''Creating Credentials".

   ``` sql	 
	CREATE LOGIN EKM_Login_v2
	FROM ASYMMETRIC KEY ekm_login_key_v2 ;
	GO
	ALTER LOGIN EKM_Login_v2
	ADD CREDENTIAL ekm_tde_cred_v2 ;
	GO
   ```

8\. Rotating Master Encryption Key (MEK)
Run the following commands on the standalone server or primary replica to rotate the Master Encryption Key (MEK) for Data Encryption Key (DEK):
 	 
    ``` sql	 
	USE <database>
	ALTER DATABASE ENCRYPTION KEY
	ENCRYPTION BY SERVER ASYMMETRIC KEY ekm_login_key_v2;
    ```

9\. Validate status of the encryption by executing the following script
    
    ``` sql	 
	SELECT DB_NAME(database_id) AS DatabaseName, encryption_state,
	encryption_state_desc =
	CASE encryption_state
	WHEN '0'THEN 'No database encryption key present, no encryption'
	WHEN '1'THEN 'Unencrypted'
	WHEN '2'THEN 'Encryption in progress'
	WHEN '3'THEN 'Encrypted'
	WHEN '4'THEN 'Key change in progress'
	WHEN '5'THEN 'Decryption in progress'
	WHEN '6'THEN 'Protection change in progress (The certificate or asymmetric key that is encrypting the database encryption key is being changed.)'
	ELSE 'No Status'
	END,
	percent_complete,encryptor_thumbprint, encryptor_type FROM sys.dm_database_encryption_keys
    ```


*Created on: 11/24/24*

*Last Reviewed on: 2/7/25*
