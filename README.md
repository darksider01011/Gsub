# Gsub –  Unearth hidden subdomains with Google’s power 
**Gsub** is a evasion-focused subdomain enumeration tool that uses **Google Dorks** and OSINT techniques to uncover hidden subdomains without triggering rate limits or CAPTCHAs. Designed for security professionals who prioritize stealth and completeness over raw speed. 

![banner](./images/new-banner.png "banner")

### options
```bash
  -d, --domain TARGET  Set target domain
  -p, --probe          Enable probe mode
  -f, --file FILE      Set file name to write results
```
### Probe Mode
```bash
python3 Gsub.py -d example.com -p
```
### Normal Mode
```bash
python3 Gsub.py -d example.com 
```

