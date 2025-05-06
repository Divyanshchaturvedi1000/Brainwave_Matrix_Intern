from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔐 Replace this with your own VirusTotal API key
API_KEY = '9758b93b1f7c228c5c592996c26f19ac937e0d37d8ee5a3f3c4f480c546441b4'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_url():
    url_to_scan = request.form['url']
    
    headers = {
        "x-apikey": API_KEY
    }

    # Submit URL for scanning
    scan_response = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data={"url": url_to_scan}
    )

    if scan_response.status_code == 200:
        scan_id = scan_response.json()["data"]["id"]

        # Fetch the scan report
        report_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        result_response = requests.get(report_url, headers=headers)
        
        if result_response.status_code == 200:
            data = result_response.json()
            stats = data["data"]["attributes"]["stats"]
            malicious = stats["malicious"]
            harmless = stats["harmless"]
            suspicious = stats["suspicious"]

            verdict = "Phishing/Malicious" if malicious > 0 else "Safe"
            return render_template("result.html", url=url_to_scan, verdict=verdict, stats=stats)
    
    return "Error scanning the URL. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
