#!/usr/bin/python3

# Native modules

import os
import pathlib
from customArgParser import CustomArgumentParser

# Non-native modules

import requests
import argparse


# Initializing terminal parser and adding commands

parser = CustomArgumentParser(prog='HTTPChecker 1.0', description='Check for working/listening web-servers')

parser.add_argument('-f', '--file', metavar='\b', required=True)
parser.add_argument('-o', '--output', metavar='\b')
parser.add_argument('--add-schema', metavar='\b')
args = parser.parse_args()


# Reading list of hosts file

pathToFile = args.__dict__['file']
with open(pathToFile, 'r') as f:
    hosts = f.read().splitlines()


# (OPTIONAL) adding schema to hosts

schemas = {
    'https': 'https://',
    'http': 'http://',
    'ftp': 'ftp://'
}

if args.__dict__['add_schema'] is not None:
    schema = args.__dict__['add_schema']
    for i in range(len(hosts)):
        hosts[i] = schemas[schema] + hosts[i]
    

# Checking for HTTP/HTTPS Web-servers

results = []

def printResInfo(res=None, redir=False):
    if redir:
        print(f'{host}  ---  code: {res.status_code}  ---  redirects to: ' + res.headers['Location'])
        results.append(f'{host}  ---  code: {res.status_code}  ---  redirects to: ' + res.headers['Location'])
    else:
        print(f'{host}  ---  code: {res.status_code}')
        results.append(f'{host}  ---  code: {res.status_code}')

for host in hosts:
    try:
        try:
            res = requests.head(host, headers={'connection': 'close'})
            if res.status_code in [301, 302, 303, 307]:
                printResInfo(res, redir=True)
            else:
                printResInfo(res)
        except requests.exceptions.ConnectionError as e:
            print(f'{host}   ---   Doesn\'t exist or couldn\'t establish a connection.')
    except requests.exceptions.MissingSchema as e:
        print(f'No schema was found for the host: {host}, try using --add-schema [schema]?')


# (OPTIONAL) Output file preparation and saving

if args.__dict__['output'] is not None:
    path = os.path.dirname(os.path.abspath(__file__)) + '\\results'
    with open(path, 'w+') as f:
        for result in results:
            f.write(f'{result}\n')

