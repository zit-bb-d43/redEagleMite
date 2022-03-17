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
    outfile = "final_domains.txt"

    # domain folgen
    for dom in dns_domains:
      print(f"{dom} -> ", end="")
      for prot in ["http", "https"]:
        try:
          response = requests.get(prot + "://" + dom)
          if response.status_code == 200:
            finaldomain = urlparse(response.url).hostname
            # warum ist der Hostname doppelt?
            print(finaldomain)
            with open(outfile, mode='a') as f:
              f.write(finaldomain)
              f.close()
        except:
          print("Oops, error")


    # ToDo: file uniq machen?

    exit(0)
