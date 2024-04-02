import pandas as pd
import json

def extract_data():
    # Extraction des données à partir des fichiers CSV
    
    cols_to_drop = ['nbre_acte_corona', 'nbre_acte_tot', 'nbre_acte_corona_h', 
                       'nbre_acte_corona_f', 'nbre_acte_tot_h', 'nbre_acte_tot_f']
    urgences_df = pd.read_csv('donnees-urgences-SOS-medecins.csv',sep=';', usecols=lambda col: col not in cols_to_drop)
    tranches_age_df = pd.read_csv('code-tranches-dage-donnees-urgences.csv')

    # Extraction des données à partir du fichier JSON
    with open('departements-region.json', 'r') as file:
        departements_regions_data = json.load(file)

    # Création d'une liste pour stocker les données
    departements_data = []
    for item in departements_regions_data:
        departements_data.append([item['num_dep'], item['dep_name'], item['region_name']])

    # Création du dataframe à partir de la liste de données
    departements_df = pd.DataFrame(departements_data, columns=['num_dep', 'dep_name', 'region_name'])

    return urgences_df, tranches_age_df, departements_df

def clean_data(urgences_df, tranches_age_df, departements_df):
    
    urgences_df = urgences_df.rename(columns={'sursaud_cl_age_corona': 'Code_age','dep':'num_dep'})
    urgences_df = urgences_df.fillna(0)

    # Convertir la colonne date_de_passage en type datetime dans le dataframe des urgences
    urgences_df['date_de_passage'] = pd.to_datetime(urgences_df['date_de_passage'], errors='coerce')
    urgences_df['date_de_passage'] = urgences_df['date_de_passage'].dt.strftime('%d/%m/%Y')

    # Convertir les autres colonnes en type int, excluant la colonne date_de_passage
    for col in urgences_df.columns:
        if col != 'date_de_passage':
            urgences_df[col] = pd.to_numeric(urgences_df[col], errors='coerce',downcast='integer')

    
    tranches_age_df[['code_age', 'Description']] = tranches_age_df['code_age;Description'].str.split(';', expand=True)
    tranches_age_df['code_age'] = pd.to_numeric(tranches_age_df['code_age'], errors='coerce',downcast='integer')

    # Supprimer la colonne 'Code_age;Description' d'origine
    tranches_age_df.drop(columns=['code_age;Description'], inplace=True)

    return urgences_df, tranches_age_df, departements_df

def main():
    # Extraction des données
    urgences_df, tranches_age_df, departements_df = extract_data()
    urgences_df, tranches_age_df, departements_df = clean_data(urgences_df, tranches_age_df, departements_df)

    # Affichage des dataframes pour vérification
    print("DataFrame pour les urgences :\n", urgences_df.head())
    print("\nDataFrame pour les tranches d'âge :\n", tranches_age_df.head())
    print("\nDataFrame pour les départements et régions :\n", departements_df.head())
    print(tranches_age_df.columns)
    print(departements_df.columns)

if __name__ == '__main__':
    main()