# Open a file with access mode 'a'
#file_object=open("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/test.txt",'a')
# Append 'hello' at the end of file
#file_object.write('hello')
# Close the file
#file_object.close()

#compare 2 files

#filecmp.cmp('/opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults.conf', '/opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults_mod.conf', shallow=True)

# Importing difflib
import difflib

import os

with open("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/test.txt") as file_1:
    file_1_text = file_1.readlines()

with open("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/test2.txt") as file_2:
    file_2_text = file_2.readlines()

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt',
        tofile='file2.txt', lineterm=''):
    #print(len(line))
    if len(line) > 0:
    #os.system('mv   /opt/cloudera/parcels/CDH/lib/spark/conf/spark-defaults.conf')
        print('Hello')
