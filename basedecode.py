import base64
import sys



with open('image.gif', 'rb') as input_file:
    decoded = base64.b64decode(input_file.read())
    
with open ('decoded.gif', 'wb') as fh:
    fh.write(decoded)
