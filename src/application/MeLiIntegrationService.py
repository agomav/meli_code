from infraestructure.apiconsumer.MeLiApiConsumer import MeLiAPIClient
from infraestructure.apiconnection.MeLiAuthHandler import authHandler


class MeliService:

    token=''

     
    def __init__(self):
      print("creating...") 
      


    def __new__(self, *args, **kw):
        if not hasattr(self, '_instance'):
            orig = super(MeliService, self)
            self._instance = orig.__new__(self, *args, **kw)
        return self._instance
    
    
    def auth_handler(self, api_code):
        self.token=authHandler.get_access_token(api_code)
        print("from service, the token is: " + self.token)
        

        
    
    
    def ml_get_request(self,endpoint):
        getter=MeLiAPIClient()
        getter._set_token(self.token)
        print("token enviado es:" + self.token)
        return getter._get(endpoint)
    
    def get_token(self):
        return self.token
        

      