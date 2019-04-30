#!/bin/bash

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

folder_name=$1

echo $folder_name
cd repos/$folder_name

git shortlog HEAD -n -s --no-merges > $SCRIPTDIR/out/commits/$folder_name

# cat all | cut -d/ -f2 | xargs -n 1 -P 4 ./num-commits.sh
