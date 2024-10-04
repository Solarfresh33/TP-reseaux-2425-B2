# TP1 : Maîtrise réseau du votre poste

## I. Basics

☀️ Carte réseau WiFi

ipconfig

Configuration IP de Windows

```
Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::c4e6:c919:d4f6:f354%18
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.73.79
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   ```
   CIDR : /20

☀️ Déso pas déso
```
10.33.7
10.33.79.255
4094
```	

☀️ Passerelle du réseau

arp -a

```
10.33.79.254
7c-5a-1c-d3-d8-76 
```

☀️ Serveur DHCP et DNS

```
ipconfig /all 

    Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
    Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                             1.1.1.1
```

☀️ Table de routage

```
route print

    IPv4 Table de routage
    ===========================================================================
    Itinéraires actifs :
    Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254      10.33.73.79     30

```

## II. Go further

☀️ Hosts ?
```
ping b2.hello.vous

Envoi d’une requête 'ping' sur B2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=17 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=18 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=17 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=25 ms TTL=55

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 17ms, Maximum = 25ms, Moyenne = 19ms
```

☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...

```
netstat -n

    Proto  Adresse locale          Adresse distante        État
    TCP    10.33.73.79:62165      172.64.155.209:443     ESTABLISHED

```

☀️ Requêtes DNS

```
nslookup www.thinkerview.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.thinkerview.com
Addresses:  2a06:98c1:3120::7
          2a06:98c1:3121::7
          188.114.97.7
          188.114.96.7
```

```
nslookup 143.90.88.12
Serveur :   dns.google
Address:  8.8.8.8

Nom :    EAOcf-140p12.ppp15.odn.ne.jp
Address:  143.90.88.12
```

☀️ Hop hop hop
```
tracert ynov.com

Détermination de l’itinéraire vers ynov.com [104.26.11.233]
avec un maximum de 30 sauts :

  1     6 ms     3 ms     4 ms  10.33.79.254
  2     3 ms     3 ms     3 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     4 ms     2 ms     3 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     5 ms     4 ms     4 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    13 ms    12 ms    12 ms  164.147.6.194.rev.sfr.net [194.6.147.164]
  6     *        *        *     Délai d’attente de la demande dépassé.
  7    18 ms    17 ms    16 ms  162.158.20.31
  8    17 ms    19 ms    16 ms  104.26.11.233
```

☀️ IP publique

```
195.7.117.146
```

## III. Wireshark

☀️ Capture ARP

```
ping 10.3.79.254

Envoi d’une requête 'Ping'  10.3.79.254 avec 32 octets de données :
Réponse de 109.0.120.158 : Impossible de joindre l’hôte de destination.
Réponse de 109.0.120.158 : Impossible de joindre l’hôte de destination.
Réponse de 109.0.120.158 : Impossible de joindre l’hôte de destination.
Réponse de 109.0.120.158 : Impossible de joindre l’hôte de destination.

Statistiques Ping pour 10.3.79.254:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
```

☀️ Capture DNS

[Capture DNS vers Youtube.com](./TP-reseaux-2425-B2/TP1/CaptureDNS.png)


☀️ Capture TCP

[Capture TCP vers Dofus.com](./TP-reseaux-2425-B2/TP1/CaptureTCP.png)


