#!/bin/bash

# Default author name
author="Your Name"

# Parse command-line options
while getopts "u:" opt; do
  case $opt in
    u)
      author=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# List all directories in the current directory
for dir in */; do
    # Remove the trailing slash from the directory name
    dir_name="${dir%/}"
    # Replace underscores with spaces
    formatted_name="${dir_name//_/ }"
    # Create the index.md file with the desired content
    cat <<EOL > "$dir/index.md"
---
author: "$author"
date: "$(date +%Y-%m-%d)"
description: "A brief description of the document."
tags: ["tag1", "tag2", "tag3"]
---

# $formatted_name
EOL
done
