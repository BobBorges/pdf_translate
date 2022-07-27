#!/bin/bash

path=`dirname $0`
trgtfile="$1"

python3 "$path"/pdf_extract_text.py "$trgtfile"

