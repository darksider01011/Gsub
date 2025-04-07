# Gsub –  Unearth hidden subdomains with Google’s power 
**Gsub** is a evasion-focused subdomain enumeration tool that uses **Google Dorks** to uncover hidden subdomains without triggering rate limits or CAPTCHAs. Designed for security professionals who prioritize stealth and completeness over raw speed. 

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
## Gsub output
```text
         ___________ __  ______
        / ____/ ___// / / / __ )
       / / __ \__ \/ / / / __  |
      / /_/ /___/ / /_/ / /_/ /
      \____//____/\____/_____/

         Powered By Google


Mode: Normal
File: output.txt
Domain: microsoft.com
IP: 255.255.255.255
=======================================
Dork: site:*.microsoft.com -www

Results:

math.microsoft.com
account.microsoft.com
azure.microsoft.com
create.microsoft.com
support.microsoft.com
copilot.microsoft.com
learn.microsoft.com
apps.microsoft.com
devblogs.microsoft.com
developer.microsoft.com
adoption.microsoft.com
techcommunity.microsoft.com
msdn.microsoft.com
careers.microsoft.com
news.microsoft.com
answers.microsoft.com
=======================================
Dork: site:microsoft.com

Results:

clarity.microsoft.com
forms.microsoft.com
apps.microsoft.com
copilot.microsoft.com
account.microsoft.com
word.cloud.microsoft.com
careers.microsoft.com
microsoft.com
developer.microsoft.com
support.microsoft.com
visualstudio.microsoft.com
learn.microsoft.com
adoption.microsoft.com
myaccount.microsoft.com
rewards.microsoft.com
events.teams.microsoft.com
krs.microsoft.com
r.office.microsoft.com
dotnet.microsoft.com
msdn.microsoft.com
create.microsoft.com
azure.microsoft.com
appsource.microsoft.com
go.microsoft.com
=======================================
Dork: site:*.microsoft.com

Results:

clarity.microsoft.com
forms.microsoft.com
apps.microsoft.com
account.microsoft.com
word.cloud.microsoft.com
careers.microsoft.com
microsoft.com
developer.microsoft.com
support.microsoft.com
visualstudio.microsoft.com
learn.microsoft.com
adoption.microsoft.com
myaccount.microsoft.com
rewards.microsoft.com
events.teams.microsoft.com
krs.microsoft.com
r.office.microsoft.com
dotnet.microsoft.com
azureforeducation.microsoft.com
msdn.microsoft.com
create.microsoft.com
azure.microsoft.com
appsource.microsoft.com
=======================================
Dork: inurl:microsoft.com -www site:microsoft.com

Results:

account.microsoft.com
myaccount.microsoft.com
support.microsoft.com
learn.microsoft.com
unlocked.microsoft.com
techcommunity.microsoft.com
serviceshub.microsoft.com
support.serviceshub.microsoft.com
partner.microsoft.com
securitypartners.transform.microsoft.com
coach.microsoft.com
dialin.teams.microsoft.com
cqd.teams.microsoft.com
answers.microsoft.com
azure.microsoft.com
msrc.microsoft.com
appsource.microsoft.com
developer.microsoft.com
blogs.microsoft.com
devblogs.microsoft.com
planetarycomputer.microsoft.com
cdx.transform.microsoft.com
dev.teams.microsoft.com
lti.microsoft.com
news.microsoft.com
careers.microsoft.com
=======================================
Dork: site:*.*.microsoft.com

Results:

visualstudiogallery.msdn.microsoft.com
powerpoint.cloud.microsoft.com
word.cloud.microsoft.com
cmt3.research.microsoft.com
about.ads.microsoft.com
jobs.careers.microsoft.com
events.teams.microsoft.com
r.office.microsoft.com
dmc.partner.microsoft.com
support.serviceshub.microsoft.com
catalog.update.microsoft.com
hs.windows.microsoft.com
unistore.www.microsoft.com
query.prod.cms.rt.microsoft.com
emails.azure.microsoft.com
=======================================

All results for microsoft.com:

math.microsoft.com
account.microsoft.com
azure.microsoft.com
create.microsoft.com
support.microsoft.com
copilot.microsoft.com
learn.microsoft.com
apps.microsoft.com
devblogs.microsoft.com
developer.microsoft.com
adoption.microsoft.com
techcommunity.microsoft.com
msdn.microsoft.com
careers.microsoft.com
news.microsoft.com
answers.microsoft.com
clarity.microsoft.com
forms.microsoft.com
word.cloud.microsoft.com
visualstudio.microsoft.com
myaccount.microsoft.com
rewards.microsoft.com
events.teams.microsoft.com
krs.microsoft.com
r.office.microsoft.com
dotnet.microsoft.com
appsource.microsoft.com
go.microsoft.com
azureforeducation.microsoft.com
unlocked.microsoft.com
serviceshub.microsoft.com
support.serviceshub.microsoft.com
partner.microsoft.com
securitypartners.transform.microsoft.com
coach.microsoft.com
dialin.teams.microsoft.com
cqd.teams.microsoft.com
msrc.microsoft.com
blogs.microsoft.com
planetarycomputer.microsoft.com
cdx.transform.microsoft.com
dev.teams.microsoft.com
lti.microsoft.com
visualstudiogallery.msdn.microsoft.com
powerpoint.cloud.microsoft.com
cmt3.research.microsoft.com
about.ads.microsoft.com
jobs.careers.microsoft.com
dmc.partner.microsoft.com
catalog.update.microsoft.com
hs.windows.microsoft.com
unistore.www.microsoft.com
query.prod.cms.rt.microsoft.com
emails.azure.microsoft.com

Number of subdomains: 54

========================================
```
