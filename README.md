# PYTHON

```shell
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv .venv && curl -sSL https://install.python-poetry.org | python3 -
curl -fsSL https://get.docker.com | bash
PORT=9000 ./devserver.sh 
```

```powershell
py -m venv venv
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\afons\AppData\Roaming\Python\Scripts", "User")
```

# GIT

```shell
git config --global user.name "Alexandre Afonso"
git config --global user.email "contato@alexandreafonso.com.br"
```

# CONTAINERS DOCKER

```shell
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres --name db postgres
docker build -t pmd-app:v0.1 -f Dockerfile .
docker run --rm -p 3000:3000 --name pmd pmd-app:v0.1
ssh root@xxx "docker image prune -a -f"
```

# BANCO DE DADOS


```shell
docker exec -it db pg_dump -U postgres -d postgres --no-owner > /tmp/pmdapp.backup.sql # Backup sem compreensão
cat pmdapp.backup.sql | docker exec -i db psql -U pmdapp -d pmdapp # Restaurando sem compreensão

docker exec -it db pg_dump -U postgres -d postgres -Fc > /tmp/pmdapp.backup.dump # Backup com compreensão
cat pmdapp.backup.dump | docker exec -i db pg_restore -U pmdapp -d pmdapp --no-owner # Restaurando com compreensão
```

```sql
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'pmdapp' AND pid <> pg_backend_pid(); -- Encerra conecões com os servidores
DROP DATABASE pmdapp;
CREATE DATABASE pmdapp OWNER pmdapp;
```

# QDRANT

```shell
docker run -d -p 6333:6333 -p 6334:6334 -e QDRANT__SERVICE__API_KEY=58698e77-373a-4398-8236-114738670958 --name qdrant qdrant/qdrant
```

# AMAZON S3

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST"
        ],
        "AllowedOrigins": [
            "*.github.dev",
            "*.cloudworkstations.dev",
            "http://localhost:3000"
        ],
        "ExposeHeaders": []
    }
]
```

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::s3.n8n.alexandreafonso.com.br/public/*"
        }
    ]
}
```

# POPPLER LIBRARY (pdftotext)

```shell
sudo apt update
sudo apt install poppler-utils -y
```

# ADDONS VSCODE

- Jupter (CTRL+Shift+P peça para selecionar o interpretador; se necessário, irá instalar)
- Python
- Tailwindcss

```json
{"jupyter.interactiveWindow.textEditor.executeSelection": true}
```