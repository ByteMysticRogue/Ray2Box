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

from singbox.singboxGen import GenerateSingBox
from json import dumps
from re import match
from requests import get, RequestException
from base64 import b64decode
import argparse


def is_base64(contents: str) -> bool:
    if len(contents) % 4 != 0:
        return False
    
    if not match(r'^[A-Za-z0-9+/=]+$', contents):
        return False
    
    return True

def handle_request(url):
    try:
        resp = get(url, timeout=2)
        if resp.status_code == 200:
            resp = resp.text
            if is_base64(resp):
                content = b64decode(resp).decode('utf-8').strip().split('\n')
            else:
                content = [line.strip() for line in resp.split('\n') if not line.startswith('#')]
        return content
    except RequestException as e:
        return f"Error fetching URL: {e}"

def create_parser():
    parser = argparse.ArgumentParser(description="Ray2Box - a Command-line Tool To Convert V2ray links to Singbox Configs")
    parser.add_argument("-u", "--url", metavar="", dest="url", help="Fetch Configs From URL", type=str)
    parser.add_argument("-f", "--file", metavar="", dest="file", help="Read Configs From Text File", type=str)
    parser.add_argument("-l", "--link", metavar="", dest="link", help="Convert a Single Link", type=str)
    parser.add_argument("-o", "--output", metavar="", dest="output", help="Output file name", type=str)

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    file_name = args.output

    if args.url:
        urlConfigs = handle_request(args.url)
        if not urlConfigs:
            print("No configurations retrieved from the URL.")
            return
        generated = GenerateSingBox(urlConfigs)
    elif args.file:
        filePath = args.file
        try:
            with open(f'{filePath}', 'r', encoding="utf-8-sig") as f:
                fileConfigs = [line.strip() for line in f]
                if not fileConfigs:
                    print("No configurations found in the file.")
                    return
                f.close()
            generated = GenerateSingBox(fileConfigs)
        except FileNotFoundError:
            print(f"File not found: {filePath}")
            return
        except IOError as e:
            print(f"Error reading file: {e}")
            return
    elif args.link:
        linkConfig = [args.link]
        generated = GenerateSingBox(linkConfig)
    else:
        parser.print_help()
        return

    try:
        with open(f'{file_name}.json', 'w', encoding='utf-8-sig') as f:
            f.write(dumps(generated, indent=4, ensure_ascii=False))
        print("Singbox Config Converted successfully:D")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()