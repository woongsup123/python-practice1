s = '/usr/local/bin/python'

li = s.split('/')
li.remove('')
print(li)

li = s.rsplit('/',1)
print(li)
