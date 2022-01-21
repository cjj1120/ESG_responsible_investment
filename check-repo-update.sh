changed=0
git remote update && git status -uno | grep -q 'Your branch is behind' && changed=1
if [ $changed = 1 ]; then
    echo "Not up to date";
else
    echo "Up-to-date"
fi