import chardet 

rawdata = open('25 يوحنا3.txt', 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)