page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
#imprimindo posicição onde a primeira url é encontrada
print start_link
# código aplicado para imprimir somente a url
parcial_url = page[start_link:]
start_url = parcial_url.find('"')
inicio_url = parcial_url[start_url+1:]
fim_url = inicio_url.find('"')
url = inicio_url[:fim_url]
print url

#segunda forma de fazer a mesma coisa
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print url