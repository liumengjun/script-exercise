#!/usr/bin/python
import sys, os, re, shutil
#Created by Liang Sun on Aug 9, 2012

from_str = r'mlls-row'
to_str = r'mala-row'
# files_to_replace = r'.(h|m|mm|cpp|inl|def|txt|php|tpl|css|js)$'
files_to_replace = r'.(scss|less|css|html)$'

def replace_l(infile, outfile):
    f1 = open(infile)
    f0 = open(outfile, 'wb') # write file in binary mode, in case Windows OS
    data = f1.readlines()
    for line in data:
        f0.write(re.sub(from_str, to_str, line))
        # f0.write(line.replace(from_str, to_str))
        # if (line.find(from_str) != -1):
            # print line.replace(from_str, to_str)
    f1.close()
    f0.close()

def walk_folder(path):
    print "Current Path: " + path
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(files_to_replace, filename):
                print "----" + filename + "...."
                # fi = open(os.path.join(dirpath, filename))
                # fo = open(os.path.join(dirpath, filename + ".bk"), 'w')
                # fo.write(fi.read())
                # fo.close()
                # fi.close()
                shutil.copyfile(os.path.join(dirpath, filename),os.path.join(dirpath, filename + ".bk"))
                replace_l(os.path.join(dirpath, filename + ".bk"),
                          os.path.join(dirpath, filename))
                print "Done."
                os.remove(os.path.join(dirpath, filename + ".bk"))

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    walk_folder(path)
    print
    print "All files have been translated successfully."
    print
    print "Created for you by Liang Sun on Aug 9, 2012."
    raw_input()