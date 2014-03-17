# -*- coding: utf-8 -*-
# A simple file that reads and check if your YAML files are correct
#
# Author: Kristian Botnen
# Email: kristian.botnen@adm.uib.no
# License: The MIT License
# Requirements: pip install pyyaml
#
# Usage:
#
# $ python yamlcheck.py -f test.yaml
# or
# $ python yamlcheck.py -f /path/to/folder
#
# 

import os
import argparse
import yaml

parser = argparse.ArgumentParser(description='Process some yaml.')
parser.add_argument('-f', '--f', metavar='', help='file or folder', action="store")
args = parser.parse_args()
inputstring = args.f

#This method tries to load a given filename, and parse it with pyyaml.
def parsefile(filename):
  try: 
    yamlfile = open(filename, 'r')
    try: 
      yaml.load(yamlfile)
      #print filename, "ok"
    except Exception as e:
      print "YAML error" + str(e)    
  except (IOError, TypeError) as e:
    print "I/O error:" + str(e)
    
#Check if argument is single file
if os.path.isfile(inputstring):
  filename = inputstring
  print "Parsing the file:" + filename
  parsefile(filename)
#Check if the argument is folder
elif os.path.isdir(inputstring):
  foldername = inputstring
  filenamearray = []
  
  print "Parsing the folder:" + foldername
  for root, dirs, files in os.walk(foldername):
    for file in files:
      if file.lower().endswith("yaml"):
        filenamearray.append(os.path.join(root, file))
        parsefile((os.path.join(root, file)))
#Can not determine what the user gave as argument, probably a nonexisting file / folder    
else:
  print "Cant determine if input is file or folder:" + inputstring
