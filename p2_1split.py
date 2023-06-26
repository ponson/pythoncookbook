import re

line = 'asdf        fjdk   ; afrd, jfed,asdf, foo'
out = re.split(r'\s*[;,\s]\s*', line)
print(out)