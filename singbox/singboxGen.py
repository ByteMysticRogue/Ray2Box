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

from Parsers.vless import vless
from Parsers.vmess import vmess
from Parsers.trojan import trojan
from Parsers.ss import ss
from Parsers.hy2 import hy2
from json import load
from re import match, compile
from template.template import jsontemplate

def parse_outbound_configs(configs: list) -> list:
    parsed_configs = [] 
    
    for config in configs:
        parsed_config = {}

        if config.startswith('vless://'):
            config = config.removeprefix('vless://')
            parsed_config = vless(config)
        elif config.startswith('vmess://'):
            config = config.removeprefix('vmess://')
            parsed_config = vmess(config)
        elif config.startswith('trojan://'):
            config = config.removeprefix('trojan://')
            parsed_config = trojan(config)
        elif config.startswith('ss://'):
            config = config.removeprefix('ss://')
            parsed_config = ss(config)
        elif config.startswith('hy2://'):
            config = config.removeprefix('hy2://')
            parsed_config = hy2(config)

        if len(parsed_config) != 0:
            parsed_configs.append(parsed_config)

    return parsed_configs

def GenerateSingBox(configArr: list) -> dict:
    domain_pattern = compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$")


    Template = jsontemplate()


    try:
        outbounds = parse_outbound_configs(configArr)
        index = 2
        
        for outbound in outbounds:
            try:
                domain = outbound['server']
                if domain and bool(match(domain_pattern, domain)) and domain not in Template['dns']['rules'][0]['domain']:
                    Template['dns']['rules'][0]['domain'].append(domain)
                
                tag = outbound['tag']
                Template['outbounds'][0]['outbounds'].append(tag)
                Template['outbounds'][1]['outbounds'].append(tag)
                Template['outbounds'].insert(index, outbound)
                index += 1
            except KeyError as e:
                return f"Missing key '{e}' in the outbound config: {outbound}"
            except Exception as e:
                return f"Error processing outbound configuration: {e}"
        
        return Template
    
    except Exception as e:
        return f"Error during outbound processing: {e}"