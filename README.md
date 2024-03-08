# datarunner

Este é um projeto para desenvolvimento de um sistema web que permite aos usuários registrarem seus treinos de corrida e receberem ajustes personalizados com base nos dados informados.

## Tecnologias Utilizadas

- Frontend: React
- API: Django Rest Framework
- Banco de Dados: PostgreSQL

## Funcionalidades

- Cadastro de Usuários: Os usuários podem se cadastrar no sistema.
- Registro de Treinos: Os usuários podem registrar seus treinos de corrida, informando dados como distância percorrida, tempo, velocidade média, entre outros.
- Ajustes de Treinos: Com base nos dados informados pelos usuários, a API realizará ajustes nos treinos, fornecendo recomendações personalizadas para melhorar o desempenho.
- Histórico de Treinos: Os usuários podem visualizar o histórico de seus treinos registrados.
- Estatísticas: O sistema fornecerá estatísticas sobre os treinos, como distância total percorrida, tempo médio, velocidade média, entre outros.

## Como Usar

1. Clone o repositório.
2. Instale as dependências do frontend:

```bash
   npm install
```

    Instale as dependências do backend (certifique-se de ter o Python e o pip instalados):

```bash
    pip install -r requirements.txt
```

Configure o banco de dados PostgreSQL e atualize as configurações no arquivo settings.py do Django.
Execute as migrações do banco de dados:

```bash
    python manage.py migrate
```

Inicie o servidor Django:

```bash
    python manage.py runserver
```

Inicie o servidor do frontend:
```bash
    npm start
```

Acesse o sistema em http://localhost:3000.

# Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões e feedbacks.

# Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.