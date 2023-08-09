import requests
import logging
from bs4 import BeautifulSoup as bs
import requests


logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO )

class ScrapProduct():
    def __init__(self , url_webpage) -> None:
        self.website =  url_webpage
    
    def _get_web_products (self):
        url = self.website
        logger.info(f'Getting data from: {url}')
        request  = requests.get(url)

        html_file = request.text
        return html_file
    
    def _parsing_html(self ):

        html_file = self._get_web_products()
        soup = bs(html_file , features="html.parser" )
        return soup 
    
    def  getting_product_info(self) -> list:
        soup =  self._parsing_html()
      
        list_elements = soup.find_all("div" , attrs={'class' : 'OfferBox' })

        all_product_list=[]
        for  element in list_elements:

            product_tile = element.find("div" , attrs={'class' : 'OfferBoxTitle' }).text.split('\n')[2] #The attribute text returns a string with multiple blank lines
            brand = product_tile.split(' ')[0]  #The brand is the first word in element
            price =  element.find("span" , attrs={'class' : 'offerprice' }).text.replace(" ","").split('\n')[1] #The attribute text returns a string with multiple blank lines
            

            if brand != 'Refurbished':
                product_dict_info = {'product_tile':product_tile ,'product_brand': brand ,'product_price': price }
                all_product_list.append(product_dict_info) 

      
        return  all_product_list