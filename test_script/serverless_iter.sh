#!/bin/bash

while true; do
    for i in {1..10}; do
        ./test_sl.sh &
    done
    sleep 1
done
