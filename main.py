# Structure code 


import json
import requests
from bs4 import BeautifulSoup

def scrape_site_1():
    url = "https://..."
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Extraction...
    return data

def scrape_site_2():
    url = "https://..."
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Extraction...
    return data

def save_json(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_csv(data, filename="data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    data1 = scrape_site_1()
    data2 = scrape_site_2()

    merged = data1 + data2  # ou autre logique

    save_json(merged)
    save_csv(merged)

    print("Scraping terminé. Fichiers générés : data.json et data.csv")

if __name__ == "__main__":
    main()
