import requests

def recherche_adresse():
    try:
        print("########Résultats####### \n")
       
        response = requests.get('https://ipapi.co/json/')
        response_json = response.json()
        print(f"Adresse : {response_json['ip']}\nversion ip: {response_json['version']}\nPays: {response_json['country']}\nVille: {response_json['city']} ")
    except Exception as e:
        print(f"Probleme survenu")
    finally:
        print("\n########Dieuredieuf#######")
         #test pour la fusion des 2 branches
        print("\n########modification sur la branche feature#######")
recherche_adresse()
