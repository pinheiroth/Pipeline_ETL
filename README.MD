Web Scraping ETL 

Este projeto realiza Web Scraping no Mercado Livre para extrair informações sobre produtos específicos, armazená-las em um banco de dados SQLite3 e enviar notificações no Telegram quando o preço mais baixo for detectado.

📌 Funcionalidades

Extrai dados de produtos do Mercado Livre a cada 10 segundos.

Armazena os dados no banco SQLite3, adicionando uma nova linha de monitoramento a cada ciclo.

Monitora o menor preço e envia notificações para o Telegram caso haja uma redução.

🛠 Tecnologias Utilizadas

Python (linguagem principal)

SQLite3 (banco de dados local)

Requests (para realizar as requisições HTTP)

Telegram Bot API (para envio de notificações)

📦 Requisitos

Certifique-se de instalar todas as dependências antes de rodar o projeto.

pip instal requests

pip install BeautifulSoup

pip install pandas


📜 Arquivo requirements.txt

certifi==2025.1.31
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0

🚀 Como Executar

Configure o seu bot no Telegram

Crie um bot no Telegram usando o @BotFather.

Obtenha o token do bot e o ID do chat onde deseja receber notificações.

Defina essas informações no código como variáveis de ambiente ou diretamente no script.

Execute o script principal

python main.py

📊 Estrutura do Banco de Dados

A tabela monitoramento contém os seguintes campos:

id (INTEGER, PRIMARY KEY)

nome_produto (TEXT)

preco (REAL)

data_extracao (DATETIME)

✨ Contribuições

Sinta-se à vontade para contribuir com melhorias no projeto. Para isso:

Faça um fork do repositório.

Crie uma nova branch (feature-minha-melhoria).

Faça as alterações e submeta um Pull Request.

📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo como desejar.

