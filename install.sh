#!/bin/bash

# 1. Verificam/Cream mediul virtual (.venv)
if [ ! -d ".venv" ]; then
    echo "Se creeaza mediul virtual..."
    python3 -m venv .venv
else
    echo "Mediul virtual exista deja."
fi

# 2. Activam mediul si instalam
echo "⬇Se instaleaza librariile: streamlit, pandas, numpy, plotly, requests..."
source .venv/bin/activate

# Actualizam pip ca sa nu avem erori vechi
pip install --upgrade pip

# Instalam lista din fisier
pip install -r requirements.txt

echo "Librariile au fost instalate"