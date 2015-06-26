#!/usr/bin/python
#by bruno v0id

#just another test with regex

import re

file=open("login.html","r")
line=file.readline()

tag=re.compile("(<) (html) (>)")
result=tag.match(line)

html=file.read()
form=re.search("<form.+",html).group()

start=re.search(" ",form).end()
end=re.search(">",form).start()

parameters=form[start:end]
pattern=re.compile('(\w+)="([\w.]+)"')

result=pattern.findall(parameters)
for element in result:
 print("\033[37m %s -->\033[36m %s"%(element[0],element[1]))
