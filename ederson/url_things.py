import urllib.parse
import urllib.request

url = 'https://pt.wikipedia.org/wiki/John_Lennon'
parsed_url = urllib.parse.urlparse(url)

print("Componentes da URL:")
print("Esquema:", parsed_url.scheme) 
print(parsed_url.query)