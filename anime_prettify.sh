#!/bin/bash

files="*"
regex="\[.*\]\s(.+)\s-\s([0-9]+)\s\[.*\]\.(\w+)"
for f in $files
do
	if [[ $f =~ $regex ]]; then
		anime_name="${BASH_REMATCH[1]}"
	    anime_num="${BASH_REMATCH[2]}"
	    anime_ext="${BASH_REMATCH[3]}"
	    new_filename="${anime_num} - ${anime_name}.${anime_ext}"

	    echo "Renaming ${f} to ${new_filename}"
	    mv "$f" "${new_filename}"
	fi
    
    
done