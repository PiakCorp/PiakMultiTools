import requests
import re
import websocket
import random 
import time
import os
import sys
import json
import string
import tls_client
import datetime
from tls_client import Session
from fake_useragent import UserAgent
from pystyle import System, Colors, Write

global_settings = {
    "name": "RADU MULTI-TØØL",
    "creator": "H4cK3dR4Du#0001",
    "github": "https://github.com/H4cK3dR4Du",
    "discord": "https://discord.gg/nebularw",
}

def balance_capmonster():
    proxy = (random.choice
             (open
              ("proxies.txt", "r").readlines()
              ).strip()
    if len(open
           ("proxies.txt", "r")
           .readlines()
           ) != 0
    else None
    )
    session_proxy = Session(
        client_identifier="chrome_114",
        random_tls_extension_order=True
    )
    session_proxy.proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy
    }
    with open("config.json") as imradu:
        data2 = json.load(imradu)
        key = data2.get("capmonster_key")
    payload = {
        "clientKey": key
    }
    try:
        response = session_proxy.post("https://api.capmonster.cloud/getBalance", json=payload)
        if response.status_code == 200:
            data = response.json()
            balance = data["balance"]
            return balance
        elif "ERROR_KEY_DOES_NOT_EXIST" in response.text:
            return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        pass
    except Exception as e:
        pass

def global_headers():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
        'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
    }

proxy_links_default = f"""
https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all
http://olaf4snow.com/public/proxy.txt
http://atomintersoft.com/products/alive-proxy/proxy-list/3128
http://rammstein.narod.ru/proxy.html
http://sergei-m.narod.ru/proxy.htm
http://tomoney.narod.ru/help/proxi.htm
http://westdollar.narod.ru/proxy.htm
http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/
http://atomintersoft.com/products/alive-proxy/socks5-list
http://atomintersoft.com/anonymous_proxy_list
http://atomintersoft.com/products/alive-proxy/proxy-list/com
http://atomintersoft.com/proxy_list_domain_com
http://atomintersoft.com/proxy_list_domain_edu
http://atomintersoft.com/proxy_list_domain_net
http://atomintersoft.com/proxy_list_domain_org
http://atomintersoft.com/proxy_list_port_3128
http://atomintersoft.com/proxy_list_port_80
http://atomintersoft.com/proxy_list_port_8000
http://atomintersoft.com/proxy_list_port_81
http://atomintersoft.com/transparent_proxy_list
https://free-proxy-list.net/
https://www.us-proxy.org/
https://free-proxy-list.net/uk-proxy.html
https://www.sslproxies.org/
https://free-proxy-list.net/anonymous-proxy.html
https://www.socks-proxy.net/
http://proxydb.net/
https://raw.githubusercontent.com/thespeedx/proxy-list/master/socks5.txt
https://raw.githubusercontent.com/thespeedx/proxy-list/master/socks4.txt
https://raw.githubusercontent.com/thespeedx/proxy-list/master/http.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt
https://raw.githubusercontent.com/shiftytr/proxy-list/master/socks4.txt
https://raw.githubusercontent.com/shiftytr/proxy-list/master/socks5.txt
http://globalproxies.blogspot.com/
http://biskutliat.blogspot.com/
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html
http://vipprox.blogspot.com/2013_06_01_archive.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html
http://vipprox.blogspot.com/p/blog-page_7.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html
http://vipprox.blogspot.com/2013_02_01_archive.html
http://alexa.lr2b.com/proxylist.txt
http://vipprox.blogspot.com/2013_03_01_archive.html
http://free-ssh.blogspot.com/feeds/posts/default
http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html
http://proxyfirenet.blogspot.com/
https://www.javatpoint.com/proxy-server-list
https://openproxy.space/list/http
https://openproxy.space/list/socks4
https://openproxy.space/list/socks5
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt
https://free-proxy-list.com/
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all
http://spys.me/proxy.txt
https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt
https://www.us-proxy.org
https://free-proxy-list.net
https://raw.githubusercontent.com/thespeedx/socks-list/master/socks5.txt
https://raw.githubusercontent.com/thespeedx/socks-list/master/socks4.txt
https://raw.githubusercontent.com/thespeedx/socks-list/master/http.txt
https://proxy50-50.blogspot.com/
https://www.my-proxy.com/free-anonymous-proxy.html
https://www.my-proxy.com/free-socks-4-proxy.html
https://www.my-proxy.com/free-socks-5-proxy.html
https://www.my-proxy.com/free-proxy-list.html
https://www.my-proxy.com/free-proxy-list-2.html
https://www.my-proxy.com/free-proxy-list-3.html
https://www.my-proxy.com/free-proxy-list-4.html
https://www.my-proxy.com/free-proxy-list-5.html
https://www.my-proxy.com/free-proxy-list-6.html
https://www.my-proxy.com/free-proxy-list-7.html
https://www.my-proxy.com/free-proxy-list-8.html
https://www.my-proxy.com/free-proxy-list-9.html
https://www.my-proxy.com/free-proxy-list-10.html
https://www.my-proxy.com/free-elite-proxy.html
https://www.proxyscan.io/download?type=http
https://www.proxyscan.io/download?type=https
https://www.proxyscan.io/download?type=socks4
https://www.proxyscan.io/download?type=socks5
https://multiproxy.org/txt_all/proxy.txt
http://rootjazz.com/proxies/proxies.txt
http://ab57.ru/downloads/proxyold.txt
https://proxy-spider.com/api/proxies.example.txt
https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt
https://www.proxy-list.download/api/v1/get?type=socks4
https://raw.githubusercontent.com/saisuiu/lionkings-http-proxys-proxies/main/cnfree.txt
https://raw.githubusercontent.com/saisuiu/lionkings-http-proxys-proxies/main/free.txt
https://raw.githubusercontent.com/zuoxiaolei/proxys/main/proxys/proxys.txt
https://raw.githubusercontent.com/hyperbeats/proxy-list/main/socks4.txt
https://raw.githubusercontent.com/hyperbeats/proxy-list/main/socks5.txt
https://raw.githubusercontent.com/hyperbeats/proxy-list/main/http.txt
https://raw.githubusercontent.com/hyperbeats/proxy-list/main/https.txt
https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt
https://raw.githubusercontent.com/almroot/proxylist/master/list.txt
https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http_old.txt
https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt
https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/hproxy.txt
https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-socks5.txt
https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt
https://raw.githubusercontent.com/saschazesiger/free-proxies/master/proxies/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation/socks5.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/socks5.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation/socks4.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation/socks5.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation/http.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_anonymous/socks4.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_anonymous/socks5.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_anonymous/http.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation_anonymous/http.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation_anonymous/socks4.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies_geolocation_anonymous/socks5.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies/socks4.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies/socks5.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/master/proxies/http.txt
https://raw.githubusercontent.com/tahaluindo/free-proxies/main/proxies/all.txt
https://raw.githubusercontent.com/bardiafa/proxy-leecher/main/proxies.txt
https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt
https://raw.githubusercontent.com/saschazesiger/free-proxies/master/proxies/socks5.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt
https://raw.githubusercontent.com/zevtyardt/proxy-list/main/all.txt
https://raw.githubusercontent.com/ercindedeoglu/proxies/main/proxies/https.txt
https://raw.githubusercontent.com/ercindedeoglu/proxies/main/proxies/http.txt
https://raw.githubusercontent.com/ercindedeoglu/proxies/main/proxies/socks4.txt
https://raw.githubusercontent.com/ercindedeoglu/proxies/main/proxies/socks5.txt
https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt
https://raw.githubusercontent.com/saschazesiger/free-proxies/master/proxies/raw.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/main/proxies/socks5.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/uptimerbot/proxy-list/main/proxies/socks4.txt""".splitlines()

def make_user_agents_valid():
    def generate_user_agents(num_agents):
        ua = UserAgent()
        user_agents = [ua.random for _ in range(num_agents)]
        return user_agents

    def main():
        num_agents = 5
        user_agents = generate_user_agents(num_agents)

        for ua in user_agents:
            print(ua)
    
    main()

def check_webhook():
    def is_valid_webhook(url):
        try:
            response = requests.head(url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def main():
        webhook_url = input("Webhook : ")
        if is_valid_webhook(webhook_url):
            return True
        else:
            return False

def get_servers(token):
    headers = {
        'Authorization': token
    }

    response = requests.get('https://discord.com/api/v10/users/@me/guilds', headers=headers)

    if response.status_code == 200:
        servers = response.json()
        for server in servers:
            print(server)
            return server
    else:
        print('Error :', response.status_code)

def remove_duplicates(file):
    lines = []
    duplicates = set()
    with open(file, 'r') as f:
        lines = f.readlines()
        
    unique_lines = []
    for line in lines:
        if line in duplicates:
            continue
        else:
            duplicates.add(line)
            unique_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(unique_lines)
    
def bye_bye(login, fecha_good):
    Write.Print(f"""
    —–-—▒▒▒▒▒▒▒▒▒▒
    —–-▒███████████▒
    —▒████▒▒▒▒▒▒▒███▒
    -▒████▒▒▒▒▒▒▒▒▒███▒……………….▒▒▒▒▒▒
    -▒███▒▒▒▒▒███▒▒▒███▒…………..▒██████▒
    -▒███▒▒▒▒██████▒▒███▒……….▒██▒▒▒▒██▒         [ Made By H4cK3dR4Du#0001 ]
    —▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒         [ Discord : discord.gg/nebularw ]
    —–▒███▒▒████████▒██▒…▒███▒▒███▒▒██▒         [ Thanks For Using My Tool ♥ ]
    ——–▒██▒▒██████████▒▒███▒▒████▒▒██▒
    ———▒██▒▒██████████████▒████▒▒██▒
    ———-▒██▒▒█████████████████▒▒██▒             [ Github : https://github.com/H4cK3dR4Du ]
    ————▒██▒▒██████████████▒▒██▒                [ Youtube : https://youtube.com/@H4cK3dR4Du ]
    ————–▒██▒▒████████████▒▒██▒                 [ TikTok : https://www.tiktok.com/@radutool ]
    —————-▒██▒▒██████████▒▒██▒                  
    —————–▒██▒▒████████▒▒██▒                    
    ——————-▒██▒▒██████▒▒██▒                     [ {login} ]
    ———————▒██▒▒████▒▒██▒                       [ {fecha_good} ]
    ———————-▒██▒▒███▒▒█▒                        [ RaduTool V1.0 ]
    ————————▒██▒▒█▒▒█▒
    ————————-▒██▒▒▒█▒
    —————————▒██▒█▒                             [ Goodbye! ]
    —————————♥♥♥♥♥♥                             [ Exit In : 3s ]
    —————————-♥♥♥♥♥
    ——————————♥♥♥
    —————————-—♥♥
    ———————————♥
""", Colors.red_to_blue, interval=0.000)
    time.sleep(3)
    exit()