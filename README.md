# EVENTEX

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.
3. Ative a virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:albrom5/eventex.git wttd
cd wttd
python -m venv .wttd
.wttd/Scripts/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Define DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para a Heroku.

```console
heroku create minha_instancia
heroku config:set SECRET_KEY=<>
```
