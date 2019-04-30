#!/usr/bin/env python3.7

import sys

commits = dict()

for line in sys.stdin:
    line = line.strip()
    filename, rest = line.split(':')
    num_commits, name = rest.strip().split('\t')
    num_commits = int(num_commits)

    reponame = filename.split('/')[-1]

    commits[reponame] = num_commits

total_commits = 0

for repo, count in sorted(commits.items(), key=lambda i: -i[1]):
    print(f'{repo}: {count} commits')
    total_commits += count

print()
print(f'TOTAL: {total_commits} commits')

# grep -i 'Rasmus Wriedt' out/commits/* | ./summarize-commits.py
