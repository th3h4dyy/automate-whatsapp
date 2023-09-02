#!/bin/bash

function create_static_folders() {
    for ((i=1; i<=12; i++))
    do 
        mkdir -p statics/$i
    done
}


function main() {
    create_static_folders
    gunicorn backend:app -k uvicorn.workers.UvicornWorker -w 12 --bind 0.0.0.0:25060 --bind 0.0.0.0:25061 --bind 0.0.0.0:25062 --bind 0.0.0.0:25063 --bind 0.0.0.0:25064 --bind 0.0.0.0:25065 --bind 0.0.0.0:25066 --bind 0.0.0.0:25067 --bind 0.0.0.0:25068 --bind 0.0.0.0:25069 --bind 0.0.0.0:25070 --bind 0.0.0.0:25071 
}

main

