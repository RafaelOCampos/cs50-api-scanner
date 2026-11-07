# analyzer.py

# Dicionário dos cabeçalhos de segurança e descrições / Security headers and descriptions
SECURITY_HEADERS = {
    'Strict-Transport-Security': 'Força HTTPS / Enforces HTTPS.',
    'Content-Security-Policy': 'Ajuda a prevenir injeção de dados e XSS / Helps prevent data injection and XSS.',
    'X-Content-Type-Options': 'Ajuda a prevenir MIME sniffing (use "nosniff") / Helps prevent MIME sniffing (use "nosniff").',
    'X-Frame-Options': 'Ajuda a prevenir clickjacking (use DENY ou SAMEORIGIN) / Helps prevent clickjacking (use DENY or SAMEORIGIN).',
    'Permissions-Policy': 'Restringe recursos do navegador / Restricts browser features.',
    'Cache-Control': 'Controla o armazenamento em cache / Controls caching behavior.'
}

def analyze_headers(headers):
    """
    Analisa os cabeçalhos HTTP retornados pela API / Analyze HTTP response headers.
    Retorna os cabeçalhos encontrados e ausentes / Return found and missing headers.
    """
    results = {
        'found': {},
        'missing': {}
    }
    
    # Converte os nomes para minúsculas para comparação / Lowercase names for comparison
    lower_headers = {k.lower(): v for k, v in headers.items()}

    for header, description in SECURITY_HEADERS.items():
        if header.lower() in lower_headers:
            results['found'][header] = lower_headers[header.lower()]
        else:
            results['missing'][header] = description
            
    return results
