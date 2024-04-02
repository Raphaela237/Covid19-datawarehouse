# Projet ETL COVID-19 Data Warehouse

Ce projet vise à extraire, transformer et charger (ETL) des données relatives à la pandémie de COVID-19 en France dans un entrepôt de données. Il utilise des données provenant de différentes sources telles que des fichiers CSV et JSON, et effectue diverses opérations de nettoyage et de transformation pour préparer les données à l'analyse.

## Installation

1. Clonez ce dépôt sur votre machine locale :
git clone <URL_du_dépôt>

2. Installez les dépendances Python requises en exécutant la commande suivante dans le répertoire du projet :
pip install -r requirements.txt

## Utilisation

1. Assurez-vous d'avoir les fichiers suivants dans le répertoire racine du projet :
- `donnees-urgences-SOS-medecins.csv`
- `code-tranches-dage-donnees-urgences.csv`
- `departements-region.json`

2. Exécutez le script ETL en exécutant la commande suivante dans votre terminal :
python etl.py

3. Les données nettoyées seront affichées dans votre terminal.

## Dépendances

- pandas : version 1.3.3
- json : version standard de Python

## Structure du projet

|-- README.md
|-- etl.py
|-- donnees-urgences-SOS-medecins.csv
|-- code-tranches-dage-donnees-urgences.csv
|-- departements-region.json
|-- requirements.txt

## Licence

Ce projet est distribué sous la licence MIT. Veuillez consulter le fichier LICENCE pour plus d'informations.

Cette version du README.md utilise une syntaxe Markdown pour structurer le contenu de manière lisible et organisée, facilitant ainsi la compréhension et l'utilisation du projet.
