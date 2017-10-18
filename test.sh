#!/bin/bash

# automate testing of new heurtistics

for num in {1..10}
    do
        > output.txt
        python3 GameManager_3.py > output.txt
        last_line=$(tac output.txt |egrep -m 1 .)
        line="${num}) $last_line"
        echo $line >> results.txt
    done 
