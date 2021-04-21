# coded by @__k_maaz__

def ip_to_info(ipadress='') :
    # defining color tags for decoration
    blue='\033[0;34m' ; yellow= '\033[0;33m' ; white='\033[0;37m' ; close= '\033[0m'
    from urllib.request import urlopen
    from json import load
    if ipadress == '' :
        url = 'https://ipinfo.io/json'
    else :
        url = f'https://ipinfo.io/{ipadress}/json'
    json_data = load(urlopen(url))
    for key in json_data :
        print(' '+blue+str(key)+close , yellow+str(json_data[key])+close , sep=white+' '*(9-len(key))+'→  '+close,end='\n\n')

ip_to_info(input("Enter the ip adress\n[No input for the default] : "))
