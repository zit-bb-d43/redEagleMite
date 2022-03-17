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

    # domains folgen
    finaldoms = set()
    for dom in dns_domains:
      for prot in ["http", "https"]:
        print(f"{prot}://{dom} -> ", end="")
        try:
          response = requests.get(prot + "://" + dom)
          if response.status_code == 200:
            finaldomain = urlparse(response.url).hostname
            print(finaldomain)
            finaldoms.add(finaldomain)
        except:
          print("Oops, error")


    # ToDo: file uniq machen?
    with open(outfile, mode='w') as f:
      for dom in list(finaldoms):
        f.write("%s\n" % dom)
      f.close()

    exit(0)
