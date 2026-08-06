# Chapa Site

Site pra encontrar "chapas" (fretes/carretos), com busca por nome, cidade ou estado.

## Rodando localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # pra acessar /admin/
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/`.

## Deploy no Railway (domínio: cegonheiros.online)

### 1. Subir pro GitHub
```bash
git init
git add .
git commit -m "primeiro commit"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/chapa-site.git
git push -u origin main
```

### 2. Criar o projeto no Railway
1. railway.app → **New Project** → **Deploy from GitHub repo** → escolhe o repositório
2. **New** → **Database** → **Add PostgreSQL** (o Railway injeta a variável `DATABASE_URL` sozinho)

### 3. Configurar variáveis de ambiente (aba Variables do serviço do app)
| Variável | Valor |
|---|---|
| `SECRET_KEY` | gere uma nova (não use a de exemplo do settings.py) |
| `DEBUG` | `False` |

### 4. Configurar Start Command e migração (aba Settings → Deploy)
Este projeto já tem um `Procfile`, então o Railway deve detectar sozinho. Se não detectar, preencha manualmente:

- **Pre-deploy Command** (ou "Add pre-deploy step"):
  ```
  python manage.py collectstatic --noinput && python manage.py migrate
  ```
- **Custom Start Command**:
  ```
  gunicorn chapa_site.wsgi --bind 0.0.0.0:$PORT
  ```

> ⚠️ Esse é o passo que costuma causar o erro **502 Bad Gateway**: se o Start Command estiver vazio ou com o comando de migração no lugar do comando de start, o app nunca fica escutando a porta.

### 5. Gerar domínio e conectar o seu
1. Settings → Networking → **Generate Domain** (gera algo tipo `xxxx.up.railway.app`, útil pra testar)
2. Settings → Networking → **Custom Domain** → digita `cegonheiros.online`
3. Copia o registro **CNAME** que o Railway mostrar e cadastra no painel DNS de onde você comprou o domínio
4. Repete pra `www.cegonheiros.online` se quiser os dois funcionando

### 6. Criar um usuário admin em produção
No painel do Railway, abre o **Shell** do serviço (ou usa o Console) e roda:
```bash
python manage.py createsuperuser
```
Depois acesse `https://cegonheiros.online/admin/` pra cadastrar os chapas.

## Estrutura do projeto
```
chapa_site/       → configurações do projeto Django (settings, urls, wsgi)
chapas/           → app principal (model Chapa, views, templates)
requirements.txt  → dependências Python
Procfile          → comandos de release (migração) e start (gunicorn)
```
