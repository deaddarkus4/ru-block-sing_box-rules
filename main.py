import json
import subprocess

import requests

txt = requests.get('https://antifilter.download/list/domains.lst')
targets = txt.text.splitlines()

sign_json = {
    'version': 1,
    'rules': [
        {
            'domain': targets
        }
    ]
}

with open('geosite-ru-block.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(sign_json, indent=2))

result = subprocess.run('sing-box rule-set compile geosite-ru-block.json')
if result.returncode == 0:
    print('geosite-ru-block.srs saved successful')
else:
    print(result.stderr)
#######################################################################
txt = requests.get('https://antifilter.download/list/allyouneed.lst')

targets = txt.text.splitlines()

sign_json = {
    'version': 1,
    'rules': [
        {
            'ip_cidr': targets
        }
    ]
}

with open('geoip-ru-block.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(sign_json, indent=2))

subprocess.run('sing-box rule-set compile geoip-ru-block.json')
if result.returncode == 0:
    print('geoip-ru-block.srs saved successful')
else:
    print(result.stderr)
