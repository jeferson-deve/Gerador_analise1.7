<<<<<<< HEAD
# coding=utf-8
__author__ = 'Jeferson de Souza'

from calculos import *
import configparser
import platform
import os
#import random

file_config = 'config/config.ini'
config = configparser.ConfigParser()
config.read([file_config])

#esquema de configuração do programa.. (fase de teste)

HNO3 = float(config.getfloat('concentracao', 'hno3'))
CACO3 = float(config.getfloat('concentracao', 'caco3'))
NO3 = float(config.getfloat('concentracao', 'no3'))

# Fator de correção
SODA = float(config.getfloat('fatorc', 'soda'))
EDTA = float(config.getfloat('fatorc', 'edta'))
HCL = float(config.getfloat('fatorc', 'hcl'))

# Volumes dos tanques
Acido = int(config.getfloat('volume', 'acido'))
Coagulante = int(config.getfloat('volume', 'coagulante'))
Composto = int(config.getfloat('volume', 'composto'))
Talco = int(config.getfloat('volume', 'talco'))

file_name = 'Calculos.txt'

def limpar_tela():
    sytema = platform.system()
    if sytema == 'Windows':
        os.system('cls')
    if sytema == 'Linux':
        os.system('clear')




def salvar(file):
    try:
        with open(file, 'w') as file:
            config.write(file)
        return 'salvo..'
    except:
        return 'falha'

=======
__author__ = 'Jeferson de Souza'

from calculos import *
import random

HNO3 = 58.3
CACO3 = 99.9
NO3 = 65.8

# Fator de corre????????????????o
SODA = 1.0751
EDTA = 0.8
HCL = 0.9756

# Volumes dos tanques
Acido = 2900
Coagulante = 3900
Composto = 0
Talco = 2000
file_name = 'Calculos.txt'

>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

def calculo_solucao(nome, arquivar_op=0):
    print('Calculo solido %s' % nome)
    parametro_up = float(input('Valor minimo: '))
    parametro_dow = float(input('Valor maximo: '))
    quantidade = int(input('Quantos calculos gostaria: '))

    if arquivar_op == 1:
        file_tes = open(file_name, 'a+')
        print('\n\n Calculo solido %s' % nome, file=file_tes)
        for i in range(quantidade):
            placa1_a = sort_num(66.001, 101.992)
            placa1_b = sort_num(66.001, 101.992)

<<<<<<< HEAD
            amostra_a = sort_num(1.500, 1.999)
            amostra_b = sort_num(1.500, 1.999)
=======
            amostra_a = sort_num(1.500, 2.500)
            amostra_b = sort_num(1.500, 2.500)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

            resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
            resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

            placa3a = find_c(resultado_a, amostra_a, placa1_a)
            placa3b = find_c(resultado_b, amostra_b, placa1_b)

            print('|%.3f' % placa1_a, '\t', '%.3f|' % placa1_b, file=file_tes)
            print('|%.3f' % amostra_a, '\t\t', '%.3f|' % amostra_b, file=file_tes)
            print('|%.3f' % placa3a, ' \t', '%.3f|' % placa3b, file=file_tes)
            print('|%.1f' % resultado_a, '\t\t', '%.1f|' % resultado_b, file=file_tes)
            print('|\t (%.1f)' % ((resultado_a + resultado_b) / 2), file=file_tes)
            print('---------------------', file=file_tes)
        file_tes.close()
    for i in range(quantidade):
        placa1_a = sort_num(66.001, 101.992)
        placa1_b = sort_num(66.001, 101.992)

<<<<<<< HEAD
        amostra_a = sort_num(1.500, 1.999)
        amostra_b = sort_num(1.500, 1.999)
=======
        amostra_a = sort_num(1.500, 2.500)
        amostra_b = sort_num(1.500, 2.500)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

        resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
        resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

        placa3a = find_c(resultado_a, amostra_a, placa1_a)
        placa3b = find_c(resultado_b, amostra_b, placa1_b)

        print('|%.3f' % placa1_a, '\t',    '%.3f|' % placa1_b)
        print('|%.3f' % amostra_a, '\t\t', '%.3f|' % amostra_b)
        print('|%.3f' % placa3a, '\t',    '%.3f|' % placa3b)
        print('|%.1f' % resultado_a, '\t\t ',  '%.1f|' % resultado_b)
        print('|%.1f' % ((resultado_a + resultado_b) / 2))
        print('----------------------')


def calculo_nitrato(nome, arquivar_op=0):
<<<<<<< HEAD
    print('\n\n Calculo de concentracão %s' % nome)
=======
    print('\n\n Calculo de concentra????????o %s' % nome)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
    parametro_no3_a = float(input('Valor Minimo: '))
    parametro_no3_b = float(input('Valor Maximo: '))
    quantidade = int(input('Quantos calculos gostaria: '))

    if arquivar_op == 1:
        file_tes = open(file_name, 'a+')
<<<<<<< HEAD
        print('Calculo de concentracão %s' % nome, file=file_tes)
=======
        print('Calculo de concentra????????o %s' % nome, file=file_tes)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

        for i in range(quantidade):
            print('NO3', file=file_tes)
            resultado_no3 = sort_num(parametro_no3_a, parametro_no3_b)  # trocar pelo parametro
            volume_edta = resultado_no3 / EDTA
            print('|%.1f|' % volume_edta, file=file_tes)
            print('|%.1f|' % resultado_no3, file=file_tes)
            print('--------', file=file_tes)
        file_tes.close()

    for i in range(quantidade):
        print('NO3')
        resultado_no3 = sort_num(parametro_no3_a, parametro_no3_b)  # trocar pelo parametro
        volume_edta = resultado_no3 / EDTA
        print('|%.1f|' % volume_edta)
        print('|%.1f|' % resultado_no3)
        print('--------')


def calculo_acido(nome, arquivar=0):
<<<<<<< HEAD
    print('\n\nCalculo concentração de %s' % nome)
=======
    print('\n\nCalculo concentra????ao de %s' % nome)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
    quantidade = int(input('Quantos calculos gostaria: '))

    if arquivar == 1:
        file_tes = open(file_name, 'a+')
<<<<<<< HEAD
        print('Calculo concentracão de %s' % nome, file=file_tes)
        for i in range(quantidade):
            peso = sort_num(3501, 3999)
            volume = reverse_ac(sort_num(1.0, 1.4), sort_num(3500, 3999), SODA)
=======
        print('Calculo concentra????ao de %s' % nome, file=file_tes)
        for i in range(quantidade):
            peso = sort_num(3501, 4000)
            volume = reverse_ac(sort_num(1.0, 1.4), sort_num(3500, 4100), SODA)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            print('|%d|' % peso, file=file_tes)
            print('|%.1f|' % volume, file=file_tes)
            print('|%.1f|' % analise_ac(volume, peso, SODA), file=file_tes)
            print('--------', file=file_tes)
        file_tes.close()

    for i in range(quantidade):
<<<<<<< HEAD
        peso = sort_num(3501, 3999)
        volume = reverse_ac(sort_num(1.0, 1.4), sort_num(3500, 3999), SODA)
=======
        peso = sort_num(3501, 4000)
        volume = reverse_ac(sort_num(1.0, 1.4), sort_num(3500, 4100), SODA)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
        print('|%d|' % peso)
        print('|%.1f|' % volume)
        print('|%.1f|' % analise_ac(volume, peso, SODA))
        print('--------')

def calculo_carbonato(nome, arquivar_op=0):
    print('\n\n Calculo solido %s' % nome)
    parametro_up = float(input('Valor minimo: '))
    parametro_dow = float(input('Valor maximo: '))
    quantidade = int(input('Quantos calculos gostaria: '))

    if arquivar_op == 1:
        file_tes = open(file_name, 'a+')
        print('\n\n Calculo solido %s' % nome, file=file_tes)
        for i in range(quantidade):
<<<<<<< HEAD
            placa1_a = sort_num(0.699, 1.990)
            placa1_b = sort_num(0.699, 1.990)

            amostra_a = sort_num(11.500, 11.999)
            amostra_b = sort_num(11.500, 11.999)
=======
            placa1_a = sort_num(0.099, 2.990)
            placa1_b = sort_num(0.099, 2.990)

            amostra_a = sort_num(12.000, 14.000)
            amostra_b = sort_num(12.000, 14.000)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

            resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
            resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

            placa3a = find_c(resultado_a, amostra_a, placa1_a)
            placa3b = find_c(resultado_b, amostra_b, placa1_b)

            print('|%.3f|' % placa1_a, ' | ', '%.3f|' % placa1_b, file=file_tes)
            print('|%.3f|' % amostra_a, ' | ', '%.3f|' % amostra_b, file=file_tes)
            print('|%.3f|' % placa3a, ' | ', '%.3f|' % placa3b, file=file_tes)
            print('|%.1f|' % resultado_a, ' | ', '%.1f|' % resultado_b, file=file_tes)
            print('|%.1f|' % ((resultado_a + resultado_b) / 2), file=file_tes)
            print('-----------------------', file=file_tes)
        file_tes.close()
    for i in range(quantidade):
<<<<<<< HEAD
        placa1_a = sort_num(0.699, 1.990)
        placa1_b = sort_num(0.699, 1.990)

        amostra_a = sort_num(11.500, 11.999)
        amostra_b = sort_num(11.500, 11.999)
=======
        placa1_a = sort_num(0.099, 2.990)
        placa1_b = sort_num(0.099, 2.990)

        amostra_a = sort_num(12.000, 14.000)
        amostra_b = sort_num(12.000, 14.000)
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba

        resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
        resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

        placa3a = find_c(resultado_a, amostra_a, placa1_a)
        placa3b = find_c(resultado_b, amostra_b, placa1_b)

        print('|%.3f|' % placa1_a, ' |', '%.3f|' % placa1_b)
        print('|%.3f|' % amostra_a, ' |', '%.3f|' % amostra_b)
        print('|%.3f|' % placa3a, ' |', '%.3f|' % placa3b)
        print('|%.1f|' % resultado_a, ' |', '%.1f|' % resultado_b)
        print('|%.1f|' % ((resultado_a + resultado_b) / 2))
        print('-----------------------')


if __name__ == '__main__':
    print('-----------------------------------')
    print('|Gerador de Calculos Ficticios.    |')
<<<<<<< HEAD
    print('|V -  1.7                          |')
=======
    print('|V -  1.0.2                        |')
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
    print('|Desenvolvido por: Jeferson S.     |')
    print('|Email: mp_bra_nco@hotmail.com     |')
    print('-----------------------------------')



    solucao = 1000
    while solucao != 0:
<<<<<<< HEAD

=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
        print('Escolha uma OP: ')
        print('[1] - Ctf-3f')
        print('[2] - Talco')
        print('[3] - Composto')
        print('[4] - Polimero')
        print('[5] - Acido')
        print('[6] - Nitrato')
        print('[7] - Cabonato')
<<<<<<< HEAD
        print('[8] - Editar Configuração') #nova função
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
        print('[0] - SAIR')

        solucao = int(input('Opcao: '))
        if solucao == 0:
            break
<<<<<<< HEAD


=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
        salvar_op = input('Deseja Gerar um txt?  [s/n]: ')
        salvar_op = salvar_op.upper()
        op_num = 0

        if salvar_op == 'S':
            op_num = 1
        elif salvar_op == 'N':
            op_num = 2
        else:
            print('Valor invalido, somento [S =  Sim | N = N??o]')

        if solucao == 1:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'CTF-3F'
            if salvar_op == 'S':
                calculo_solucao(nome, op_num)
            else:
                calculo_solucao(nome, op_num)

        elif solucao == 2:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Talco'
            if salvar_op == 'S':
                calculo_solucao(nome, op_num)
            else:
                calculo_solucao(nome)

        elif solucao == 3:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Composto'
            if salvar_op == 'S':
                calculo_solucao(nome, op_num)
            else:
                calculo_solucao(nome)

        elif solucao == 4:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Polimero'
            if salvar_op == 'S':
                calculo_solucao(nome, op_num)
            else:
                calculo_solucao(nome)

        elif solucao == 5:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Acido'
            if salvar_op == 'S':
                calculo_acido(nome, op_num)
            else:
                calculo_acido(nome)

        elif solucao == 6:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Nitrato'
            if salvar_op == 'S':
                calculo_nitrato(nome, op_num)
            else:
                calculo_nitrato(nome)

        elif solucao == 7:
<<<<<<< HEAD
            limpar_tela()
=======
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba
            nome = 'Carbonato'
            if salvar_op == 'S':
                calculo_carbonato(nome, op_num)
            else:
                calculo_carbonato(nome)

<<<<<<< HEAD
        elif solucao == 8:
            limpar_tela()
            solucao = 100
            print('Editar configurações')

            while solucao != 0:
                limpar_tela()
                print('Escolha uma OP: ')
                print('[1] - Editar concentração')
                print('[2] - Editar Fator de correção')
                print('[3] - Volume dos tanques')
                print('[0] - SAIR')

                solucao = int(input('Opcao: '))
                if solucao == 0:
                    break

                if solucao == 1:
                    print('\nEdito de concentração..\n')
                    sesao = 'concentracao'
                    op1 = 'hno3'
                    op2 = 'caco3'
                    op3 = 'no3'

                    valor_op1 = config.getfloat(sesao, op1)
                    valor_op2 = config.getfloat(sesao, op2)
                    valor_op3 = config.getfloat(sesao, op3)

                    print('\nQual valor quer editar: ')
                    print('[1] - HNO3')
                    print('[2] - CACO3')
                    print('[3] - NO3')
                    valor = int(input('>> '))

                    if valor == 1:
                        novo = float(input('Novo valor HNO3: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(novo))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(valor_op3))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 2:
                        novo = float(input('Novo valor Caco3: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(novo))
                        config.set(sesao, op3, str(valor_op3))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 3:
                        novo = float(input('Novo valor No3: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(novo))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()
                    else:
                        print('Valor invalido.')


                elif solucao == 2:
                    print('\n\nFator de correção\n')
                    sesao = 'fatorc'
                    op1 = 'soda'
                    op2 = 'edta'
                    op3 = 'hcl'

                    valor_op1 = config.getfloat(sesao, op1)
                    valor_op2 = config.getfloat(sesao, op2)
                    valor_op3 = config.getfloat(sesao, op3)

                    print('\nQual valor quer editar: ')
                    print('[1] - SADA')
                    print('[2] - EDTA')
                    print('[3] - HCL')
                    valor = int(input('>> '))

                    if valor == 1:
                        novo = float(input('Novo valor SODA: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(novo))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(valor_op3))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 2:
                        novo = float(input('Novo valor EDTA: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(novo))
                        config.set(sesao, op3, str(valor_op3))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 3:
                        novo = float(input('Novo valor HCL: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(novo))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()
                    else:
                        print('Valor invalido.')


                elif solucao == 3:
                    print('Volume dos tanques')
                    sesao = 'volume'
                    op1 = 'acido'
                    op2 = 'coagulante'
                    op3 = 'composto'
                    op4 = 'talco'

                    valor_op1 = config.getfloat(sesao, op1)
                    valor_op2 = config.getfloat(sesao, op2)
                    valor_op3 = config.getfloat(sesao, op3)
                    valor_op4 = config.getfloat(sesao, op4)

                    print('\nQual valor deseja editar: ')
                    print('[1] - Acido')
                    print('[2] - Coagulante')
                    print('[3] - Composto')
                    print('[3] - Talco')
                    valor = int(input('>> '))

                    if valor == 1:
                        novo = float(input('Novo volume Acido: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(novo))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(valor_op3))
                        config.set(sesao, op4, str(valor_op4))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 2:
                        novo = float(input('Novo volume coagulante: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(novo))
                        config.set(sesao, op3, str(valor_op3))
                        config.set(sesao, op4, str(valor_op4))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 3:
                        novo = float(input('Novo volume composto: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(novo))
                        config.set(sesao, op4, str(valor_op4))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    elif valor == 4:
                        novo = float(input('Novo volume talco: '))

                        #apaga toda seção
                        config.remove_section(sesao)
                        config.add_section(sesao)

                        #rafaz toda a seção
                        config.set(sesao, op1, str(valor_op1))
                        config.set(sesao, op2, str(valor_op2))
                        config.set(sesao, op3, str(valor_op3))
                        config.set(sesao, op4, str(novo))
                        salvar(file_config)
                        print('Configuração salva com sucesso. \n\n')
                        limpar_tela()

                    else:
                        print('Valor invalido.')



                else:
                    print('Valor Inválido!! \n\n') # fim da função 8



        else:
            print('Valor Inválido!! \n\n')
=======
        else:
            print('Valor Inv??lido!! \n\n')
>>>>>>> 3a28b01cbb82963ba62127399bf55302360e78ba


