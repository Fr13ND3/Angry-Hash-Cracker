from os import system
try:
    import requests
except ModuleNotFoundError:
    system('pip install requests')
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    system('pip install bs4')
from datetime import datetime
from time import sleep
time_now = datetime.now().strftime('%H:%M:%S')
print("""

    #######    #######    #######             ##########  ######        ##        ###        ###
         ##    ##         ##     ##               ##      ##           ## ##      ## #      # ##
       ##      #######    ##      ##   #######    ##      #######     #######     ##  #    #  ##
     ##        ##         ##     ##               ##      ##         ##     ##    ##   #  #   ##
    #######    #######    #######                 ##      #######   ##       ##   ##    ##    ##

""")

u_hash = input('[+] Please Enter Your Hash : ')
if int(len(u_hash)) < 16:
    print("\n[-] your hash is not correct ..." )
    exit()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
}
try:
    p = ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
    print("\n[*] Connection to WebSite ...")
    req = requests.get(f'https://hashtoolkit.com/reverse-hash/?hash={u_hash}',headers=headers)
    if req.status_code == 200:
        for i in p:
            print(i,end="")
            
            sleep(0.02)
    else:
        print("[-] Connection Error ! Please Check Your Internet !! or OFF\ON Your VPN\n")
        exit()
    print("\n\n[*] Cracking Your Hash ...")
    for i in p:
        print(i,end="")
        sleep(0.1)
except Exception:
    print("[-] Connection Error ! Please Check Your Internet !! or OFF\ON Your VPN\n")
    exit()
soup = BeautifulSoup(req.content,'html.parser')
result_crack = str(soup.find_all('span'))


result_crack = result_crack.split(',')

len_res = len(result_crack)
if len_res < 10:
    print("Your Hash is Not Cracked \ntype Hash : anonymouse")
else:
    result_crack = result_crack[10]
    result_crack = result_crack.split('>')
    result_crack = "".join(result_crack[1])
    result_crack = result_crack.split('<')
    result_crack = "".join(result_crack[0])
    if result_crack == u_hash:
        print(f"\nYour Hash is Not Cracked \ntype Hash : anonymouse\n Time:{time_now}")
        exit()
    print(f"""

Hash : {u_hash}
Your Hash is Cracked : {result_crack} 
Time : {time_now} 
   """)

print("Channel Telegram : @FR13ND3")
# 8b1a9953c4611296a827abf8c47804d7