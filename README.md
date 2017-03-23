# Python base64 encoder
Playing with base64 encoding for educational purposes. If you need a business ready solution, better use the base64 python module.


Use it this way:

Start the interactive shell in the same directory in which the base64.py script is stored.


 python3 
 
 \>\>\> import base64
 
 \>\>\> encoder = base64.Base64Encoder()
 
 \>\>\> text = encoder.encode("Hello World")
 
 \>\>\> print(text)
 
 SGVsbG8gV29ybGQ=
 
 Or use the script directly:
 
 
 ./base64.py "Hello World"
 
 SGVsbG8gV29ybGQ=
