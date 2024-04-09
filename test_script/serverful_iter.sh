#!/bin/bash

while true; do
    for i in {1..10}; do
        ./test_sf_alt.sh &
    done
    sleep 1
done
