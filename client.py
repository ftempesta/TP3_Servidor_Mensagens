#abre o servidor = ok
#cliente conecta = ok
#cliente escreve uma mensagme qualquer e envia pro servidor = ok

#servidor le e tem 4 opcoes:
#mensagem enviada pelo cliente é um +, -, #, qualquer
#o serviddor trata a mensagem recebida e caso seja um + ou -, coloca na tabela interna pra saber qual usuario tem qual interesse
#ao retransmitir a mensagem, é verificado pra quem enviar olhando nessa tabela
#caso seja um #, olhe na tabela e envie pra todos q tem interesse
#se for qualquer, envia pra todo mundo
# eu tenho interesse com a # brasil
# mas alguem manda mensagem: "oi gente"
# "oi gente #brasil" <== só pra quem deu +brasil
# "oi gente" < == pra todo mundo

#-------------------------------------------------------------------------------------------------------------------------------------------


#CLIENT.PY
import select
import socket
import sys

def RecebeMensagem():
    mensagemRecebida, endereco = udp.recvfrom(502)
    if(mensagemRecebida != ""):
        mensagemRecebida=bytes.decode(mensagemRecebida)
        print('mensagemRecebido')
  

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

mensagem = "mesagem a ser enviada"
while True:
    readable, writable, exceptional = select.select([udp, sys.stdin], [], [])
    for controlador in readable:
        print(controlador)
        print(readable)

        if(controlador == udp):
            print("Recebendo uma mensagem")
            RecebeMensagem()
            continue
        if(controlador == sys.stdin):
            #envia mensagem pro servidor
            mensagem = sys.stdin.readline()
            #essa mensagem é enviada para o servidorm
            destino = (serverIp, serverPort)
            udp.sendto(bytes(mensagem,'utf-8'), destino)
            continue            

        
udp.close()

