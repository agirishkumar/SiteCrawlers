import scrapy
from ..items import FlipkartItem

class FlipkartScrapy(scrapy.Spider):
    name = 'flipkart'
    start_urls = [
        'https://www.flipkart.com/vimal-jonney-solid-men-hooded-neck-black-t-shirt/p/itm721078c3d700e?pid=TSHFGZY5H2HDDCEZ&lid=LSTTSHFGZY5H2HDDCEZMNFNP2&marketplace=FLIPKART&srno=s_1_3&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=a77a6565-2577-4c01-a264-709924c07a29.TSHFGZY5H2HDDCEZ.SEARCH&ppt=sp&ppn=sp&ssid=8al99ygsk00000001579342408685&qH=04ad3bdbbe706182',
    ]

    def parse(self, response):
        items = FlipkartItem()
        images =[]
        links = []

        product_name = response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/h1/span[2]/text()').extract_first()
        brand = response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/h1/span[1]/text()').extract_first()
        price =  response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div/div[1]/text()').extract_first()
        seller = response.xpath('//*[@id="sellerName"]/span/span/text()').extract_first()
        images.append(response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[1]/div/div').extract_first())
        images.append(response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[2]/div/div').extract_first())
        images.append(response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[3]/div/div').extract_first())
        images.append(response.xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/div').extract_first())


        for image in images:
            links.append(image[image.find("(")+1:image.find(")")])

        items['name'] = product_name
        items['brand'] = brand
        items['price'] = price
        items['seller'] = seller
        items['image1'] = links[0]
        items['image2'] = links[1]
        items['image3'] = links[2]
        items['image4'] = links[3]

        yield items