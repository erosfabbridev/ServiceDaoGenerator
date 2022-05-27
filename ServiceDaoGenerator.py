
from string import Template
import os, glob


def riempiClassi():

    numeroDiClassiDaGenerare = int(input("[+] Inserisci quantità di classi da generare: "))
    classi = [" "] * numeroDiClassiDaGenerare

    if numeroDiClassiDaGenerare >1:
        for i in range(numeroDiClassiDaGenerare):
            classi[i] = input("[+"+str(i+1)+"]Inserisci il nome della classe: ")
    else:
        classi[0] = input("[+]Inserisci il nome della classe: ")
    return classi
    

def riempiClassiFile(nomeFile):
    classiArray = []
    for file in glob.glob(nomeFile+".*"):
        with open(file) as my_file:
            for line in my_file:
                classiArray.append(line.strip())
    return classiArray


def creaClassi(classiInput):
    for classe in classi:
  
        try:
            os.mkdir('classi_generate/'+classe+'_classiGenerate')
        except:
            print("[-]Non creo la cartella classi_generate/"+classe+'_classiGenerate'+", esiste già!")
        
        #DAO Interface
            result = src.substitute(nomeprogetto=nomeDelProgetto, classminuscola=classe, classmaiuscola=classe.capitalize())
            resultfile = open('classi_generate/'+classe+'_classiGenerate/'+classe.capitalize()+'DAO.java', 'w')
            resultfile.write(result)
        print("[+]Ho creato la classe "+classe+"DAO")
        #DAOimpl Class
        with open('templates/DAOImpl.template', 'r') as f:
            src = Template(f.read())
            result = src.substitute(nomeprogetto=nomeDelProgetto, classminuscola=classe, classmaiuscola=classe.capitalize())
            resultfile = open('classi_generate/'+classe+'_classiGenerate/'+classe.capitalize()+'DAOImpl.java', 'w')
            resultfile.write(result)
        print("[+]Ho creato la classe "+classe+"DAOImpl")
    
        #DAOService Interface
        with open('templates/Service.template', 'r') as f:
            src = Template(f.read())
            result = src.substitute(nomeprogetto=nomeDelProgetto, classminuscola=classe, classmaiuscola=classe.capitalize())
            resultfile = open('classi_generate/'+classe+'_classiGenerate/'+classe.capitalize()+'DAOService.java', 'w')
            resultfile.write(result)
        print("[+]Ho creato la classe "+classe+"DAOImpl")
    
        #DAOServiceImpl Class
        with open('templates/ServiceImpl.template', 'r') as f:
            src = Template(f.read())
            result = src.substitute(nomeprogetto=nomeDelProgetto, classminuscola=classe, classmaiuscola=classe.capitalize())
            resultfile = open('classi_generate/'+classe+'_classiGenerate/'+classe.capitalize()+'DAOServiceImpl.java', 'w')
            resultfile.write(result)
        print("[+]Ho creato la classe "+classe+"DAOImplClass")
    



print("IMPORTANTE: tutti i nomi delle classi devono essere scritti in minuscolo!")

nomeDelProgetto = input("[+] Inserisci nome del progetto: ")
scelta = input("[+]Inserisci 1 per prendere classi da file, 2 per inserirle da console: ")

classi = []

if scelta == "1":
    classi = riempiClassiFile(input("[+]inserisci nome file senza estensione: "))
    
elif scelta == "2":
    classi = riempiClassi()

 
try:
    os.mkdir('classi_generate')
except:
    print("[-]Non creo la cartella classi_generate, esiste già!")
     
creaClassi(classi)

 
