from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank
def download_pubmed(keyword): 
    """Permite descargar articulos desde PUB med"""
    Entrez.email = 'daniela.endara@est.ikiam.edu.ec'
    handle = Entrez.esearch(db="pubmed", term= keyword, usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    record["Count"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed", rettype="medline", retmode="text", retstart=0, retmax=543, webenv=webenv, query_key=query_key)  
    out_handle = open("data/resultado_pubmed.txt", "w")
    resultado = handle.read()
    handle.close()
    out_handle.write(resultado)
    out_handle.close()
    return (id_list)  



import csv 
import re
import pandas as pd 
from collections import Counter

def mining_pubs(tipo):
    """Utiliza la variable AD para realizar el data frame """
    with open("resultado_pubmed.txt", errors="ignore") as f: 
        texto = f.read() 
    if  tipo == "AD": 
        texto = re.sub(r" [A-Z]{1}\.","", texto)
        texto = re.sub(r"Av\.","", texto)
        texto = re.sub(r"Vic\.","", texto)
        texto = re.sub(r"Tas\.","", texto)
        AD = texto.split("AD  - ")
        n_paises = []
        for i in range(len(AD)): 
            pais = re.findall("\S, ([A-Za-z]*)\.", AD[i])
            if not pais == []: 
                if not len(pais) >= 2:  
                    if re.findall("^[A-Z]", pais[0]): 
                        n_paises.append(pais[0])
        conteo=Counter(n_paises)
        resultado = {}
        for clave in conteo:
            valor = conteo[clave]
            if valor != 1: 
                resultado[clave] = valor 
        veces_pais = pd.DataFrame()
        veces_pais["pais"] = resultado.keys()
        veces_pais["numero de autores"] = resultado.values()
        return (veces_pais)