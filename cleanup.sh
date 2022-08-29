#!/bin/env

userdel --remove $1
rpm -qa --last > list
yum remove ${awk '{print $1}' < list)