import requests
from requests.exceptions import HTTPError

url = "https://tasks.aidevs.pl/text_pasta_history.txt"

try:
    response = requests.get(url)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    if response.status_code == 403:
        print(f'HTTP error occurred: {http_err}. This is a 403 error, access is forbidden.')
    else:
        print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')