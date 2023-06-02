import streamlit as st
import pickle
from utils.recomendador import recomendador

peliculas = pickle.load(
    open("./pickle_files/lista_peliculas.pkl","rb")
)

ml_function = pickle.load(
    open("./pickle_files/similarity.pkl","rb")
)


st.header("RECOMENDADOR DE PELICULAS")
pick_option = st.selectbox("Seleccione una pelicula",peliculas.titulo.values )
amount = st.radio("Cantidad de peliculas", tuple(range(1,6)) )

if st.button(f"Recomendame {amount} pelicula simil"):
    st.write(f"Pelicula seleccionada:\n * {pick_option}")
    stream = recomendador(pick_option,peliculas,ml_function,amount+1)
    st.write("Las peliculas que te puedo recomendar en base a recomendaciones por Machine Learning")
    for index,pelicula in enumerate(stream):
       if index != 0:
        st.write(stream[index])

    