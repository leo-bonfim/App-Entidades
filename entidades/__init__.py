# -*- coding: utf-8 -*-

import spacy
import re
import os

my_path = os.path.abspath(os.path.dirname(__file__))
nlp = spacy.load(my_path)

def achar_entidades(publicacao):
    metadados = {}
    publicacao = publicacao.replace('\n', '')
    publicacao = re.sub('( ){2,}', ' ', publicacao).strip()
    publicacao = publicacao.upper()
    
    doc = nlp(publicacao)
    
    flag_advogado = False
    if 'ADVOGADO' in publicacao:
        flag_advogado = True
    
    for ent in doc.ents:
        
        label = ent.label_
        text = ent.text
        
        if label == 'ADV' and flag_advogado == True:
            label = 'ADVOGADO'
            
        if label not in metadados:
            metadados[label] = []
            metadados[label].append(text)
        else:
            if text not in metadados.get(label):
                metadados[label].append(text)
                
    return metadados;