# report_generator.py

from colorama import init, Fore, Style

# Inicializa as cores com reinicialização automática / Initialize colors with automatic reset
init(autoreset=True)

def print_report(url, results):
    """
    Gera o relatório dos cabeçalhos analisados / Print the report for analyzed headers.
    """
    print(f"\n{Style.BRIGHT}{Fore.CYAN}=== Relatório de Segurança de API / API Security Report ===")
    print(f"{Style.BRIGHT}Alvo / Target: {url}\n")

    # Exibe os cabeçalhos encontrados / Display found headers
    print(f"{Fore.GREEN}{Style.BRIGHT}[+] Cabeçalhos encontrados / Found headers:")
    if not results['found']:
        print(f"{Fore.YELLOW}    Nenhum cabeçalho de segurança detectado / No security headers detected.")
    else:
        for header, value in results['found'].items():
            print(f"    - {Style.BRIGHT}{header}:{Style.NORMAL} {value}")

    # Exibe os cabeçalhos ausentes / Display missing headers
    print(f"\n{Fore.RED}{Style.BRIGHT}[-] Cabeçalhos ausentes (vulnerabilidades) / Missing headers (vulnerabilities):")
    if not results['missing']:
        print(f"{Fore.GREEN}    Nenhuma ausência detectada / No missing headers detected.")
    else:
        for header, description in results['missing'].items():
            print(f"    - {Style.BRIGHT}{header}:{Style.NORMAL} {description}")
    
    print(f"\n{Style.BRIGHT}{Fore.CYAN}=====================================\n")
