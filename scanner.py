# scanner.py

import argparse
import requests
import sys
from analyzer import analyze_headers
from report_generator import print_report

def main():
    # Configuração de argumentos de linha de comando (CLI)
    parser = argparse.ArgumentParser(description="Automated API Security Scanner - CS50 Final Project")
    parser.add_argument("-u", "--url", help="A URL da API alvo (ex: https://api.github.com)", required=True)
    args = parser.parse_args()

    url = args.url

    # Validação básica de URL
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Erro: A URL deve começar com http:// ou https://")
        sys.exit(1)

    print(f"Iniciando scan em: {url} ...")
    
    try:
        # Faz a requisição GET na API (timeout de 10 segundos para evitar travamentos)
        response = requests.get(url, timeout=10)
        
        # Extrai os cabeçalhos da resposta HTTP
        headers = response.headers
        
        # Envia para a engine de análise
        analysis_results = analyze_headers(headers)
        
        # Gera o relatório no terminal
        print_report(url, analysis_results)

    except requests.exceptions.RequestException as error:
        print(f"\nErro fatal: Não foi possível conectar ao alvo. Detalhes: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
