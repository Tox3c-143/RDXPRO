import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    __import__("RDXPRO").Ariyan()
    
elif b == '32bit':
    print('wait for 33bit')
 
