from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.chrome.options import Options
import os
import sys
import time
import re

os.environ['MOZ_HEADLESS'] = '1'
website = str(input('Insert the URL of the website: '))

print('Please wait while we extract the sources...')

browser = webdriver.Firefox(executable_path=r'D:\Python\Learning-Python\Personal projects\File extractor\web_drivers\geckodriver.exe')
try:
    browser.get(website)
except selenium.common.exceptions.InvalidArgumentException as e:
    browser.close()
    print('Invalid or non-existent URL provided, please provide a valid URL.')
    time.sleep(5)
    sys.exit(1)

content = browser.page_source
regex = re.compile(r'src=".+?"')
sources = regex.finditer(content)
matches = [match.group(0) for match in sources]
for link in matches:
    if '.js' in link:
        continue
    else:
        print(f'\n{link}')

browser.close()

print('')
save_or_not = input('Would you like to save the matches in a local .txt file? (y/n): ')
if save_or_not == 'y':
    file_name = str(input('Type in the name of the file: '))
    path = f'D:\Python\Learning-Python\Personal projects\File extractor\sources\{file_name}.txt'
    with open(path, 'w', encoding='utf-8') as s_file:
        with open(path, 'a', encoding='utf-8') as s_file:
            s_file.write(f'SOURCES GATHERED FROM: {website}\n\n')
            for link in matches:
                if '.js' not in link:
                    s_file.write(f'{link}\n\n')
                else:
                    continue
            print(f'\nFile created at: {path}\n')
            time.sleep(5)
            sys.exit(1)
else:
    print('\nClosing...')
    time.sleep(5)
    sys.exit(1)
