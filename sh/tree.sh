#!/bin/sh
# tree.sh
find . -print | sed -e 's;[^/]*/;|___ ;g;s;___ |;  |;g'
