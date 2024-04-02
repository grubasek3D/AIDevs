import requests
import logging
from typing import Any, Dict, Optional

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RESTAPIBuilder:
    def __init__(self):
        self.url: Optional[str] = None
        self.headers: Dict[str, Any] = {}
        self.params: Dict[str, Any] = {}
        self.data: Optional[Dict[str, Any]] = None
        self.json: Optional[Dict[str, Any]] = None
        self.method: Optional[str] = None
        self.timeout: Optional[int] = None

    def set_url(self, url: str) -> 'RESTAPIBuilder':
        self.url = url
        return self

    def set_headers(self, headers: Dict[str, Any]) -> 'RESTAPIBuilder':
        self.headers = headers
        return self

    def set_params(self, params: Dict[str, Any]) -> 'RESTAPIBuilder':
        self.params = params
        return self

    def set_data(self, data: Dict[str, Any]) -> 'RESTAPIBuilder':
        self.data = data
        return self

    def set_json(self, json: Dict[str, Any]) -> 'RESTAPIBuilder':
        self.json = json
        return self

    def set_method(self, method: str) -> 'RESTAPIBuilder':
        self.method = method.upper()
        return self

    def set_timeout(self, timeout: int) -> 'RESTAPIBuilder':
        self.timeout = timeout
        return self

    def set_headers(self, headers: Dict[str, Any]) -> 'RESTAPIBuilder':
        self.headers = headers
        return self

    def log_request(self):
        logging.info(f"Preparing {self.method} request to {self.url}")
        logging.info(f"Headers: {self.headers}")
        logging.info(f"Params: {self.params}")
        if self.data:
            logging.info(f"Data: {self.data}")
        if self.json:
            logging.info(f"JSON: {self.json}")

    def log_response(self, response: requests.Response):
        logging.info(f"Received response from {response.url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Headers: {response.headers}")
        logging.info(f"Body: {response.text}")

    def execute(self) -> Optional[requests.Response]:
        if self.url is None or self.method is None:
            logging.error("URL or HTTP method is not set")
            return None
        
        self.log_request()

        try:
            response = requests.request(self.method,
                                        self.url,
                                        headers=self.headers,
                                        params=self.params,
                                        data=self.data,
                                        json=self.json,
                                        timeout=self.timeout)
            
            response.raise_for_status()  # This will raise for HTTP errors
            self.log_response(response)
            return response
        except requests.exceptions.HTTPError as e:
            logging.error(
                f"HTTP Error: {e.response.status_code} for {e.request.url}")
        except requests.exceptions.ConnectionError:
            logging.error("Connection error occurred.")
        except requests.exceptions.Timeout:
            logging.error("Request timed out.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
        # Handle other specific exceptions or a general catch-all here if needed

        # Return None or a custom response indicating failure if required
        return None
