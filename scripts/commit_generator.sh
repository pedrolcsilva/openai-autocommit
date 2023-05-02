#!/bin/sh
regex="([a-z0-9]*) auto"
commits_to_generate=()
commits=$(git log --pretty=format:"%h %s")
echo "$commits"

while read -r line; do
    if [[ $line =~ $regex ]]; then
        commit="${BASH_REMATCH[1]}"
        commits_to_generate+=("$commit")
    fi
done < <(echo "$commits")

for commit in "${commits_to_generate[@]}"; do
    diff=$(git show "$commit")
    python main.py "$diff" "$commit"

done