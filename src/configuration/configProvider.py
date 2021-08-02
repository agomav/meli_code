import json
import sys
import os

class configurationServer:
    config_dict=''

    def __new__(self, *args, **kw):
        if not hasattr(self, '_instance'):
            orig = super(configurationServer, self)
            self._instance = orig.__new__(self, *args, **kw)
        return self._instance
    
    
    def __init__(self):
        self.load_config_file()


    def load_config_file(self):
        

        try:
            with open("config.json") as f:
                
                self.config_dict= json.loads(f.read())
                print("propertes has been loaded")
        except Exception as e:
            print("Error!!, cannot load configuration file", e)

    
    def getProperty(self,key):

        if key in self.config_dict:
            return self.config_dict[key]
        raise ValueError("Unable to find the property: ", key ,"in the configuration file")
    
    
    def refresh_app_properties(self):
        self.load_config_file()
    


    
    
    






