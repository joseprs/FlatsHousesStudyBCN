import pickle
import numpy as np
import pandas as pd


def data_processing(surface, rooms, bathrooms, pool, environment_value, elevator, energy_value, air_conditioning,
                    neighbor, energy_letter, environment_letter, floor):
    
    energy_letter_dict = {"Missing":"energy_letter_0", "A":"energy_letter_1", "B":"energy_letter_2",
                          "C":"energy_letter_3", "D":"energy_letter_4", "E":"energy_letter_5",
                          "F":"energy_letter_6", "G":"energy_letter_7",
    }
    energy_letter = energy_letter_dict[energy_letter]

    environment_letter_dict = {"Missing":"environment_letter_0", "A":"environment_letter_1", "B":"environment_letter_2",
                          "C":"environment_letter_3", "D":"environment_letter_4", "E":"environment_letter_5",
                          "F":"environment_letter_6", "G":"environment_letter_7",
    }
    environment_letter = environment_letter_dict[environment_letter]

    neighbor = "level8_" + neighbor.replace(" ","_")
    floor = "floor_desc_" + floor

    X_test_columns = np.load("support_files/X_test_columns.npy", allow_pickle=True)
    X_test_columns_dtypes = np.load("support_files/X_test_columns_dtypes.npy", allow_pickle=True)

    X_test_real = pd.DataFrame(columns=X_test_columns)

    new_row = {"rooms":rooms, "bathrooms":bathrooms, "surface":surface, "energy_value":energy_value, "environment_value":environment_value, "elevator":elevator,
            "Aire acondicionado":air_conditioning, "Piscina":pool}
    
    dummies_dict = {f"{col}":False for col in X_test_columns[8:]}

    new_row.update(dummies_dict)

    new_row[neighbor] = True
    new_row[energy_letter] = True
    new_row[environment_letter] = True
    new_row[floor] = True

    X_test_real = pd.concat([X_test_real, pd.DataFrame(new_row, index=[0])], ignore_index=True)

    for column, type in zip(X_test_columns, X_test_columns_dtypes):
        X_test_real[column] = X_test_real[column].astype(type)

    return X_test_real


def predict_flat_value(input):

    with open("models/flat_prices_predictor_model.pkl", 'rb') as file:  
        model = pickle.load(file)
    
    return model.predict(input)[0]