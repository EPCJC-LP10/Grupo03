# -*- coding: utf-8 -*-

import menu
import ingredientes
import util


# nome dos ficheiros
fxIngrediente = "ingredientes.dat"
fxRefeicao = "refeicao.dat"
fxingre_refeicao= "refeicao_ingredientes.dat"


def ler_ficheiros():
	# adicionar todos ficheiros a ler
	ingredientes.listaIngrediente = util.ler_ficheiro(fxIngrediente)
 #    alunos.listaAlunos = util.ler_ficheiro(fxRefeicoes)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxIngrediente, ingredientes.listaIngrediente)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        ingredientes.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


