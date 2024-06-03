#!/usr/bin/env python3
import sys

def filer(file):
        with open(file, 'r') as fi:
            return fi.read()

def wfile(file, content):
    with open(file, 'w') as fi:
        fi.write(content)

def replace(ip, file):
    term = "OUR_IP"
    print(f'Replacing with "OUR_IP" with: {ip}')
    content = filer(file)
    mcontent = content.replace(term, ip)
    wfile(file, mcontent)
    print("Done! ;)")

def main():
    try:
        file = sys.argv[1]
        ip = sys.argv[2]
        replace(ip, file)
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file> <yourIP>")
    

if __name__ == '__main__':
    main()