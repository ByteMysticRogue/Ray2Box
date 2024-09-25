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

from .transport import v2rayTransport
from .security import security
from .configInfo import processVless

def vless(conf):
    info = processVless(conf)
    temp = {
        "type": "vless",
        "tag": f"{info['tag']}",
        "domain_strategy": "prefer_ipv4",
        "server": f"{info['address']}",
        "server_port": int(info['port']),
        "uuid": f"{info['uuid']}",
        "packet_encoding": "packetaddr"
    }

    if 'flow' in info.keys():
        temp['flow'] = info['flow']

    tls = security(info)
    if tls:
        temp['tls'] = tls

    transport, network = v2rayTransport(info)
    if transport:
        temp['transport'] = transport

    if network:
        temp['network'] = network

    return temp