#SERVER.PY
import socket
import sys

# Endereço IP servidor
localIp = ""
#Porta do servidor
localPort = int(sys.argv[1])

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (localIp, localPort)
udp.bind(origem)

tabelaInteresses = dict()

while True:
    mensagemRecebida, cliente = udp.recvfrom(1024)
    print(mensagemRecebida, cliente)
    mensagem = bytes.decode(mensagemRecebida)
    if ("+" in mensagem):
        # for i in range(len(mensagem)):
        #     if (mensagem[i] == "+"):
        #         print("teste")
        #         #pegar a tag e guardar na tabela
        # tabelaInteresses.append([cliente, mensagem])
        # print(tabelaInteresses)
        print("Tag adicionada com sucesso")

        if tag in tabelaInteresses:
            tabelaInteresses[tag].add(cliente)
        else:
            tabelaInteresses[tag] = {cliente}


    elif ("-" in mensagem):
        print("Tag retirada com sucesso")
        print(mensagem)
        if tag in tabelaInteresses and cliente in tabelaInteresses[tag]:
            tabelaInteresses[tag].remove(cliente)
    else:
        print('Manda mensagem pra todo mundo')

udp.close()