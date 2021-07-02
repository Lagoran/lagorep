#compare 2 files

#filecmp.cmp('/opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults.conf', '/opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults_mod.conf', shallow=True)

# Importing difflib, os
import difflib
import os

with open('/opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults.conf') as file_1:
    file_1_text = file_1.readlines()

with open('spark-defaults_mod.conf') as file_2:
    file_2_text = file_2.readlines()

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt',
        tofile='file2.txt', lineterm=''):
    #print(len(line))
    if len(line) > 0:
       os.system('cp spark-defaults_mod.conf /opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults.conf')
       #print('Hello')
