#!/usr/bin/env bash


function yolo () {
  rsync -r . pi@192.168.2.16:/home/pi
}

yolo

while read line
do
  echo $line
  yolo
done < <(inotifywait -mr --exclude ".git" -e close_write ".")

