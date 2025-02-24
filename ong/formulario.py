import os
import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="/home/marcelo/programacao/codigo-python/ong/ong.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def menuprincipal():
    os.system("clear")
    print("1 - Inserir Novo Formulario")
    print("2 - Atualizar Formulario")
    print("3 - Deletar Formulario")
    print("4 - Consultar Formulario")
    print("5 - Consultar Formulario por Nome")
    print("6 - Sair")

def menuInserir():
    os.system("clear")
    #          (T_NOME, [N_RG], [N_CPF], T_MAE, [N_CPF-MAE], T_PAI, [N_CPF-PAI])
    vnome=input("Nome: ")
    vrg=input("RG: ")
    vcpf=input("CPF: ")
    vmae=input("Mae: ")
    vcpfmae=input("CPF Mae: ")
    vpai=input("Pai: ")
    vcpfpai=input("CPF Pai: ")

    #vsql= "INSERT INTO tb_pessoa (T_NOME, [N_RG], [N_CPF], T_MAE, [N_CPF-MAE], T_PAI, [N_CPF-PAI]) VALUES('"+vnome+"',(vrg),(vcpf),'"+vmae+"',(vcpfmae),'"+vpai+"',(vcpfpai)"
    vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI) VALUES ('%s', %s, %s, '%s', %s, '%s', %s)" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai)

    modificar(vcon,vsql)

def menuAtualizar():
    os.system("clear")
    vid=input("Digite o ID do registro a ser alterado: ")
    vsql="SELECT * FROM tb_pessoa WHERE N_ID="+vid
    r=consultar(vcon,vsql)
    rnome=r[0][1]
    rrg=r[0][2]
    rcpf=r[0][3]
    rmae=r[0][4]
    rcpfmae=r[0][5]
    rpai=r[0][6]
    rcpfpai=r[0][7]
    vnome=input("Nome: ")
    vrg=input("RG: ")
    vcpf=input("CPF: ")
    vmae=input("Mae: ")
    vcpfmae=input("CPF Mae: ")
    vpai=input("Pai: ")
    vcpfpai=input("CPF Pai: ")
    if(len(vnome)==0): vnome=rnome
    if(len(vrg)==0): vrg=rrg
    if(len(vcpf)==0): vcpf=rcpf
    if(len(vmae)==0): vmae=rmae
    if(len(vcpfmae)==0): vcpfmae=rcpfmae
    if(len(vpai)==0): vpai=rpai
    if(len(vcpfpai)==0): vcpfpai=rcpfpai
    vsql= "UPDATE tb_pessoa SET T_NOME='"+vnome+"',T_RG='"+vrg+"',T_CPF='"+vcpf+"',T_MAE='"+vmae+"',T_CPFMAE='"+vcpfmae+"',T_PAI='"+vpai+"',T_CPFPAI='"+vcpfpai+"' WHERE N_ID="+vid
    modificar(vcon,vsql)

def menuDeletar():
    os.system("clear")
    vid=input("Digite o ID a ser deletado: ")
    vsql="DELETE FROM tb_pessoa WHERE N_ID="+vid
    print(vsql)
    modificar(vcon,vsql)

def menuConsultar():
    vsql="SELECT * FROM tb_pessoa"
    resultado=consultar(vcon,vsql)
    for r in resultado:
        print("ID:{0:_<3} Nome:{1:_<30} RG:{2:_<15} CPF:{3:<11} MAE:{4:<30} CPF-MAE:{5:_<11} PAI:{6:<30} CPF-PAI:{7:_<11}".format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
    r=input("Digite qualquer tecla para continua...")

def menuConsultarNome():
    vnome=input("Digite um nome para pesquisa: ")
    vsql="SELECT * FROM tb_pessoa WHERE T_NOME LIKE '%"+vnome+"%'"
    resultado=consultar(vcon,vsql)
    for r in resultado:
        print("ID:{0:_<3} Nome:{1:_<30} RG:{2:_<15} CPF:{3:<11} MAE:{4:<30} CPF-MAE:{5:_<11} PAI:{6:<30} CPF-PAI:{7:_<11}".format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
    r=input("Digite qualquer tecla para continua...")

def modificar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operacao Realizada com sucesso")

def consultar(conexao,sql):
        c=conexao.cursor()
        c.execute(sql)
        res=c.fetchall()
        return res

opcao=0
vcon=ConexaoBanco()
while opcao != 6:
    menuprincipal()
    opcao=int(input("Digite uma opcao: "))
    if opcao == 1:
        menuInserir()
    elif opcao == 2:
        menuAtualizar()
    elif opcao == 3:
        menuDeletar()
    elif opcao == 4:
        menuConsultar()
    elif opcao == 5:
        menuConsultarNome()
    elif opcao == 6:
        os.system("clear")
        print("Programa finalizado")
    else:
        os.system("clear")
        print("Opcao Invalida")
        os.system("sleep 1")
vcon.close()
