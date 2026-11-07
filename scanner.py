# scanner.py

import argparse
import requests
import sys
from analyzer import analyze_headers
from report_generator import print_report

def main():
    # Configuração de argumentos de linha de comando (CLI) / Configure command-line arguments (CLI)
    parser = argparse.ArgumentParser(description="Automated API Security Scanner - CS50 Final Project")
    parser.add_argument(
        "-u",
        "--url",
        help="URL da API alvo / Target API URL (ex: https://api.github.com)",
        required=True,
    )
    args = parser.parse_args()

    url = args.url

    # Validação básica de URL / Basic URL validation
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Erro / Error: A URL deve começar com http:// ou https://")
        sys.exit(1)

    print(f"Iniciando análise / Starting scan: {url} ...")
    
    try:
        # Faz uma requisição GET (timeout de 10 segundos) / Send a GET request (10-second timeout)
        response = requests.get(url, timeout=10)
        
        # Extrai os cabeçalhos da resposta HTTP / Extract HTTP response headers
        headers = response.headers
        
        # Envia os cabeçalhos para análise / Pass headers to the analyzer
        analysis_results = analyze_headers(headers)
        
        # Gera o relatório no terminal / Generate the terminal report
        print_report(url, analysis_results)

    except requests.exceptions.RequestException as error:
        print(
            f"\nErro fatal / Fatal error: Não foi possível conectar ao alvo / "
            f"Could not connect to target. Detalhes / Details: {error}"
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
