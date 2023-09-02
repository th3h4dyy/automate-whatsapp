#!/bin/bash

# Read all files and directories from base directory and copy to multiple dirs.
function copy_base_dir_content_to_multiple_dirs() {
    
    for ((i=25060; i<=25071; i++))
    do 
        cp -r base ./$i
    done
}

# Create Virtualenv for each directory
function create_and_activate_venv() {
    python3 -m venv venv
    source ./venv/bin/activate
}

# For each directory, run the backend app with service port as an argument.
function run_apps() {
    for ((i=25060; i<=25071; i++))
    do
        int_re='^[0-9]+$'
        port_status=$(lsof -t -i :$i)+1
        if ! [[ port_status =~ $int_re ]]
        then
            lsof -t -i :$i | xargs kill
        fi 
        cd $i && nohup uvicorn backend:app --host 0.0.0.0 --port $i > nohup.out &
    done
}



function main() {
    copy_base_dir_content_to_multiple_dirs
    create_and_activate_venv
    run_apps
}

main 