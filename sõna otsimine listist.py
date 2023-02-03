words = ["elu", "arm", "roomama", "tants", "jaks", "püha", "lihavõte", "raudne", "sehkendama", "tumm", 	"toonekurg",
    "ninaluu", "kaltsium", "aastaselt", "summa", "aerutaja", "rahvas", "õnnelik", "mood", "heitma",
    "jalg", "sein", "kontrabass", "aastaselt", "petujutt"]

otsitav = input("Sisesta otsitav sõna: ")
if otsitav in words:
    print(f"Jah, sinu sõna on antud järjendis.")
else:
    print("Sinu otsitavat sõna ei olnud järjendis.")