# RedEagleMite

Folgt redirects und extrahiert finale Location.

## an den Start bringen:

```bash
git clone https://github.com/zit-bb-d43/redEagleMite.git
pip install -r requirements.txt
```

## Anwenden

So geht's:

* Domainlist zusammentragen
* Domaintransfer machen
* alles durch redEagleMite schicken

```bash

# domain.lst zusammentragen
ssh NAMESERVER grep -R "^zone " /etc/named/* | grep -v arpa | awk '{print $2}' | sed 's/\"//g' > domains.lst


# mit der Domainliste:
for DOMAIN in $( cat domains.lst )
do
  dig @mydnsserver $DOMAIN axfr | grep -E 'IN\sA|IN\sAAAA' | awk '{print $1}' >> dns_domains.txt
done

# bereinigen
sed -i -e 's/\.$//g' dns_domains.txt

# evtl. kopieren
tar cf - dns_domains.txt | ssh -o "ProxyCommand /usr/bin/nc --proxy PROXY:PROXYPORT %h %p" USER@TARGETHOST "tar xvf -"

# durch redEagleMite drehen
python .\redEagleMite.py .\dns_domains.txt
```
