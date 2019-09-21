# Load Packages
from __future__ import unicode_literals, print_function

import os
import random
from pathlib import Path
import spacy
from tqdm import tqdm # loading bar
import json

def main():
    json_data = open('statics/BASE_DE_TREINO.json', encoding="utf8")
    TRAIN_DATA = json.load(json_data);
    
    model = None
    output_dir=Path(os.path.realpath('') + '/entidades')
    n_iter=250
    
    nlp = spacy.blank('pt')
        
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe('ner')
        
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            if len(ent) > 0:
                 ner.add_label(ent[2])
    
    contador = 0;
    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            contador += 1;
            print(contador)
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in tqdm(TRAIN_DATA):
                nlp.update(
                    [text],
                    [annotations],
                    drop=0.5,
                    sgd=optimizer,
                    losses=losses)
            print(losses)   
            
    if output_dir is not None:
        output_dir = output_dir
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print('Salvando em.: ', output_dir)
    
if  __name__ == '__main__':
    main()