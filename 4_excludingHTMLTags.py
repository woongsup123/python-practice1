import re

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

print(re.sub('<.*?>', '', s))

replaced_s = ''
flag = False
for c in s:
    if c == '<':
        flag = True
    elif c == '>':
        flag = False
        continue
    if not flag:
        replaced_s += c

print(replaced_s)
