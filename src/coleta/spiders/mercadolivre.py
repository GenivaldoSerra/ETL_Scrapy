import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/informatica/portateis-acessorios/_Container_black-friday-f1-ce-games-e-notebooks#applied_filter_id%3Dcategory%26applied_filter_name%3DCategorias%26applied_filter_order%3D4%26applied_value_id%3DMLB430687%26applied_value_name%3DPort%C3%A1teis+e+Acess%C3%B3rios%26applied_value_order%3D7%26applied_value_results%3D212%26is_custom%3Dfalse"]

    def parse(self, response):
        pass
