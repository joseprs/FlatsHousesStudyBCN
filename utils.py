import os
import pandas as pd
import numpy as np

def remove_outliers_iqr(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def remove_outliers_zscore(df, column, threshold=2):
    z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
    return df[z_scores < threshold]

def get_data(dir="data/"):

    dataframes = []
    for file in os.listdir(dir):
        if file[0] != '.':
            df = pd.read_csv(f"data/{file}")
            dataframes.append(df)
    df = pd.concat(dataframes).drop_duplicates().rename(columns={"orientation.1":"orientation_desc", "floor.1":"floor_desc", "antiquity.1":"antiquity_desc", "conservationState.1":"conservationState_desc", "hotWater.1":"hotWater_type_desc", "heating.1":"heating_desc"})
    bool_features_cols = ['furnished','parking', 'Aire acondicionado', 'Parquet', 'Horno', 'Microondas', 'Serv. portería', 'Balcón', 'Lavadero', 'Armarios', 'Calefacción',
        'Suite - con baño', 'Nevera', 'Puerta Blindada', 'Terraza', 'Electrodomésticos', 'Alarma', 'Cocina Equipada', 'Lavadora',
        'Cocina Office', 'Patio', 'Videoportero', 'Piscina', 'Gres Cerámica', 'Jardín Privado', 'Trastero', 'Internet', 'Domótica', 'TV',
        'Ascensor interior', 'Sistema Video vigilancia CCTV 24h', 'Z. Comunitaria', 'Zona Deportiva', 'Zona Infantil',
        'Piscina comunitaria', 'Gimnasio', 'Baño de huéspedes', 'Cuarto para el servicio', 'Jacuzzi', 'Bodega', 'Sauna',
        'Cuarto lavado plancha', 'Energía Solar', 'elevator', 'Pista de Tenis', 'Porche cubierto'] # df.columns[45:87]
    
    for colname in bool_features_cols:
        df[colname] = np.where(df[colname]>0, True, False)
    
    df = df[(df["value"]>0) & (df["value"].notna()) & (df["surface"]>0) & (df["surface"].notna()) & (df["surface"] < 1000) & (df["energy_value"]<999)]
    
    cols_drop = ["transactions", "transaction_type", "periodicity_id", "energyCertificate", "surfaceLand", "countryId", "level1Id",
                 "level2Id", "level3Id", "level4Id", "level5Id", "level6Id", "level7Id", "level8Id",
                 "conservationState", "orientation", "hotWater", "heating", "antiquity"] # , "floor"
    try:
        df = df.drop(columns=cols_drop)
    except:
        print("Some error ocurred. Maybe already dropped columns")
    
    df_iqr = remove_outliers_iqr(df, "value") # df_iqr
    df_z = remove_outliers_zscore(df, "value")
    
    print(f"IQR: {len(df_iqr)} | Actual: {len(df)} | {(len(df_iqr)/len(df))*100:.2f}%")
    print(f"IQR: {len(df_z)} | Actual: {len(df)} | {(len(df_z)/len(df))*100:.2f}%")
    
    df = df_iqr.copy()
    duplicates_columns = ["value", "energy_value", "energy_letter","environment_value", "rooms", "bathrooms", "surface", "floor", "upperLevel"]
    df = df.drop_duplicates(subset=duplicates_columns, keep='first').reset_index(drop=True)
    print("Total different flats: ", df.shape)

    return df
    