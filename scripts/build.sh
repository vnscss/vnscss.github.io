#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "Este script deve ser executado como root."
  exit 1
fi

rm -rf ./index.html
endpoint="http://localhost:9000"
wget "$endpoint"

rm -rf ./static
cp -a ./django-proj/static ./static


rm -rf ./media
cp -a ./django-proj/conteudo ./media


rm -rf ./article
mkdir -p ./article
for slug in $(curl -s "$endpoint/api/articles/"); do
    wget "$endpoint/article/$slug" -O "./article/$slug"
done



