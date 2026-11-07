# Automated API Security Scanner
#### Video Demo:  [COLE AQUI A URL DO YOUTUBE]
#### Name: Rafael Oliveira Campos
#### City/Country: Timóteo, Minas Gerais, Brazil

## Description
The Automated API Security Scanner is a Python-based tool designed to validate the security posture of web application programming interfaces (APIs). As modern applications heavily rely on APIs, ensuring they implement proper security headers and configurations is a critical step in a DevSecOps pipeline. 

This project automates the process of sending requests to a target API endpoint, analyzing the HTTP response headers, and identifying missing or misconfigured security controls (such as CORS policies, Strict-Transport-Security, Content-Security-Policy, and X-Frame-Options). At the end of the execution, the tool generates a comprehensive security report detailing the vulnerabilities found and providing remediation steps.

This tool was built to bridge the gap between quality assurance and cybersecurity, allowing automated tests to fail or warn developers if security standards are not met before deployment.

## Files Structure
Here is a breakdown of the files included in this project and their respective roles:

*   **`scanner.py`**: The main execution script. It handles the command-line arguments (CLI), orchestrates the HTTP requests using the `requests` library, and invokes the analysis engine.
*   **`analyzer.py`**: This module contains the core logic for inspecting headers. It cross-references the headers returned by the API against a predefined dictionary of required security headers and acceptable values.
*   **`report_generator.py`**: Responsible for formatting the findings. It takes the raw analysis data and exports it into a readable format (e.g., JSON or a structured CLI output) for easy integration with CI/CD pipelines.
*   **`requirements.txt`**: Lists all external Python dependencies required to run the project (e.g., `requests`, `colorama` for terminal styling).
*   **`test_endpoints.txt`**: A sample text file containing mock API URLs used to demonstrate and test the scanner's capabilities without targeting live production systems inappropriately.

## Design Decisions
During the development of this tool, several architectural and design choices were made:

1.  **Language Choice (Python):** Python was selected due to its powerful standard library and the `requests` module, which makes handling HTTP transactions straightforward. It is also the industry standard for security scripting and automation.
2.  **Modular Architecture:** Instead of writing a single monolithic script, the logic was split into `scanner.py`, `analyzer.py`, and `report_generator.py`. This makes the codebase maintainable, easier to unit test, and scalable if future modules (like authentication testing or payload injection) need to be added.
3.  **Focus on Security Headers:** While API security encompasses many areas (like rate limiting or SQLi), I chose to focus strictly on security headers for this scope. Misconfigured headers are a common OWASP vulnerability and are easily verifiable through passive scanning, ensuring the tool is safe to use and doesn't perform intrusive or destructive actions against unauthorized targets.
4.  **No GUI (Command Line Interface):** A CLI approach was chosen over a graphical interface because this tool is intended to be used by engineers or integrated into automated continuous integration pipelines, where visual interfaces are not applicable.

## How to Run
To execute the Automated API Security Scanner locally, follow these steps:

1.  **Install dependencies:** Ensure you have Python 3 installed. Run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute the scanner:** Run the main script passing the target API URL as an argument.
    ```bash
    python scanner.py --url [https://api.example.com](https://api.example.com)
    ```

3.  **Read the report:** The tool will output the results directly to the terminal, highlighting missing headers in red and properly configured headers in green.
