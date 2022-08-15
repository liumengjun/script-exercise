#!/bin/bash
mysql -uroot -p123456 -e 'create database if not exists new_db;'
list_table=$(mysql -uroot -p123456 -Nse "select table_name from information_schema.TABLES where TABLE_SCHEMA='old_db'")

for table in $list_table
do
    mysql -uroot -p123456 -e "rename table old_db.$table to new_db.$table"
done
