import json
from domain.entity.item import  item_ml


class filter:
    
    item_ent=item_ml()
    
    category_id=None
    seller_id=None
    currency_id=None
    
    
    


    def __init__(self) :
       ""
    
        
        



    def process_item(self, response,site,identifier):
        item_dic=response
        
        self.item_ent.set_site(site.strip())
        self.item_ent.set_id(identifier.strip())
        
    
        if 'start_time' in item_dic:
            
            self.item_ent.set_startTime(item_dic['start_time'])

        if 'price' in item_dic:
            self.item_ent.set_price(item_dic['price'])
        
        if 'category_id' in item_dic:
            self.category_id= item_dic['category_id']

        if 'currency_id' in item_dic:
            self.currency_id=   item_dic['currency_id']

        if 'seller_id' in item_dic:
            self.seller_id= item_dic['seller_id']
    

    
    def process_category(self,response):
        
        item_dic=response
        if "name" in item_dic:
           self.item_ent.set_name(item_dic["name"]) 
    

    def process_user(self, response):
        item_dic=response
        if "nickname" in item_dic:
           nick=item_dic["nickname"]
           print("nick is: ", nick)
           self.item_ent.set_nick(nick)
    
    def process_currency(self,response):
        item_dic=response
        if "description" in item_dic:
            self.item_ent.set_description(str(item_dic["description"])) 

    
    
    
    def get_currencyID(self):
        return self.currency_id
    
    def get_sellerID(self):
        return self.seller_id
    
    def get_categoryID(self):
        return self.category_id

    def get_item_definition(self):
       return self.item_ent.get_full_obj_def()
    
    
        

