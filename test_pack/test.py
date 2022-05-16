import re

a= '12121212'

b = re.findall(r'([\d]{2})([\d]{2})([\d]{4})', a)
print (b)

b = re.compile(r'([\d]{2})([\d]{2})([\d]{4})')
print(b.search(a))

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print ( result.group(0))