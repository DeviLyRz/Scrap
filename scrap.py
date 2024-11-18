import requests
from bs4 import BeautifulSoup

# URL do site que você deseja fazer scraping
url = "https://www.passeidireto.com/arquivo/114371724/relatorio-estagio-ii-pedagogia-unopar"  # Substitua pela URL do seu site

# Cabeçalho com um User-Agent para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Fazendo a requisição HTTP
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisa o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Salva o HTML completo da página em um arquivo local
    with open('pagina_completa.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("O conteúdo completo do site foi salvo em 'pagina_completa.html'")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
