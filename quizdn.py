# -*- coding: utf-8 -*- console
import time



SCORE = 0


lista_de_perguntas = [
       {
       "title": "o L é um...?", # Cabeça da pergunta
       "right_answer": "A", #Aqui é onde coloca a resposta certa da pergunta
       "answers": [ #Lista de perguntas para saber qual resposta
           {
               "value": "A", #Aqui é valor da resposta
               "description": "Detetive" #aqui é onde aparece a opção
           },
           {
               "value": "B",
               "description": "Ajudante"
           },
           {
               "value": "C",
               "description": "Assassino"
           }
       ]
   },
          {
       "title": "O que é um Death Note?",
       "right_answer": "B",
       "answers": [
           {
               "value": "A", 
               "description": "Nome de um Shinigami"
           },
           {
               "value": "B",
               "description": "Um caderno que pode matar pessoas com rosto e nome"
           },
           {
               "value": "C",
               "description": "Nome do anime"
           }
       ]
   },
          {
       "title": "O que é um shinigami?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A", 
               "description": "Deus da morte"
           },
           {
               "value": "B",
               "description": "Sun ji-Woo"
           },
           {
               "value": "C",
               "description": "Um monstro"
           }
       ]
   },
   {
       "title": "Quem pega o primeiro Death Note no anime?", 
       "right_answer": "C", 
       "answers": [ 
           {
               "value": "A", 
               "description": "L" 
           },
           {
               "value": "B",
               "description": "Near"
           },
           {
               "value": "C",
               "description": "Lith"
           }
       ]
   },
   {
       "title": "Qual o outro nome do Light?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "Kira"
           },
           {
               "value": "B",
               "description": "Yagami"
           },
           {
               "value": "C",
               "description": "Kishiba"
           }
       ]
   },
]

"""
   Já com as perguntas feitas, vamos fazer o looping fazer a pergunta
   e colocar para poder ele fazer a conta de pontos.

"""
print("Gosta de Death Note? Então Prove Responda!\n\n")


for pergunta in lista_de_perguntas:
   print("Pergunta) %s \n\n" % pergunta['title'])
   

   for resposta in pergunta['answers']:
       print( "%s) %s\n" % (resposta['value'], resposta['description']) )
       
   
   answer_selected = input("\nResposta: ")
   
   
   if answer_selected.lower() == pergunta['right_answer'].lower(): 
       SCORE += 2 
   else:
       SCORE = SCORE - 1
       

print("Perguntas finalizadas. Sua pontuação é: %s" % SCORE)

time.sleep(15.4)