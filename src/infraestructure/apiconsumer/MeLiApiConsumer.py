
import requests as req
from requests.adapters import HTTPAdapter
from configuration.configProvider import configurationServer


class MeLiAPIClient:
    
    url_base=''
    current_token=''
    access_key=''
    app_id=''

    def __init__(self):
        prop=configurationServer()
        self.url_base=prop.getProperty('me_li_req_enpoint_url')   
        self.access_key=prop.getProperty('me_li_secret_key') 
        self.app_id=prop.getProperty('me_li_app_id') 



    def _get(self, endpoint,**kwargs):
        print("bASE IS: "+ self.url_base)


        get_full_url=str(self.url_base)+str(endpoint)

        print('THE FULL URL NOW IS: ' , get_full_url)

        
        return self._request('GET', str(get_full_url),**kwargs)

    
    def _set_token(self,new_token):
        self.current_token=new_token

    

    def _request(self, method, endpoint, params=None):
        bearer="Bearer " + self.current_token
       
        _params = {"Authorization": bearer}
        print("full url is now: "+endpoint) 
        
        response = req.get(endpoint,headers=_params, timeout=30)
        print("done !!! get")
        return self._parse(response)
    
    
    def _parse(self, response):
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        return r