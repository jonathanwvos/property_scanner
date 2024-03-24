from bs4 import BeautifulSoup
from money_parser import price_str
from os.path import join
from .utils import datestring

from os.path import dirname, join, realpath
import scrapy


BASE_URL = 'https://www.property24.com'


class Property24Scrapy(scrapy.Spider):
    name = 'Property24'

    def __init__(self):
        super().__init__()
        self.url = "{base_url}/to-rent/western-cape/9/p{page_no}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse"
        # self.url = "{base_url}/to-rent/cape-town/western-cape/432/p{page_no}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse"
        self.no_pages = 1
        # self.output_file = open(join('data', f'property_24_{datestring()}.csv'), 'w')
        self.output_file = open(join(dirname(realpath(__file__)), '..', '..', 'data', 'property_24.csv'), 'w')
        self.output_file.write('url;price;title;location;type;bedrooms;bathrooms;parking spaces;floor size\n')

    def start_requests(self):
        yield scrapy.Request(url=self.url.format(base_url=BASE_URL, page_no=1), callback=self.determine_no_pages)

    def determine_no_pages(self, response):
        pagination_html = response.css('body .p24_theme .p24_results .container .row .col-9 .p24_pager .pagination').get()
        soup = BeautifulSoup(pagination_html, features='lxml')
        last_element = soup.find_all('li')[-1]
        self.no_pages = int(last_element.find('a')['data-pagenumber'])
        
        for page_no in range(1, self.no_pages):
            yield scrapy.Request(url=self.url.format(base_url=BASE_URL, page_no=page_no), callback=self.parse_listing_page)

    def set_title_and_type(self, data, soup):
        title = soup.find(class_='p24_title')
        title_str = ''
        type_str = ''
        
        if title:        
            title_str = title.text
            
            if 'House' in title_str or 'house' in title_str:
                type_str = 'house'
            elif 'Townhouse' in title_str:
                type_str = 'townhouse'
            elif 'Apartment' in title_str:
                type_str = 'apartment'
        
        data['title'] = title_str
        data['type'] = type_str
    
    def set_price(self, data, soup):
        price = soup.find(class_='p24_price')
        
        if not price or 'POA' in price.text or 'per day' in price.text or 'per week' in price.text or 'per m²' in price.text:
            raise Exception('Invalid price')
        
        data['price'] = price_str(price.text.strip())
    
    def set_location(self, data, soup):
        location = soup.find(class_='p24_location')
        
        if location:
            data['location'] = location.text.strip()

    def set_bedrooms(self, data, soup):
        bedrooms = soup.find(title='Bedrooms')

        if bedrooms:
            data['bedrooms'] = bedrooms.span.text.strip()
    
    def set_bathrooms(self, data, soup):
        bathrooms = soup.find(title='Bathrooms')
        
        if bathrooms:
            data['bathrooms'] = bathrooms.span.text.strip()
    
    def set_parking_spaces(self, data, soup):
        parking_spaces = soup.find(title='Parking Spaces')
        
        if parking_spaces:
            data['parking spaces'] = parking_spaces.span.text.strip()
    
    def set_floor_size(self, data, soup):
        floor_size = soup.find(title='Floor Size')

        if floor_size:
            data['floor size'] = price_str(floor_size.span.text.replace('m²', '').strip())

    def set_url(self, data, soup):
        data['url'] = f"{BASE_URL}{soup.a['href']}"

    def parse_listing_page(self, response):
        class_str = "body .p24_theme .p24_results .container .row .col-9 .js_resultTile"
        for listing in response.css(class_str).getall():
            data = {
                'url': '',
                'price': '',
                'title': '',
                'location': '',
                'type': '',
                'bedrooms': '',
                'bathrooms': '',
                'parking spaces': '',
                'floor size': '',
            }
            soup = BeautifulSoup(listing, features='lxml')
            
            try:
                self.set_price(data, soup)
                self.set_url(data, soup)
                self.set_title_and_type(data, soup)
                self.set_location(data, soup)
                self.set_bedrooms(data, soup)
                self.set_bathrooms(data, soup)
                self.set_parking_spaces(data, soup)
                self.set_floor_size(data, soup)
            except Exception as e:
                continue
            
            self.output_file.write(f"{';'.join(data.values())}\n")
