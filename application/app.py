import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns([1, 4])

with col1:
    st.image("application/media/bcn.jpeg", use_column_width=False, width=150)

with col2:
    st.title("Barcelona Flat Value Predictor")

with st.form(key='flats_features_form'):
    col3, col4, col5, col6 = st.columns([1,1,1,1])

    with col3:
        input5 = st.text_input("Surface")
        input1 = st.text_input("Rooms")
    with col4:
        input3 = st.text_input("Bathrooms")
        boolean_value = st.checkbox("Pool")
    with col5:
        input9 = st.text_input("Environment Value")
        boolean_value = st.checkbox("Elevator")
    with col6:
        input7 = st.text_input("Energy Value")
        boolean_value = st.checkbox("Air-conditioning")
        
        
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
    energy_letter = st.selectbox("Energy Letter:", ["Option 1", "Option 2", "Option 3"])
    environment_letter = st.selectbox("Environment Letter:", ["Option 1", "Option 2", "Option 3"])
    floor = st.selectbox("Floor:", ["Option 1", "Option 2", "Option 3"])

    st.form_submit_button(label='Submit')