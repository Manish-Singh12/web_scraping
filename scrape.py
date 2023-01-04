# Importing libraries
import requests
import bs4
import re
from bs4 import BeautifulSoup
import logging as lg
import os

# Logging credentials
os.mkdir('logging')
os.chdir(os.getcwd() + '\\' + 'logging')
lg.basicConfig(filename='logger.log',format='%(asctime)s %(name)s %(levelname)s %(message)s',level=lg.INFO)
console_log = lg.StreamHandler()
console_log.setLevel(lg.INFO)
format = lg.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
console_log.setFormatter(format)
lg.getLogger('').addHandler(console_log)
logger = lg.getLogger('Manish')

try:
    # Setting url for webscraping
    url = 'http://web.mta.info/developers/turnstile.html'
    logger.info('Set the url for scraping')

    # Connecting to url and getting response
    res = requests.get(url)
    logger.info('Connect to url by using requests.get method and getting response')

    # Parse HTML and save to BeautifulSoup object
    parsed_html = BeautifulSoup(res.text,'html.parser')
    logger.info('Parse the html response by using BeautifulSoup feature html.parser')

    # Printing the number of anchor tags available
    print(len(parsed_html.findAll('a')))
    logger.info('Using findAll method to find all anchor tags available and printing count of them')

    # Finding the position of latest Saturday with respect to anchor tag
    Saturday_regex = re.compile(r'Saturday')
    Saturday_list = parsed_html.findAll('a')

    for i in range(len(Saturday_list)):
        anchor_text = Saturday_list[i].getText()
        Sat_text = Saturday_regex.search(anchor_text)
        if Sat_text == None:
            logger.info('latest Saturday not found')
            continue
        else:
            print(i)
            logger.info('Found latest Saturday')
            break

    latest_Saturday_tag = Saturday_list[i]
    print(latest_Saturday_tag)
    logger.info('Found the latest Saturday tag')

    link = latest_Saturday_tag['href']
    print(link)
    logger.info('Found link of latest Saturday using href under anchor tag')

    download_url = 'http://web.mta.info/developers/' + link
    print(download_url)
    logger.info('Prepared the final url for getting data from latest Saturday')

    data_res = requests.get(download_url)
    logger.info('Connect to final url by using requests.get method and getting response')

    data_text = data_res.text
    logger.info('Converted the response object to text')

    os.chdir('D:\\Web scraping')
    os.mkdir('scrape_file')
    os.chdir(os.getcwd() + '\\' + 'scrape_file')
    file = open('latestSaturday.csv','w')
    file.write(data_text)
    file.close()
    os.chdir('D:\\Web scraping' + '\\' + 'logging')
    logger.info('Create file in csv format using open method write mode and passed all the text data into it and finally closed the file')


except Exception as e:
    print('We can check our log for more info if our code will fail')
    logger.error('error has occured')
    logger.exception(str(e))

