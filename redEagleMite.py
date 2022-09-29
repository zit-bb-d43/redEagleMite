import requests
# to extract domain
from urllib.parse import urlparse
import sys

def help():
  print(f"usage: {sys.argv[1]} <filename>")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    help()
    exit(1)
  else:
    # liest file mit Domains ein. Eine Domain pro Zeile
    dns_domains = open(sys.argv[1], "r").read().splitlines()
    bad_domainfile = "bad_domains.txt"
    outfile = "final_domains.txt"

    # domains in sets sammeln, um sie am Ende einfacher sortiert und unique in Datei zu schreiben
    finaldoms = set()
    baddoms = set()
    for dom in dns_domains:
      for prot in ["http://", "https://"]:
        print(f"{prot}{dom} -> ", end="")
        try:
          # wenn dom noch nicht in finaldomain, abklopfen
          if dom not in finaldoms:
            response = requests.get(prot + dom)
            if response.status_code == 200:
              finaldomain = urlparse(response.url).hostname
              print(f"good: {finaldomain}")
              finaldoms.add(finaldomain)
            else:
              print("bad: {finaldomain} {response.status_code}")
              baddoms.add(prot + dom)
        except Exception as e:
          print("Oops, error" + e)
          baddoms.add(prot + dom)

    # unerreichbare Domains
    with open(bad_domainfile, mode='w') as f:
      for dom in list(baddoms):
        f.write("%s\n" % dom)
      f.close()
      
    # gute domains
    with open(outfile, mode='w') as f:
      for dom in list(finaldoms):
        f.write("%s\n" % dom)
      f.close()

  exit(0)
