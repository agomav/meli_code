import os
from threading import Thread
import queue
from application.MeLiIntegrationService import MeliService
from domain import endpointsFactory as urlProvider
from domain.UseCase.meLiFilterImp import filter
from infraestructure.repositories.itemRepository import itemRepository
from infraestructure.dbconnector import get_db_connecion
from configuration.configProvider import configurationServer
from application.errorReportService import errorGenerator



class fileProcessor:
    DELIMITER=''
    fil =filter()


    str_queue= queue.Queue()
    
    def __init__(self) -> None:
        prop=configurationServer()
        self.DELIMITER=prop.getProperty('file_current_delimiter')
        self.err_han=errorGenerator()
        

    
        
    
    
    def get_items(self,site_curr,identifier_curr):
        
        endpoint=urlProvider._build_items_endpoint(site_curr,identifier_curr)
        ml_ser=MeliService()
        response=ml_ser.ml_get_request(endpoint)
        if "error" in response:
            
            self.err_han.add_row_error_report(site_curr+','+identifier_curr,"error ocurred processing this item, API error response was: " + response["error"])
            raise ValueError("error ocurred processing this item: " + response["error"])



        self.fil.process_item(response,site_curr,identifier_curr)
        #print(fil.get_item_definition())
        #print("arguments: " , fil.get_sellerID() , fil.get_categoryID() , fil.get_currencyID())
        return response
    
    def get_categories(self,category_id):
        
        endpoint=urlProvider._build_categories_endpoint(category_id)
        ml_ser=MeliService()
        response=ml_ser.ml_get_request(endpoint)
        self.fil.process_category(response)
        self.str_queue.put(response)
        #return response

    
    def get_currencies(self,currency_id):
        endpoint=urlProvider._build_currencies_endpoint(currency_id)
        ml_ser=MeliService()
        response=ml_ser.ml_get_request(endpoint)
        self.fil.process_currency(response)
        self.str_queue.put(response)
        #return response

    
    def get_users(self,user_id):
        endpoint=urlProvider._build_users_endpoint(user_id)
        ml_ser=MeliService()
        response=ml_ser.ml_get_request(endpoint)
        self.fil.process_user(response)
         
        self.str_queue.put(response)
        #return response

    
    def _process_line(self, current_line ):
        
        if self.DELIMITER not in current_line:
            self.err_han.add_row_error_report(current_line.strip(), "Line not processed due to delimiter not supported.")
            return
        

        line_fields=current_line.strip().split(self.DELIMITER)
        site=line_fields[0]
        identifier=line_fields[1]

        if site=='' or identifier=='':
            self.err_han.add_row_error_report(current_line.strip(),"Field are mndatory. Line not processed: Site or identifier are empty")
            return
        

        if site.isalpha() == False or identifier.isnumeric()==False:
            
            self.err_han.add_row_error_report(current_line.strip(),"one or more fields in line contains specials chars. Site must be String and Identifier Int")
            
            print("sent the data")
            return





        self.get_items(site,identifier)
        print("site is: " +site + " and identif is: " + identifier)
        curr_category=self.fil.get_categoryID()
        curr_currency= self.fil.get_currencyID() 
        curr_user=self.fil.get_sellerID()


        if curr_category is not None and curr_category !='':
           t_category=Thread(target=self.get_categories(curr_category),name='CAT')
        
        if curr_user is not None and curr_user !='':
           t_user=Thread(target=self.get_users(curr_user),name='USER')
        
        if curr_currency is not None and curr_currency !='':
           t_currency=Threadtarget=Thread(target=self.get_currencies(curr_currency),name='CURR')
        print("threads defined!!")
       
        pool_t={t_category,t_user,t_currency}
        
        response=''
        for tr in pool_t:
            tr.start()
            print("start occured")

            response=self.str_queue.get()
            print("response from: " , tr.name, response )
        
        for trd in pool_t:
            trd.join()
        
        print("finished paralell processing")
        print(self.fil.get_item_definition())

        repo=itemRepository(db_connection=get_db_connecion())
        repo.insert(self.fil.get_item_definition())


        return response
            
    


        
        
        
        
        
        
        
    
    

