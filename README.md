## PROJECT OF DATA SCIENCE AND MACHNE LEARNING

:pencil2:

En este proyecto se debe trabajar con un dataset de peliculas.
Se usa como concepto de machine learning un modelo sencillo de cosine similarity para la busqueda de patrones de generos y tipos de peliculas, usando bag of text.

Si bien es un modelo simple, también se ha generado un pequeño front-end mirando las recomendaciones que realiza la función por medio de streams usando pickle.

DEPENDENCIES:

-   pandas
-   scikit-learn
-   streamlit

ARCHIVOS DE VITAL IMPORTANCIA:

-   recomendador_project.ipynb => donde se realaiza ciertas etapas de limpieza, informacion y categorización del dataset buscado, para seleccionar el modelo que sea el que se ajuste a este proyecto
-   app/app.py ==> el front realizado en base de python
-   dataset => el dataset que se puede descargar directamente desde un servidor en la nube
-   app/utils/recomendador.py ==> la función simplificada para utilizar el archivo pickle con el modelo cosine.similarity

# USO

para levantar el proyecto debemos correr el siguiente shell que automatiza directamente el proyecto.

```
 source machine_learning_init.sh

```
