# Kafka Producer & Consumer in Python

Questo progetto contiene un semplice esempio di utilizzo di Apache Kafka in Python tramite la libreria `kafka-python`.

---

## Struttura del progetto

- `producer.py`: script che produce e invia messaggi al topic Kafka.
- `consumer.py`: script che consuma e stampa i messaggi dal topic Kafka.

---

## Requisiti

- Apache Kafka in esecuzione su `localhost:9092`
- Python 3.x
- Libreria Python `kafka-python`

Puoi installare la libreria con:

```bash
pip install kafka-python
```
## Come eseguire

Assicurati che Kafka sia in esecuzione su localhost:9092.

### Avvia il consumer:

```bash
python consumer.py
```

### Avvia il producer:

```bash
python producer.py
```
![Invio messaggi](Screenshot%202025-06-13%20alle%2017.00.11.png)

*Vedrai i messaggi prodotti comparire in output sul consumer.*


**Calcolare il lag tra i messaggi prodotti e quelli consumati**
```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

![Diagramma del flusso Kafka](Screenshot%202025-06-13%20alle%2015.22.50.png)

### Verifica dello stato del Consumer Group (LAG)

- **LAG = 0**: significa che il consumer ha letto tutti i messaggi disponibili nel topic, quindi è completamente aggiornato.
- **LAG > 0**: ci sono messaggi non ancora letti dal consumer; potrebbe indicare un ritardo o un problema.
