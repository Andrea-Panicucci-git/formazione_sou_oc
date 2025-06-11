
# Kubernetes Secret Volume Example

## Descrizione

Questo progetto mostra come creare un Secret in Kubernetes e montarlo come volume all'interno di un Pod. Il Pod utilizza un container Alpine che legge i dati del secret da un volume montato in sola lettura.

---
## Scopo
1. Dimostrare la creazione di un Secret Kubernetes con dati sensibili (username e password).
2. Mostrare come montare un Secret come volume all’interno di un Pod.
3. Fornire un esempio base per gestire dati riservati in applicazioni containerizzate.
---
## File inclusi
**1. secret.yml:** definizione del Secret con username e password codificati in base64.
**2. pod.yml:** definizione del Pod che monta il Secret come volume in /etc/secret-data.
---
## Come eseguirlo
1. Applicare il Secret nel cluster:
```bash
    kubectl apply -f secret.yml
```
2. Applicare il Pod che monta il Secret:
```bash
    kubectl apply -f pod.yml
```
---
## Controllare che il Pod sia in esecuzione:
```bash
kubectl get pods
```

Accedere al Pod per verificare i file montati:

```bash
kubectl exec -it secret-vol-pod -- cat /etc/secret-data/username
kubectl exec -it secret-vol-pod -- cat /etc/secret-data/password
```