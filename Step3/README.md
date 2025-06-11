
# Progetto Ubuntu SSH Docker Image
Questo repository contiene il Dockerfile e la configurazione necessaria per creare e gestire un'immagine Docker personalizzata basata su Alpine/Ubuntu con un server SSH preconfigurato. La pipeline Jenkins associata automatizza il processo di build, push e esecuzione di questa immagine.

## Contenuto del Repository
**Dockerfile:** 
Il file che definisce l'immagine Docker, inclusa l'installazione di OpenSSH, la creazione di un utente (vagrant), la configurazione di sudo e l'aggiunta di una chiave pubblica SSH per l'accesso.
**Jenkinsfile:** Definisce la pipeline CI/CD che automatizza:
1. La build dell'immagine Docker.
2. Il push dell'immagine a un registry Docker.
3. L'esecuzione di un container dall'immagine appena creata.
4. La pulizia del container dopo l'esecuzione.
**key/id_rsa.pub:**
 La chiave pubblica SSH che viene copiata all'interno dell'immagine per consentire l'accesso basato su chiave all'utente vagrant. Assicurati che questa chiave corrisponda alla chiave privata che utilizzi per connetterti.
## Come Funziona
1. La pipeline Jenkins avvia una build.
2. Il Dockerfile viene utilizzato per creare l'immagine andreapanicucci/my_alpine_ssh con un tag basato sul numero di build Jenkins ($BUILD_NUMBER).
3. L'immagine viene autenticata e caricata nel registry specificato (localhost:5000).
4. Un container viene avviato dall'immagine, mappando la porta 22 del container (SSH) a una porta specificata sull'host (es. 2222).
5. Dopo l'esecuzione, il container viene automaticamente fermato e rimosso per pulire le risorse.
## Accesso al Container via SSH
Una volta che un container è in esecuzione (ad esempio, mappato sulla porta 2222):

```Bash
ssh -p 2222 vagrant@localhost
```
**Nota: Assicurati che la chiave privata SSH corrispondente a key/id_rsa.pub sia presente e caricata nel tuo agente SSH locale.**