import faker
from faker import Faker
import fake
import numpy as np
import pandas as pd
import random
import string
from datetime import datetime, timedelta
import psycopg2
from sqlalchemy import create_engine



fake = Faker('pt-BR')


#print("Tabela Irrigação Intelligente: ")

#ID
def gerar_id(tamanho):
    return ''.join(random.choice(string.digits) for _ in range(tamanho))

ids = []


for _ in range(0,10000):
    ids.append(gerar_id(tamanho=5))

#print(ids)



# Temperatura do ar
temperatura_celsos= []

for x in range(0,10000):
    temperatura_celsos.append(str(fake.random_int(17,35)) + " C°")

#print(temperatura_celsos)
cidade = []

for _  in range(0,10000):
    cidade.append("Limoeiro do Norte")

#print(cidade)

#radiação solar (W/m²)
radiacao_solar = []

for x in range(0,10000):
    radiacao_solar.append(fake.random_int(100,1000,20))


#hora
hora = []

for _ in range(0,10000):  
    hora.append(fake.time())

#print(hora)
#precipitação_clima(milimetros)
precipitacao = []

for _ in range(0,10000):
    vlr_precip = round(random.uniform(0.1, 1.9), 1)
    precipitacao.append(vlr_precip)


#umidade do solo em percentagem
umidade_solo = []

for _ in range(0,10000):
    vlr = random.randint(10, 80)  
    umidade_solo.append(f"{vlr}%")

#temperatura do solo
temperatura_solo= []

for x in range(0,10000):
    temperatura_solo.append(str(fake.random_int(17,24)) + " C°")


#textura do solo
textura_solo = []

# Criar dados fictícios
np.random.seed(42)

# Gerar dados de quantidade de água necessária para irrigação
quantidade_agua_necessaria = np.random.uniform(200, 800, 10000)

# Gerar dados de precipitação (simulando chuva)
precipitacao1 = np.random.uniform(0, 20, 10000)

# Ajustar a quantidade de água necessária com base na precipitação
quantidade_agua_real = np.maximum(quantidade_agua_necessaria - precipitacao, 0)





#print("Temperatura do Ar:", temperatura_celsos[:10])
#print("Radiação Solar:", radiacao_solar[:10])
#print("Hora:", hora[:10])
#print("Precipitação:", precipitacao[:10])
#print("Umidade do Solo:", umidade_solo[:10])
#print("temperatura Solo:", temperatura_solo[:10])




#textura do solo
dados_textura_solo = []

for _ in range(0,10000):
    
    areia = np.random.randint(0, 101)
    silte = np.random.randint(0, 101 - areia)  
    argila = 100 - areia - silte 
    

    dados_textura_solo.append({
        'Areia': f'{areia}%',
        'Silte': f'{silte}%',
        'Argila': f'{argila}%'
    })




#print("textura solo: ",dados_textura_solo[:5])



data_irrigacao = []

# Define a data de início e fim
data_inicio = datetime(2018, 1, 1)
data_fim = datetime(2023, 12, 31)

# Gera datas aleatórias no formato '%d/%m/%y'
for _ in range(10000):  # você pode ajustar o número de datas conforme necessário
    data_aleatoria = data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days))
    data_formatada = data_aleatoria.strftime('%d/%m/%y')
    data_irrigacao.append(data_formatada)

# Exibe algumas das datas aleatórias
#for data in data_irrigacao[:10]:
  #  print(data)
#print("data_irrigacao:", data_irrigacao[:10])




print("***********************************************************************************************************************************")
print("Tabela Solo: ")

#umidade do solo em percentagem

PH_solo = [["ácido"],["neutro"],["alcalino"]]


def escolha(x):
    yield random.choice(x)


def gerar_ph(PH_solo):
    ph_solo1 = list(map(lambda x: next(escolha(x)),
                 (PH_solo for i in range(0, 10000))))
    return ph_solo1


ph = gerar_ph(PH_solo)

#hectares irrigado
hectares_irrig = []

for _  in range(0,10000):
    hectares_irrig.append("7000")



#herosao
herosao = []

for _  in range(0,10000):
    herosao.append("Falso")

#estrutura
estrutura = []

for _  in range(0,10000):
    estrutura.append("Granulacao")

#print("Umidade do Solo:", umidade_solo[:10])
#print("temperatura Solo:", temperatura_solo[:10])
#print("Textura do solo:", dados_textura_solo[:5])
#print("Hectares em KM: ", hectares_irrig)
#print("Herosão: ", herosao)
#print("Estrutura: ", estrutura)


#print("***********************************************************************************************************************************")
#print("Tabela Clima: ")

#velocidade vento em m/s
velocidade_vento = []

for _ in range(0,10000):
    velocidade = round(random.uniform(3.0, 17.9), 1)
    velocidade_vento.append(velocidade)


#print("velocidade vento: ", velocidade_vento )


#radiação solar (W/m²)
radiacao_solar = []

for x in range(0,10000):
    radiacao_solar.append(fake.random_int(100,1000,20))

#print("Radiação solar: ", radiacao_solar)

#precipitação_clima(milimetros)
precipitacao = []

for _ in range(0,10000):
    vlr_precip = round(random.uniform(0.1, 1.9), 1)
    precipitacao.append(vlr_precip)

#print("Precipitação: ", precipitacao)

# Temperatura do clima em celsos
temperatura_clima= []

for x in range(0,10000):
    temperatura_clima.append(str(fake.random_int(17,35)) + " C°")

#print("temperatura: ", temperatura_clima)

#umidade do solo em percentagem
umidade_relat_clima = []

for _ in range(0,10000):
    vlr = random.randint(10, 90)  
    umidade_relat_clima.append(f"{vlr}%")

#print("Temperatura do Ar:", umidade_relat_clima[:10])

#print("***********************************************************************************************************************************")
#print("Tabela Plantacao: ")

#nomes plantacoes
plantacao_nomes12 = ["Milho", "Feijao", "Melancia", "Mamao", "Mamao", "Banana", "Cana-de-Acucar", "Abacaxi"]

# Dicionário de ordens para cada cultura
ordens_culturas = {
    "Milho": "Gramineae",
    "Feijao": "Fabales",
    "Melancia": "Cucurbitales",
    "Mamao": "Caricales",
    "Banana": "Zingiberales",
    "Cana-de-Acucar": "Poales",
    "Abacaxi": "Bromeliales"
}

# String para armazenar as ordens das plantações
ordens = ""

for _ in range(10000):
    cultura = random.choice(plantacao_nomes12)
    ordem = ordens_culturas.get(cultura, "")
    ordens += f"{cultura}: {ordem}\n"


plantacao_nomes13 = ["Milho", "Feijao", "Melancia", "Mamao", "Mamao", "Banana", "Cana-de-Acucar", "Abacaxi"]

# Lista para armazenar os tipos das plantações
tipos = []

for _ in range(10000):
    cultura = random.choice(plantacao_nomes13)
    tipo_cultura = ""

    if cultura == "Milho":
        tipo_cultura = "Cereal"
    elif cultura == "Feijao":
        tipo_cultura = "Leguminosa"
    elif cultura in ("Melancia", "Mamao", "Banana", "Abacaxi"):
        tipo_cultura = "Fruta"
    elif cultura == "Cana-de-Acucar":
        tipo_cultura = "Cereal"

    tipos.append(f"{cultura}: {tipo_cultura}")

# Exemplo de como imprimir os tipos
print(tipos)



plantacao_nomes = [["Milho"],["Feijao"],["Melancia"],["Mamao"],["Mamao"],["Banana"],["Cana-de-Acucar"],["Abacaxi"]]

def escolha(x):
    yield random.choice(x)

def gerar_planta(plantacao_nomes):
    plantas = [next(escolha(x))[0] for x in (plantacao_nomes for i in range(0, 10000))]
    return plantas

pp = gerar_planta(plantacao_nomes)


print(len(ids))
print(len(temperatura_celsos))
print(len(radiacao_solar))
print(len(precipitacao))
print(len(hora))
print(len(data_irrigacao))
print(len(umidade_solo))
print(len(temperatura_solo))
print(len(cidade))
print(len(dados_textura_solo))
print(len(ph)) 
print(len(estrutura))
print(len(herosao))
print(len(velocidade_vento))
print(len(umidade_relat_clima))
print(len(tipos))



#dataframe
df = pd.DataFrame({
    'id':ids,
    'temp_ar':temperatura_celsos,
    'radiacao_solar':radiacao_solar,
    'precipitacao_clima' : precipitacao,
    'qtd_agua_necessaria': np.round(quantidade_agua_necessaria, 1),
    'precipitacao_chuva': np.round(precipitacao1, 1),
    'Qtd_Agua_apos_chuva': np.round(quantidade_agua_real, 1),
    'hora_irrig':hora,
    'data_irrig': data_irrigacao,
    'umidade_solo':umidade_solo,
    'temp_solo':temperatura_solo,
    'cidade': cidade,
    'ph_solo': ph,
    'herosao': herosao,
    'veloc_vento':velocidade_vento,
    'umidade_relativ': umidade_relat_clima,
    'plantacoes_nomes': pp,
    'tipo_plantacao': tipos
   })


df = df.applymap(str)
#df = df.explode()


print(df)


engine = create_engine("postgresql://postgres:Paulo12345@localhost:5432/irrigacao_agua")

connection = engine.connect()

df.to_sql("irrigacao_agua", engine, if_exists = "append", index = False)

engine.dispose


#df.to_csv('irrigacao.csv', index=False)
