#CLIENT.PY
import select
import socket
import sys

#Funcao de receber mensagem
def RecebeMensagem():
    #recebe por meio do udp
    mensagemRecebida, endereco = udp.recvfrom(502)
    #verifica se nao veio uma mensagem vazia
    if(mensagemRecebida != ""):
        #decodifica a mensagem
        mensagemRecebida=bytes.decode(mensagemRecebida)
        #printa a mensagem pro usuario
        print(mensagemRecebida)
  

#porta do cliente
localPort = int(sys.argv[1])
#IP servidor
serverIp = sys.argv[2]
#Porta servidor
serverPort = int(sys.argv[3])

#Cria o Socket UDP e define o Destino
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = ("127.0.0.1", localPort)
udp.bind(destino)

while True:
    #Cria o select
    readable, writable, exceptional = select.select([udp, sys.stdin], [], [])
    for controlador in readable:
        #se o controlador for um udp, ele esta recebendo a mensagem
        if(controlador == udp):
            #chama a funcao de receber mensagens
            RecebeMensagem()
            continue
        #se o controlador for um stdin, esta recebendo input do usuario
        if(controlador == sys.stdin):
            #le a linha inteira de input do usuario
            mensagem = sys.stdin.readline()
            #essa mensagem é enviada para o servidor
            destino = (serverIp, serverPort)
            udp.sendto(bytes(mensagem,'utf-8'), destino)
            continue            

#fecha a conexao
udp.close()

