import requests

url = "https://instance-019e76bc-ee54-705b-b538-deb96bc69e7e.challenges.root-me.pro"
payloads = ["{{7*7}}", "${7*7}", "[[7*7]]", "<%= 7*7 %>", "{7*7}"]

for p in payloads:
    # This is just a conceptual loop, I will do it manually for each field
    print(f"Testing {p}")
