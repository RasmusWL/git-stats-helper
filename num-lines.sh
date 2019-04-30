#!/bin/bash

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

NAME=$1

folder_name=$2

echo $folder_name
cd repos/$folder_name

git log --author="$NAME" --pretty=tformat: --numstat \
| gawk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' > $SCRIPTDIR/out/lines/$folder_name

# cat all | cut -d/ -f2 | xargs -n 1 -P 4 ./num-lines.sh <AUTHOR>
