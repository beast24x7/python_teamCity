#python
try: #prevent unexpected crash
  ofile = open(filename)
except:
  print "file cannot be openned:", filename
  exit()

#read one line at a time
for line in ofile:
  line = line.rstrip() #delete "/n" from original file line
  print line
  
#read "whole" file at a time
wholeFile = ofile.read()