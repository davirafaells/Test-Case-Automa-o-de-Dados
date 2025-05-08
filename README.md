# Automação de Processos e Dados

Este projeto consome dados da API JSONPlaceholder, processa informações de usuários e posts, gera relatórios em Excel e PDF, e simula o envio por email.

---

## Funcionalidades

- Obtenção de usuários e posts via API.
- Cálculo da média de caracteres dos posts.
- Geração de relatórios em Excel (automático) e PDF (opcional).
- Simulação de envio do relatório por email.

---

## Requisitos

- Python 3.6 ou superior.
- Bibliotecas necessárias: `requests`, `pandas`, `reportlab`.
  A lista completa está disponível no arquivo `requirements.txt`.

---

## Instalação

Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## Como Usar

### Fluxo de Execução

Para iniciar o programa, execute:

```bash
python main.py
```

O processamento inclui:
- Obtenção de dados de usuários e posts.
- Cálculo das métricas necessárias.
- Geração automática do relatório em Excel na pasta `relatórios/`.

### Menu Interativo

Será exibido um menu no console solicitando a geração do relatório em PDF:

```
Deseja gerar o relatório em PDF também?
1 - Sim
2 - Não
Escolha:
```

- Opção 1: Gera o PDF na mesma pasta dos relatórios.
- Opção 2: Prossegue sem gerar o PDF.

### Simulação de Envio

O caminho do arquivo gerado é enviado a um endpoint fictício. O resultado da simulação é exibido no console.

---

## Exemplo de Saída

```
INFO: Relatório gerado em: relatórios/relatorio (1).xlsx
INFO: Relatório PDF gerado em: relatórios/relatorio (1).pdf
INFO: Simulação de envio realizada com sucesso.
```

---

## Detalhes Técnicos

- Nomenclatura dos arquivos evita sobrescrita (ex.: `relatorio (1).xlsx`, `relatorio (2).xlsx`).
- O conteúdo dos relatórios inclui:
  - ID e nome do usuário.
  - Quantidade de posts.
  - Média de caracteres por post (com duas casas decimais).

---

## Documentação Complementar

Para mais informações sobre o fluxo do projeto, tratamento de erros e decisões de implementação, consulte o arquivo:  
[`DOCUMENTACAO.md`](DOCUMENTACAO.md)
