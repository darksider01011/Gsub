# Gsub –  Unearth hidden subdomains with Google’s power 
**Gsub** is a evasion-focused subdomain enumeration tool that uses **Google Dorks** and OSINT techniques to uncover hidden subdomains without triggering rate limits or CAPTCHAs. Designed for security professionals who prioritize stealth and completeness over raw speed. 

![banner](./images/new-banner.png "banner")

### options
```bash
  -d, --domain TARGET  Set target domain
  -p, --probe          Enable probe mode
  -f, --file FILE      Set file name to write results
```
### Install requirements 
 ```bash
 pip install -r requirements.txt
 ```
### Probe Mode
```bash
python3 Gsub.py -d example.com -p
```
### Normal Mode
```bash
python3 Gsub.py -d example.com 
```
### apple.com
```text
Mode: Normal
Domain: apple.com
IP: 255.255.255.255
=======================================
Dork: site:*.apple.com -www

Results:

podcasts.apple.com
support.apple.com
apps.apple.com
music.apple.com
jobs.apple.com
checkcoverage.apple.com
developer.apple.com
investor.apple.com
=======================================
Dork: site:apple.com

Results:

tv.apple.com
developer.apple.com
apple.com
support.apple.com
stocks.apple.com
beta.apple.com
itunesconnect.apple.com
checkcoverage.apple.com
podcasts.apple.com
locate.apple.com
=======================================
Dork: site:*.apple.com

Results:

apple.com
checkcoverage.apple.com
tv.apple.com
developer.apple.com
support.apple.com
store.apple.com
stocks.apple.com
beta.apple.com
itunesconnect.apple.com
podcasts.apple.com
music.apple.com
apps.apple.com
=======================================
Dork: inurl:apple.com -www site:apple.com

Results:

support.apple.com
music.apple.com
developer.apple.com
discussions.apple.com
regulatoryinfo.apple.com
apps.apple.com
ecommerce.apple.com
locate.apple.com
=======================================
Dork: site:*.*.apple.com

Results:

offer.shazam.apple.com
replay.music.apple.com
=======================================
All results for apple.com:

podcasts.apple.com
support.apple.com
apps.apple.com
music.apple.com
jobs.apple.com
checkcoverage.apple.com
developer.apple.com
investor.apple.com
tv.apple.com
stocks.apple.com
beta.apple.com
itunesconnect.apple.com
locate.apple.com
store.apple.com
discussions.apple.com
regulatoryinfo.apple.com
ecommerce.apple.com
offer.shazam.apple.com
replay.music.apple.com

Number of subdomains: 19
========================================
```
