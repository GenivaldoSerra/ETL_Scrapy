import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/informatica/portateis-acessorios/_Container_black-friday-f1-ce-games-e-notebooks#applied_filter_id%3Dcategory%26applied_filter_name%3DCategorias%26applied_filter_order%3D4%26applied_value_id%3DMLB430687%26applied_value_name%3DPort%C3%A1teis+e+Acess%C3%B3rios%26applied_value_order%3D7%26applied_value_results%3D212%26is_custom%3Dfalse"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')
        
        for product in products:
            
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            old_price = prices[0] if len(prices) == 3 else None
            new_price = prices[1] if len(prices) >= 2 else prices[0]
            
            yield {
                'name': product.css('a::text').get(),
                'old_price': old_price,
                'new_price': new_price,
                'reviews_rating': product.css('span.poly-reviews__rating::text').get(),
                'reviews_total': product.css('span.poly-reviews__total::text').get()
            }
