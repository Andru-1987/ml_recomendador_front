# %% [markdown]
# IMPORTACION DE MODULOS Y SETEO DE PATH DE DATOS

# %%
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


path_dataset:str = "dataset/movies_dataset.csv"

# %%
movie_set = pd.read_csv(path_dataset)

# %%
movie_set.tail(10)

# %%
movie_set.columns = ['index_id','titulo','genero','idioma_original','review','popularidad','fecha_salida','voto_promedio','votos']

# %%
movie_set.info()

# %%
movie_set.describe()

# %%
movie_set.genero = movie_set.genero.astype('category')
movie_set.genero.cat.categories

# %%
sns.set_style('darkgrid')

m = plt.hist(movie_set.voto_promedio, bins =15,ec='Black')
plt.xlim(xmin=0.0)
plt.title("VOTOS POR PULARIDAD", fontsize=20)
plt.ylabel("CANTIDAD DE VOTOS", fontsize=15)
plt.xlabel("VALOR DE POPULARIDAD", fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# %%
sns.set_style('darkgrid')
sns.jointplot(data = movie_set, x='popularidad' ,y='votos', kind='hex')

# %% [markdown]
# LIMPIEZA DE DATOS

# %%
movie_set.genero = movie_set.genero.astype('str')

# %%
movies = movie_set[['index_id', 'titulo', 'review', 'genero']]

# %%
movies.isnull().sum()


# %%
movies['tags'] = movies['review'] + movies['genero']

# %%
movie_df = movies.drop(columns=['review','genero'])

# %% [markdown]
# VECTORIZACION
# ---
# 
# - Se piensa con el conceptio de bag of words
# 

# %%
from sklearn.feature_extraction.text import CountVectorizer


# %%

cv = CountVectorizer(max_features=10000, stop_words='english')


# %%
vector = cv.fit_transform(movie_df['tags'].values.astype('U')).toarray()

# %%
vector

# %%
from sklearn.metrics.pairwise import cosine_similarity

# %%
similarity = cosine_similarity(vector)

# %%
similarity[9923]

# %% [markdown]
#     CORE UTILIZANDO SIMILARIDAD DE COSENO
# 
# ---

# %%


def recomendador(input:str,amount:int = 3):
    i = movie_df[movie_df['titulo'] == input].index[0]
    l = sorted(
        list(
            enumerate(similarity[i])
        ),
        reverse=True,
        key=lambda x:x[1]
    )
    for _ in l[:amount]:
        print( movie_df.iloc[_[0]].titulo )


# %%
import pickle


# %%

pickle.dump(movie_df,open('./pickle_files/lista_peliculas.pkl','wb'))
pickle.dump(similarity,open('./pickle_files/similarity.pkl','wb'))


# %%
pickle.load(open('./pickle_files/lista_peliculas.pkl','rb'))


