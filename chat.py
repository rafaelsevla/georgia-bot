from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Georgia Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
            'Hi', 'Hello', 'How are you?', 'I am fine, thanks',
            'voce eh linda', 'eu sei sou mae da vitoria']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("User: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Georgia: ', resposta)
    else:
        print('Georgia: Ainda não sei responder esta pergunta')