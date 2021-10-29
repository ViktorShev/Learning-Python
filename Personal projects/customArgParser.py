import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        message = '''
-h, --help         Show this message and exit.
-f, --file         Specify the path to the file with the subdomains or IP\'s.
-o, --output       Save the check results into a file.
--add-schema       Add the specified schema to the start of all hosts in the file (https / http / ftp).

Usage example:     httpcheck -f D:/test.txt --o results.txt --add-schema https'''

        file.write(message+'\n')