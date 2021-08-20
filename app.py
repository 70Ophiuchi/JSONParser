import re
import requests

def reader(url):
    resp = requests.get(url)
    dictionary = resp.json()

    for x in range(107):
        name = dictionary[x]
        
        if not "tcpPorts" in name:
            nameFinal = f"ID {str(name['id'])} serviceArea {str(name['serviceArea'])} serviceAreaDisplayName {str(name['serviceAreaDisplayName'])} updPorts {str(name['udpPorts'])} expressRoute {str(name['expressRoute'])}"
            Final = nameFinal.replace(" ", "_")
        else:
            nameFinal = f"ID {str(name['id'])} serviceArea {str(name['serviceArea'])} serviceAreaDisplayName {str(name['serviceAreaDisplayName'])} tcpPorts {str(name['tcpPorts'])} expressRoute {str(name['expressRoute'])}"
            Final = nameFinal.replace(" ", "_")

        try:
            ip6 = []
            ip4 = []
            IPV4 = ''
            IPV6 = ''
            for x in name["ips"]:
                if re.search("::", x):
                    ip6.append(str(x))
                    IPV6 = '\n'.join(ip6)
                else:
                    ip4.append(x)
                    IPV4 = '\n'.join(ip4)
        except KeyError:
            print("could not find IPs")

    

        try:
            URL = "\n".join(name["urls"])
        except KeyError:
            print("could not find URLs")


        with open(f"{Final}_URLs.txt", "w") as f:
            try:   
                f.write(URL)
            except KeyError:
                f.write("URL does not exist")

        with open(f"{Final}_IPV4.txt", "w") as  r:
            try:
                r.write(IPV4)
            except KeyError:
                r.write('IP does not exist')

        with open(f"{Final}_IPV6.txt", "w") as  r:
            try:
                r.write(IPV6)
            except KeyError:
                r.write('IP does not exist')

reader('https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7')
