#!/bin/bash
# TODO: use sed to do both work...

FILES=data/*.emlx
MBOX=data/mbox
egrep -ho "\b(?:\d{1,3}\.){3}\d{1,3}\b])" $FILES | cut -d ']' -f 1
