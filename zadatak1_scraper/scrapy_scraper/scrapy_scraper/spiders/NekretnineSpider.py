import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import random

class NekretnineSpider(CrawlSpider):
    name = 'nekretnine'
    allowed_domains = ["4zida.rs"]
    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        
        izdavanje_links=[
            "https://www.4zida.rs/izdavanje-stanova",
            "https://www.4zida.rs/izdavanje-stanova/beograd",
            "https://www.4zida.rs/izdavanje-stanova/novi-beograd-beograd",
            "https://www.4zida.rs/izdavanje-stanova/vozdovac-opstina-beograd",
            "https://www.4zida.rs/izdavanje-stanova/novi-sad",
            "https://www.4zida.rs/izdavanje-stanova/nis",
            "https://www.4zida.rs/izdavanje-stanova/kragujevac",
        ]

        prodaja_stanova_links = [
            "https://www.4zida.rs/prodaja-stanova",
            "https://www.4zida.rs/prodaja-stanova/beograd",
            "https://www.4zida.rs/prodaja-stanova/novi-beograd",
        ]
        
        prodaja_kuca_links = [
            "https://www.4zida.rs/prodaja-kuca",
            "https://www.4zida.rs/prodaja-kuca/beograd",
            "https://www.4zida.rs/prodaja-kuca/kragujevac",
            "https://www.4zida.rs/prodaja-kuca/novi-sad",
            "https://www.4zida.rs/prodaja-kuca/nis",
        ]

        pocetna = "https://www.4zida.rs"

        self.start_urls = prodaja_stanova_links + [pocetna]
        random.shuffle(self.start_urls)
    
    
    rules = (
        Rule(LinkExtractor(allow=('/prodaja-stanova'))),
        Rule(LinkExtractor(
            #allow=('/izdavanje-stanova'),
            #allow=('/prodaja-stanova'),
            allow=('/prodaja-stanova', '/prodaja-kuca', '/izdavanje-stanova'),
            deny=(
                #'/prodaja/stanovi/',
                #'/izdavanje/stanovi/',
                #'/prodaja/kuce/',
                '/blog/',
                '/novogradnja/',
                '/agencija/',
                '/prodaja/poslovni-prostor',
                '/prodaja-poslovnih-prostora',
                '/prodaja-placeva',
                '/prodaja/placevi'
                )
            )
        ),
        Rule(LinkExtractor(allow=('/prodaja/stanovi/', '/prodaja/kuce/', '/izdavanje/stanovi/',)), callback='parse'),
        #Rule(LinkExtractor(allow=('/izdavanje/stanovi/',)), callback='parse'),
        #Rule(LinkExtractor(allow=('/prodaja/stanovi/beograd',)), callback='parse'),


    )

    info_fields_mapping = {
        'Depozit' : 'depozit',
        'Uslovi za stanare' : 'uslovi_za_stanare',
        'Površina': 'povrsina',
        'Plac': 'plac',
        'Broj soba': 'broj_soba',
        'Uknjiženost': 'uknjizenost',
        'Grejanje': 'grejanje',
        'Broj etaža': 'broj_etaza',
        'Stanje': 'stanje',
        'Godina izgradnje': 'godina_izgradnje',
        'Spratnost': 'spratnost',
        'Lift': 'lift',
        'Infrastruktura': 'infrastruktura',
        'Parking': 'parking',
        'Garaža': 'garaza',
        'Unutrašnje prostorije': 'unutrasnje_prostorije',
        'Nameštenost': 'namestenost',
        'Opremljenost': 'opremljenost',
        'Useljivo': 'useljivo',
        'Orijentacija nekretnine': 'orijentacija_nekretnine',
        'Tip objekta': 'tip_objekta',
        'Tip stana': 'tip_stana',
        'Tip kuće': 'tip_kuce',
        'Autobuske linije': 'autobuske_linije',
        'Tramvajske linije': 'tramvajske_linije',
        'Trolejbuske linije': 'trolejbuske_linije',
        'Šifra oglasa': 'sifra_oglasa'
    }


    def parse(self, response):        
        
        info_blok = response.xpath('//html/body/app-root/app-main/app-ad-details/div/div/main/article/section[1]/div[2]')
        # cena = info_blok.xpath('//div[2]/div[2]/span/text()').get()
        # print(cena)

        # div.prices:nth-child(1) > span:nth-child(1) > strong:nth-child(1)
        cena = response.css('div.prices:nth-child(1) > span:nth-child(1) > strong:nth-child(1)::text').get()
        print(cena)
        # adresa = response.xpath('//html/body/app-root/app-main/app-ad-details/div/div/main/article/section[1]/div[2]/div[1]/section/div[1]/text()').get()
        adresa = response.css(".address::text").get()
        
        # lokacija = response.xpath('/html/body/app-root/app-main/app-ad-details/div/div/main/article/section[1]/div[2]/div[1]/section/div[2]/text()').get()
        lokacija = response.css(".location::text").get()
        
        grad = ''
        sira_lokacija = ''
        uza_lokacija = ''
        if lokacija:
            lokacija = lokacija.split(',')
            grad = lokacija[len(lokacija) - 1].strip() if len(lokacija) >= 1 else ''
            sira_lokacija = lokacija[len(lokacija) - 2].strip() if len(lokacija) >= 2 else ''
            uza_lokacija = lokacija[len(lokacija) - 3].strip() if len(lokacija) >= 3 else ''
        
        # opis = response.xpath('//html/body/app-root/app-main/app-ad-details/div/div/main/article/section[1]/div[8]/div/text()').get()
        opis = response.css(".description::text").get()
        if opis:
            opis = opis.strip().replace('\n', '')
        else:
            opis = ''

        usluga = 'izdavanje' if 'izdavanje' in response.request.url else 'prodaja'
        tip = 'stan' if (usluga == 'izdavanje' or 'prodaja/stanovi' in response.request.url)  else 'kuca'

        nekretnina = {
            'usluga': usluga,
            'tip': tip,
            'cena' : cena,
            'depozit': '',
            'uslovi_za_stanare': '',
            'grad': grad,
            'sira_lokacija':sira_lokacija,
            'uza_lokacija':uza_lokacija,
            'adresa': adresa,
            'povrsina': '',
            'plac':'',
            'broj_soba':'',
            'uknjizenost':'',
            'grejanje':'',
            'broj_etaza':'',
            'stanje':'',
            'godina_izgradnje':'',
            'spratnost':'',
            'lift':'',
            'infrastruktura':'',
            'parking':'',
            'garaza':'',
            'unutrasnje_prostorije':'',
            'namestenost':'',
            'opremljenost':'',
            'useljivo':'',
            'orijentacija_nekretnine':'',
            'tip_objekta':'',
            'tip_stana': '',
            'tip_kuce':'',
            'autobuske_linije':'',
            'tramvajske_linije':'',
            'trolejbuske_linije':'',
            'sifra_oglasa':'',
            'opis': opis,
            'link':response.request.url
        }

        properties = info_blok.xpath('//div[contains(@class, "wrapper") and contains(@class, "ng-star-inserted")]').getall()
        for prop in properties:
            div_label = Selector(text=prop).xpath('//div[@class="label"]/text()').get()
            div_val = Selector(text=prop).xpath('//div[@class="value"]/text()').get()
            
            div_label = div_label.replace(':', '')
            nekretnina[self.info_fields_mapping[div_label]] = div_val
        return nekretnina    
