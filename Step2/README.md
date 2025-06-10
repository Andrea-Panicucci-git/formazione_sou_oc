# Gestione CSR e certificati
---
## 1. Creare Root CA self-signed:
```bash
openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt -subj "/CN=MyRootCA"
```
---
## 2. Creare CSR:
### Crea una chiave privata e CSR:
```bash
openssl genrsa -out myapp.key 2048
openssl req -new -key myapp.key -out myapp.csr -subj "/CN=myapp.example.com"
```
---
## 3. Firmare CSR con Root CA:
```bash
openssl x509 -req -in myapp.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out myapp.crt -days 500 -sha256
```