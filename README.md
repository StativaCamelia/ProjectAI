# ProjectAI

# Implicare Membrii Echipa:
  Documentare cu privire la tema(în colaborare):
    Gagea Eusebiu Andrei
    Stativă Camelia-Georgiana
    Zănceanu Ana-Maria
  ## Link-uri utile
    https://cloud.google.com/natural-language/docs/analyzing-entities
    https://www.depends-on-the-definition.com/named-entity-recognition-with-bert/
    https://towardsdatascience.com/train-ner-with-custom-training-data-using-spacy-525ce748fab7
  # Cod Sursa: API + Frontend(în colaborare):
    Gagea Eusebiu Andrei
    Stativă Camelia-Georgiana
    Zănceanu Ana-Maria

  # Mod de funcționare:
    Din pagina principală, apăsând butonul de Start now, se ajunge în pagina de search. În primul input se va introduce întrebarea, iar în al doilea se primește query-ul primit ca răspuns. Acesta se poate modifica și copia pentru a fi introdus în motorul de căutare Google.
    
    Ce se petrece în spate:
    
    -întrebarea primită este tradusă în limba engleză
    
    -se desparte în propoziții în funcție de AND sau OR
    
    -pentru fiecare propoziție se apelează api-ul analyzingEntities de la google și se preiau entitățile principale din propoziții
    
    -aceste entități vor fi trecute prin api-ul de similarități a.î. să identificăm operatorii și valorile acestora cu care se va construi query-ul
    
    -ca rezultat se va afișa query-ul trimit
