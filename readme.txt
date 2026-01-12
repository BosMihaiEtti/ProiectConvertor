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
Librariile necesare sunt listate in fisierul 'requirements.txt':
- streamlit
- pandas
- numpy
- plotly
- requests

INSTALARE
---------
Exista doua metode de instalare. Alegeti una dintre ele:

METODA 1: AUTOMATA (Recomandat pentru Linux/macOS)
1. Deschideti terminalul in folderul radacina al proiectului.
2. Oferiti drepturi de executie scriptului de instalare:
   chmod +x install.sh
3. Rulati scriptul (acesta creeaza mediul virtual si instaleaza totul):
   ./install.sh

METODA 2: MANUALA (Windows / Linux)
1. Deschideti terminalul in folderul radacina.

2. Creati un mediu virtual:
   Windows: python -m venv .venv
   Linux/Mac: python3 -m venv .venv

3. Activati mediul virtual:
   Windows: .\.venv\Scripts\activate
   Linux/Mac: source .venv/bin/activate

4. Instalati dependintele din fisierul de configurare:
   pip install -r requirements.txt

RULARE APLICATIE
----------------
Important: Aplicatia trebuie pornita din folderul radacina (principal) pentru a
putea accesa corect modulele din backend.

1. Asigurati-va ca mediul virtual este activat (vedeti pasul 3 de mai sus).

2. Porniti aplicatia cu comanda:
   streamlit run frontend/web_interface.py

Aplicatia se va deschide automat in browser la adresa http://localhost:8501

AUTORI (ECHIPA DE PROIECT)
--------------------------
1. Bosie Mihai
2. Dobrescu Andrei Alexandru
3. Ciocirlan Mario Florin
4. Nicolaie Rares George
