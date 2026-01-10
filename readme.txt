PROIECT CONVERTOR VALUTAR SI ANALIZA FOREX
==========================================

DESCRIERE
---------
Aceasta aplicatie este un instrument software pentru conversia valutara in timp real
si vizualizarea evolutiei pietei financiare (grafice tip Candlestick).
Proiectul este structurat modular (Backend/Frontend) si utilizeaza API-uri externe
pentru date financiare.

CERINTE DE SISTEM
-----------------
- Python 3.8 sau mai nou
- Conexiune la internet (pentru preluarea cursurilor valutare)

LIBRARII NECESARE
-----------------
Urmatoarele pachete Python sunt necesare pentru functionarea aplicatiei:
- streamlit
- pandas
- numpy
- plotly
- requests

INSTALARE
---------
1. Deschideti terminalul in folderul radacina al proiectului.

2. (Optional dar recomandat) Creati un mediu virtual:
   Windows: python -m venv venv
   Mac/Linux: python3 -m venv venv

3. Activati mediul virtual:
   Windows: .\venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

4. Instalati dependintele:
   pip install streamlit pandas numpy plotly requests

RULARE APLICATIE
----------------
Pentru a porni interfata grafica, urmati acesti pasi in terminal:

1. Navigati in folderul de frontend:
   cd frontend

2. Porniti aplicatia folosind Streamlit:
   streamlit run web_interface.py

Aplicatia se va deschide automat in browserul implicit la adresa http://localhost:8501

AUTORI (ECHIPA DE PROIECT)
--------------------------
1. Bosie Mihai
2. Dobrescu Andrei Alexandru
3. Ciocirlan Mario Florin
4. Nicolaie Rares