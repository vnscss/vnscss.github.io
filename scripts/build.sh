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

wget "$endpoint/api/404/" -O ./404.html

rm -rf ./static
cp -a ./django-proj/static ./static


rm -rf ./media
cp -a ./django-proj/conteudo ./media


rm -rf ./article
mkdir -p ./article
for slug in $(curl -s "$endpoint/api/articles/"); do
    wget "$endpoint/article/$slug" -O "./article/$slug"
done


kill -TERM -$pid 2>/dev/null
wait $pid 2>/dev/null


