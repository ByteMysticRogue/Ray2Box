def jsontemplate():
    configJson = {
    "log": {
        "disabled": False,
        "level": "error",
        "timestamp": True
    },
    "experimental": {
        "clash_api": {
            "external_controller": "127.0.0.1:9090",
            "external_ui": "metacubexd",
            "external_ui_download_url": "https://github.com/MetaCubeX/metacubexd/archive/refs/heads/gh-pages.zip",
            "external_ui_download_detour": "direct",
            "default_mode": "rule"
        },
        "cache_file": {
            "enabled": True,
            "path": "cache.db",
            "store_fakeip": False,
            "store_rdrc": False,
            "rdrc_timeout": "7d"
        }
    },
    "dns": {
        "servers": [
            {
                "address": "https://1.1.1.1/dns-query",
                "address_resolver": "dns-local",
                "detour": "Proxy",
                "strategy": "ipv4_only",
                "tag": "dns-remote"
            },
            {
                "address": "78.157.42.100",
                "address_resolver": "dns-local",
                "detour": "direct",
                "strategy": "ipv4_only",
                "tag": "dns-direct"
            },
            {
                "address": "8.8.8.8",
                "detour": "direct",
                "tag": "dns-local"
            },
            {
                "address": "rcode://success",
                "tag": "dns-block"
            }
        ],
        "rules": [
            {
                "domain": [],
                "rule_set": [
                    "geosite-ir"
                ],
                "server": "dns-direct"
            },
            {
                "disable_cache": True,
                "rule_set": [
                    "geosite-category-ads-all",
                    "geosite-malware",
                    "geosite-phishing",
                    "geosite-cryptominers"
                ],
                "server": "dns-block"
            },
            {
                "outbound": "any",
                "server": "dns-direct"
            }
        ],
        "independent_cache": True
    },
    "inbounds": [
        {
            "type": "tun",
            "tag": "tun-in",
            "domain_strategy": "ipv4_only",
            "interface_name": "sing-tun",
            "inet4_address": "172.19.0.1/30",
            "mtu": 1492,
            "auto_route": True,
            "strict_route": True,
            "stack": "gvisor",
            "endpoint_independent_nat": True,
            "sniff": True,
            "sniff_override_destination": False
        }
    ],
    "outbounds": [
        {
            "tag": "Proxy",
            "type": "selector",
            "outbounds": [
                "Auto"
            ]
        },
        {
            "tag": "Auto",
            "type": "urltest",
            "outbounds": [],
            "url": "http://cp.cloudflare.com/generate_204",
            "interval": "5m",
            "tolerance": 50
        },
        {
            "tag": "direct",
            "type": "direct"
        },
        {
            "tag": "block",
            "type": "block"
        },
        {
            "tag": "dns-out",
            "type": "dns"
        }
    ],
    "route": {
        "auto_detect_interface": True,
        "override_android_vpn": True,
        "final": "Proxy",
        "rules": [
            {
                "protocol": "dns",
                "outbound": "dns-out"
            },
            {
                "network": "udp",
                "port": 443,
                "protocol": "quic",
                "outbound": "block"
            },
            {
                "ip_is_private": True,
                "outbound": "direct"
            },
            {
                "rule_set": [
                    "geosite-category-ads-all",
                    "geosite-malware",
                    "geosite-phishing",
                    "geosite-cryptominers",
                    "geoip-malware",
                    "geoip-phishing"
                ],
                "outbound": "block"
            },
            {
                "rule_set": [
                    "geoip-ir",
                    "geosite-ir"
                ],
                "outbound": "direct"
            }
        ],
        "rule_set": [
            {
                "tag": "geosite-ir",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geosite-ir.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geosite-category-ads-all",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geosite-category-ads-all.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geosite-malware",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geosite-malware.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geosite-phishing",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geosite-phishing.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geosite-cryptominers",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geosite-cryptominers.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geoip-ir",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geoip-ir.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geoip-malware",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geoip-malware.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            },
            {
                "tag": "geoip-phishing",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Chocolate4U/Iran-sing-box-rules/rule-set/geoip-phishing.srs",
                "download_detour": "direct",
                "update_interval": "1d"
            }
        ]
    }
}
    
    return configJson