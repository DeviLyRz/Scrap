import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import emoji

# Função para fazer scraping da página
def scrape_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers, verify=True)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_content = soup.get_text(strip=True)
        return page_content
    else:
        return f"Erro ao acessar o site: {response.status_code}"

# Função para remover emojis e substituir caracteres especiais
def clean_text(text):
    text = emoji.replace_emoji(text, replace='')
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('–', '-').replace('—', '-')
    return text

# Função para salvar o conteúdo em PDF com formatação aprimorada
def save_to_pdf(content, filename="output.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Fonte DejaVuSans para suporte a Unicode
    pdf.add_font('DejaVu', '', 'C:/Users/erick.penna/Documents/Python/scrapper/Font/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    # Limpa o conteúdo
    content = clean_text(content)

    # Divide o texto em linhas para uma melhor formatação
    max_line_length = 90  # Ajuste para controlar o número de caracteres por linha
    formatted_lines = []
    for line in content.splitlines():
        while len(line) > max_line_length:
            split_point = line.rfind(" ", 0, max_line_length)  # Quebra no último espaço antes de ultrapassar o limite
            if split_point == -1:  # Caso não haja espaço, quebra diretamente
                split_point = max_line_length
            formatted_lines.append(line[:split_point].strip())
            line = line[split_point:].strip()
        formatted_lines.append(line)

    # Adiciona as linhas formatadas ao PDF
    for line in formatted_lines:
        pdf.multi_cell(0, 10, line)
        pdf.ln(2)  # Adiciona um pequeno espaçamento entre as linhas

    try:
        pdf.output(filename)
        print(f"Conteúdo salvo em {filename}")
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")

# URL do site para fazer scraping
url = "https://www.passeidireto.com/arquivo/119819503/quiz-etica-cidadania-e-sustentabilidade-senac-ead"

# Realiza o scraping
content = scrape_page(url)

# Verifica se houve erro no scraping
if "Erro" not in content:
    save_to_pdf(content, "conteudo_formatado.pdf")
else:
    print(content)
