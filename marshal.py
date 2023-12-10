#!/usr/bin/python3
#-*- coding: utf-8 -*-
#marshal py3

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")
       
import os
import time
time.sleep(0.09)
os.system('clear')
print("\033[1;32m TOOL IS OPENING   ➣")


animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["\033[0;93m[■□□□□□□□□□]","\033[0;94m[■■□□□□□□□□]", "\033[0;92m[■■■□□□□□□□]", "\033[0;91m[■■■■□□□□□□]", "\033[0;97m[■■■■■□□□□□]", "\033[0;32m[■■■■■■□□□□]", "\033[0;94m[■■■■■■■□□□]", "\033[0;93m[■■■■■■■■□□]", "\033[0;91m[■■■■■■■■■□]", "\033[0;92m[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.1000)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


os.system("xdg-open https://facebook.com/groups/590005482506415/")
time.sleep(1)

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[1;32m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """

\t\033[1;33m███████╗  ███╗░░██╗  ░█████╗░
\t\033[1;33m██╔════╝  ████╗░██║  ██╔══██╗     
\t\033[1;33m█████╗░░  ██╔██╗██║  ██║░░╚═╝\033[1;36m𝐌𝐄𝐇𝐄𝐃𝐈࿐
\t\033[1;33m██╔══╝░░  ██║╚████║  ██║░░██╗\033[1;36m𝐇𝐀𝐒𝐀𝐍࿐   
\t\033[1;33m███████╗  ██║░╚███║  ╚█████╔╝
\t\033[1;33m╚══════╝  ╚═╝░░╚══╝  ░╚════╝░


""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

os.system('clear')
try:
    print(bannerpy3)
    print (g+' ['+w+'••'+g+'] '+w+'\033[0;93m➣Example '+y+':'+w+'\033[0;92m /sdcard/h4x.py\n')
    file = input(g+' ['+w+'°•°'+g+'] '+w+'\033[1;32mInput Your File Location'+y+' :'+w+' ')
    print()
    nn = input(y+' ['+w+'?'+y+'] '+w+'\033[0;92mInter Output File Name'+y+' :'+w+' ')
    o = nn.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+file+'"\n')
        os.system("xdg-open https://github.com/H4X-GG")
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File already to compiled\n') 
        sys.exit()

fileout = open(o + '.py', 'w')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('#Compiled By MEHEDI\n')
fileout.write('#github : https://github.com/H4X-GG\n')
fileout.write('#YouTube : https://youtube.com/@H4XTERMUX\n')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3)
os.system('clear')
print(bannerpy3)
print('\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print ('THANKS FOR USING MY TOOLS ')
print('JOIN MY FACEBOOK GROUP ')
print ('SOURCE FILE : '+file)
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + o + '.py')
print('\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

