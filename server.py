#Vamos começar a fazer tudo no mesmo arquivo e eu separo depois, ok
#já tá enviando e recebendo???


#SERVER.PY
import socket
import sys

# Endereço IP servidor
localIp = "127.0.0.2"
#Porta do servidor
localPort = int(sys.argv[1])

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (localIp, localPort)
udp.bind(origem)

tabelaInteresses = []

while True:
    mensagemRecebida, cliente = udp.recvfrom(1024)
    print(mensagemRecebida, cliente)
    mensagem = bytes.decode(mensagemRecebida)
    if ("+" in mensagem):
        for i in range(len(mensagem)):
            if (mensagem[i] == "+"):
                #pegar a tag e guardar na tabela
        tabelaInteresses.append([cliente, mensagem])
        print(tabelaInteresses)
    if ("-" in mensagem):
        # for item in tabelaInteresses:
            # if (item[1] ==  )
            print(mensagem)
    if ("#" in mensagem):
        print('ok')
    #eh algo sendo digitado pelo usuario
           # mensagem = sys.stdin.readline()
            #print(mensagem)
            #if(mensagem . contains ("+"))
            #if(mensagem.contains ("-"))
            #if(mensagem.contains("#"))
            #envia pra todo mundo

    #if(mensagem . contains ("+"))
    #if(mensagem.contains ("-"))
    #if(mensagem.contains("#"))
    #envia pra todo mundo

udp.close()