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

def v2rayTransport(info: dict) -> (dict, str):
    transport = {}
    network = None
    host = f"{info.get('host', '')}"
    path = f"{info.get('path', '')}"
    serviceName = f"{info.get('serviceName', '')}"
    headerType = f"{info.get('headerType', '')}"

    if info['type'] == 'ws':
        transport = {
            "type": "ws",
            "path": path.split("?")[0],
            "headers":{
                "Host": host
                },
            "max_early_data": 0,
            "early_data_header_name": ""
        }

    elif info['type'] == 'grpc':
        transport = {
            "type": "grpc",
            "service_name": serviceName,
            "idle_timeout": "15s",
            "ping_timeout": "15s",
            "permit_without_stream": False
        }

    elif info['type'] == 'http':
        network = 'tcp'
        transport = {
            "type": "http",
            "headers": {
                "host": host
            },
            "path": path,
            "idle_timeout": "15s",
            "ping_timeout": "15s"
        }

    elif info['type'] == 'tcp' and (headerType == '' or headerType == 'none'):
        network = 'tcp'
    
    elif info['type'] == 'tcp' and headerType == "http":
        network = 'tcp'
        transport = {
            "type": "http",
            "headers": {
                "host": host
            },
            "path": path,
            "idle_timeout": "15s",
            "ping_timeout": "15s"
        }

    elif info['type'] == 'httpupgrade':
        transport = {
            "type": "httpupgrade",
            "path": path.split("?")[0],
            "headers": {
                "host": host
            }
        }
    return transport, network