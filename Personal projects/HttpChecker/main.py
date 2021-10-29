#!

# Native modules
import os
import pathlib

# Non-native modules
import requests
import argparse


# Initializing terminal parser and adding commands

parser = argparse.ArgumentParser(prog='HTTPChecker 1.0', description='Check for working/listening web-servers', add_help=False)

parser.add_argument('-f', '--file', help='Specify the path to the file with the subdomains or IP\'s', metavar='\b', required=True)
parser.add_argument('-o', '--output', help='Save the check results into a file', metavar='\b')
parser.add_argument('--add-schema', help='Add the specified schema to the start of all hosts in the file', metavar='\b')
args = parser.parse_args()


# Reading list of hosts file

pathToFile = args.__dict__['file']
with open(pathToFile, 'r') as f:
    hosts = f.read().splitlines()


# (OPTIONAL) adding schema to hosts

schemas = {
    'https': 'https://',
    'http': 'https://',
    'ftp': 'ftp://'
}

if args.__dict__['add_schema'] is not None:
    schema = args.__dict__['add_schema']
    for i in range(len(hosts)):
        hosts[i] = schemas[schema] + hosts[i]
    

# Checking for HTTP/HTTPS Web-servers

results = []
for host in hosts:
    try:
        try:
            req = requests.get(host, headers={'connection': 'close'})
            print(f'{host}   ---   {req.status_code}')
            results.append(f'{host}   ---   {req.status_code}')
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

