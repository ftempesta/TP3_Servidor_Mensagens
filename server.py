#SERVER.PY
import socket
import sys

# Endereço IP servidor
localIp = ""
#Porta do servidor
localPort = int(sys.argv[1])

#Cria a conexao UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (localIp, localPort)
udp.bind(origem)

#cria um dicionario aonde sera uma tabela com tags e seus interessados
tabelaInteresses = dict()

while True:
    #a cada interacao, os enderecos de envio sao resetados
    enderecosPraEnvio = set()
    #recebe a mensagem do cliente
    mensagemRecebida, cliente = udp.recvfrom(1024)
    #decodifica a mensagem
    mensagem = bytes.decode(mensagemRecebida)
    #verifica se a mensagem tem um \n no final e tira ela (acho que sempre entra, mas melhor conferir)
    if(mensagem[-1:] == "\n"):
        mensagem = mensagem[:-1]
    #cria uma lista com todas as palavras separadas por espacos, cada espaco define um novo elemento na lista
    listaPalavras = mensagem.split()
    #percorre por todas as palavras possiveis
    for palavra in listaPalavras:
        #a cada palavra faz uma serie de veririfacoes
        #se a palavra comecar com +, define o novo interesse do usuario pela tag
        if ("+" == palavra[0]):
            #pega a parte depois do +
            tag = palavra[1:]
            #verifica se ja existe uma tag dentro da dicionario de tags
            if tag in tabelaInteresses:
                #se ja existir, adiciona o endereco do usuario na tag
                tabelaInteresses[tag].add(cliente)
            else:
                #se nao existir, usuario passa a ser o primeiro e novo interessado
                tabelaInteresses[tag] = {cliente}
            #cria uma mensagem de sucesso para envio ao usuario, confirmando seu interesse
            msgSucesso = "Tag \""+tag+"\" adicionada a lista de interesse com sucesso"
            #envia para o cliente ativo que tal tag foi adicionada na lista de interesse
            udp.sendto(bytes(msgSucesso,'utf-8'), cliente)
        #caso a palavra comecar com -, remove o interesse do usuario pela tag
        elif ("-" == palavra[0]):
            #pega a parte depois do -
            tag = palavra[1:]
            #verifica se a tag existe e, se existir, verifica se o usuario possui interesse previo pela tag
            if tag in tabelaInteresses and cliente in tabelaInteresses[tag]:
                #caso tudo isso se conclua, remove o interesse
                tabelaInteresses[tag].remove(cliente)
            #cria uma mensagem de sucesso para envio ao usuario, confirmando o seu desinteresse pela tag
            msgSucesso = "Tag \""+tag+"\" removida da lista de interesse com sucesso"
            #envia para o cliente ativo que tal tag foi removida da lista de interesse
            udp.sendto(bytes(msgSucesso,'utf-8'), cliente)
        else:
            #caso nao seja nem + nem -, verifica se eh um #
            if("#" == palavra[0]):
                #pega a palavra depois do #
                tag = palavra[1:]
                #verifica se aquela palavra esta no dicionario
                if tag in tabelaInteresses:
                    #caso esteja, pega todos os interessados
                    interessados = tabelaInteresses[tag]
                    #da uma uniao de enderecos finais a serem enviados (pode ter mais de um # na frase)
                    enderecosPraEnvio = enderecosPraEnvio.union(interessados)

    #ao passar por todas as palavras disponiveis na frase, verifica se ha enderecos para que a mensagem seja enviada
    for endereco in enderecosPraEnvio:
        #caso exista, cria uma mensagem final como exemplificado: "Usuario:mensagem"
        mensagemFinal = str(cliente) +":"+ mensagem
        #envia para o endereco atual do loop
        udp.sendto(bytes(mensagemFinal,'utf-8'), endereco)

#fecha a conexao
udp.close()