# Port Scanner

## </> O que é? 

A varredura de portas é um método de varredura para determinar quais portas em um dispositivo de rede estão abertas, seja um servidor, um roteador ou uma máquina normal. Um scanner de porta é apenas um script ou programa projetado para sondar um host em busca de portas abertas.

## </> Pra que serve?

Um scanner de porta ajuda a detectar uma violação de segurança potencial, identificando os hosts conectados à sua rede e os serviços em execução, como o protocolo de transferência de arquivos (FTP) e o protocolo de transferência de hipertexto (HTTP).

Para proteger seu ambiente de rede e garantir o funcionamento estável da rede, é crucial rastrear todas as entidades que acessam seus recursos de rede.

## </> Tipos de varreduras de rede usadas

As portas de rede são verificadas usando vários protocolos de varredura de rede para garantir a obtenção de dados precisos sobre o status e os serviços em execução nas portas. As verificações de porta mais comumente usadas são:

> **Ping scans**  

Essas varreduras ICMP varrem todo o bloco de endereço IP, ou um único IP de destino, para verificar se o destino está ativo. Depois de enviar uma solicitação de eco, se o destino enviar uma resposta ICMP, essa varredura determinará que o destino está ativo.

> **TCP scan**  

Esta é uma varredura de porta comumente usada por ferramentas de varredura de porta que realiza um processo de handshake completo com o destino para determinar seu status. O scanner de porta inicialmente envia ao destino uma solicitação de sincronização (SYN). Ao receber o sinalizador SYN, o alvo envia ao scanner uma confirmação (SYN-ACK). O scanner de porta então envia um pacote ACK denotando que recebeu a resposta SYN-ACK do alvo. Com base na resposta recebida, o scanner de porta determina o status das portas de rede.

> **UDP scan**  

Uma varredura UDP tenta encontrar portas abertas em uma rede. É um protocolo sem conexão que funciona enviando um pacote de rede ao destino. Esse pacote de rede geralmente não carrega nenhuma carga, mas pode ser configurado para carregar uma carga aleatória para cada porta. Com base na resposta ICMP recebida de cada destino, o scanner de porta determina o status do destino.
Por que você precisa de um scanner de porta?  

Para proteger seu ambiente de rede e garantir o funcionamento estável da rede, é crucial rastrear todas as entidades que acessam seus recursos de rede.

As portas servem como pontos finais de comunicação em uma rede, e qualquer serviço executado nelas pode facilmente obter acesso a dados confidenciais na máquina de destino. É imperativo monitorar e rastrear todos os serviços em execução  e dispositivos de rede associados.

> **Você sabia?**
> As portas TCP são alvos mais fáceis para hackers e crackers porque utilizam um protocolo orientado a conexão que pode fornecer feedback útil ao invasor. As portas UDP usam um protocolo sem conexão que não fornece necessariamente informações relevantes para um invasor.

## </> Tipos de portas

As portas podem ser categorizadas em três grandes intervalos:

1. Portas conhecidas **(0-1023)**

2. Portas registradas **(1024-49151)**

3. Portas dinâmicas ou privadas **(49152-65535)**