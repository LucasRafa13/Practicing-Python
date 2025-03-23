# FlaskAuth API

API de autenticação desenvolvida com **Flask** e **MySQL**, ideal para testes e aprendizado.  
Utiliza `podman-compose` (ou `docker-compose`) para orquestração dos containers.

---

## ⚙️ Requisitos

- [Podman](https://podman.io/) ou [Docker](https://www.docker.com/)
- [podman-compose](https://github.com/containers/podman-compose) ou `docker-compose`
- Python 3.x (caso vá rodar a API localmente)

---

## 🚀 Subindo a aplicação


```bash
git clone https://github.com/LucasRafa13/Practicing-Python
cd FlaskAuth
podman-compose up -d


## 🚀 Estrutura

FlaskAuth/
├── models 
├── app.py
├── database.py
├── data/              ← volume com dados do MySQL
├── docker-compose.yml
├── README.md
└── requirements.txt

```