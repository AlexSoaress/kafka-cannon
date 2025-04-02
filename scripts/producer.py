#!/usr/bin/env python3

from confluent_kafka import Producer
import json
import time
import uuid
import random
import threading
import concurrent.futures
from datetime import datetime, timezone


NUM_THREADS = 10
TOTAL_MESSAGES = 900000
MESSAGES_PER_THREAD = TOTAL_MESSAGES // NUM_THREADS
TOPPIC = 'alex'

conf = {
    'bootstrap.servers': 'localhost:9092',
    'queue.buffering.max.messages': 1000000,
    'batch.num.messages': 10000,
    'linger.ms': 5
}

producer = Producer(conf)
lock = threading.Lock()

def delivery_report(err, msg):
    if err is not None:
        with lock:
            print(f'Erro ao entregar: {err}')

def gerar_transacao():
    return {
        "transaction_id": str(uuid.uuid4()),
        "account_number": f"{random.randint(1000000000, 9999999999)}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "currency": "BRL",
        "type": random.choice(["debit", "credit"]),
        "merchant": {
            "name": random.choice(["Loja do João", "Supermercado XYZ", "Posto BR", "Amazon"]),
            "category": random.choice(["Vestuário", "Alimentação", "Combustível", "E-commerce"])
        },
        "location": {
            "lat": round(random.uniform(-30.0, -10.0), 6),
            "lon": round(random.uniform(-60.0, -30.0), 6)
        },
        "status": random.choice(["completed", "pending", "failed"])
    }

def enviar_transacoes(thread_id, qtd):
    for i in range(qtd):
        transacao = gerar_transacao()
        producer.produce(
            TOPPIC,
            json.dumps(transacao).encode('utf-8'),
            callback=delivery_report
        )
        producer.poll(0)
        if i % 20 == 0:
            with lock:
                print(f"[Thread-{thread_id}] {i} mensagens enviadas...")

print(f"Iniciando envio com {NUM_THREADS} threads e {TOTAL_MESSAGES} mensagens totais...")

inicio = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = []
    for t in range(NUM_THREADS):
        futures.append(executor.submit(enviar_transacoes, t, MESSAGES_PER_THREAD))
    concurrent.futures.wait(futures)

producer.flush()

fim = time.time()
print(f"\nEnvio finalizado: {TOTAL_MESSAGES} mensagens em {fim - inicio:.2f} segundos.")


