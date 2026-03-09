from datetime import datetime

agora = datetime.now()


for i in range(20):
    agora = datetime.now()
    with open('logs.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f' {agora} | Aquivo movido para tal pasta \n')
    