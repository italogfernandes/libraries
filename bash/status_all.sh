#!/bin/bash
for d in */ ; do
    echo ""
    echo ""
    echo "*********************************************************************"
    echo "Entering in folder: " $d
    echo "*********************************************************************"
    cd $d
    git status
    cd ..
done

