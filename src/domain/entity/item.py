

class item_ml:

    site=None
    id=None
    price=None
    start_time=None
    name=None
    description=None
    nickname=None


    def __init__(self):
      ''
    

   #setter
    def set_site(self,site):
      self.site=site

    def set_id(self,id):
      self.id=id

    def set_price(self,price):
      self.price=price

    def set_startTime(self,start_time):
      self.start_time=start_time

    def set_name(self,name):
      self.name=name

    def set_description(self,description):
      self.description=description
    
    def set_nick(self,nick):
      self.nickname=nick

    def set_nickname(self,nickname):
      self.nickname=nickname

    #getters
    def get_site(self):
       return self.site

    def get_id(self):
       return self.id

    def get_price(self):
      return self.price

    def get_startTime(self):
      return self.start_time

    def get_name(self):
      return self.name

    def get_description(self):
      return self.description

    def set_nickname(self):
      return self.nickname


    def get_full_obj_def(self):
       
     obj= {
        "site": self.site,
         "id": self.id,
         "price":self.price,
         "start_time": self.start_time,
        "name":self.name,
        "description":self.description,
        "nickname":self.nickname
        }
     return obj
        









