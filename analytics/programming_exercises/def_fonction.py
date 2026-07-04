ips = ["<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>", "<INTERNAL_IP>"]

def verifier_ips(liste_ips):
    print("Adresses IP internes :")
    index = 0
    while index < len(liste_ips):
        adresse = liste_ips[index]
        if "192.168" in adresse:
            print(adresse)
        index = index + 1

# On utilise des parenthèses ici
verifier_ips(ips)
