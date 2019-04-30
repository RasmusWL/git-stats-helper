# git-stats-helper

## Create list of all repos

I couldn't find a method to get ALL repos in one, but had to loop over them

```
curl -u '<GITHUB USERNAME>' 'https://api.github.com/orgs/<ORG>/repos?type=all&per_page=100&page=1' > page1.json
curl -u '<GITHUB USERNAME>' 'https://api.github.com/orgs/<ORG>/repos?type=all&per_page=100&page=2' > page2.json
<...>
```

_with 2 factor auth, had to create a token: https://github.com/settings/tokens_

Then used jq to get the full github name to a file

```
jq -r '.[] | .full_name' < page1.json >> all
jq -r '.[] | .full_name' < page2.json >> all
<...>
```

## Clone all repos

With 4 processes

```
mkdir repos
cd repos
cat ../all | xargs -I% -n 1 -P 4 git clone git@github.com:\%
```

## Number of commits for all projects

```
mkdir -p out/commits/
cat all | cut -d/ -f2 | xargs -n 1 -P 4 ./num-commits.sh
grep -i '<AUTHOR NAME>' out/commits/* | ./summarize-commits.py
```

## Number of lines added/removed

```
mkdir -p out/lines
cat all | cut -d/ -f2 | xargs -n 1 -P 4 ./num-lines.sh <AUTHOR NAME>
egrep 'total lines: .' out/lines/* | ./summarize-lines.py
```
