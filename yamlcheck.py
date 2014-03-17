# -*- coding: utf-8 -*-
#!/usr/bin/python
#__author__ = 'Kristian Botnen'

import os
import argparse
import yaml

parser = argparse.ArgumentParser(description='Process some yaml.')
parser.add_argument('-f', '--f', metavar='', help='file or folder', action="store")
args = parser.parse_args()

inputstring = args.f

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
    
#Check if argument is folder or single file
if os.path.isfile(inputstring):
  filename = inputstring
  print "Parsing the file:" + filename
  parsefile(filename)

elif os.path.isdir(inputstring):
  foldername = inputstring
  filenamearray = []
  
  print "Parsing the folder:" + foldername
  for root, dirs, files in os.walk(foldername):
    for file in files:
      if file.lower().endswith("yaml"):
        filenamearray.append(os.path.join(root, file))
        parsefile((os.path.join(root, file)))
    
else:
  print "Cant determine if input is file or folder:" + inputstring
