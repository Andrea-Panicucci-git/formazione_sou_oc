# ..
Gestione delle Resource Quotas in Kubernetes
Questo README spiega l'uso delle Resource Quotas in Kubernetes per controllare l'allocazione delle risorse nei namespace.

1. Il Manifest ResourceQuota
Una ResourceQuota è una risorsa a livello di namespace che impone limiti su:

Risorse di Calcolo: CPU (requests.cpu, limits.cpu), Memoria (requests.memory, limits.memory).
Risorse di Storage: Spazio (requests.storage), numero di PVCs (persistentvolumeclaims).
Conteggio Oggetti: Numero di Pods, Services, Deployments, ecc.
Esempio di Manifest (resource-quota-example.yaml)

YAML
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-dev-quota
  namespace: dev-environment # Il namespace a cui si applica
spec:
  hard:
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"
    pods: "20"
    persistentvolumeclaims: "10"
    deployments.apps: "10"
2. Applicazione e Verifica
Per applicare e testare una quota:

1. Crea il Namespace

Bash
kubectl create namespace dev-environment
2. Applica la Quota

Bash
kubectl apply -f resource-quota-example.yaml
Verifica lo stato e l'utilizzo corrente:

Bash
kubectl describe resourcequota team-dev-quota -n dev-environment
3. Testa il Limite

Crea o scala un Deployment nel namespace che superi una delle soglie definite nella quota.

Esempio di Deployment (nginx-test-deployment.yaml):

YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-quota-test
  namespace: dev-environment
spec:
  replicas: 1
  selector:
    matchLabels: { app: nginx-test }
  template:
    metadata: { labels: { app: nginx-test }}
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        resources:
          requests: { cpu: "200m", memory: "256Mi" }
          limits: { cpu: "400m", memory: "512Mi" }
Applica: kubectl apply -f nginx-test-deployment.yaml -n dev-environment

Prova a scalare per superare un limite (es. se pods è 2, scala a 3):

Bash
kubectl scale deployment nginx-quota-test --replicas=3 -n dev-environment
Comportamento Atteso:

Kubernetes rifiuterà la richiesta e mostrerà un errore Forbidden, indicando quale limite della ResourceQuota è stato superato.

Error from server (Forbidden): admission webhook ... ResourceQuota "team-dev-quota" exceeded: ...
Pulizia

Bash
kubectl delete deployment nginx-quota-test -n dev-environment
kubectl delete resourcequota team-dev-quota -n dev-environment
kubectl delete namespace dev-environment # Se non serve più
Le Resource Quotas sono fondamentali per la stabilità e l'equità nell'allocazione delle risorse nei cluster Kubernetes.
