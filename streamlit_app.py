import streamlit as st
st.image("img/neuronas.jpg", use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.title("Una neurona como una entrada y un peso")
    w = st.slider("Selecciona un valor:", min_value=0, max_value=5, value=0, key="slider_tab1")
    x = st.number_input("Inserte el valor de la entrada", key="slider_tab1_x")
    if st.button("Calcular Salida", type="primary", key="calcular_tab1_button_1"):  # Asegúrate de que el key sea único
        y = w * x
        st.write("El valor de la salida es:", y)


with tab2:
    st.title("Dos neuronas como una entradas y dos peso")

    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso0:", min_value=0, max_value=5, value=0, key="slider_tab2_col1")
        x0 = st.number_input("Entrada x0", key="slider_tab2_x0")

    with col2:
        w1 = st.slider("Peso1:", min_value=0, max_value=5, value=0, key="slider_tab2_col2")
        x1 = st.number_input("Entrada x1", key="slider_tab2_x1") 

    if st.button("Calcular Salida", type="primary", key="calcular_tab2_button_2"):  # Asegúrate de que el key sea único
        y = w0 * x0 + w1 * x1
        st.write("El valor de la salida es:", y)


with tab3:
    st.title("Tres neuronas como una entrada, tres peso y un sesgo")

    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso0:", min_value=0, max_value=5, value=0, key="slider_tab3_col1")
        x0 = st.number_input("Entrada x0", key="slider_tab3_x0")

    with col2:
        w1 = st.slider("Peso1:", min_value=0, max_value=5, value=0, key="slider_tab3_col2")
        x1 = st.number_input("Entrada x1", key="slider_tab3_x1")

    with col3:
        w2 = st.slider("Peso2:", min_value=0, max_value=5, value=0, key="slider_tab3_col3")
        x2 = st.number_input("Entrada x2", key="slider_tab3_x2") 

    b = st.number_input("Introduzca el valor del sesgo", key="slider_tab3_b")

    if st.button("Calcular Salida", type="primary", key="calcular_tab3_button_3"):  # Asegúrate de que el key sea único
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.write("El valor de la salida es:", y)
