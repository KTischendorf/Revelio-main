---
author: "Justin West"
date: "2025-01-15"
description: "Process Guide"
tags: ["DBops", "Database Operations", "Process Guide", "Column Level Encryption", "Key Rotation", "TDE"]
---

# Always Encrypted Column Level Key Rotation

1. Request new certificate from the JHA CERT store (If not already requested by BU)
2. Install new certificate on the client and server certificate store
3. Create a new master key referencing the new certificate
       PLEASE NOTE:  Servers are Case Sensitive
``` SQL
--- Create New Master Key
CREATE COLUMN MASTER KEY [NewMasterKeyName]
WITH
(
     KEY_STORE_PROVIDER_NAME = N'MSSQL_CERTIFICATE_STORE',
     KEY_PATH = N'LocalMachine/My/[CertThumbprint]
);
GO
```

4. Rotate master key
* Login to SMSS->Connect to server -> Security -> Always Encrypted Keys -> Column Master Keys
* Right click key in question
* Click Rotate
5. Select newly created master key from resulting window
6. Clean up the old master key
  * Right click old master key -> Choose Cleanup
7. Drop the old master key from column encryption key
  ``` SQL
  --- Drop master key from encryption key
  ALTER COLUMN ENCRPYTION KEY [EncryptionKeyName]
  DROP VALUE
  (
       COLUMN_MASTER_KEY = [OldMasterKeyName]
  );
  GO
  ```
8. Drop the old master key
 ``` sql
 DROP COLUMN MASTER KEY [OldMasterKeyName]
 GO
 ```
---

*Created on: 11/24/24*

*Last Reviewed on: 2/7/25*
