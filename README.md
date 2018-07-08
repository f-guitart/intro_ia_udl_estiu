# Introducció a la Intel·ligència Artificial (Universitat d'Estiu UdL 2018)

Codi del curs d'Introducció a la IA de la Universitat d'Estiu a la UdL.

Conté els exemples que s'utilitzaran durant les sessions dedicades al processat del llenguatge natural.

Els scripts utilitzen l'API de Google Cloud Platform per a NLP i estan pensat per ser utilitzats en el terminal de GCP o amb la Google Cloud SDK Shell.

## Contingut

### Scripts exemple:
* read_json.py: exemple de com llegit un fitxer JSON
* script_example.py: fitxer d'exemple per provar que l'API de GCP funciona correctament

### Scripts:
Els scripts estan adaptats del següent enllaç https://cloud.google.com/natural-language/docs/how-to.

* entity_analyzer.py: analitza les entitats del text o ducment passat per paràmetre
* entity_sentiment_analyzer.py: analitza les entitats i els sentiments del context del text o document passat per paràmetre
* sentiment_analyzer.py: analitza el sentiment del text i les frases del text o document passat per paràmetre
* syntax_analyzer.py: analitza sintàcticament el text passat per paràmetre
* text_classifier.py: classifica el document passat per paràmetre

### Altres fitxers:
* exemple_json.json: exemple de fitxer JSON
* monty_python_holy_grail.txt: text del guió de la película "Monty Python and The Holy Grail Script" (http://montypython.50webs.com/Holy_Grail_Scripts.htm)
* quijote.txt: part del llibre "El ingenioso hidalgo don Quijote de la Mancha" (http://www.cervantesvirtual.com/obra-visor/el-ingenioso-hidalgo-don-quijote-de-la-mancha-6/html/05f86699-4b53-4d9b-8ab8-b40ab63fb0b3_2.html#I_0_)

## Com utilitzar

Per tal de tenir tot el contingut d'aquest repositori a la vostra consola, podeu fer el següent:

> `git clone https://github.com/f-guitart/intro_ia_udl_estiu.git`

Tot seguit:

> `cd intro_ia_udl_estiu`

En general els Scripts accepten l'opció `-h` per rebre informació de com executar-los.

Per rebre informació:

> `script.py -h`

Per passar un text per paràmetre:
> `script.py -t Text a analitzar`

Per passar un document:
> `script.py -d ruta/al/document.txt`

