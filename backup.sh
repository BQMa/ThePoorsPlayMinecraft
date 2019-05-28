#!/bin/bash
date +"%F %R" >> gitlog
git add . 1>>gitlog 2>&1 &&
echo "finish add" >> gitlog &&
git commit -m "`date +"%F %R"`" 1>>gitlog 2>&1 &&
echo "finish commit" >> gitlog &&
git push 1>>gitlog 2>&1 &&
echo "finish push" >> gitlog
echo >> gitlog
