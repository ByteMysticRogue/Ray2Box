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

def AlpnBasedOnTransport(proto: str, type: str) -> list:

    if proto == 'hy2':
        alpnList = [
            "h3"
            ]
    elif type in ['ws', 'tcp', 'httpupgrade']:
        alpnList = [
            "http/1.1"
            ]
    elif type in ['grpc', 'http']:
        alpnList = [
            "h2",
            "http/1.1"
        ]

    return alpnList

def fingerPrint(fpValue: str) -> dict:
    if fpValue != "":
        return {
            "enabled": True,
            "fingerprint": f"{fpValue}"
        }
    
    return {
            "enabled": False,
            "fingerprint": ""
        }
def security(info: dict) -> dict:
    tls = {}
    https_ports = ["443", "2053", "2083", "2087", "2096", "8443"]
    
    alpn = AlpnBasedOnTransport(info.get('protocol', ''), info.get('type', ''))
    sni = f"{info.get('sni', info['address'])}"
    insecure = bool(int(info.get('insecure', 0)))
    fp = fingerPrint(info.get('fp', ''))
    if info['port'] in https_ports:
        if info.get('security') == 'reality':
            pbk = f"{info.get('pbk', '')}"
            sid = f"{info.get('sid', '')}"
            tls = {
                "enabled": True,
                "server_name": sni,
                "insecure": insecure,
                "alpn": alpn,
                "utls": fp,
                "reality": {
                        "enabled": True,
                        "public_key": pbk,
                        "short_id": sid
                }
            }
        else:
            tls = {
                    "enabled": True,
                    "server_name": sni,
                    "insecure": insecure,
                    "alpn": alpn,
                    "utls": fp
                    }
    return tls