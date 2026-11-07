# Automated API Security Scanner
#### Video Demo: [COLE AQUI A URL DO YOUTUBE]
#### Name: Rafael Oliveira Campos
#### City/Country: Timóteo, Minas Gerais, Brazil

## Description
The Automated API Security Scanner is a Python-based Command Line Interface (CLI) tool that checks whether an API response includes selected security headers. This check can help developers and QA engineers identify headers that may be missing, but it does not assess an API's overall security or determine whether the header values are correctly configured.

This project automates the process of sending an HTTP GET request to a target API endpoint, extracting the HTTP response headers, and analyzing them. The tool checks for the presence or absence of selected headers, including Strict-Transport-Security, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, Permissions-Policy, and Cache-Control. It generates an easy-to-read report directly in the terminal. It checks header presence only; it does not validate header values or provide remediation steps.

## Files Structure
Here is a breakdown of the files included in this project and their respective roles:

*   **`scanner.py`**: The main execution script. It uses the `argparse` library to handle command-line arguments, orchestrates the HTTP requests using the `requests` library (with a built-in timeout to prevent hangs), and invokes the analysis and reporting modules.
*   **`analyzer.py`**: This module contains the core verification logic. It holds a predefined dictionary (`SECURITY_HEADERS`) of required security headers and their descriptions. It cross-references the headers returned by the API (converting them to lowercase for accurate comparison) and categorizes them strictly into 'found' or 'missing'. It identifies if headers are present or absent; it does not verify if the values are well-configured.
*   **`report_generator.py`**: Responsible for formatting the terminal output. It utilizes the `colorama` library to print a visually distinct report, coloring the section titles green for found headers and red for missing headers (vulnerabilities).
*   **`requirements.txt`**: Lists all external Python dependencies required to run the project (`requests`, `colorama`, and specifically `urllib3<2` to ensure SSL/TLS compatibility on macOS environments).
*   **`.gitignore`**: Ensures that the local Python virtual environment (`.venv`) is not tracked by Git, keeping the repository clean.
*   **`.vscode/settings.json`**: (Local development only) Directs the Visual Studio Code workspace to use the isolated Python interpreter from the virtual environment.

## Design Decisions
During the development of this tool, several architectural and design choices were made:

1.  **Modular Architecture:** Instead of writing a single monolithic script, the logic was split into `scanner.py`, `analyzer.py`, and `report_generator.py`. This separation of concerns makes the codebase highly maintainable, easier to unit test, and scalable.
2.  **Virtual Environment Isolation:** A `.venv` keeps project dependencies separate from the system Python installation. Compatibility can still depend on the Python version, operating system, and SSL/TLS configuration.
3.  **Focus on Presence of Security Headers:** The scanner makes a GET request and checks the presence of selected HTTP response headers. It does not send exploit payloads or modify the target, but only scan systems you own or are authorized to test.
4.  **CLI over GUI:** A Command Line Interface approach was chosen over a graphical interface because this tool is intended to be used by engineers in terminal environments.

## How to Run
To execute the Automated API Security Scanner locally, follow these steps in your terminal:

1.  **Activate the Virtual Environment:**
    Ensure you are in the project directory and activate the environment:
    ```bash
    source .venv/bin/activate
    ```

2.  **Install dependencies:**
    Install the required libraries listed in the requirements file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute the scanner:**
    Run the main script passing the target API URL using the `-u` argument:
    ```bash
    python scanner.py -u https://api.github.com
    ```

4.  **Read the report:**
    The tool will output the results directly to the terminal, separating found and missing headers into distinct sections.
