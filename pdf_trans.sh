#!/bin/bash
path=`dirname $0`
tgt_file="$1"
src_lang="$2"
tgt_lang="$3"
python3 "$path"/pdf_trans.py "$tgt_file" "$src_lang" "$tgt_lang"
