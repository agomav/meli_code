import os
import json
import requests as req
from configuration.configProvider import configurationServer


class authHandler:


    
    def get_auth_url():
     prop= configurationServer()
     
     ME_LI_APP_ID=prop.getProperty('me_li_app_id')
     
     FULL_AUTH_URL_TEMPLATE=prop.getProperty('me_li_auth_url_tem')
     FULL_AUTH_URL_TEMPLATE.replace("&", "&amp;")
     
     url=FULL_AUTH_URL_TEMPLATE.replace('{}',ME_LI_APP_ID)
     print(url)
     return url


    def get_access_token(api_code):
        prop= configurationServer()
        
        ME_LI_FULL_URL_API_TEMPLATE=prop.getProperty('me_li_outh_url')
     
        ME_LI_SECRET_KEY=prop.getProperty('me_li_secret_key')
        ME_LI_APP_ID=prop.getProperty('me_li_app_id')

        ME_LI_FULL_URL_API_TEMPLATE.replace("&", "&amp;")
     
        working_url=ME_LI_FULL_URL_API_TEMPLATE.replace('{}',ME_LI_APP_ID,1)

        working_url1=working_url.replace('{}',ME_LI_SECRET_KEY,1)

        new_url=working_url1.replace('{}',api_code,1)

        print("full new url is: " + new_url)



        if api_code != '':

          r = req.post(new_url, allow_redirects=False)

          new_token = r.json()['access_token']

          
          return new_token

        
        return ""
      
      

    






