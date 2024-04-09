#!/bin/bash

while true; do
    for i in {1..10}; do
        ./serverless.sh &
    done
    sleep 1
done
