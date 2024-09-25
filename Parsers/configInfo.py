# github: https://github.com/ByteMysticRogue
# Copyright (C) 2024  ByteMysticRogue

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from re import search, findall
from urllib import parse
from base64 import b64decode
from json import loads

def extractAddress(config: str) -> str:
    ipv4_pattern = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    domain_pattern = r'(?<=@)([^:\s]+)(?=[:])'
    
    match = search(domain_pattern, config)
    if match:
        return match.group(1)
    
    match = search(ipv4_pattern, config)
    if match:
        return match.group(0)  
    
    return None

def extractPort(config: str) -> str:
    port_part = config.split(":")[1]
    port = port_part.split("#")[0]
    return port

def extractUUID(config: str) -> str:
    id_pattern = r"([0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}|[\w\-]+)"
    uuid = findall(id_pattern, config)[0]

    return uuid

def processParams(baseUrl: list) -> dict:
    configDict = {}
    configDict['uuid'] = extractUUID(baseUrl[0])
    configDict['address'] = extractAddress(baseUrl[0])
    configDict['port'] = extractPort(baseUrl[0])

    params = parse.parse_qsl(baseUrl[1], keep_blank_values=True)

    tag = "Proxy"
    for key, value in params:
        if '#' in value:
            value, tag = value.split('#', 1)
        configDict[key] = value

    configDict['tag'] = tag
    return configDict


def processTrojan(config: str) -> dict:
    baseUrl = config.split("?")
    json = processParams(baseUrl)
    json['protocol'] = 'trojan'
    
    return json

def processVless(config: str) -> dict:
    baseUrl = config.split("?")
    json = processParams(baseUrl)
    json['protocol'] = 'vless'
    
    return json

def processVmess(config: str) -> dict:
    decodedConfig = loads(b64decode(config).decode('utf-8'))
    # override some keys
    decodedConfig['security'] = decodedConfig.pop('tls')
    decodedConfig['headerType'] = decodedConfig.pop('type')
    decodedConfig['type'] = decodedConfig.pop('net')
    decodedConfig['protocol'] = 'vmess'
    
    return decodedConfig

def processSS(config: str) -> dict:
    configDict = {}
    baseUrl = config.split('@')
    decodeB64part = b64decode(baseUrl[0]).decode('utf-8').split(":")
    configDict['method'] = decodeB64part[0]
    configDict['password'] = decodeB64part[1]
    configDict['address'] = extractAddress(baseUrl[1])
    configDict['port'] = extractPort(baseUrl[1])
    configDict['tag'] = parse.unquote(baseUrl[1].split("#")[1])
    
    return configDict

def processHY2(config: str) -> dict:
    baseUrl = config.split("?")
    json = processParams(baseUrl)
    json['protocol'] = 'hy2'
    
    return json