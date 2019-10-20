#!/bin/bash

filename=./urls.txt

while read line || [[ -n "$line" ]]; do
    echo downloading $line
    curl -O $line
done < "$filename"
