---
author: "Vance Stokes"
date: "2025-01-28"
description: "Patching Linux Systems"
tags: ["network", "patching", "linux", "security"]
---
# Linux Patching Procedures

## Overview

This document outlines the procedures for patching Linux systems to ensure they are up-to-date with the latest security updates and bug fixes. Regular patching is essential to protect systems from vulnerabilities and maintain their stability and performance.

## Prerequisites

Before you begin the patching process, ensure you have the following:

- Access to the Linux system(s) you want to patch.
- Administrative privileges on the system(s).
- Knowledge of the package management system used by your Linux distribution (e.g., apt, yum, dnf).

## Patching Procedures

### 1. Update Package List

Before installing any updates, it is recommended to update the package lists to ensure you have the latest information about available updates.

#### Red Hat-based Systems (RHEL, CentOS)

```bash
sudo yum check-update
```

### 2. Install Updates

Once you have updated the package lists, you can proceed to install the available updates.

#### Red Hat-based Systems (RHEL, CentOS)

```bash
sudo yum update
```

### 3. Reboot the System

After installing updates, it is essential to reboot the system to apply any kernel updates and ensure all services are running with the latest patches.

```bash
sudo reboot
```

### 4. Verify Updates

After rebooting the system, you can verify that the updates have been successfully installed.

#### Red Hat-based Systems (RHEL, CentOS)

```bash
sudo yum list updates
```

### Issues and Troubleshooting

If you encounter any issues during the patching process, refer to the system logs and package manager logs for error messages and troubleshooting steps. You can also check the vendor's documentation for specific guidance on patching procedures.

#### Not enough Space

If you encounter issues due to insufficient disk space, consider cleaning up unnecessary files or expanding the disk space to accommodate the updates.

`/boot/` partition is full

``` bash
sudo yum clean all
```

This will clean up the yum cache and free up some space. If this doesn't work, please go ahead and validate the `boot` directory to see if there are any old kernels that can be removed.

---

Validate the kernel:

``` bash
uname -r
```

---

This will show you all the files in the `/boot` directory.

``` bash
ls -al /boot
```

---

Remove old kernels:

``` bash
sudo package-cleanup --oldkernels --count=1
```

This hasn't been tested yet and will need to be validated.  The other way to `rm` the old kernels is to do it manually. but does have the chance of causing issues.  All files that match the active kernel need to stay, the rest shouldn't have any dependencies.

### Conclusion

Regular patching of Linux systems is crucial to maintaining their security and performance. By following the procedures outlined in this document and staying informed about security updates, you can ensure that your systems are protected from known vulnerabilities and threats. If you have any questions or need assistance with the patching process, contact your system administrator or IT support team for help.

---

## Additional Resources

- [Red Hat Enterprise Linux Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [CentOS Documentation](https://www.centos.org/docs/)

## References

- [Linux Patch Management Best Practices](https://www.redhat.com/sysadmin/linux-patch-management)
- [Linux Patch Management Guide](https://www.linux.com/topic/linux-how-to/linux-patch-management-guide/)
- [Linux Security Updates](https://www.linuxsecurity.com/features/features/linux-security-updates)
