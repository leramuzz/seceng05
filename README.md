# Flask API Security Example

Dieses Projekt enthält eine Flask-basierte API mit absichtlich eingebauten Sicherheitslücken, die typische **OWASP API-Sicherheitslücken** simulieren. Die API enthält mehrere Endpunkte, die bekannte Sicherheitsprobleme wie **Unrestricted Resource Consumption**, **Server Side Request Forgery (SSRF)**, **Unsafe Consumption of APIs** und **Security Misconfiguration** demonstrieren.

## Anforderungen

Stellen Sie sicher, dass Sie die folgenden Voraussetzungen installiert haben:

- **Python 3.x**
- **pip** (Python-Paket-Manager)

## Installation

1. **Öffnen Sie das Projekt**

   ```bash
   git clone https://github.com/leramuzz/seceng05.git
   cd seceng05
   ```

2. **Virtuelle Umgebung erstellen**

   Erstellen Sie eine virtuelle Umgebung, um die Abhängigkeiten isoliert zu installieren:

   ```bash
   python -m venv venv
   ```

3. **Virtuelle Umgebung aktivieren**

   Auf Windows:

   ```bash
   venv\Scripts\activate
   ```

   Auf macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. **Abhängigkeiten installieren**

   ```bash
   pip install -r requirements.txt
   ```

5. **Anwendung ausführen**

   ```bash
   python main.py
   ```

   Die Anwendung läuft standardmäßig auf http://127.0.0.1:5000.
