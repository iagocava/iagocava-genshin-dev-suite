# IagoCava Genshin Dev Suite — Arquivo Mestre de Continuidade

**Versão:** 1.1  
**Data-base:** 27/10/2026  
**Finalidade:** este é o arquivo canônico para retomar o projeto em qualquer novo chat, computador ou sessão de desenvolvimento.

---

## 1. COMO USAR ESTE ARQUIVO EM UM NOVO CHAT

Ao iniciar um novo chat, anexe **este arquivo (`PROJECT_MASTER.md`)** e escreva apenas:

> Leia o PROJECT_MASTER.md. Quero continuar do ponto registrado em "ESTADO ATUAL". Considere o código existente como fonte de verdade e não recomece o projeto. Hoje quero trabalhar em: [tarefa].

Se também houver código já desenvolvido, anexe os arquivos relevantes ou informe o link/repositório e o **último commit**.

### Regra de continuidade

Antes de iniciar uma nova tarefa:
1. Ler **ESTADO ATUAL**.
2. Ler **ÚLTIMA SESSÃO**.
3. Verificar o **último commit Git**.
4. Identificar o próximo item ainda não concluído.
5. Reutilizar módulos existentes antes de criar novos.
6. Atualizar este arquivo ao final da sessão.

Este arquivo deve ser tratado como **fonte de verdade de gestão do projeto**.

---

# 2. VISÃO DO PRODUTO

Construir progressivamente um ecossistema de ferramentas para:

- Genshin Impact;
- criação de conteúdo;
- lives;
- Discord;
- análise de contas;
- planejamento de pulls;
- acompanhamento de recursos;
- métricas de lives;
- automação de rotinas do criador.

Objetivo secundário: transformar o projeto em um **portfólio técnico real**, demonstrando:

- Python;
- orientação a objetos;
- APIs REST;
- JSON;
- SQLite;
- testes automatizados;
- análise de dados;
- bots;
- backend;
- frontend;
- Git/GitHub;
- arquitetura modular.

Nome de trabalho do ecossistema:

**IagoCava Genshin Dev Suite**

Produto final planejado:

**IagoCava Creator Control Center**

---

# 3. DECISÃO DE LINGUAGEM E STACK

## Linguagem principal

**Python**

### Motivos

Python será priorizado porque possui excelente ecossistema para:

- APIs HTTP;
- Discord;
- SQLite;
- análise de dados;
- automações;
- dashboards;
- FastAPI;
- Streamlit;
- testes;
- integração posterior com IA e serviços web.

A experiência prévia em **C++** será aproveitada por meio de:

- organização modular;
- tipagem;
- classes;
- enums;
- dataclasses;
- separação entre interface e lógica;
- testes;
- algoritmos;
- estruturas de dados.

## Papel futuro do C++

C++ não será descartado.

Pode ser utilizado futuramente em módulos específicos, por exemplo:

- simulações Monte Carlo de grande volume;
- algoritmos de otimização;
- processamento de dados de alto desempenho;
- biblioteca nativa integrada ao Python com `pybind11`.

**Regra:** não usar C++ apenas por familiaridade quando Python resolver o problema de maneira mais simples e sustentável.

---

# 4. STACK TÉCNICA PLANEJADA

## Base

- Python 3.11+
- VS Code
- Git
- GitHub
- SQLite
- `venv`
- `pip`
- `pytest`
- `ruff`

## Interfaces

### Primeiras versões
- CLI
- Streamlit

### Evolução
- FastAPI
- frontend web dedicado

## Bibliotecas prováveis

- `httpx` ou `requests`
- `pydantic`
- `pandas`
- `streamlit`
- `discord.py`
- `pytest`

Bibliotecas devem ser adicionadas **somente quando necessárias**.

---

# 5. PRINCÍPIO DE ARQUITETURA

O projeto será organizado como **monorepo modular**.

A lógica de negócio não deve ficar presa à interface.

Exemplo:

```text
Interface Streamlit
       |
       v
Aplicação
       |
       v
genshin_core
       |
       +--> pity
       +--> pulls
       +--> currencies
       +--> probability
       +--> persistence
       +--> api_clients
```

Assim, a mesma lógica poderá ser usada por:

- terminal;
- Streamlit;
- Discord;
- FastAPI;
- Creator Control Center.

---

# 6. ESTRUTURA PLANEJADA DO REPOSITÓRIO

```text
iagocava-genshin-dev-suite/
│
├── README.md
├── PROJECT_MASTER.md
├── project_status.json
├── pyproject.toml
├── .gitignore
├── .env.example
│
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   └── session_log.md
│
├── src/
│   └── iagocava_genshin/
│       │
│       ├── core/
│       │   ├── models/
│       │   ├── currency/
│       │   ├── pity/
│       │   ├── probability/
│       │   ├── persistence/
│       │   └── api_clients/
│       │
│       ├── apps/
│       │   ├── pull_calculator/
│       │   ├── savings_tracker/
│       │   ├── uid_analyzer/
│       │   ├── discord_bot/
│       │   ├── live_analytics/
│       │   └── creator_hub/
│       │
│       └── shared/
│           ├── config/
│           ├── logging/
│           └── utils/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── data/
│   └── .gitkeep
│
└── scripts/
```

---

# 7. ROADMAP GERAL

## FASE 0 — Fundação do repositório

**Objetivo:** criar a base reutilizável antes de desenvolver as aplicações.

### Entregas

- [x] Criar repositório Git.
- [x] Criar ambiente virtual.
- [x] Criar estrutura de diretórios.
- [x] Criar `pyproject.toml`.
- [x] Configurar `pytest`.
- [x] Configurar `ruff`.
- [x] Criar `.gitignore`.
- [x] Criar README inicial.
- [x] Criar pacote `core`.
- [x] Fazer primeiro commit.
- [x] Publicar o repositório no GitHub (`iagocava/iagocava-genshin-dev-suite`).

### Definition of Done

A execução:

```bash
pytest
```

deve funcionar sem erros, mesmo que inicialmente existam apenas testes básicos.

---

# 8. PROJETO 1 — GENSHIN PULL CALCULATOR

**Status inicial:** PLANEJADO  
**Prioridade:** 1  
**Objetivo:** calcular recursos, pity e probabilidades de obtenção.

## Funcionalidades V1

- [ ] Entrada de primogemas.
- [ ] Entrada de Destinos Entrelaçados.
- [ ] Conversão para quantidade total de pulls.
- [ ] Registro do pity atual.
- [ ] Registro de garantia.
- [ ] Seleção de objetivo.
- [ ] Cálculo básico de pulls disponíveis.
- [ ] Resultado em CLI.
- [ ] Testes unitários.

## V2

- [ ] Simulação probabilística.
- [ ] Monte Carlo.
- [ ] Probabilidade estimada por objetivo.
- [ ] Streamlit.
- [ ] Gráficos.

## Módulos reutilizáveis esperados

```text
core/currency/
core/pity/
core/probability/
core/models/
```

## Saída esperada

Exemplo:

```text
Primogems: 38.400
Destinos: 27
Total disponível: 267 pulls
Pity atual: 43
Garantido: não
Objetivo: C2
```

---

# 9. PROJETO 2 — TSARITSA SAVINGS TRACKER

**Dependência principal:** Projeto 1.

## Reutilização

Reutilizar:

- conversão de moedas;
- cálculo de pulls;
- modelos de pity;
- probabilidades.

## Novidades

- [ ] SQLite.
- [ ] Histórico de saldo.
- [ ] Metas.
- [ ] Projeção de progresso.
- [ ] Registro por data.
- [ ] Dashboard Streamlit.

## Exemplo

```text
Projeto Tsaritsa
Meta: C2R1
Pulls atuais: 312
Meta estimada: 600
Progresso: 52%
```

---

# 10. PROJETO 3 — GENSHIN UID ANALYZER

**Dependências:** Core compartilhado + persistência.

## Objetivo

Consultar dados públicos de uma conta Genshin por UID por meio de um provedor/API compatível e gerar uma análise de personagens/builds.

## Componentes

- [ ] Cliente HTTP.
- [ ] Modelos de resposta.
- [ ] Parser.
- [ ] Cache.
- [ ] SQLite.
- [ ] Sistema de score.
- [ ] Tratamento de falhas.
- [ ] Interface Streamlit.
- [ ] Testes com respostas simuladas.

## Regra arquitetural

O provedor externo deve ser isolado:

```text
api_clients/
    genshin_provider.py
```

Assim, uma mudança de API não quebra o restante da aplicação.

---

# 11. PROJETO 4 — DISCORD ACCOUNT ANALYSIS BOT

**Dependência principal:** Projeto 3.

## Objetivo

Usar o analisador de UID em um bot para fila de análise durante as lives.

## Funcionalidades

- [ ] `/analisar UID`
- [ ] `/fila`
- [ ] `/proximo`
- [ ] `/remover`
- [ ] `/status`
- [ ] Integração com UID Analyzer.
- [ ] Persistência da fila.
- [ ] Logs.

## Reutilização

O bot **não deve reimplementar** análise de personagens.

Deve chamar o serviço criado no Projeto 3.

---

# 12. PROJETO 5 — TIKTOK LIVE ANALYTICS

## Objetivo

Criar banco histórico das lives e calcular KPIs.

## Dados

- data;
- duração;
- tema;
- viewers;
- pico simultâneo;
- média simultânea;
- seguidores ganhos;
- curtidas;
- comentários;
- compartilhamentos.

## Indicadores

- [ ] Seguidores/hora.
- [ ] Conversão por live.
- [ ] Comparação por tema.
- [ ] Média móvel.
- [ ] Crescimento semanal.
- [ ] Melhor dia.
- [ ] Melhor formato.

## Stack

- Python;
- SQLite;
- pandas;
- Streamlit.

---

# 13. PROJETO 6 — IAGOCAVA CREATOR CONTROL CENTER

**Projeto integrador.**

## Objetivo

Unificar os módulos anteriores.

```text
Creator Control Center
│
├── Genshin
│   ├── Pull Calculator
│   ├── Savings Tracker
│   └── UID Analyzer
│
├── Discord
│   └── Analysis Queue
│
└── Creator Analytics
    └── Live Dashboard
```

## Regra

Este projeto só deve integrar funcionalidades já estáveis.

Não duplicar lógica.

---

# 14. REGRAS DE REUTILIZAÇÃO

Antes de criar qualquer função nova, perguntar:

1. Essa lógica já existe no `core`?
2. Pode virar função genérica?
3. Outro projeto precisará dela?
4. Ela depende de Streamlit/Discord sem necessidade?
5. Pode ser testada independentemente?

### Proibido

Criar duas implementações diferentes para:

- conversão de primogemas;
- pity;
- cálculo de pulls;
- leitura de UID;
- cálculo de score;
- persistência básica.

---

# 15. PADRÃO DE CÓDIGO

## Nomes

Python:

```python
calculate_total_pulls()
current_pity
is_guaranteed
```

Classes:

```python
PullInventory
BannerState
CharacterBuild
```

## Tipagem

Preferir:

```python
def calculate_total_pulls(
    primogems: int,
    intertwined_fates: int
) -> int:
    ...
```

## Funções

Cada função deve possuir uma responsabilidade principal.

## UI

Nunca colocar toda a lógica dentro do arquivo Streamlit.

Errado:

```text
streamlit_app.py
    800 linhas
```

Correto:

```text
streamlit_app.py
    chama serviços

core/
    contém regras
```

---

# 16. TESTES

Todo módulo importante deve possuir testes.

Estrutura:

```text
tests/
    unit/
    integration/
```

Exemplo:

```text
test_currency.py
test_pity.py
test_probability.py
```

Ao concluir uma tarefa:

```bash
pytest
```

deve ser executado.

---

# 17. GIT — REGRA DE CONTINUIDADE

Cada sessão relevante deve terminar, sempre que possível, com um commit.

Formato sugerido:

```text
feat: implement pull currency conversion
fix: correct guaranteed pity calculation
test: add pity unit tests
docs: update project master
refactor: move pull logic to core
```

## Branches

Inicialmente:

```text
main
develop
```

Para tarefas maiores:

```text
feature/pull-calculator
feature/savings-tracker
feature/uid-analyzer
```

Não criar branches demais enquanto o projeto ainda for pequeno.

---

# 18. ESTADO ATUAL

> ESTA SEÇÃO DEVE SER ATUALIZADA EM TODA SESSÃO.

**Projeto atual:** Projeto 1 — Genshin Pull Calculator  
**Etapa:** Início do desenvolvimento funcional  
**Status:** PRONTO PARA IMPLEMENTAÇÃO  
**Branch atual publicada:** `main`  
**Último commit validado antes desta sincronização:** `2d54f24` — `docs: add project roadmap and session tracking`  
**Versão funcional atual:** fundação técnica `0.1.0`; funcionalidades do Pull Calculator ainda não implementadas

### Já concluído

- [x] Definição do roadmap geral.
- [x] Escolha de Python como linguagem principal.
- [x] Definição de arquitetura modular.
- [x] Definição da estratégia de reutilização.
- [x] Instalação e configuração do ambiente Python/VS Code.
- [x] Criação e ativação do ambiente virtual `.venv`.
- [x] Inicialização do Git e branch `main`.
- [x] Criação da estrutura modular `src/iagocava_genshin`.
- [x] Configuração do `pyproject.toml`.
- [x] Configuração e validação de `pytest`.
- [x] Configuração e validação de Ruff.
- [x] Criação do `.gitignore`.
- [x] Criação do pacote `core`.
- [x] Primeiro commit da fundação (`4563c5f`).
- [x] Publicação no GitHub.
- [x] Commit da documentação/roadmap (`2d54f24`).

### Em andamento

- [ ] Iniciar a implementação do Projeto 1 — Genshin Pull Calculator.

### Próxima tarefa exata

**Criar a branch `feature/pull-calculator` e implementar no `core/currency` a conversão reutilizável de primogemas e Destinos Entrelaçados em pulls, acompanhada de testes unitários.**

Regras iniciais a representar no código:

- `160` primogemas = `1` pull;
- `1` Destino Entrelaçado = `1` pull;
- a lógica deve permanecer independente da CLI/Streamlit;
- entradas inválidas ou negativas devem receber tratamento explícito;
- executar `pytest`, `ruff check .` e `ruff format --check .` antes do commit.

### Bloqueios

Nenhum.

---

# 19. ÚLTIMA SESSÃO

**Data:** 27/10/2026

## Objetivo

Sincronizar o arquivo mestre de continuidade com o estado real do repositório publicado no GitHub.

## Concluído

- Repositório `iagocava/iagocava-genshin-dev-suite` confirmado como público.
- Branch padrão `main` confirmada.
- Commit `4563c5f` confirmado como fundação técnica do projeto.
- Commit `2d54f24` confirmado como publicação da documentação e roadmap.
- Estrutura `src/iagocava_genshin/{apps,core,shared}` confirmada.
- Teste inicial `tests/unit/test_package.py` confirmado.
- Fase 0 reclassificada como concluída.
- Próxima etapa definida como implementação funcional do Pull Calculator.

## Arquivos alterados

- `PROJECT_MASTER.md`
- `docs/SESSION_LOG.md`

## Decisões técnicas

- Manter a arquitetura monorepo modular já definida.
- Implementar primeiro a lógica de moedas/pulls no `core`, sem dependência da interface.
- Utilizar uma branch de feature para o primeiro módulo funcional.

## Próxima sessão

Criar `feature/pull-calculator` e implementar a primeira função reutilizável de conversão de recursos em pulls, com testes unitários.

---

# 20. MODELO PARA ATUALIZAR AO FINAL DE CADA SESSÃO

Copiar e preencher:

```text
DATA:
PROJETO:
BRANCH:
COMMIT:

OBJETIVO DA SESSÃO:

CONCLUÍDO:
- 
- 

ARQUIVOS CRIADOS:
- 

ARQUIVOS ALTERADOS:
- 

TESTES EXECUTADOS:
- 

DECISÕES TÉCNICAS:
- 

PROBLEMAS/BLOQUEIOS:
- 

PRÓXIMA TAREFA EXATA:
- 
```

Depois atualizar as seções:

- ESTADO ATUAL;
- ÚLTIMA SESSÃO.

---

# 21. PROMPT DE RETOMADA — CURTO

Usar em um novo chat:

> Leia o arquivo PROJECT_MASTER.md anexado e trate-o como a fonte de verdade do projeto. Não reinicie o desenvolvimento. Identifique o ESTADO ATUAL, a ÚLTIMA SESSÃO e a PRÓXIMA TAREFA EXATA. Vou anexar também os arquivos de código necessários. Continue a implementação preservando a arquitetura, reutilizando o core e atualize o PROJECT_MASTER.md ao final.

---

# 22. PROMPT DE RETOMADA — COM GIT

> Leia o PROJECT_MASTER.md e continue o projeto a partir do estado registrado. O último commit válido é `[HASH]`, na branch `[BRANCH]`. Considere o código desse commit como fonte de verdade. Antes de escrever código novo, verifique quais módulos existentes podem ser reutilizados. Minha tarefa de hoje é: `[TAREFA]`.

---

# 23. POLÍTICA DE MUDANÇAS DE ARQUITETURA

Mudanças importantes devem ser registradas antes de serem esquecidas.

Exemplo:

```text
DEC-001
Data: 26/10/2026
Decisão: Python será a linguagem principal.
Motivo: integração com APIs, Discord, SQLite, dados e interfaces.
Consequência: C++ ficará reservado para módulos de desempenho.
```

Arquiteturas podem evoluir, mas não devem mudar silenciosamente.

---

# 24. CRITÉRIO PARA UM PROJETO SER CONSIDERADO CONCLUÍDO

Um projeto da roadmap só muda para `CONCLUÍDO` quando possuir:

- [ ] funcionalidade principal operacional;
- [ ] código reutilizável separado da UI;
- [ ] testes principais;
- [ ] tratamento mínimo de erros;
- [ ] README atualizado;
- [ ] exemplo de uso;
- [ ] commit estável;
- [ ] status atualizado neste documento.

---

# 25. META DE PORTFÓLIO

Ao final, o repositório deve permitir que um recrutador entenda:

1. qual problema foi resolvido;
2. quais tecnologias foram utilizadas;
3. como a arquitetura evoluiu;
4. quais partes foram reutilizadas;
5. quais testes existem;
6. como executar;
7. quais decisões técnicas foram tomadas;
8. como o projeto se relaciona a um caso real de criação de conteúdo.

O objetivo não é somente "ter código".

O objetivo é demonstrar **engenharia de software aplicada a um problema real**.
