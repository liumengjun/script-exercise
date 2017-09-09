#!/bin/bash
set -e

video_output_csv_file=$1

if [ -z "$video_output_csv_file" ]; then
    echo "video_output.csv file is must"
    exit -1
fi

if [ ! -e "$video_output_csv_file" ]; then
    echo "$video_output_csv_file not exist"
    exit -1
fi

basedir="face_files/"
for line in $(cat $video_output_csv_file); do
    # echo $line
    number=`echo $line | cut -d "," -f1`
    # echo $number
    mkdir -p $basedir$number 2>/dev/null || true
    file_name=`echo $line | cut -d "," -f2`
    # echo $file_name
    url=`echo $line | cut -d "," -f3 | cut -d "?" -f1`
    # echo $url

    path=$basedir$number/$file_name
    echo $path
    if [ -e $path ]; then
        echo "exist"
        # true # do nothing
    else
        echo "not exist"
        # wget -O $path.tmp $url
        curl -o $path.tmp $url
        mv $path.tmp $path
    fi
done

echo
echo "All download!"
