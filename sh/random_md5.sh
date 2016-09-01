#!/bin/sh
# generate random md5 string
# on MacOS md5
# on Linux md5sum
head -100 /dev/urandom | md5

