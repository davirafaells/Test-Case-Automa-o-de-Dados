# Documentação Técnica – Automação de Processos e Dados

## 1. Introdução

Este projeto foi desenvolvido como exercício prático para demonstrar habilidades em consumo de APIs, processamento de dados e geração de relatórios automatizados. A aplicação simula um processo comum em rotinas de análise de dados, integrando etapas como coleta de informações, cálculos estatísticos e entrega dos resultados em diferentes formatos.

---

## 2. Funcionamento do Projeto

### 2.1 Coleta de Dados

A aplicação consome dados da API pública JSONPlaceholder:

- **Usuários:** `GET /users`  
  Retorna uma lista de usuários com informações como ID e nome.

- **Posts:** `GET /posts?userId={id}`  
  Coleta os posts de cada usuário, filtrando por seu ID.

### 2.2 Processamento

Para cada usuário, a aplicação calcula:

- Quantidade total de posts.
- Média de caracteres nos campos de texto (`body`) de seus posts.

Os dados são organizados em uma tabela com as seguintes colunas:

- ID do usuário
- Nome do usuário
- Quantidade de posts
- Média de caracteres (duas casas decimais)

### 2.3 Geração de Relatórios

Os resultados processados são exportados como relatórios em dois formatos:

- **Excel:** gerado automaticamente na pasta `relatórios/`.
- **PDF:** opcional, a partir de um menu interativo exibido no console.

O nome dos arquivos é incrementado caso já exista um com o mesmo nome, evitando sobrescrita (ex.: `relatorio (1).xlsx`).

### 2.4 Simulação de Envio

Após gerar os relatórios, a aplicação simula o envio do arquivo para um endpoint fictício (`/send-email`). O caminho do arquivo é exibido no console como parte da simulação.

---

## 3. Tecnologias e Ferramentas

- **Linguagem:** Python 3.11
- **Bibliotecas utilizadas:**
  - `requests`: Requisições HTTP
  - `pandas`: Análise e exportação de dados
  - `reportlab`: Geração de arquivos PDF

### Instalação das dependências

```bash
pip install -r requirements.txt
```

### Execução principal

```bash
python main.py
```

---

## 4. Tratamento de Erros

- **API fora do ar ou lenta:** uso de `timeout` e tratamento com `try/except`.
- **Usuário sem posts:** a média é exibida como 0 e o caso é logado.
- **Conflito de nomes de arquivos:** verificação e incremento automático do nome.

---

## 5. Conclusão

O projeto cumpre todos os requisitos propostos no desafio: consumo de API, cálculos estatísticos simples, geração de relatórios e simulação de envio. As soluções adotadas priorizam clareza, modularidade e robustez para facilitar manutenção e possíveis expansões futuras.

A execução é simples e pode ser adaptada para casos reais com APIs diferentes ou integrações reais com serviços de email.

---