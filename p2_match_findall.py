import re

text = 'Today is 11/27/2012,. PyCon start 3/13/2013.'
text2 = '11/27/2012   3/13/2013.'
dateText = '11/27/2012,. PyCon start 3/13/2013. '
datepart = re.compile(r'(\d+)/(\d+)/(\d+)')
# m = datepart.match(text2)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# print(datepart.findall(text2))
for m in datepart.finditer(text):
    print(f"{m.group(3)}-{m.group(1)}-{m.group(2)}")

