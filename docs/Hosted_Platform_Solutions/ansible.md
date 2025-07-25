---
author: "Sasha Karcz"
date: "2024-11-04"
description: "Ansible Configuration Management"
tags: ["HPS", "Ansible", "Configuration", "Management"]
---

# HPS Configuration Management

## Introduction

Infrastructure as Code (IaC) or the method by which written logic is used to
control a complete infrastructure. This logic or code can be captured as a
distributed set of files (repo) by tools such as Git. This repo demonstrates
the details and methods needed.

## Current environment

HPS has one managment server for Ansible (`atxhstinfans01.jhahosting.com`). All the code for Ansible exists in a [GitHub repository](https://github.com/jkhy/jhansible). To run an Ansible command, connect to `atxhstinfans01.jhahosting.com` and then change directories to the `/etc/ansible` directory:

```bash
cd /etc/ansible
```

Since HPS supports the Windows fleet, Ansible is configured to use WinRM (listening on port `5985`). Future deployments _may_ look at using OpenSSH. Linux hosts are managed using OpenSSH (port `22`).

## OS Requirements Linux

- ssh-client
- sshpass - Some modules need this for password based login

## Python Requirements

See the setup file.

### Step by step:

1. Make a containing directory and move into it.
1. Clone this repo
1. Move cloned repo to `/etc/ansible`
1. Set the Ansible Vault password
1. Run the playbook (assuming vault and roles work)

### Configuration

Some items to configure for your environment are:

1. Ansible Vault secret aka `.ansible_vault` file
1. Inventory

Note the ansible config is defaulting some settings so the command actually looks like:

``` bash
$ ansible-playbook --vault-id .ansible_vault -e @vault.yml -i inventory/* playbooks/main.yml
```

This is useful to know when trouble-shooting.

## Inventory

The basic outline of the inventory is as follows:

```bash
inventory/
├── group_vars
│   └── all.yml
├── host_vars
├── mgt.yml
├── obd.yml
├── obx.yml
└── yhf.yml
```

Each service gets a specific inventory file. Variables common to all services should go into the `inventory/group_vars/all.yml` file. Per service variables should go into either the service inventory file (_e.x._ `inventory/yhf.yml`) or into a new group variable file (_e.x._ `inventory/group_vars/yhf.yml`).

### Running commands

Each service inventory is further broken up into data centers: `ATX`, `BMO`, `CLT`, `MMO`, _... etc_. To run an adhoc command on all hosts for a service in a specific data center, we need only do:

```bash
ansible -m win_ping -i inventory/yhf.yml atx
```

Or, if we wish to run a playbook on (such as `playbooks/win_uptime.yml`) on all the `YHF` hosts in `ATX`:

```bash
 ansible-playbook playbooks/win_uptime.yml -l atxyhf*,mmoyhf*
```
 

## Vault

In this example we use the Ansible vault which is a portable encryption
mechanisim that allows secrets to be checked in as encrypted text documents.

On the Ansible server, someone will need to create the `.ansible_vault` file. It's contents can be found in KeePass `General > Ansible Vault` on the HPS shared KeePass Database (`\\jhacorp.com\mmco\Groups\CloudServices\database.kdbx`).

* https://docs.ansible.com/ansible/latest/user_guide/vault.html

### Encrypting secrets (you will actually use this)

```bash
ansible-vault encrypt_string --vault-password-file /etc/ansible/.ansible_vault 'SuperSecretPassword' --name 'ADMIN_PASSWORD' --encrypt-vault-id default >> /etc/ansible/inventory/group_vars/all.yml
```

### Create:

Note the --vault-id .ansible_vault is set in ansible.cfg

```bash
$ ansible-vault create inventory/group_vars/vault.yml
```

### Edit:

Note the --vault-id .ansible_vault is set in ansible.cfg

```bash
$ ansible-vault edit inventory/group_vars/vault.yml
```

### View:

Open with 'more' or 'less' tools. Note the --vault-id .ansible_vault is set in ansible.cfg

```bash
$ ansible-vault view inventory/group_vars/vault.yml
```

### Export:

Some times you need the whole config in the vault. You can export with the `decrypt` option to save the output to file.

```bash
ansible-vault decrypt --output vault.raw.yml inventory/group_vars/vault.yml
```

## Roles

Organizing roles can be a challenge. Ansible is very flexible which gives too many options at times.
 
### File system hirearchy

Each role will have its own directory in `roles/` such as `roles/windows_prometheus`. The directory structure will contain the following:

```
roles/windows_prometheus/
├── handlers
│   └── main.yml
├── tasks
│   └── main.yml
└── templates
    └── config.yaml.j2
```

| Directory     | What it is for      |
| ------------- | ------------------- | 
| handlers      | Sometimes you want a task to run only when a change is made on a machine. For example, you may want to restart a service if a task updates the configuration of that service, but not if the configuration is unchanged. Ansible uses handlers to address this use case. Handlers are tasks that only run when notified. Required file: `main.yml` |
| tasks         | This directory contains one or more files that have specific tasks that the role provides to the playbook for execution. Required file: `main.yml` |
| templates     | This directory contains one or more files that are unique to each host/service/deployment. Templates use jinja2 and should have a `.j2` extension. Best practice is to name the file whatever the final file should be but with `.j2` tacked on. Example: `config.yaml.j2` |
| files         |  This directory contains one or more files that are the same for each host/service/deployment. Best practice is to name the file whatever the final file should be. Example: `config.yaml` |

## Playbooks

Playbooks are collections of one or more roles that target specific hosts or host groups. For example, the playbook to just install the Prometheus exporters for Windows servers (`playbooks/windows_prometheus.yml`) looks like:

```
---

- name: "Configure Prometheus on Windows Hosts"
  hosts: all
  gather_facts: true
  roles:
    - role: "windows_prometheus"
```

This targets all hosts and applies all the tasks defined in the `roles/windows_prometheus/tasks/main.yml` file. We could run this playbook on all `ATX` hosts for `YHF` via:

```bash
ansible-playbook playbooks/windows_prometheus.yml -l atxyhf*,mmoyhf*
```

Additional roles can be added to any playbook:

```
---

- name: "Configure Fuzzy Kitty 5000 service"
  hosts: fk5
  gather_facts: true
  roles:
    - role: "windows_prometheus"
    - role: "super_awesome_new_role"
    - role: "fuzzy_kitty_5000"
    - role: "awesome_security"
```

NOTE: This playbook is running on a host group named `fk5` (for Fuzzy Kitty 5000). It would expect a new inventory file (`inventory/fk5.yml`) with the `fk5` group defined.

### Running PowerShell scripts

There is a role and playbook set up to run PowerShell scripts. Check in the PowerShell script into the `powershell_script` directory. We can pass host/group, and script as extra variables to the playbook:

```bash
ansible-playbook playbooks/powershell.yml -e host=mmoyhfapp20 -e script=process.ps1
```
