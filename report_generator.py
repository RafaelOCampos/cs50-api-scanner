# report_generator.py

from colorama import init, Fore, Style

# Inicializa as cores no terminal (autoreset garante que a cor não "vaze" para a próxima linha)
init(autoreset=True)

def print_report(url, results):
    """
    Gera um relatório visual no terminal com base nos cabeçalhos analisados.
    """
    print(f"\n{Style.BRIGHT}{Fore.CYAN}=== Relatório de Segurança de API ===")
    print(f"{Style.BRIGHT}Alvo (Target): {url}\n")

    # Exibe cabeçalhos configurados corretamente (Sucesso)
    print(f"{Fore.GREEN}{Style.BRIGHT}[+] Cabeçalhos de Segurança Encontrados:")
    if not results['found']:
        print(f"{Fore.YELLOW}    Nenhum cabeçalho de segurança detectado.")
    else:
        for header, value in results['found'].items():
            print(f"    - {Style.BRIGHT}{header}:{Style.NORMAL} {value}")

    # Exibe cabeçalhos ausentes (Vulnerabilidades)
    print(f"\n{Fore.RED}{Style.BRIGHT}[-] Cabeçalhos de Segurança Ausentes (Vulnerabilidades):")
    if not results['missing']:
        print(f"{Fore.GREEN}    Nenhuma ausência detectada. A API está bem configurada!")
    else:
        for header, description in results['missing'].items():
            print(f"    - {Style.BRIGHT}{header}:{Style.NORMAL} {description}")
    
    print(f"\n{Style.BRIGHT}{Fore.CYAN}=====================================\n")
