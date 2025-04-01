IMAGEM DO CANHAO E DA MOSCA

### O que é Apache Kafka?

Apache Kafka é uma plataforma distribuída de streaming de eventos. Ele permite **publicar**, **armazenar** e **consumir** fluxos contínuos de dados em tempo real.

Analogia: pense no Kafka como uma esteira de produção – os dados (eventos) entram, seguem por essa esteira (tópico), e os consumidores pegam o que precisam.

### Conceitos principais

| Conceito         | Definição |
|------------------|-----------|
| **Broker**       | Servidor Kafka responsável por armazenar e entregar mensagens. |
| **Topic**        | Categoria onde as mensagens são publicadas. |
| **Partition**    | Subdivisão de um tópico usada para escalar e distribuir mensagens. |
| **Producer**     | Quem envia mensagens para o Kafka. |
| **Consumer**     | Quem lê mensagens do Kafka. |
| **Consumer Group** | Um grupo de consumidores que divide o trabalho entre as partições. |
| **Offset**       | Marcador da posição de leitura de um consumidor dentro de uma partição. |


![image](https://github.com/user-attachments/assets/a2f7e01d-4b9f-4f01-925c-7416f9562f8e)


## Cálculo de partição no Kafka com chave

```text
chave = "cliente_1"
hash("cliente_1") = 83428       # valor gerado pelo algoritmo de hash
número_de_partições = 3

partição = 83428 % 3 = 1

Portanto, a mensagem com chave "cliente_1" será direcionada para a partição 1
```

### Calculando o módulo manualmente (em calculadora comum):

```text
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

