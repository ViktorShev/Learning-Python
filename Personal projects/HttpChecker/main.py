#!/usr/bin/python3

import requests
import argparse
import sys


# Rewriting -h (help) command
class CustomArgumentParser(argparse.ArgumentParser):

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        message = '''
-h, --help         Show this message and exit.
-f, --file         Specify the path to the file with the subdomains or IP\'s.
-o, --output       Save the check results into a file.
--add-schema       Add the specified schema to the start of all hosts in the file (https / http / ftp).
-t, --threads      Specify the amount of threads to use when making HTTP requests.

Usage example:     httpcheck -f D:/test.txt -o results.txt --add-schema https -t 10'''

        file.write(message+'\n')

# Initializing terminal parser, adding commands and defining program's functions
def parse_args():
    parser = CustomArgumentParser(prog='HTTPChecker 2.0', description='Check for working/listening web-servers')

    parser.add_argument('-f', '--file', metavar='\b', required=True)
    parser.add_argument('-o', '--output', metavar='\b')
    parser.add_argument('--add-schema', metavar='\b')
    parser.add_argument('-t', '--threads', metavar='\b', default=1)
    
    return parser.parse_args()

def get_list_from_domains_file():
    path_to_file = parse_args().__dict__['file']
    with open(path_to_file, 'r') as f:
        domains_list = f.read().splitlines()
    
    return domains_list

def add_schema_to_domains(domains_list):
    schemas = {'https': 'https://', 'http': 'http://', 'ftp': 'ftp://'}
    schema = parse_args().__dict__['add_schema']
    if schema is not None:
        for i in range(len(domains_list)):
            domains_list[i] = schemas[schema] + domains_list[i]
    else:
        return domains_list

def get_domain_status(domain):
    try:
        res = requests.head(domain, headers={'connection': 'close'})
        if res.status_code in (301, 302, 303, 307):
            status_stdout_string = f'{domain}  ---  code: {res.status_code}  ---  redirects to: ' + res.headers['Location']
        else:
            status_stdout_string = f'{domain}  ---  code: {res.status_code}'
    except requests.exceptions.ConnectionError as e:
        status_stdout_string = f'{domain}   ---   refused connection or doesn\'t exist.'
    except requests.exceptions.MissingSchema as e:
        status_stdout_string = f'No schema was found for the host: {domain}, try using --add-schema [schema]?'

    return status_stdout_string

def process_domains(domains_list):
    saved_results_for_output_file = []
    for domain in domains_list:
        status = get_domain_status(domain)
        print(status)
        saved_results_for_output_file.append(status)

    return saved_results_for_output_file

def save_file(file=None, results_list=[]):
    if file:
        with open(file, 'w+') as f:
            for result in results_list:
                f.write(f'{result}\n')

# ADD MULTITHREAD SUPPORT (-t, --threads)

# Execution
domains_list = get_list_from_domains_file()
file = parse_args().__dict__['output']
add_schema_to_domains(domains_list)
results = process_domains(domains_list)
save_file(file=file, results_list=results)