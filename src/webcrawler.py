import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# Declaração de constantes
HTTP = "https://br.advfn.com/bolsa-de-valores/bovespa/"
DIR_HTML = "../html/"

# Ler a lista de arquivos CSV
html_files = [f for f in listdir(DIR_HTML) if (isfile(join(DIR_HTML, f)))]

lst_acoes = []
for html in html_files:
    with open("{0}{1}".format(DIR_HTML, html), encoding='utf8') as f:        
        soup = BeautifulSoup(f.read(), 'html.parser')
        for td in soup.find_all("td", {"class": "String Column2 ColumnLast"}):
            lst_acoes.append(td.text)
    
    with open("../acoes.txt", "w") as f:
        for acao in lst_acoes:
            f.write("%s\n" % acao)