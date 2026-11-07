# analyzer.py

# Dicionário com os principais cabeçalhos de segurança e suas descrições
SECURITY_HEADERS = {
    'Strict-Transport-Security': 'Força a comunicação segura via HTTPS.',
    'Content-Security-Policy': 'Previne ataques de injeção de dados e XSS (Cross-Site Scripting).',
    'X-Content-Type-Options': 'Previne ataques de MIME-sniffing (deve estar como "nosniff").',
    'X-Frame-Options': 'Previne ataques de Clickjacking (deve estar como DENY ou SAMEORIGIN).',
    'Permissions-Policy': 'Restringe quais recursos do navegador a API/aplicação pode usar.',
    'Cache-Control': 'Garante que informações sensíveis não fiquem salvas no cache do navegador.'
}

def analyze_headers(headers):
    """
    Analisa os cabeçalhos HTTP retornados pela API.
    Retorna um dicionário separando o que foi encontrado e o que está faltando.
    """
    results = {
        'found': {},
        'missing': {}
    }
    
    # Converte os cabeçalhos recebidos para minúsculas para facilitar a comparação exata
    lower_headers = {k.lower(): v for k, v in headers.items()}

    for header, description in SECURITY_HEADERS.items():
        if header.lower() in lower_headers:
            results['found'][header] = lower_headers[header.lower()]
        else:
            results['missing'][header] = description
            
    return results
