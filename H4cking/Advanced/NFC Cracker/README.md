# NFC CRACKER

Near Field Communication (NFC) é uma tecnologia de comunicação sem fio de curto alcance que permite a troca de dados entre dispositivos a uma distância de até 10 centímetros. Baseada na tecnologia RFID (Radio-Frequency Identification), o NFC é amplamente utilizado em várias aplicações, como pagamentos móveis, cartões de transporte, controle de acesso e compartilhamento de informações entre dispositivos.

### Principais características do NFC:

1. **Curto alcance**: A comunicação ocorre em distâncias muito curtas, geralmente até 10 cm, o que adiciona uma camada de segurança, já que a proximidade física é necessária para a interação.

2. **Baixa taxa de transferência de dados**: A taxa de transferência de dados do NFC é relativamente baixa em comparação com outras tecnologias de comunicação sem fio, como Wi-Fi ou Bluetooth. Geralmente, varia entre 106 Kbps e 424 Kbps.

3. **Comunicação bidirecional**: O NFC permite a comunicação bidirecional, ou seja, ambos os dispositivos envolvidos podem enviar e receber dados.

4. **Facilidade de uso**: A interação via NFC é geralmente simples e intuitiva. Basta aproximar os dispositivos para que a comunicação seja iniciada.

5. **Compatibilidade com RFID**: O NFC é compatível com as tecnologias de RFID existentes, o que facilita a integração com sistemas e dispositivos já em uso.

### Exemplos de aplicações do NFC:

1. **Pagamentos móveis**: Serviços como Google Pay, Apple Pay e Samsung Pay utilizam NFC para permitir pagamentos rápidos e seguros aproximando o smartphone de um terminal de pagamento compatível.

2. **Cartões de transporte**: Muitas cidades utilizam NFC em seus sistemas de transporte público, permitindo que os passageiros paguem as tarifas apenas aproximando um cartão ou dispositivo móvel dos leitores nas estações ou nos veículos.

3. **Controle de acesso**: Em edifícios comerciais e residenciais, o NFC é usado para controlar o acesso, substituindo chaves físicas por cartões ou smartphones compatíveis.

4. **Compartilhamento de informações**: O NFC facilita a troca de informações, como contatos, fotos e arquivos, entre dispositivos. Um exemplo popular é o Android Beam (descontinuado), que permitia o compartilhamento rápido de conteúdo entre smartphones Android.

5. **Emparelhamento de dispositivos**: O NFC é utilizado para emparelhar dispositivos Bluetooth, como fones de ouvido e alto-falantes, simplificando o processo de conexão.

Em resumo, o NFC é uma tecnologia versátil e segura que melhora a conveniência e a eficiência em diversas áreas do dia a dia, tornando as interações digitais mais simples e rápidas.

### Exemplo de uso do `nfcpy` em Python:

1. **Instalação do nfcpy**:
   Primeiro, você precisa instalar o `nfcpy` usando o pip:

   ```bash
   pip install nfcpy
   ```

2. **Leitura de uma tag NFC**:
   O exemplo abaixo mostra como ler uma tag NFC utilizando `nfcpy`:

   ```python
   import nfc

   def on_connect(tag):
       print("Tag detected!")
       print(tag)
       return True

   clf = nfc.ContactlessFrontend('usb')

   if clf:
       clf.connect(rdwr={'on-connect': on_connect})
       clf.close()
   else:
       print("No NFC device found.")
   ```

   Neste exemplo, a função `on_connect` é chamada quando uma tag NFC é detectada. A função imprime as informações da tag.

3. **Escrita em uma tag NFC**:
   O exemplo abaixo mostra como escrever em uma tag NFC utilizando `nfcpy`:

   ```python
   import nfc
   import ndef

   def on_connect(tag):
       uri_record = ndef.UriRecord('http://example.com')
       tag.ndef.records = [uri_record]
       print("URI record written to the tag")
       return True

   clf = nfc.ContactlessFrontend('usb')

   if clf:
       clf.connect(rdwr={'on-connect': on_connect})
       clf.close()
   else:
       print("No NFC device found.")
   ```

   Neste exemplo, a função `on_connect` cria um registro URI (`ndef.UriRecord`) e o escreve na tag NFC.

### Requisitos de Hardware:

Para usar NFC com Python, você precisará de um leitor/escritor NFC compatível. Muitos dispositivos USB estão disponíveis no mercado, como o ACR122U, que é amplamente suportado pela biblioteca `nfcpy`.

### Dicas:

- Certifique-se de que o seu dispositivo NFC está corretamente instalado e reconhecido pelo sistema operacional.
- Teste o código com diferentes tags NFC para garantir a compatibilidade.
- Explore a documentação do `nfcpy` para mais funcionalidades e exemplos avançados: [Documentação do nfcpy](https://nfcpy.readthedocs.io/).