#!/bin/sh

echo "CREATE FILES"

mdkir ./pickle_files/{lista_peliculas,similarity}.pkl

virtualenv venv && source ./venv/bin/activate

echo "VENV CREATED"

pip install -r requirements.txt 

echo "FILE INSTALLED DEPENDENCIES"

python .recomendador.py && streamlit run ./app/app.py



