![image](https://github.com/user-attachments/assets/f7de91cc-2e54-4b92-9a04-822125281a8a)


# Kafka o canhao do processamento assincrono?

### O que é mensageria?

Mensageria é um modelo de comunicação assíncrona onde sistemas trocam informações por meio de intermediários, como filas ou tópicos.

Um produtor envia uma **mensagem** com dados necessários para outro sistema executar uma ação. Essa mensagem é colocada em uma fila e lida por um consumidor, geralmente de forma ordenada e direta.

Esse modelo facilita o desacoplamento, melhora a resiliência e permite que os sistemas funcionem de forma independente.

![image](https://github.com/user-attachments/assets/b50dbc6f-e048-4cb6-87c9-d26e74727f09)

### O que são eventos?

Eventos são notificações de que **algo aconteceu** em um sistema. Por exemplo: "pagamento confirmado", "usuário cadastrado", "produto atualizado".

Diferente da mensageria tradicional, os eventos são publicados em **tópicos** e podem ser consumidos por **vários sistemas ao mesmo tempo**.  
O produtor não sabe (nem precisa saber) quem vai consumir o evento, e os consumidores escolhem o que fazer com ele.

![image](https://github.com/user-attachments/assets/f45a86ed-ed1f-41ee-8604-31d83cbd8fa5)


### Diferença fundamental

A **mensagem** é geralmente direcionada de um sistema para outro, com intenção clara e controle da ação — é um modelo **um para um** (1:1). O **evento** é uma notificação genérica, publicada sem destino fixo, e pode ser consumido por múltiplos sistemas — é um modelo **um para muitos** (1:N).

### O que é Apache Kafka?

Apache Kafka é uma plataforma distribuída de streaming de eventos. Ele permite **publicar**, **armazenar** e **consumir** fluxos contínuos de dados em tempo real.

Analogia: pense no Kafka como uma esteira de produção – os dados (eventos) entram, seguem por essa esteira (tópico), e os consumidores pegam o que precisam.

### Conceitos principais
![image](https://github.com/user-attachments/assets/5c56e735-d914-4348-9b84-b2abdb311572)

| Conceito           | Definição                                                                 |
|--------------------|--------------------------------------------------------------------------|
| **Broker**         | Servidor Kafka responsável por armazenar e entregar mensagens.           |
| **Topic**          | Categoria onde as mensagens são publicadas.                              |
| **Partition**      | Subdivisão de um tópico usada para escalar e distribuir mensagens.       |
| **Producer**       | Quem envia mensagens para o Kafka.                                       |
| **Consumer**       | Quem lê mensagens do Kafka.                                              |
| **Consumer Group** | Um grupo de consumidores que divide o trabalho entre as partições.       |

O Kafka funciona como uma central de transporte de eventos. O fluxo básico é o seguinte:

1. Producers enviam mensagens para um tópico.
2. O tópico é dividido em partições, que ficam armazenadas nos brokers.
3. Cada partição mantém a ordem das mensagens.
4. Consumers, organizados em consumer groups, leem as mensagens dessas partições.
5. Dentro de um mesmo group, cada partição é lida por apenas um consumer.

#### Importante: o Kafka **não apaga a mensagem após o consumo**. A retenção é feita com base em tempo ou tamanho.

Internamento o kafka usa uma seria de funcoes para decidir o melhor caminho para um evento/mensagem seguir, por exempl, abaixo temos como um producer decide para qual particao uma mesagem é enviada de acordo com a sua chave.

```text
chave = "cliente_1"
hash("cliente_1") = 83428       # valor gerado pelo algoritmo de hash
número_de_partições = 3

partição = 83428 % 3 = 1

Portanto, a mensagem com chave "cliente_1" será direcionada para a partição 1

### Calculando o módulo manualmente (em calculadora comum):

1. Divida o hash pelo número de partições:
   83428 ÷ 3 = 27809,333...

2. Pegue apenas a parte inteira do resultado:
   27809

3. Multiplique esse valor pelo número de partições:
   27809 × 3 = 83427

4. Subtraia esse valor do hash original:
   83428 - 83427 = 1

Resultado final:
   83428 % 3 = 1
```
## Kafka vs SQS – Principais Diferenças

| Característica              | Apache Kafka                                         | Amazon SQS                                         |
|----------------------------|------------------------------------------------------|---------------------------------------------------|
| Tipo                       | Plataforma de streaming de eventos                   | Fila de mensagens gerenciada                      |
| Entrega                    | Publish-subscribe (vários consumidores)              | Point-to-point (uma mensagem por consumidor)      |
| Persistência               | Armazena mensagens por tempo configurável (ex: 7 dias) | Mensagens expiram após X tempo ou leitura        |
| Ordem                      | Garante ordem por partição                           | Garante ordem apenas na FIFO queue (com custo adicional) |
| Escalabilidade             | Escala horizontal com partições                      | Escala automaticamente, sem controle fino         |
| Retenção                   | Baseada em tempo ou tamanho, mesmo após consumo      | Mensagens são removidas após leitura              |
| Consumer groups            | Divide mensagens entre consumidores                  | Não há equivalente direto a consumer group        |
| Tempo real                 | Projetado para baixa latência                        | Maior latência, adequado para uso geral           |
| Infraestrutura             | Requer gerenciamento de cluster (ou uso de MSK/Confluent Cloud) | Totalmente gerenciado pela AWS           |
| Throughput                 | Muito alto                                           | Alto, mas menor comparado ao Kafka                |

# Hands-on

Neste laboratório, vamos executar o Kafka utilizando Docker com as imagens oficiais da Confluent.  
Depois, vamos rodar dois scripts simples: um para **enviar dados simulados** (producer) e outro para **consumir esses dados** (consumer).

### Etapas

1. Subir o Kafka com Docker
2. Executar o script de envio de mensagens
3. Executar o script de leitura de mensagens

**Comandos uteis:**

Obter o UUID para o cluster:  
```docker run --rm confluentinc/cp-kafka:7.6.1 kafka-storage random-uuid```  
Subir o compose com o kafka:  
```docker-compose up -d```  
Criando o ambiente virtual do python:  
```python3 -m venv .venv```  
Ativando o ambinte virtual:  
```source .venv/bin/activate```  
Intalando as libs:  
```pip install -r requirements.txt```

Referencias:  
https://fidelissauro.dev/mensageria-eventos-streaming/  
https://docs.confluent.io/cloud/current/get-started/index.html  
https://kafka.apache.org/documentation/
