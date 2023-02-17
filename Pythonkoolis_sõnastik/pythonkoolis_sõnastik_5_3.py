from pythonkoolis_sõnastik_5_1 import inglise, itaalia
e_inglise = {}
e_itaalia = {}
for key,value in inglise.items():
    e_inglise[value] = key
    
for key,value in itaalia.items():
    e_itaalia[value] = key

if __name__ == "__main__":
    print (e_inglise)
    print (e_itaalia)