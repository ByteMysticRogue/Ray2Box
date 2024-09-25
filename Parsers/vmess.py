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

from json import dumps
from .security import security
from .transport import v2rayTransport
from .configInfo import processVmess

def vmess(conf):
    info = processVmess(conf)
    temp = {
            "type": "vmess",
            "tag": info['ps'],
            "domain_strategy": "prefer_ipv4",
            "server": info['add'],
            "server_port": int(info['port']),
            "uuid": info["id"],
            "security": info['scy'],
            "alter_id": int(info["aid"]),
            "global_padding": False,
            "authenticated_length": True,
            "packet_encoding": "packetaddr"
        }
    tls = security(info)
    if tls:
        temp['tls'] = tls

    transport, network = v2rayTransport(info)
    if transport:
        temp['transport'] = transport

    if network:
        temp['network'] = network

    return temp