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

from .configInfo import processSS

def ss(conf):
    info = processSS(conf)
    temp = {
        "type": "shadowsocks",
        "tag": info['tag'],
        "server": info['address'],
        "server_port": int(info['port']),
        "method": info['method'],
        "password": info['password'],
        "domain_strategy":"prefer_ipv4",
        "udp_over_tcp": False
    }
    return temp
