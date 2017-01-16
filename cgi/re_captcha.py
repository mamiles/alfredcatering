import requests
import sys


class ReCaptcha(object):
    def __init__(self, secret_key):

        self.secret_key = secret_key
        self.url = 'https://www.google.com/recaptcha/api/siteverify'
        self.data = {}

    def __callApi(self, response):
        try:
            headers = {'User-Agent': 'DebuguearApi-Browser', }
            payload = {'secret': self.secret_key, 'response': response}
            r = requests.request(method='POST', url=self.url, headers=headers, data=payload)
            return r.json()

        except Exception:
            print(sys.exc_info())
            return False

    def is_success(self, response):
        self.data = self.__callApi(response)
        if self.data:
            try:
                return self.data['success']
            except:
                return None
        else:
            return None

    def get_error_codes(self):
        """
        missing-input-secret	The secret parameter is missing.
        invalid-input-secret	The secret parameter is invalid or malformed.
        missing-input-response	The response parameter is missing.
        invalid-input-response	The response parameter is invalid or malformed.
        """
        try:
            return self.data['error-codes']
        except:
            return None

    def get_hostname(self):
        try:
            return self.data['hostname']
        except:
            return None

    def get_challenge_ts(self):
        #return time stamp
        try:
            return self.data['challenge_ts']
        except:
            return None
