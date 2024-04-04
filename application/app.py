import streamlit as st

from predict import predict_flat_value, data_processing

st.set_page_config(layout="wide")
col1, col2 = st.columns([1, 4])

with col1:
    st.image("application/media/bcn.jpeg", use_column_width=False, width=150)

with col2:
    st.title("Barcelona Flat Value Predictor")

with st.form(key='flats_features_form'):
    col3, col4, col5, col6 = st.columns([1,1,1,1])

    with col3:
        surface = st.text_input("Surface")
        rooms = st.text_input("Rooms")
    with col4:
        bathrooms = st.text_input("Bathrooms")
        pool = st.checkbox("Pool")
    with col5:
        environment_value = st.text_input("Environment Value")
        elevator = st.checkbox("Elevator")
    with col6:
        energy_value = st.text_input("Energy Value")
        air_conditioning = st.checkbox("Air-conditioning")
        
        
    neighbor = st.selectbox("Neighbor:", ['Dreta de l Eixample', 'El Raval', 'Barri Gotic',
       'L Antiga Esquerra de l Eixample',
       'La Nova Esquerra de l Eixample',
       'Sant Pere  Sta  Caterina i la Ribera', 'Sant Gervasi  Galvany',
       'Sagrada Familia', 'Vila de Gracia', 'Barri de les Corts',
       'El Poble Sec   Parc de Montjuic', 'Sant Andreu de Palomar',
       'Sant Antoni', 'El Camp d en Grassot i Gracia Nova',
       'Diagonal Mar i el Front Maritim del Poblenou', 'El Guinardo',
       'La Marina del Port', 'El Camp de l Arpa del Clot',
       'El Putget i el Farro', 'El Poblenou', 'Fort Pienc',
       'Sant Gervasi i la Bonanova', 'Vilapicina i la Torre Llobeta',
       'El Clot', 'La Salut', 'Pedralbes', 'La Prosperitat',
       'La Verneda i la Pau', 'La Barceloneta', 'Sants', 'Les Roquetes',
       'Sants Badal', 'Sant Marti de Provencals',
       'La Maternitat i Sant Ramon', 'El Besos i el Maresme',
       'La Teixonera', 'El Carmel', 'La Bordeta', 'La Sagrera',
       'Provencals del Poblenou', 'El Baix Guinardo', 'Sarria',
       'El Turo de la Peira', 'Hostafrancs', 'Navas', 'Can Baro',
       'El Parc i la Llacuna del Poblenou', 'Horta',
       'La Vila Olimpica del Poblenou', 'El Bon Pastor',
       'La Font de la Guatlla', 'La Font d en Fargues',
       'El Congres i els Indians', 'Les Tres Torres', 'La Guineueta',
       'Vallcarca i els Penitents', 'Trinitat Vella', 'Verdum', 'Porta',
       'La Marina del Prat Vermell', 'El Coll', 'Ciutat Meridiana',
       'Vallvidrera   Tibidabo   Les Planes', 'Sant Genis dels Agudells',
       'Torre Baro', 'La Clota', 'La Trinitat Nova', 'Canyelles',
       'Montbau', 'Vallbona', 'Zona Franca   Port', 'Can Peguera',
       'Baro de Viver'])
    
    energy_letter = st.selectbox("Energy Letter:", ["Missing", "A", "B", "C", "D", "E", "F", "G"])
    environment_letter = st.selectbox("Environment Letter:",  ["Missing", "A", "B", "C", "D", "E", "F", "G"])
    
    floor = st.selectbox("Floor:", ['1planta', '2planta', '3planta', '4planta', '5planta', 'Bajos',
       '6planta', 'Entresuelo', '7planta', '8planta', 'Otro', 'Principal',
       'Apartirdela15planta', '10planta', 'Sotano', '9planta', '11planta',
       '13planta', '12planta', '15planta', 'Subsotano', '14planta'])

    submit_button = st.form_submit_button(label='Submit')
    
    # process data

    if submit_button:
        data = data_processing(surface, rooms, bathrooms, pool, environment_value, elevator, energy_value, air_conditioning,
                    neighbor, energy_letter, environment_letter, floor)
        
        prediction = predict_flat_value(data)
        st.write(f"Your flat value is around: {prediction}€")
