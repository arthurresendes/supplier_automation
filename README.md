# Supplier Automation

Sistema web para automação de abertura de chamados de fornecedores a partir de planilhas, eliminando o preenchimento manual de formulários.

---

## 🔗 Links

| | |
|---|---|
| 🌐 Front-end (Vercel) | https://supplier-automationn.vercel.app |
| 📋 Formulário alvo da automação | https://arthurresendes.github.io/supplier_automation/chamado.html |

> ⚠️ A primeira requisição pode demorar alguns segundos — o servidor no Render entra em modo de hibernação quando inativo.

---

## 🛠️ Stack

<p>
  <img src="https://skillicons.dev/icons?i=py" alt="Python" height="48">
  <img src="https://skillicons.dev/icons?i=fastapi" alt="FastAPI" height="48">
  <img src="https://skillicons.dev/icons?i=react" alt="React" height="48">
  <img src="https://skillicons.dev/icons?i=vite" alt="Vite" height="48">
  <img src="https://skillicons.dev/icons?i=docker" alt="Docker" height="48">
  <img src="https://skillicons.dev/icons?i=html" alt="HTML" height="48">
  <img src="https://skillicons.dev/icons?i=css" alt="CSS" height="48">
</p>

---

## 📋 Formato da Planilha

A planilha enviada deve conter obrigatoriamente as seguintes colunas (com exatamente esses nomes):

| Solicitante | Colaborador | Matricula | Valor |
|---|---|---|---|
| João Silva | Maria Souza | 12345 | 500.00 |

Formatos aceitos: `.xlsx` e `.csv`

---

## 🕐 Histórico de Versões

### v1 — Streamlit (local)

A primeira versão rodava 100% localmente com **Streamlit** como interface e **SQLite** como banco de dados interno.

**Como funcionava:**

1. O usuário subia uma planilha `.xlsx` diretamente na interface Streamlit.
2. A planilha era lida com Pandas e exibida na tela.
3. O usuário selecionava um colaborador no dropdown.
4. Ao clicar em "Executar automação", o Selenium abria o Chrome **visível na máquina** e preenchia o formulário automaticamente.
5. O RITM gerado era capturado e salvo de volta na planilha para download.
6. O registro era gravado em um banco **SQLite local** (`supplier.db`).

**Stack:** Python · Streamlit · Pandas · Selenium (Chrome visível) · SQLite

**Limitações:**
- Rodava apenas na máquina do desenvolvedor — sem possibilidade de deploy
- O Chrome abria de forma visível, travando o computador durante a automação
- Um colaborador processado por vez
- Sem rate limiting ou controle de acesso
- Banco de dados local, sem persistência externa
- Streamlit misturava lógica e interface no mesmo arquivo

---

### v2 — FastAPI + React (atual)

A versão atual separou o projeto em **back-end** e **front-end** independentes, preparados para deploy em nuvem.

**Arquitetura:**

```
┌─────────────────────┐        ┌──────────────────────────┐
│   Front-end (React) │ ──────▶│   Back-end (FastAPI)     │
│   Vite + CSS Modules│        │   Python + Selenium      │
│   Deploy: Vercel    │        │   Deploy: Render (Docker)│
└─────────────────────┘        └──────────────────────────┘
```

**Como funciona:**

1. O usuário acessa a interface React no navegador.
2. Faz upload de uma planilha `.xlsx` ou `.csv`.
3. O front-end envia o arquivo para o endpoint `/api/v1/transform-file`.
4. O back-end valida os campos obrigatórios e retorna os dados como JSON.
5. A tabela é renderizada com um botão **"Abrir chamado"** por linha.
6. Ao clicar, o front-end chama o endpoint `/api/v1/open-desk` com os dados do colaborador.
7. O back-end executa o Selenium em modo **headless** dentro de um container Docker, preenche o formulário e retorna o RITM gerado.
8. O RITM aparece na tela em tempo real.

**O que mudou em relação à v1:**

| Item | v1 — Streamlit | v2 — FastAPI + React |
|---|---|---|
| Interface | Streamlit (local) | React (web) |
| Deploy | Não tinha | Back: Render · Front: Vercel |
| Selenium | Chrome visível | Headless em container Docker |
| Processamento | 1 colaborador por vez | Todos da planilha, linha a linha |
| Rate Limiting | Não tinha | 5 req/min por IP (slowapi) |
| Formatos aceitos | Apenas `.xlsx` | `.xlsx` e `.csv` |
| Banco de dados | SQLite local | Removido — RITM exibido na tela |
| Validação de planilha | Não tinha | Verifica campos obrigatórios (Pydantic) |

---

## 📁 Estrutura do Projeto

```
supplier_automation/
├── Back-end/
│   ├── main.py            # Inicialização FastAPI, CORS, rate limit
│   ├── rotas.py           # Endpoints: /transform-file e /open-desk
│   ├── rpa_selenium.py    # Automação do formulário com Selenium
│   ├── schemas.py         # Schema Pydantic para validação dos dados
│   ├── limitador.py       # Configuração do rate limiter por IP
│   ├── requirements.txt   # Dependências Python com versões fixas
│   └── Dockerfile         # Container com Python + Chromium
│
├── Front-end/front-supplier/
│   ├── src/
│   │   ├── api/
│   │   │   ├── abrirChamado.js     # Chamada ao endpoint /open-desk
│   │   │   └── planilhaConsumo.js  # Chamada ao endpoint /transform-file
│   │   ├── pages/
│   │   │   └── Planilha.jsx        # Página principal com tabela e ações
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
├── Versao_Antiga_Streamlit/
│   ├── main.py            # App Streamlit original
│   ├── banco.py           # Operações no SQLite
│   └── criacao_banco.py   # Criação da tabela CHAMADO
│
├── chamado.html           # Formulário alvo da automação
└── planilha_base.xlsx     # Planilha modelo com os campos necessários
```

---

## 🔌 Endpoints da API

### `GET /`
Health check. Retorna `{ "Message": "Hello World" }`.

### `POST /api/v1/transform-file`
Recebe uma planilha e retorna os dados como JSON.

- **Body:** `multipart/form-data` com o arquivo no campo `file`
- **Retorno:** `{ "Result": [ { "Solicitante": "...", "Colaborador": "...", ... } ] }`
- **Erros:** 400 se o arquivo não for `.xlsx`/`.csv` ou faltar campo obrigatório

### `POST /api/v1/open-desk`
Executa a automação Selenium e abre o chamado.

- **Body:** JSON com `Solicitante`, `Colaborador`, `Matricula`, `Valor`
- **Retorno:** `{ "Success": true, "RITM": "RITM0012345" }`
- **Rate limit:** 5 requisições por minuto por IP

---

## 📬 Contato

<p>
  <a href="https://www.linkedin.com/in/arthur-resende-gomes-3312bb305" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" height="48" width="48" alt="LinkedIn" />
  </a>
</p>
