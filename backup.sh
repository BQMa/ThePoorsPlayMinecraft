#!/bin/bash
GITLOG="gitlog"
date +"%F %R" >> $GITLOG
git add . 1>>$GITLOG 2>&1 &&
echo "finish add" >> $GITLOG &&
git commit -m "`date +"%F %R"`" 1>>$GITLOG 2>&1 &&
echo "finish commit" >> $GITLOG &&
git push 1>>$GITLOG 2>&1 &&
echo "finish push" >> $GITLOG
echo >> $GITLOG
