![image](https://github.com/user-attachments/assets/f7de91cc-2e54-4b92-9a04-822125281a8a)


# Kafka o canhao do processamento assincrono?

### O que é Apache Kafka?

Apache Kafka é uma plataforma distribuída de streaming de eventos. Ele permite **publicar**, **armazenar** e **consumir** fluxos contínuos de dados em tempo real.

Analogia: pense no Kafka como uma esteira de produção – os dados (eventos) entram, seguem por essa esteira (tópico), e os consumidores pegam o que precisam.

### Conceitos principais

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

