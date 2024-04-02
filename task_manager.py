import configparser
import logging
from rest_api_builder import RESTAPIBuilder
from urllib.parse import urlparse
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaskManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.base_url = self.config['API']['base_url']
        self.apikey = self.config['API']['apikey']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
            }

    def getToken(self, taskName) -> str:
        response = RESTAPIBuilder().set_url(f"{self.base_url}token/{taskName.lower()}") \
                                   .set_method('POST') \
                                   .set_json({'apikey': self.apikey}) \
                                   .execute()

        if response and response.status_code == 200:
            token = response.json().get('token')
            return token
        return None

    def getTask(self, token: str) -> dict:
        response = RESTAPIBuilder().set_url(f"{self.base_url}task/{token}") \
                                   .set_method('GET') \
                                   .execute()

        if response and response.status_code == 200:
            return response.json()
        return None

    def getHint(self, taskName: str) -> dict:
        response = RESTAPIBuilder().set_url(f"{self.base_url}hint/{taskName}") \
                                   .set_method('GET') \
                                   .execute()

        if response and response.status_code == 200:
            return response.json()
        return None
    
    def submitAnswer(self, token: str, answer: str) -> bool:
        response = RESTAPIBuilder().set_url(f"{self.base_url}answer/{token}") \
                                   .set_method('POST') \
                                   .set_json({'answer': answer}) \
                                   .execute()

        return response is not None and response.status_code == 200
    
    def sendData(self, token: str, data: any) -> bool:
        response = RESTAPIBuilder().set_url(f"{self.base_url}task/{token}") \
                                   .set_method('POST') \
                                   .set_data(data) \
                                   .execute()

        if response and response.status_code == 200:
            return response.json()
        return None
    
    def downloadFile(self, url, file_name, retries = 10, timeout = 60):
        if urlparse(url).scheme in ('http', 'https'):
            for i in range(retries):
                try:
                    response = RESTAPIBuilder().set_url(url) \
                                            .set_method('GET') \
                                            .set_timeout(timeout) \
                                            .set_headers(self.headers) \
                                            .execute()
                    if response is not None:
                        if response.status_code == 200:
                            print(response)
                            with open(file_name, "wb") as file:
                                file.write(response.content)
                            
                            break
                    else:
                        raise
                
                except:
                    if i == retries - 1:
                        raise
                    else:
                        time.sleep(1 ** i)
                
                finally:
                    pass
            