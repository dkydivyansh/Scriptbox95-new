#!/usr/bin/env python3
import os
import time
import sys
from sys import version_info
os.system('cls||clear')
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
con= f'{bblue}$ {bblue}Scriptbox95{purple}@{bgreen}con ~{white} '
go = f"""
{green}                              $$\            $$\     $$\                                  $$$$$$\  $$$$$$$\  
                              \__|           $$ |    $$ |                                $$  __$$\ $$  ____| 
 $$$$$$$\  $$$$$$$\  $$$$$$\  $$\  $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$\   $$\       $$ /  $$ |$$ |      
$$  _____|$$  _____|$$  __$$\ $$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ \$$\ $$  |      \$$$$$$$ |$$$$$$$\  
\$$$$$$\  $$ /      $$ |  \__|$$ |$$ /  $$ | $$ |    $$ |  $$ |$$ /  $$ | \$$$$  /        \____$$ |\_____$$\ 
 \____$$\ $$ |      $$ |      $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |  $$ | $$  $$<        $$\   $$ |$$\   $$ |
$$$$$$$  |\$$$$$$$\ $$ |      $$ |$$$$$$$  | \$$$$  |$$$$$$$  |\$$$$$$  |$$  /\$$\       \$$$$$$  |\$$$$$$  |
\_______/  \_______|\__|      \__|$$  ____/   \____/ \_______/  \______/ \__/  \__|       \______/  \______/ 
                                  $$ |                                                                       
                                  $$ |                                                                       
                                  \__|                                       {yellow} [{blue}console{yellow}]                 
{yellow}                                                                              {cyan}[{blue}\x42\x79 {green}amdivyansh{cyan}]
{white}


"""
os.system('cls||clear')
print(go)
pyver = str(version_info)
time.sleep(2)
print(con+"Setting up..")
print(con+"Python "+pyver)
if version_info<(3,0,0):
    print('[!] Please use Python 3. $ python3 scriptbox95.py')
    sys.exit()
import requests
import zipfile
import io
import re
import os
from update import download_latest_release_repository
import socket

def is_connected():
    time.sleep(2)
    print(con+"Checking For internet..")
    try:
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "www.google.com"
        port = 80
        socket_client.connect((host, port))
        socket_client.close()
        return True
    
    except Exception as e:
        return False

def setup():
    time.sleep(2)
    print(con+"Chacking For Updates..")
    from main.dta import version, getdata
    response2 = requests.get('https://api.github.com/repos/dkydivyansh/scriptbox_code_new/releases/latest')
    release_info2 = response2.json()
    ver = (release_info2['tag_name'])
    ver2 = int(version)
    ver3 = int(ver)
    print(con+"Current version is ["+version+']')
    if ver3 > ver2 or getdata == 1:
        print(con + "Update available..")
        print(con+"New version is ["+ver+']')
        print(con + "Updating..")
        download_latest_release_repository()
        os.chdir('./main')
        time.sleep(1)
        print(con+"importing files..")
        os.system('python3 compile.py')
        print(con+"file imported..")
        print(con + "Successfully Updated")
        print(con + "please restart...")
    else:
        print(con+"Updated..")
        time.sleep(2)
        print(con+"Loading..")
        time.sleep(2)
        os.chdir('./main')
        os.system('python3 main.py')
        #exec(open('main.py').read())

if is_connected():
    print(con+"Connected to the internet")
    time.sleep(2)
    setup()
else:
    print(con+"Not connected to the internet")
    print(con+"Try again..")
#download_latest_release_repository('amdivyansh', 'scriptbox95_source_data', 'main')
