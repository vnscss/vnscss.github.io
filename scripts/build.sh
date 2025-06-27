#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "Este script deve ser executado como root."
  exit 1
fi

setsid ./scripts/dev_server.sh &
pid=$!
sleep 5

rm -rf ./index.html
endpoint="http://localhost:9000"
wget "$endpoint"

rm -rf ./static
cp -a ./django-proj/static ./static



if [ ! -d ./article ]; then
  mkdir -p ./article
fi

for slug in $(curl -s "$endpoint/api/articles/"); do
    wget "$endpoint/article/$slug" -O "./article/$slug"
done


kill -TERM -$pid 2>/dev/null
wait $pid 2>/dev/null


