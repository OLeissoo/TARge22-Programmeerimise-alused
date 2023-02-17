from pythonkoolis_sõnastik_5_1 import inglise, itaalia
from pythonkoolis_sõnastik_5_3 import e_inglise, e_itaalia
"""
Lisa kõikidesse sõnastikesse järgmised sõnad:

    headaega - goodbye - arrivederci
    pott - pot - pentola
    sõnastik - dictionary - dizionario 

Tõlgi (väljastage ekraanile) järgmised sõnad:

    üks -> itaalia
    ciao - > eesti
    dog -> itaalia
    pentola - inglise
"""

#lisan algsetesse dictionaridesse
inglise["headaega"] = "goodbye"
inglise["pott"] = "pot"
inglise["sõnastik"] = "dictionary"
itaalia["headaega"] = "arrivederci"
itaalia["pott"] = "pentola"
itaalia["pott"] = "dizionario"

e_inglise["goodbye"] = "headaega"
e_inglise["pot"] = "pott"
e_inglise["dictionary"] = "sõnastik"
e_itaalia["arrivederci"] = "headaega"
e_itaalia["pentola"] = "pott"
e_itaalia["dizionario"] = "sõnastik"

#tõlgin sõnad
print(f"Üks itaalia keeles -> {itaalia['üks']}")
print(f"Ciao eesti keeles -> {e_itaalia['ciao']}")
print(f"Dog itaalia keeles -> {itaalia[e_inglise['dog']]}")
print(f"Pentola inglise keeles -> {inglise[e_itaalia['pentola']]}")