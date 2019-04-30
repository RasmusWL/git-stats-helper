#!/usr/bin/env python3.7

import sys

commits = dict()

for line in sys.stdin:
    line = line.strip()
    filename, *rest = line.split(':')

    added, removed, net = (int(part.split(':')[1]) for part in ':'.join(rest).strip().split(',') )

    reponame = filename.split('/')[-1]

    commits[reponame] = (added, removed, net)

total_added = 0
total_removed = 0
total_net = 0


for repo, (added, removed, net) in sorted(commits.items(), key=lambda i: -i[1][0]):
    print(f'{repo}: {added} added, {removed} removed, {net} net')
    total_added += added
    total_removed += removed
    total_net += net

print()
print(f'TOTAL: {total_added} added, {total_removed} removed, {total_net} net')

# egrep 'total lines: .' out/lines/* | ./summarize-lines.py
