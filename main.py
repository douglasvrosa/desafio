from fastapi import FastAPI, Query
from pydantic import BaseModel
import pymysql
import datetime

app = FastAPI()

class ExtenEvent(BaseModel):
    extension: str
    status: str
    
class CreateExtension(BaseModel):
    extension: str
    nm_extension: str
    must_record: bool
    number_transfer: str = None
    was_exported: bool

class UpdateExtension(BaseModel):
    extension: str = None
    nm_extension: str = None
    must_record: bool = None
    number_transfer: str = None
    is_active: bool = None

class Call(BaseModel):
    extension: str = None
    nu_ddd: str = None
    nu_phone: str = None


# Criar uma chamada (call) 
'''Não foi inserida a coluna DT_START pois esta definida no banco como CURRENT_TIMESTAMP'''
@app.post("/v1/insert/call/") 
async def CriarChamada(call: Call):
    sql = "INSERT INTO `call` (extension, nu_ddd, nu_phone) values (%s, %s, %s);"              
    return FuncaoMySQL(sql, (call.extension, call.nu_ddd, call.nu_phone))             

# Atualizar a data que ocorreu o evento da chamada (call), onde não é permitido atualizar dois campos ao mesmo tempo. 
# Os eventos são: dt_start (quando cria uma chamada),dt_answer (quando a chamada é atendida), dt_finish (quando a chamada é finalizada)

# 1) Foi realizado um atendimento, atualizando o DT_ANSWER
@app.put("/v1/update/call/answer/{id_call}") 
async def AtualizarAtendimentoCall(id_call: int):
    sql = "UPDATE `call` SET dt_answer = CURRENT_TIMESTAMP WHERE id_call = %s"
    return FuncaoMySQL(sql, (id_call))             

# 2) Ligação finalizada, atualizando DT_FINISH
@app.put("/v1/update/call/finish/{id_call}") 
async def AtualizarFimCall(id_call: int):
    sql = "UPDATE `call` SET dt_finish = CURRENT_TIMESTAMP WHERE id_call = %s;"
    return FuncaoMySQL(sql, (id_call))             

# Criar eventos do ramal (exten_event). Os status permitidos são: ring, in_call, available
@app.post("/v1/insert/exten_event/") 
async def EventoRamal(extenEvent: ExtenEvent):
    if extenEvent.status == 'ring' or extenEvent.status == 'in_call' or extenEvent.status == 'available':
        sql = "INSERT INTO `exten_event` (extension, status) VALUES (%s, %s);"
        return FuncaoMySQL(sql, (extenEvent.extension, extenEvent.status))
    else:
        return(f'Os status disponiveis para inserção são: ring, in_call e available. O informado foi {extenEvent.status}.')

# Criar um ramal (extension). O único campo que não é obrigatório é number_transfer.
@app.post("/v1/insert/extension/") 
async def CriarRamal(extension: CreateExtension):
    sql = "INSERT INTO `extension` (extension, nm_extension, number_transfer, must_record, was_exported) values (%s, %s, %s, %s, %s);"        
    return FuncaoMySQL(sql, (extension.extension, extension.nm_extension, extension.number_transfer, extension.must_record, extension.was_exported))            

# Atualizar um ramal (extension). Para cada atualização o campo was_exported deve ser setado para 0
@app.put("/v1/update/extension/{id_extension}") 
async def AtualizarRamal(id_extension: int, extension: UpdateExtension):
    sql = "UPDATE `extension` SET \
            extension = IFNULL(%s, extension), \
            nm_extension = IFNULL(%s, nm_extension), \
            is_active = IFNULL(%s, is_active), \
            must_record = IFNULL(%s, must_record), \
            was_exported = 0 WHERE id_extension = %s;"              
    return FuncaoMySQL(sql, (extension.extension, extension.nm_extension, extension.is_active, extension.must_record, id_extension))

# Deletar um ramal (extension)
@app.delete("/v1/delete/extension/{id_extension}") 
async def DeletarRamal(id_extension):
    sql = "DELETE FROM extension WHERE id_extension = %s;"              
    return FuncaoMySQL(sql, (id_extension))            

# Consultar um ramal (extension)
@app.get("/v1/select/extension/{id_extension}") 
def ConsultarRamal(id_extension: int):
    sql = "SELECT `id_extension`,`extension`,`nm_extension`,`is_active`,`must_record`,  `number_transfer`, `was_exported` FROM `extension` WHERE `id_extension`= %s;"
    return FuncaoMySQL(sql, (id_extension))             

# Consultar todas os ramais (extension)
@app.get("/v1/select/extension/") 
def ConsultarTodosRamais():
    sql = "SELECT `id_extension`,`extension`,`nm_extension`,`is_active`,`must_record`,  `number_transfer`, `was_exported` FROM `extension`;"
    return FuncaoMySQL(sql)

# Consultar a duração total de uma chamada (call)
@app.get("/v1/select/call/{id_call}") 
def ConsultarDuracaoChamada(id_call: int):
    sql = "SELECT \
            dt_start, \
            dt_finish, TIMESTAMPDIFF \
            ( \
            HOUR, \
            dt_start + INTERVAL TIMESTAMPDIFF(DAY,  dt_start, dt_finish) DAY, \
            dt_finish \
            ) AS horas, \
            TIMESTAMPDIFF \
            ( \
            MINUTE, \
            dt_start + INTERVAL TIMESTAMPDIFF(HOUR,  dt_start, dt_finish) HOUR, \
            dt_finish \
            ) AS minutos, \
            TIMESTAMPDIFF \
            ( \
            SECOND, \
            dt_start + INTERVAL TIMESTAMPDIFF(MINUTE,  dt_start, dt_finish) MINUTE, \
            dt_finish\
            ) AS segundos from `call` where id_call = %s;"
    return FuncaoMySQL(sql, (id_call))          

# Consultar todas as chamadas (call) de um ramal (extension) em uma data especifica
@app.get("/v1/select/call_extension/") 
def ConsultaChamadasRamalData(extension: str, date: datetime.date = Query(None, description="Inserir data no formato YYYY-MM-DD")):
    startDate = datetime.datetime.combine(date, datetime.time(00, 00, 00))
    finishDate = datetime.datetime.combine(date, datetime.time(23, 59, 59))
    sql = "SELECT `id_call`, `extension`, `nu_ddd`, `nu_phone`, `dt_start`, `dt_answer`, `dt_finish` FROM `call` WHERE extension = %s and dt_start BETWEEN %s and %s;"
    return FuncaoMySQL(sql, (extension, startDate, finishDate))               

# Consultar os eventos (exten_event) de um ramal (extension) em uma data especifica
@app.get("/v1/select/exten_event_extension/") 
def ConsultaEventoRamalData(extension: str, date: datetime.date = Query(None, description="Inserir data no formato YYYY-MM-DD")):
    startDate = datetime.datetime.combine(date, datetime.time(00, 00, 00))
    finishDate = datetime.datetime.combine(date, datetime.time(23, 59, 59))   
    sql = ('SELECT `id_exten_event`, `extension`, `status`, `dt_event` FROM `exten_event` WHERE extension = %s and dt_event BETWEEN %s AND %s;')
    return FuncaoMySQL(sql, (extension, startDate, finishDate)) 

# Função unica para o banco de dados.
def FuncaoMySQL(sql: str, params = None):
    try:
        connection = ConnectMySql()
        with connection.cursor() as cursor:   
            if params:         
                cursor.execute(sql, params)
            else:
                 cursor.execute(sql)        
            result = cursor.fetchall()
            connection.commit()    
    except pymysql.Error as error:
        result = "Ops, aconteceu alguma coisa com a conexão com MySQL! \
            Erro: {}".format(error)
    except Exception as error:
        result = "Ops, algo deu errado!  \
            Erro: {}".format(error)
    finally:
        connection.close()
        return result


# Connect to the database
def ConnectMySql():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='ayty_desafio',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)