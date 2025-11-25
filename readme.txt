Proiect: Convertor Valutar (Python)

Acesta este un proiect simplu făcut la laborator, în care am lucrat cu
Python, PyCharm, mediul virtual (venv), fișiere separate și apelarea
unor API-uri. Proiectul convertește sume între diferite monede folosind
o funcție proprie și niște cursuri preluate fie dintr-un API, fie dintr-un
fallback dacă API-ul nu merge (și de obicei nu merge).

Structura proiectului:
- main.py – programul principal, rulează în buclă și cere utilizatorului
            suma și monedele.
- conversion.py – funcția care face conversia efectivă.
- rates_api.py – încearcă să ia cursurile dintr-un API real; dacă nu,
                 folosește niște valori de rezervă ca să nu moară programul.
- api_demo_agify.py – un fișier separat unde am încercat un API mai simplu
                      (agify), doar ca exemplu de laborator.
- hello.py – primul script doar ca să testăm PyCharm.

API-uri:
Am folosit API-ul de la https://open.er-api.com pentru cursuri valutare.
E gratuit și nu cere cheie, dar din când în când nu răspunde cum trebuie,
așa că am adăugat fallback local. Codul tratează erorile ca să nu se
închidă programul.

Cum se rulează:
1. Deschizi proiectul în PyCharm.
2. Te asiguri că e activ mediul virtual al proiectului.
3. Instalezi pachetul „requests” dacă nu e instalat.
4. Rulezi main.py.

Funcționalitate:
- utilizatorul introduce o sumă și două monede
- programul încearcă să ia cursuri reale
- dacă API-ul nu merge, folosește cursurile default
- afișează rezultatul și continuă în buclă până se scrie "exit"

Concluzie:
Proiectul e simplu, dar acoperă ce s-a cerut la laborator:
PyCharm, venv, funcții, importuri între fișiere, buclă while, try/except,
un API apelat cu requests, tratat erori etc.

Nu e ceva foarte complicat, dar ne-am atins obiectivele.

Documentatie + un paragraf + impartim modular aplicatia si explicam ce face

impartim in frontend si backend si explicam ce face fiecare (tot modular).

de lucrat cu clase


+ forex