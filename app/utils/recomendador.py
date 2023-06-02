


def recomendador(input:str,df_movie,cb_ml_function,amount:int = 3)->list:
    """
    params:
        input str   :   seleccionador 
        df_movie  Dataframe  :   frame de peliculas
        cb_ml_function  Dataframe:   machine learning cosine similarity function
        amount  int    :  cantidad de items retornados

    return
        list :  peliculas --> titulos de peliculas 
    """
    
    i = df_movie[df_movie['titulo'] == input].index[0]
    l = sorted(
        list(
            enumerate(cb_ml_function[i])
        ),
        reverse=True,
        key=lambda x:x[1]
    )

    return [ df_movie.iloc[pelicula[0]].titulo for pelicula in l[:amount] ]
    