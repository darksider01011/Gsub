import re
import os 
import argparse
import requests
import datetime
from bs4 import BeautifulSoup 
from pyfiglet import Figlet
from googlesearch import search
from termcolor import colored
from colorama import Fore, Back, Style


# Unearth hidden subdomains with Google’s power

# Argument parser
parser = argparse.ArgumentParser(description='Unearth hidden subdomains with Google’s power', prog= 'Gsub.py', epilog= 'Example: python3 Gsub.py -d example.com')
parser.add_argument('-d', '--domain', type=str, help='Set target domain', default=False, required=True)
parser.add_argument('-p', '--probe', help='Enable probe mode', action='store_true')
parser.add_argument('-f', '--file', type=str,  help='Set file name to write results')
args = parser.parse_args()
domain = args.domain
sc = args.probe
file = args.file

# WARNING: Please do not change thread value (this will cause Google block your ip)
thread = 120.0 

# Date
date = datetime.datetime.now()

# Check file
if file:
    if os.path.isfile(file):
        os.remove(file) 

# Banner
f = Figlet(font='slant')
ascii_art = f.renderText('  GSUB')
colors = ['blue', 'red', 'yellow', 'green']
colored_lines = []
for line in ascii_art.split('\n'):
    colored_line = ''
    for i, char in enumerate(line):
        color = colors[i % len(colors)] if char.strip() else None
        colored_line += colored(char, color) if color else char
    colored_lines.append(colored_line)
print("")
print('\n'.join(colored_lines))
print("         Powered By Google")
print("")
print("")


# Mode status
if sc:
    print(Fore.WHITE + "Mode: Probe")
else:
    print(Fore.WHITE + "Mode: Normal")

# File name
if file:
    print(f"File: {file}")

# Domain name
print(f"Domain: {domain}")

# Public IP
try:
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print('IP: {}'.format(ip))
except requests.exceptions.ConnectionError as e:
    ip = "Null"
    print('IP:Error Fail to get public ip address')
print("=======================================")

# Lists
urls = []
domains = []
probe = []
www_unique_domains = []
basic_unique_domains = []
wild_unique_domains = []
inurl_unique_domains = []
double_unique_domains = []


# site:*.example.com -www
www_query= f"site:*.{domain} -www"
print(f"Dork: {www_query}")
print("Please wait... it might take 15 minutes")
try:
    for i in search(www_query, start=1, stop=250, num=250, pause=thread, safe='on'):
        urls.append(i)
except Exception as e:
    print(e)
    err = str(e)
    if "429" in err:
        print("Error: Your IP address has been blocked by Google's servers")
except KeyboardInterrupt:
    print('\n Keyboard interrupt!!! thanks for using Gsub') 
# Match domains 
pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
for url in urls:
    match = re.search(pattern, url)
    if match:
        domains.append(match.group(1))
# Remove duplicates
for item in domains:
    if item not in www_unique_domains:
        www_unique_domains.append(item)
# Print results
if len(www_unique_domains) == 0:
    print("\nResults:")
    print("\n Nothing Found!")
    print("")
    print("=======================================")

else:
    print("\nResults:")
    print("")
    for i in range(len(www_unique_domains)):
        print(f' {www_unique_domains[i]}')
    print("")
    print("=======================================")


# site:example.com
urls = []
domains = []
simple_query= f"site:{domain}"
print(f"Dork: {simple_query}")
try:
    for ii in search(simple_query,start=1,stop=250,num=250, pause=thread, safe='on'):
        urls.append(ii)
except Exception as e:
    print(e)
    err = str(e)
    if "429" in err:
        print("Error: Your IP address has been blocked by Google's servers")
except KeyboardInterrupt:
    print('\n Keyboard interrupt!!! thanks for using Gsub')
# Match domains 
pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
for url in urls:
    match = re.search(pattern, url)
    if match:
        domains.append(match.group(1))
# Remove duplicates
for item in domains:
    if item not in basic_unique_domains:
        basic_unique_domains.append(item)
# Print results
if len(basic_unique_domains) == 0:
    print("\nResults:")
    print("\n Nothing Found!")
    print("")
    print("=======================================")

else:
    print("\nResults:")
    print("")
    for i in range(len(basic_unique_domains)):
        print(f' {basic_unique_domains[i]}')
    print("")
    print("=======================================")


# site:*.example.com
urls = []
domains = []
wild_query= f"site:*.{domain}"
print(f"Dork: {wild_query}")
try:
    for ii in search(wild_query,start=1,stop=250,num=250, pause=thread, safe='on'):
        urls.append(ii)
except Exception as e:
    print(e)
    err = str(e)
    if "429" in err:
        print("Error: Your IP address has been blocked by Google's servers")
except KeyboardInterrupt:
    print('\n Keyboard interrupt!!! thanks for using Gsub')
# Match domains 
pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
for url in urls:
    match = re.search(pattern, url)
    if match:
        domains.append(match.group(1))
# Remove duplicates
for item in domains:
    if item not in wild_unique_domains:
        wild_unique_domains.append(item)
# Print results
if len(wild_unique_domains) == 0:
    print("\nResults:")
    print("\n Nothing Found!")
    print("")
    print("=======================================")

else:
    print("\nResults:")
    print("")
    for i in range(len(wild_unique_domains)):
        print(f' {wild_unique_domains[i]}')
    print("")
    print("=======================================")


# inurl:example.com -www site:example.com
urls = []
domains = []
inurl_query= f"inurl:{domain} -www site:{domain}"
print(f"Dork: {inurl_query}")
try:
    for ii in search(inurl_query, start=1, stop=250, num=250, pause=thread, safe='on'):
        urls.append(ii)
except Exception as e:
    print(e)
    err = str(e)
    if "429" in err:
        print("Error: Your IP address has been blocked by Google's servers")
except KeyboardInterrupt:
    print('\n Keyboard interrupt!!! thanks for using Gsub')
# Match domains 
pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
for url in urls:
    match = re.search(pattern, url)
    if match:
        domains.append(match.group(1))
# Remove duplicates
for item in domains:
    if item not in inurl_unique_domains:
        inurl_unique_domains.append(item)
# Print results
if len(inurl_unique_domains) == 0:
    print("\nResults:")
    print("\n Nothing Found!")
    print("")
    print("=======================================")
else:
    print("\nResults:")
    print("")
    for i in range(len(inurl_unique_domains)):
        print(f' {inurl_unique_domains[i]}')
    print("")
    print("=======================================")


# site:*.*.example.com
urls = []
domains = []
double_query= f"site:*.*.{domain}"
print(f"Dork: {double_query}")
try:
    for ii in search(double_query, start=1, stop=250, num=250, pause=thread, safe='on'):
        urls.append(ii)
except Exception as e:
    print(e)
    err = str(e)
    if "429" in err:
        print("Error: Your IP address has been blocked by Google's servers")
except KeyboardInterrupt:
    print('\n Keyboard interrupt!!! thanks for using Gsub')
# Match domains 
pattern = r'https?://(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
for url in urls:
    match = re.search(pattern, url)
    if match:
        domains.append(match.group(1))
# Remove duplicates
for item in domains:
    if item not in double_unique_domains:
        double_unique_domains.append(item)
# Print results
if len(double_unique_domains) == 0: 
    print("\nResults:")
    print("\n Nothing Found!")
    print("")
    print("=======================================")
else:
    print("\nResults:")
    print("")
    for i in range(len(double_unique_domains)):
        print(f' {double_unique_domains[i]}')
    print("")
    print("=======================================")


# Merge all results
unique_all_results = []
all_results = www_unique_domains + basic_unique_domains + wild_unique_domains + inurl_unique_domains + double_unique_domains

if len(all_results) > 0 :
    if domain in all_results: 
        all_results.remove(domain)

    for i in all_results:
        if i not in unique_all_results:
            unique_all_results.append(i)
    
    if domain in unique_all_results:
        unique_all_results.remove(domain)

    if sc:
        print(f"\nAll results for {domain}:")
        print("")
        for i in unique_all_results:
            print(f" {i}")
        print(f"\nNumber of subdomains: {len(unique_all_results)}")
        print("")
        print("=================================================================================================")
        print(f"\nProbe subdomains:")
        print("")
        i = 0
        for iiii in unique_all_results:
            i += 1
            target = f'https://{iiii}'
            try:
                r = requests.get(target, timeout=10)
                soup = BeautifulSoup(r.text, 'html.parser')
                try:
                    title = str(soup.title.string)
                except:
                    title = " Error: Failed to probe title"
                print(f" {i}. {iiii} || Title:{title[:60].strip()} || Status-code:{r.status_code}")
                probe.append(str(f"{i}. {iiii} || Title: {title[:60].strip()} || Status-code:{r.status_code}"))
                print("")
            except requests.exceptions.ConnectionError as e:
                ee = str(e)
                print(f" {i}. {iiii} | Title:Error: {ee[:20]} | Status-code:Error: {ee[:20]}")
                print("")

        print("=================================================================================================")
        if file:
            with open(file, "a", encoding="utf-8") as f:
                f.write("Gsub \n")
                f.write("\n")
                if sc:
                    f.write("Mode: Probe\n")
                    f.write("")
                else:
                    f.write("Mode: Normal\n")
                    f.write("")
                f.write(f'Domain: {domain}\n')
                f.write('IP: {}\n'.format(ip))    
                f.write(f'Date: {date}') 
                f.write("\n")
                f.write(f"\nAll results for {domain}:\n")

                for domain in unique_all_results:
                    f.write(f'{domain}\n')

                f.write("\n")
                f.write(f"Probe subdomains:\n")

        
                for iiiii in probe:
                    f.write(f'{iiiii}\n')         
    else:
        print(f"\nAll results for {domain}:")
        print("")
        for i in unique_all_results:
            print(f' {i}')
        print(f"\nNumber of subdomains: {len(unique_all_results)}")
        print("")
        print("========================================")
        if file:
            with open(file, "a", encoding="utf-8") as f:
                f.write("Gsub \n")
                f.write("\n")
                if sc:
                    f.write("Mode: Probe\n")
                    f.write("")
                else:
                    f.write("Mode: Normal\n")
                    f.write("")
                f.write(f'Domain: {domain}\n')
                f.write('IP: {}\n'.format(ip))    
                f.write(f'Date: {date}') 
                f.write("\n")
                f.write(f"\nAll results for {domain}:\n")

                for domain in unique_all_results:
                    f.write(f'{domain}\n')
