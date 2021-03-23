
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class Transport(object):
   # def __init__(self,host,port,user,pw):
    #    self._url = 'http://' + host + ':' + str(port)
     #   self._auth = (user,pw)

    def connection(self,host,port,user,pw):
        self._url = 'http://' + host + ':' + str(port)
        self._auth = (user,pw)

    def get(self,call):
        _response = requests.get(
            url = self._url + '/' + call,
            auth = self._auth,
            headers = {
                    'Accept':'application/yang-data+json'
            },
            verify = False
        )
        return _response

    def post(self,call,body):
        _response = requests.post(
            url = self._url + '/' + call,
            auth = self._auth,
            headers = {
                    'Accept':'application/yang-data+json'
            },
            data = body,
            verify = False
        )
        return _response

    def put(self,call,body):
        _response = requests.put(
            url = self._url + '/' + call,
            auth = self._auth,
            headers = {
                    'Accept':'application/yang-data+json'
            },
            data=body,
            verify = False
        )
        return _response

    def patch(self,call,body):
        _response = requests.path(
            url = self._url + '/' + call,
            auth = self._auth,
            headers = {
                    'Accept':'application/yang-data+json'
            },
            data=body,
            verify = False
        )
        return _response

    def delete(self,call):
        _response = requests.delete(
            url = self._url + '/' + call,
            auth = self._auth,
            headers = {
                    'Accept':'application/yang-data+json'
            },
            verify = False
        )
        return _response