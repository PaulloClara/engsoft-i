# StuKi®

Projeto referente à disciplina de Engenharia de Software I - IFPI

### Instalar/Usar

`$ git clone https://github.com/PaulloClara/stuki.git ~/.stuki && python3 ~/.stuki/install.py`\
`$ source <arquivo_bash>` ou reinicie o terminal\
`$ stuki`

#### Clonar/Configurar

`$ git clone https://github.com/PaulloClara/stuki.git`\
`$ cd stuki`\
`$ python -m venv .env`\
`$ source .env/bin/activate`\
`$ pip install -r requirements.txt`\
`$ git update-index --assume-unchanged src/store/file/bd.sqlite`

#### Ativar/Desativar Env

`$ source .env/bin/activate`\
`$ deactivate`

#### Rodar App

`$ python -B run.py --dev`

#### Rodar Testes

`$ python -B run.py --test`

#### Gerar execultavel

`$ cxfreeze run.py --target-dir dist`
