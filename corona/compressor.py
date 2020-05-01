import zlib, base64

filename = 'manual.py'
file = open(filename, 'r')
text = file.read()
file.close()
code =  base64.b64encode(zlib.compress(text.encode('utf-8'),9))
code = code.decode('utf-8')
f=open(filename+'_compress','w')
f.write(code)
f.close()
# decode the encoded text
# decoded_txt = zlib.decompress(base64.b64decode(code))
# print(decoded_txt)
