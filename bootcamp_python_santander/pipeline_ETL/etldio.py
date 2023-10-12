
import requests
import json
import pandas as pd
import openai

#Extração
arq = pd.read_csv("users_proj.csv")
id_users= arq["userID"].tolist()


sdw = "https://sdw-2023-prd.up.railway.app"
def get_user(id):
    response = requests.get(f"{sdw}/users/{id}")
    return response.json() if response.status_code == 200 else None

users = [user for id in id_users if (user := get_user(id)) is not None]
#print(json.dumps(users, indent=2))

#Transform
#chave openai
openai_key= "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"
openai.api_key = openai_key


def gerenerate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
            "content": "Você é um especialista em markting bancario."},
            {"role": "user", 
            "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimento (maximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = gerenerate_ai_news(user)
    print(news)
    user['news'].append({"icon":"https://sdw-2023-prd.up.railway.app",
                        "description": news})


#load
def update_user(user):
    response = requests.put(f"{sdw}/users/{user['id']}",json=user)
    return True if response.status_code == 200 else False

for user in users:
    sucess = update_user(user)
    print(f"user{user['name']} update? {sucess}")

#aplicar etl em um otro metodo de desafio do dia a dia