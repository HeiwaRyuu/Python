from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#my_url = "https://www.kalunga.com.br/busca/1?q=notebook"
my_url = "https://www.kalunga.com.br/depto/gamers/mouse-gamer/13/1349?menuID=109&tipo=D"

# Opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.find_all("div",{"class":"blocoproduto"})
print(len(containers))

#Creating the CSV File
filename = "mousegamer.csv"
f = open(filename, "w")

headers = "configs, preco_a_vista, preco_parcelado\n"

f.write("headers")


# print(len(containers)) 
# print(containers[0])
for container in containers:

    #Configs do produto
    config = container.div.a["title"]

    #Preço à vista
    price_cash_array = container.find_all("span", {"class":"blocoproduto__text blocoproduto__text--bold blocoproduto__price"})
    price_cash = price_cash_array[0].text

    #Preço a prazo
    pPrice = container.p
    if pPrice:
        regular_price = pPrice.text
    else:
        regular_price = "Não Parcelável"

    # print(config)
    # print(price_cash)
    # print(regular_price)
    f.write(config.replace(",", "|") + "," + price_cash.replace(",", "|") + "," + regular_price.replace(",", "|") + "\n")

f.close()



