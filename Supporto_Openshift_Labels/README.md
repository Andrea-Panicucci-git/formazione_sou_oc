# Supporto Openshift Labels:

Questo progetto dimostra la creazione di diversi oggetti Kubernetes (Deployment, ReplicaSet, Service, Ingress, DaemonSet) per gestire un'applicazione web basata su nginx, organizzata per ambiente, tipo di app e regione geografica.

---

## Struttura del progetto

- **Deployment**: App nginx in ambiente di sviluppo (`environment=dev`), tipo `web`, regione `EU`
- **Service**: LoadBalancer che espone i pod `app=web` e `environment=dev`
- **ReplicaSet**: Gestite da replicas in Deployment.yml
- **Ingress**: Instrada il traffico HTTP verso il servizio web tramite un dominio personalizzato `nginx-example.local`
- **DaemonSet**: App di logging che gira su tutti i nodi, etichettata `app=logging`

---

## Prerequisiti

- Kubernetes cluster (es. KIND, Minikube, GKE, OpenShift, ecc.)
- kubectl configurato per il cluster
- Ingress controller installato e funzionante nel cluster (es. ingress-nginx)

---

## Istruzioni

### 1. Applicare le risorse Kubernetes e verificare che tutto sia stato creato correttamente

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f replicaset.yaml
kubectl apply -f ingress.yaml
kubectl apply -f daemonset.yaml
```
```bash
kubectl get deployments,services,replicasets,ingress,daemonsets -o wide
```
### 3. Visualizzare i pod dell'app web in ambiente di sviluppo

```bash
kubectl get pods -l app=web,environment=dev
```
### 4. Accesso all'applicazione
Modificare il file /etc/hosts per associare nginx-example.local all'indirizzo IP del cluster o del nodo:
```bash 
127.0.0.1 nginx-example.local
```
### Se usi KIND o Minikube senza IP esterno, esegui il port-forwarding per il servizio LoadBalancer:
```bash
kubectl port-forward svc/webapp-dev-service 8080:80
```
### 5.Accedi all'app tramite browser o curl:
```bash
curl http://nginx-example.local:8080
```
