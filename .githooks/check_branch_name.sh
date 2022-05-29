#!/usr/bin/env bash
LC_ALL=C

local_branch="$(git rev-parse --abbrev-ref HEAD)"

valid_branch_regex="^(bug|chore|devops|feat|fix|hotfix|release)\/[a-z0-9._-]+$"

message="Commit failed. Branch names in this project must adhere to this contract: $valid_branch_regex. Please rename your branch and try again."

if [[ ! $local_branch =~ $valid_branch_regex ]]
then
    echo "$message"
    exit 1
fi

exit 0
