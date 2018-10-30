# Python Cow Obfuscator
Progetto del corso "Sicurezza del Software", Laurea magistrale "Ingegneria e scienze informatiche", Università degli studi di Verona.

## Obiettivo
L'obiettivo del progetto è comprendere il funzionamento di un offuscatore realizzandone uno.

## Il progetto
Il nostro progetto si ispira al linguaggio Cow e prevede l'offuscamento di script Python.

## Funzionalità
Python Cow Obfuscator provvede a:
- generare ed inserire codice morto
- rimuovere i commenti
- rimuovere tutte le righe vuote
- sostituire istruzioni con una sequenza di istruzioni, in modo particolare converte in cicli for e while le seguenti istruzioni:
    - var = var [+, -, *, /] var
    - var = var [+, -, *, /] integer
    - var = integer [+, -, *, /] var
- sostituire le costanti con una funzione generata che ritorna il medesimo valore
- sostituire i nomi di tutte le variabili con nomi generati in modo casuale
- sostituire i nomi di tutte le funzioni con nomi generati in modo casuale

## Avvio
python3.x pythonCowObfuscator.py -s file_to_obfuscate.py

## Autori
- Valentina Ceoletta valentina.ceoletta@studenti.univr.it
- Mattia Zanotti mattia.zanotti@studenti.univr.it
- Nicolò Zenari nicolo.zenari@studenti.univr.it

## Valutazione
30 e Lode
