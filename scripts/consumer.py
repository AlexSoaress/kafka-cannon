#!/usr/bin/env python3

from confluent_kafka import Consumer
import time

TOPPIC = 'topic_56'

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'benchmark-consumer-group-v2', 
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

consumer = Consumer(conf)
consumer.subscribe([TOPPIC])

print("▶️ Iniciando benchmark do consumo...")

message_count = 0
start_time = time.time()

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            break
        if msg.error():
            print(f"Erro: {msg.error()}")
            continue
        message_count += 1
        print(f"[{message_count}] {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass
finally:
    end_time = time.time()
    consumer.close()
    duration = end_time - start_time
    print(f"\n✅ Leitura finalizada: {message_count} mensagens em {duration:.2f} segundos.")
    if duration > 0:
        print(f"📊 Taxa média de consumo: {message_count / duration:.2f} msgs/seg")
