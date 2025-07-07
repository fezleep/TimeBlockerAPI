project: TimeBlocker API

  description: >
  
    Projeto de estudo em desenvolvimento Back-End com FastAPI. O sistema é uma API de agendamentos
    simples que inclui autenticação com JWT, operações CRUD, documentação automática, e testes.
    O objetivo principal é aplicar na prática conhecimentos essenciais de um desenvolvedor backend,
    com foco em organização de código, segurança e deploy.

about:
  author: Felipe Virginio
  status: Em desenvolvimento
  purpose: >
    Este projeto foi criado exclusivamente com fins educacionais para consolidar meus conhecimentos
    em desenvolvimento de APIs com Python. A ideia é construir uma base sólida para projetos futuros
    mais robustos e profissionais, alinhados com as exigências do mercado de trabalho como desenvolvedor backend.

technologies:
  language: Python 3.11
  backend_framework: FastAPI
  database: SQLite
  dependencies:
    - sqlalchemy
    - pydantic
    - python-jose[cryptography]
    - passlib[bcrypt]
    - email-validator
    - pytest
    - uvicorn
  tools:
    - GitHub Actions (CI/CD)
    - Docker (opcional)
    - Swagger UI

features:
  - Registro e login de usuários
  - Autenticação com JWT
  - CRUD de agendamentos
  - Banco de dados local (SQLite)
  - Testes automatizados com Pytest
  - Documentação via Swagger
  - Deploy gratuito (em breve)

usage:
  requirements:
    - Python 3.11+
    - Git
    - Virtualenv (recomendado)
  instructions:
    - step: Clone o repositório
      command: git clone https://github.com/fezleep/TimeBlockerAPI.git
    - step: Acesse o diretório do projeto
      command: cd TimeBlockerAPI
    - step: Crie e ative o ambiente virtual
      command: |
        python -m venv venv
        venv\Scripts\activate  # Windows
        source venv/bin/activate  # Linux/macOS
    - step: Instale as dependências
      command: pip install -r requirements.txt
    - step: Rode o servidor
      command: uvicorn app.main:app --reload
    - step: Acesse no navegador
      url: http://127.0.0.1:8000/docs

api_endpoints:
  - method: POST
    route: /users/register
    description: Cria um novo usuário
    payload_example:
      email: seu@email.com
      password: senha123
  - method: POST
    route: /users/login
    description: Retorna um token JWT
  - method: POST
    route: /agendamentos/
    description: Cria novo agendamento (provisoriamente com ID de usuário fixo)

testing:
  framework: Pytest
  run: pytest

docker:
  build: docker build -t timeblocker .
  run: docker run -p 8000:8000 timeblocker

roadmap:
  - Proteger rotas com JWT
  - Adicionar exportação de relatórios (PDF)
  - Criar dashboard com resumo por usuário
  - Realizar deploy gratuito no Render

contact:
  name: Felipe Virginio
  linkedin: https://www.linkedin.com/in/fezleep
  github: https://github.com/fezleep

license:
  type: MIT
