import requests
import time
import sys
from torrequest import TorRequest

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

print("""\033[1m\033[37m
     _____ ___  ____            ____              _     ___                     ____        _                                                     
    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / / ___ _ __ ___      |  _ \ _   _| |__                                                   
    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / / / _ \ '_ ` _ \     | |_) | | | | '_ \                                                  
    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / |  __/ | | | | |    |  _ <| |_| | |_) |                                                   
    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |___|_| |_| |_|    |_| \_\\__,_|_.__/                                                   
                                              |___/                                                                                                  
                                                                     \033[41m FOS- Fools of Security :)
\033[0m
""")

# Default Tor port configuration
proxyPort = 9050
ctrlPort = 9051
site = input("Digite a URL: ")
blog = int(input("Quantas visualizações? "))

def run(tr, i):
    response = tr.get(site, headers=headers, verify=False)
    print("[" + str(i) + "]" + " Blog View Added With IP:" + tr.get('http://ipecho.net/plain').content.decode('utf-8'))
    tr.reset_identity()

if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] and sys.argv[2]:
            proxyPort = int(sys.argv[1])
            ctrlPort = int(sys.argv[2])
    
    with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
        for i in range(blog):
            run(tr, i)
