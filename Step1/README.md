# Deployment Kubernetes Minimal per Nginx

## Descrizione

Questo esercizio consiste nella creazione di un Deployment Kubernetes minimal che avvia un singolo pod con un container Nginx. L’obiettivo è avere un footprint ridotto al minimo, utile per comprendere la struttura base di un Deployment e come eseguire un’applicazione containerizzata semplice in Kubernetes.

---

## Spiegazione

Il file YAML definisce un Deployment con le seguenti caratteristiche principali:

- **apiVersion: apps/v1**  
  Versione stabile dell’API per la risorsa Deployment.

- **kind: Deployment**  
  Tipo di risorsa Kubernetes utilizzata per gestire ReplicaSet e pod.

- **metadata.name: nginx-minimal**  
  Nome univoco assegnato al Deployment.

- **spec.replicas: 1**  
  Numero di repliche/pod desiderati (in questo caso uno solo per minimizzare le risorse).

- **spec.selector.matchLabels: app: nginx-minimal**  
  Label selector che identifica i pod gestiti dal Deployment.

- **spec.template.metadata.labels: app: nginx-minimal**  
  Etichetta assegnata ai pod creati, deve corrispondere al selector.

- **spec.template.spec.containers**  
  Definisce il container da eseguire all’interno del pod:  
  - `name`: nome interno del container (`nginx`)  
  - `image`: immagine Docker da utilizzare (`nginx:latest`)  
  - `ports`: la porta esposta dal container (porta 80, usata da Nginx)

L’applicazione risultante è un semplice server web Nginx, pronto a rispondere sulle richieste HTTP sulla porta 80.

---

## Conclusione

Questo esercizio mostra come definire un Deployment Kubernetes estremamente semplice ma funzionale. È un ottimo punto di partenza per chi vuole imparare a orchestrare container con Kubernetes, focalizzandosi sugli elementi essenziali: replica, selettori e definizione del pod template.

Puoi estendere questo esempio aggiungendo servizi, ingress, configurazioni di sicurezza, o implementando rollout e strategie di aggiornamento più complesse, ma la base rimane sempre questa struttura semplice e chiara.

---

## Comandi utili

Per applicare il Deployment:

```bash
kubectl apply -f nginx-minimal.yaml
```
## Per controllare lo stato:
```bash
kubectl get pods
kubectl describe deployment nginx-minimal
```
---
## Per accedere a Nginx in locale:
```bash
kubectl port-forward deployment/nginx-minimal 8080:80
```
Poi visita http://localhost:8080 nel browser.

