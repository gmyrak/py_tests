import re

str1 = 'Hello! 143 Привет! 24hh'

sr = re.match(r'.+?(\d+).+?(\d+)', str1)

if sr:
    print('OK')
    #print(sr)
    print(sr.group(2))
    #print()
else:
    print('NO')
