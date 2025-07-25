# Revelio

[![Push to GitHub Pages](https://github.com/jkhy/revelio/actions/workflows/ci.yml/badge.svg)](https://github.com/jkhy/revelio/actions/workflows/ci.yml) [![Check File Name](https://github.com/jkhy/revelio/actions/workflows/snake_case.yml/badge.svg)](https://github.com/jkhy/revelio/actions/workflows/snake_case.yml) [![Documentation Freshness](https://github.com/jkhy/revelio/actions/workflows/freshness.yml/badge.svg)](https://github.com/jkhy/revelio/actions/workflows/freshness.yml)

This is the source repo for [Jack Henry documentation](https://revelio.jackhenry.com/).

## Contributing 

To contribute to the project, follow these steps:

1. Clone the repository: `git clone https://github.com/jkhy/revelio.git`
2. Create a new branch for your changes: `git branch new-branch-name`
3. Switch to the new branch: `git checkout new-branch-name`
4. Make your changes and commit them: `git commit -m "Your commit message"`
5. Push your changes to the new branch: `git push origin new-branch-name`
6. Create a Pull Request (PR) to merge your changes back to the main branch.

[Pull Requests](https://github.com/jkhy/revelio/pulls) are automatically tested to adhere to documentation standards. PRs are also temporarly rendered to assist with reviewing.

## Setting up Git on Windows

To set up Git on Windows and configure your Git username and email, follow these steps:

1. Download Git for Windows from the official website: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer and follow the installation instructions.
3. Open the Git Bash terminal.
4. Set your Git username using the following command, replacing `Your Name` with your actual name:
    ```
    git config --global user.name "Your Name"
    ```
5. Set your Git email using the following command, replacing `your.email@jackhenry.com` with your actual email address:
    ```
    git config --global user.email "your.email@jackhenry.com"
    ```
6. Verify that your Git username and email are set correctly by running the following commands:
    ```
    git config user.name
    git config user.email
    ```
    The output should display your configured username and email.
7. You have successfully set up Git on Windows and configured your Git username and email.

Remember to use the same Git username and email when making commits to this repository.

## Directory structure

```bash
.
├── docs
│   ├── Database_Operations_Business_Partner_Portal
│   │   ├── Documents
│   │   │   ├── Audit
│   │   │   ├── Backup_Infrastructure
│   │   │   ├── Documentation
│   │   │   ├── General
│   │   │   ├── HADR
│   │   │   ├── Processes_and_Procedures
│   │   │   ├── Projects
│   │   │   ├── SCOM_Alerting
│   │   │   ├── SQL_Licensing
│   │   │   └── Site_Transitions
│   │   ├── Processes_and_Procedures
│   │   │   ├── Procedures
│   │   │   └── Processes
│   │   ├── SQL_Installation_Request_Form
│   │   ├── Team_Wiki_Data
│   │   │   ├── Audit
│   │   │   ├── AzureCare
│   │   │   ├── Backup_Infrastructure
│   │   │   └── General
│   │   ├── TechOps_DS_MS_Database_Operations_Notebook
│   │   │   ├── CPS
│   │   │   ├── DEaR_and_TDE
│   │   │   ├── General_Team_Info
│   │   │   ├── How_To_Guides
│   │   │   ├── Knowledge_Transfer
│   │   │   ├── Quick_Notes
│   │   │   └── Ransomware_Recovery
│   │   └── eData_Website
│   ├── Hosted_Platform_Solutions
│   │   ├── Kenna_Security
│   │   └── splunk
│   ├── Training
│   │   ├── images
│   │   └── videos
│   ├── markdown-help
│   ├── Team_Awesome <----- New directory
|   |   └── fluffy_kitt.md <---- New file
│   └── network
│       ├── Cheatsheets
│       ├── Diagrams
│       ├── How_To
│       │   ├── Arista
│       │   ├── Devices_SL1_architect_access
│       │   ├── backup
│       │   └── patching
│       ├── Infoblox
│       │   └── images
│       ├── Vuln_Mgmt
│       └── templates
├── presubmits
└── scripts
```

Service based documentation should be logically partitioned based on what team supports that service. When adding a new service, add it in the appropriate directory. For example, if we were going to add a page for a new service `Fluffy Kitty 5000` and a new team (Team Awesome) supports it, we would create a new directory and markdown file: `Team_Awesome/fluffy_kitty.md`.

## Document standards

- All markdown files need to have front matter, with author, date, and relivent tags.

```
---
author: "Your Name"
date: "YYYY-MM-DD"
description: "A brief description of the document."
tags: ["tag1", "tag2", "tag3"]
---
```

- File names cannot have spaces, or any special characters. In place of a space, use an underscore.

- Embed images in a `images/` directory for each page created so as to not rely on external dependencies.

## Reference material

We use [mkdocs](https://www.mkdocs.org/) to generate the static site that is our documentation page. We are using the _Material Theme_ for MkDocs. [Here](https://squidfunk.github.io/mkdocs-material/reference/) is a reference of what is supported as well as code examples. See [getting started with markdown](https://www.markdownguide.org/getting-started/) for more background into what markdown is, and why anyone would want to use it.

## Git branches

There are two branches to this repo:
- `main`: This is the main branch where the markdown code resides.
- `gh-pages`: This branch is created via [continuous integration](.github/workflows/ci.yml) that runs GitHub Actions when a push occurs. 
