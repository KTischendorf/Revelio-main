---
author: "Krystal Tischendorf"
date: "2025-11-26"
description: "Comrehensive Patching Strategy for Network Devices."
tags: ["patching", "network", "strategy","devices"]
---

## Introduction

This document outlines the comprehensive patching strategy for all devices managed by the Network Team, including routers, switches, and SDN Fabrics. It ties back to the inventory and includes a list of subnets and models of devices covered in this strategy, as well as references to certified OS for all devices.

## Devices and Subnets

- **Devices**: List of devices under management.
- **Subnet(s)**: List of subnets that will be part of this patching strategy.
- **Models**: Reference to the list of models of devices covered in this patching strategy.
- **Certified OS**: Reference to certified OS for all devices.

| Device               | Subnet(s) |
| -------------------- | ------------- |
|                      |.  |
|                      |.  |
### Requirements

Patching for all devices must be reviewed at least once a year for potential patches to address bugs, functionality, and/or security vulnerabilities. Ensure that all models of devices are on the same respective OS 1-2 times a year to reduce the scope of vulnerabilities.

### Priority

Define the priority on how specific items will be patched. For example, patches due to security vulnerabilities must be patched in accordance with security policies.

- **CVE/CVSS Prioritization**: Relative to our security policies.

| Priority/Risk Score  | Jack Henry Patching Urgency |
| -------------------- | ------------- |
| None         | Ex:  within x amount of time  |
| Low         |   |
|Medium        |   |
| High         |   |
| Critical      |



### Supported OS Certification

OS version and/or new software must be certified by Jack Henry’s network team as the standard for each hardware model supported. 

### Exceptions

Exceptions to this policy must be approved by the Director of Networking, documented, and reviewed yearly. 

### Reporting

Reference to a template for a reporting document to include sections like information about the vulnerability, current patch status, prospective patch status, expected results, actual results, findings, and suggestions for the future.

### Process

1. **Review Inventory and Patch Report**: Review the inventory and patch report for new systems that need to be reviewed.
2. **Certified OS Check**: Ensure there is a certified OS for the device.
   - If no certified OS, proceed to the OS certification procedure.
3. **Determine Patching Procedure**: Based on the manufacturer’s patch remediation steps, determine the appropriate patching procedure.
4. **Patch According to Priority Matrix**: Apply patches according to the priority matrix to address security vulnerabilities, bugs, and functionality improvements.
5. **Test in a Test Environment**: Test the patch in a test environment and document the results.
6. **Production-Level Patching**: Follow the procedure for production-level patching.
7. **Update Inventory**: Update the inventory to reflect the new patch status. This may be done manually or automatically.
8. **Document Failures**: Document any failures encountered during the patching process and revisit the procedures to address these issues.
9. **Rollback Plans**: Have rollback plans in place in case the patch causes issues. Document the rollback procedure and ensure it can be executed quickly if needed.

### OS Certification Procedure

- **Test Environment Maintenance**: Periodically copy samples from production over to test to maintain an accurate test environment. Ensure there are various OS/switch models in test that accurately represent the production environment yearly or periodically.
- **Testing Process**:
  1. Identify the OS version or new software to be certified.
  2. Deploy the OS/software in the test environment.
  3. Conduct functionality tests to ensure all features work as expected.
  4. Perform security assessments to identify any vulnerabilities.
  5. Document the test results, including any issues found and steps taken to resolve them.
- **Approval Process**:
  1. Review the documented test results.
  2. If the OS/software passes all tests, submit it for approval to the network team.
  3. Once approved, update the certified OS list and communicate the new certification to relevant stakeholders.
- **Documentation**:
  1. Maintain detailed records of all tests conducted, including dates, test cases, and results.
  2. Keep an updated list of certified OS versions for each hardware model.
  3. Document any issues encountered during the certification process and their resolutions.

### Production Documentation

- **Full System Backup**: Ensure a full system backup of the device is performed if it hasn’t been done already. This is crucial for recovery in case of any issues during the patching process.
- **Patch Deployment**:
  1. Follow the manufacturer’s guidelines for deploying patches.
  2. Schedule the patch deployment during a maintenance window to minimize impact on operations.
  3. Monitor the deployment process to ensure it completes successfully.
- **Monitoring and Validation**:
  1. After deployment, monitor the device to ensure it is functioning correctly.
  2. Validate that the patch has been applied successfully and that there are no adverse effects on the device’s performance.
- **Confirmation and Communication**:
  1. Confirm the successful deployment of the patch.
  2. Communicate the completion and results of the patching process to relevant stakeholders.
  3. Update the inventory and documentation to reflect the new patch status.
- **Rollback Plans**:
  1. Have a rollback plan in place in case the patch causes issues.
  2. Document the rollback procedure and ensure it can be executed quickly if needed.

## Conclusion

This comprehensive patching strategy ensures that all network devices are kept up-to-date with the latest patches to address bugs, functionality improvements, and security vulnerabilities. By following the outlined procedures, maintaining a certified OS, and adhering to the priority matrix, the Network Team can effectively manage and mitigate risks associated with outdated software. Regular reviews, thorough testing, and proper documentation are essential to the success of this strategy. Any exceptions must be approved and documented to maintain the integrity of the patching process. Continuous improvement and adherence to this strategy will help maintain a secure and efficient network environment.

