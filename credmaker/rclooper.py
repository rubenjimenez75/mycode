#!/usr/bin/env python3

import csv
f = open("csv_users.txt", "r")
i = 0
for row in csv.reader(f):
    i = i + 1
    filename = "admin.rc%d"%(i,)
    rcfile = open(filename, "w")
    print("OS_AUTH_URL=" + row[0], file=rcfile)
    print("OS_IDENTITY_API_VERSION=3", file=rcfile)
    print("OS_PROJECT_NAME=" + row[1], file=rcfile)
    print("OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
    print("OS_USERNAME=" + row[3], file=rcfile)
    print("OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
    print("OS_PASSWORD=" + row[5], file=rcfile)
    rcfile.close()
