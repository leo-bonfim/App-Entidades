# -*- coding: utf-8 -*-

import re
import sys
import entidades
import publicacoes_com_metadados as pm

def main():
     while True:
         
          print("\n[1] Verificar metadados\n[2] Gerar metadados\n[0] Sair\n")
          
          try:
               item = int(input("Selecione uma opção acima.: "))
          except ValueError:
               print('\nEscolha uma opção válida!')
               continue
          
          if item == 0:
               sys.exit()
          elif item == 1:
               for publicacao in pm.publicacoes:
                    print('\n-------------------------------PUBLICAÇÃO-------------------------------\n')
                    print(re.sub('( ){2,}', ' ', publicacao.conteudo))
                    print('\n-------------------------------METADADOS-------------------------------\n')
                    print(publicacao.metadados)
          elif item == 2:
               print('\n')           
               while item != 0:
                    for index, valor in enumerate(pm.publicacoes):
                         print('[' + str(index + 1) + '] ' + valor.conteudo[0:50].strip() + '...')
                    print('[0] Voltar')
                         
                    try:
                         item = int(input("\nSelecione uma opção acima.: "))
                    except ValueError:
                         print('\nEscolha uma opção válida!')
                         continue
                    
                    if item <= len(pm.publicacoes) and item >= 0:
                         if item != 0:
                              publicacao = pm.publicacoes[int(item-1)].conteudo
                              metadados = entidades.achar_entidades(publicacao)
                              print('\n' + str(metadados) + '\n')
                              pm.publicacoes[int(item-1)].metadados = metadados
                    else:
                         print('\nEscolha uma opção válida!')
          else:
               print('\nEscolha uma opção válida!')
               
if __name__ == '__main__':
     main()