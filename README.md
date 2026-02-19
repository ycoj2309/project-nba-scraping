# projet-nba-scraper

Projet qui consiste à évaluer Le NBA Salary vs Performance Scraper : 
# Scraper les salaires sur hoopshype et les stats sur Basketball-reference 
## Comparer qui est sous-payé, qui est surpayé, qui a le meilleur rapport qualité/prix
#### Extraire sur le site Hoopshype (salaires NBA) : salaire annuel + salaire total + durée du contrat + équipe + position
##### Extraire sur le site Basketball Reference (les performances) : points, rebonds, passes + minutes jouées + PER,BPM,WS,VORP + % de réussite + usage rate + stats défensives
###### Comparer les données des deux sites qui ne concordent pas forcément et faire un pourcentage 

 
# Projet Python – Scraping & Analyse de Données

Ce projet a été réalisé dans l’environnement Onyxia.  
Il consiste à scraper deux sites web, extraire les données, les fusionner, puis les exporter en deux formats :

- `data.json` : données brutes issues du scraping  
- `data.csv` : données nettoyées et structurées  

Le script principal `main.py` permet d’exécuter l’ensemble du pipeline.

---

## 📦 Contenu du repository

| Fichier        | Description |
|----------------|-------------|
| `main.py`      | Script Python principal (scraping + transformation + export) |
| `data.json`    | Données brutes récupérées depuis les sites |
| `data.csv`     | Données nettoyées et prêtes à l’analyse |
| `README.md`    | Documentation du projet |

---

## 🚀 Exécution du projet

### 1. Cloner le repository

```bash
git clone https://github.com/<Jahdiel2309>/<mon-repo>.git
cd <mon-repo>
