#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "Este script deve ser executado como root."
  exit 1
fi

rm -rf ./index.html
rm -rf ./static
rm -rf ./media
rm -rf ./article




