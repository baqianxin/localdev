!/usr/bin/env bash
echo "==================== start clean docker containers logs =========================="
docker stop $(docker ps -a -q)
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
echo "==================== end clean docker containers logs   =========================="
