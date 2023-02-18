import requests
import time

def measure_response_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    return response_time

measure_response_time('https://www.google.com')

measure_response_time('https://www.ynet.co.il')

measure_response_time('https://www.imdb.com')

