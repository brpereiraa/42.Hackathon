import requests
from bs4 import BeautifulSoup
from pprint import pprint
from continente import mateus_cont, mateus_spark_cont, trinca_bol_cont, papa_fig_cont
from elcorteingles import mateus_elc, mateus_spark_elc, trb_elc, ppf_elc
from garrafeirasoares import mateus_gs, mateus_sparkling_gs, trb_gs, ppf_gs
from elcorteingles_es import mateus_elc_es, trb_elc_es
from pysql import insert_wine

def	mateus_origin(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_gs(cont, soup)
	elif (flag == 4):
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=mateus', headers)
		soup = soup_init(link)
		mateus_elc_es(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_gs(cont, soup)
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=mateus', headers)
		soup = soup_init(link)
		mateus_elc_es(cont, soup)

def	mateus_spark(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_spark_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_spark_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_sparkling_gs(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=mateus&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		mateus_spark_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=mateus&search=text', headers)
		soup = soup_init(link)
		mateus_spark_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=mateus', headers)
		soup = soup_init(link)
		mateus_sparkling_gs(cont, soup)

def	trinca_bols(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=trinca+bolotas&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		trinca_bol_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=trinca+bolotas&search=text', headers)
		soup = soup_init(link)
		trb_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=trinca+bolotas', headers)
		soup = soup_init(link)
		trb_gs(cont, soup)
	elif (flag == 4):
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=trinca%20bolotas', headers)
		soup = soup_init(link)
		trb_elc_es(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=trinca+bolotas&start=0&srule=Continente&pmin=0.01', headers)
		soup = soup_init(link)
		trinca_bol_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=trinca+bolotas&search=text', headers)
		soup = soup_init(link)
		trb_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=trinca+bolotas', headers)
		soup = soup_init(link)
		trb_gs(cont, soup)
		link = request_url('https://www.elcorteingles.es/supermercado/bebidas/vinos/vinos-internacionales/vinos-de-portugal/buscar/?term=trinca%20bolotas', headers)
		soup = soup_init(link)
		trb_elc_es(cont, soup)

def	papa_figos(headers, cont, flag):
	if (flag == 1):
		link = request_url('https://www.continente.pt/pesquisa/?q=papa+figos&start=0&srule=Continente%2004&pmin=0.01', headers)
		soup = soup_init(link)
		papa_fig_cont(cont, soup)
	elif (flag == 2):
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=papa+figos&search=text', headers)
		soup = soup_init(link)
		ppf_elc(cont, soup)
	elif (flag == 3):
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=papa+figos', headers)
		soup = soup_init(link)
		ppf_gs(cont, soup)
	elif (flag == 0):
		link = request_url('https://www.continente.pt/pesquisa/?q=papa+figos&start=0&srule=Continente%2004&pmin=0.01', headers)
		soup = soup_init(link)
		papa_fig_cont(cont, soup)
		link = request_url('https://www.elcorteingles.pt/supermercado/pesquisar/?term=papa+figos&search=text', headers)
		soup = soup_init(link)
		ppf_elc(cont, soup)
		link = request_url('https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=papa+figos', headers)
		soup = soup_init(link)
		ppf_gs(cont, soup)

def	continente(headers):
	cont = {
		'shop_name': '',
		'ean': '',
		'path': '',
		'wine': '',
		'harv_year': '',
		'capacity': '',
		'price': '',
		'discount': '',
		'currency': '',
		'scrap_date': '',
		'location': ''
	}
	flag = 1
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
	insert_wine(cont)


def	elcorteingles(headers):
	cont = {
		'shop_name': '',
		'ean': '',
		'path': '',
		'wine': '',
		'harv_year': '',
		'capacity': '',
		'price': '',
		'discount': '',
		'currency': '',
		'scrap_date': '',
		'location': ''
	}
	flag = 2
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
	insert_wine(cont)

def	garrafeirasoares(headers):
	cont = {
		'shop_name': '',
		'ean': '',
		'path': '',
		'wine': '',
		'harv_year': '',
		'capacity': '',
		'price': '',
		'discount': '',
		'currency': '',
		'scrap_date': '',
		'location': ''
	}
	flag = 3
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	mateus_spark(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)
	papa_figos(headers, cont, flag)
	insert_wine(cont)

def	elcorteingles_es(headers):
	cont = {
		'shop_name': '',
		'ean': '',
		'path': '',
		'wine': '',
		'harv_year': '',
		'capacity': '',
		'price': '',
		'discount': '',
		'currency': '',
		'scrap_date': '',
		'location': ''
	}
	flag = 4
	mateus_origin(headers, cont, flag)
	insert_wine(cont)
	trinca_bols(headers, cont, flag)
	insert_wine(cont)

def	soup_init(link):
	soup = BeautifulSoup(link.content, 'html.parser')
	return soup

def	request_url(url, headers):
	link = requests.get(url, headers=headers)
	return link

def initvalues():
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
	}
	return headers

def main():
	headers = initvalues()
	# name = input("Shops available:\n(0) SCRAPE ALL\n(1) Continente\n(2) El Corte Ingles\n(3) Garrafeira Soares\n(4) El Corte Ingles_Es\nChoose a number: ")
	# # if (name == "0"):
	# # 	flag = 0
	# # 	continente(headers, flag)
	# # 	elcorteingles(headers, flag)
	# # 	garrafeirasoares(headers, flag)
	# # 	elcorteingles_es(headers, flag)
	# if (name == "1"):
	# 	continente(headers)
	# elif (name == "2"):
	# 	elcorteingles(headers)
	# elif (name == "3"):
	# 	garrafeirasoares(headers)
	# elif (name == "4"):
	# 	elcorteingles_es(headers)
	# else:
	continente(headers)
	elcorteingles(headers)
	garrafeirasoares(headers)
	elcorteingles_es(headers)
  
# EAN Mateus OG     : 5601012011500		path:"./img/Mateus Rosé Original.jpg"
# EAN Mateus Spark  : 5601012001310		path:"./img/Mateus Sparkling Rosé.jpg"
# EAN Trinca Bolotas: 5601012004427		path:"./img/Herdade do Peso Trinca Bolotas Tinto.jpg"
# EAN Papa Figos    : 5601012011920		path:"./img/Casa Ferreirinha Papa Figos Branco.jpg"

if __name__ == "__main__":
    main()
