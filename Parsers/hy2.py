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

from .configInfo import processHY2
from .security import security

def hy2(conf):
    info = processHY2(conf)
    temp = {
        "type": "hysteria2",
        "tag": info['tag'],
        "server": info['address'],
        "server_port": int(info['port']),
        "up_mbps": 20,
        "down_mbps": 100,
        "obfs": {
            "type": "salamander",
            "password": info['obfs-password']
        },
        "password": info['uuid'],
        "brutal_debug": False
    }

    tls = security(info)
    if tls:
        temp['tls'] = tls

    return temp