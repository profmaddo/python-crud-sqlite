import sqlite3
from sqlite3 import Error


# importar as libs (sqlite)
# criar o banco de dados
# criar as tabelas
# criar um método para incluir, alterar, deletar um para listar
# CRUD - Create, Retrieve, Update e Delete
# SQL - Create - Insert, Select, Update, Delete

def criarDataBase(dbName):
    print(f'Criando Banco Dados: {dbName}')

    conn = None

    try:
        conn = sqlite3.connect(dbName)
    except Error as e:
        print("Erro ao criar banco de dados: ", e)
    finally:
        if conn:
            conn.close()


def getDbConnection(dbName):
    conn = None
    try:
        conn = sqlite3.connect(dbName)
        print(f'Conectado: {dbName}')
        return conn
    except Error as e:
        print(e)
    return conn


def criarTabela(conn, tblName):
    ponteiro = None
    try:
        ponteiro = conn.cursor()
        ponteiro.execute(tblName)
        print(f'Tabela criada: {tblName}')
    except Error as e:
        print(e)
    finally:
        if ponteiro:
            ponteiro.close()


def listarDados(conn):
    ponteiro = None
    try:
        ponteiro = conn.cursor()
        ponteiro.execute("SELECT * FROM usuario")
        registros = ponteiro.fetchall()
        print("*** LISTANDO DADOS ***")

        for row in registros:
            print(row)


    except Error as e:
        print(e)
    finally:
        if ponteiro:
            ponteiro.close()

## CRUD - Insert

def insertUsuario(conn, usuario):

    queryInsert = ''' INSERT INTO usuario(nome, email, curso) VALUES (?, ?, ?)'''

    ponteiro = None
    try:
        ponteiro = conn.cursor()
        ponteiro.execute(queryInsert, usuario)
        print(f'Registro incluído: {ponteiro.lastrowid}')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if ponteiro:
            ponteiro.close()

## CRUD - Update
def alterarDados(conn, usuario):

    queryAlterar = ''' UPDATE usuario SET nome = ? , email = ? ,  curso = ? WHERE id = ?'''

    ponteiro = None
    try:
        ponteiro = conn.cursor()
        ponteiro.execute(queryAlterar, usuario)
        conn.commit()
        print(f'Registro alterado.')
    except Error as e:
        print(e)
    finally:
        if ponteiro:
            ponteiro.close()

def deletarDados(conn, id):
## CRUD - Delete
    try:
        sql = 'DELETE FROM usuario WHERE id=?'
        ponteiro = conn.cursor()
        ponteiro.execute(sql, (id,))
        conn.commit()
        print(f'Registro excluído: {id}')
    except Error as e:
        print(e)



if __name__ == '__main__':
    dbPath = r"/Users/marcomaddo/python-database/livePython.db"
    queryCriarTabela = '''CREATE TABLE IF NOT EXISTS usuario (id integer PRIMARY KEY, nome, email, curso)'''

    conn = getDbConnection(dbPath)

    # c:\asdasdasd\asdadasd\adasd\sqlitePython.db
    # /asdasdasd/asdadasd/adasd/sqlitePython.db

    # criarDataBase(dbPath)
    ##criarTabela(conn, queryCriarTabela)

    dadosUsuario = ("Maddo II","maddo@teste.com","Python II")
    alterarUsuario = ("Maddo V","maddo@teste.com","Python V",10)

    ##insertUsuario(conn,dadosUsuario)
    ##alterarDados(conn,alterarUsuario)
    deletarDados(conn, 1)
    deletarDados(conn, 5)
    deletarDados(conn, 24)

    listarDados(conn)

