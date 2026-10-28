# SESSION LOG

Este arquivo mantém o histórico cronológico.  
O `PROJECT_MASTER.md` mantém apenas o estado consolidado atual.

---

## Sessão 001 — 26/10/2026

**Projeto:** Planejamento geral  
**Objetivo:** definir roadmap e estratégia de continuidade.

### Concluído

- Roadmap geral definida.
- Python escolhido como linguagem principal.
- C++ preservado como opção futura para módulos específicos.
- Arquitetura monorepo modular definida.
- Estratégia de reutilização definida.
- Modelo de handoff entre chats criado.

### Próxima tarefa

Executar Fase 0 — Fundação do repositório.

---

## Sessão 002 — 26/10/2026

**Projeto:** Fase 0 — Fundação do repositório  
**Objetivo:** criar a base profissional e publicá-la no GitHub.

### Concluído

- VS Code, Python e Git configurados.
- Repositório Git inicializado na branch `main`.
- Ambiente virtual `.venv` criado.
- Estrutura `src/iagocava_genshin` e `tests` criada.
- `pyproject.toml`, `pytest`, Ruff e `.gitignore` configurados.
- Pacotes `apps`, `core` e `shared` criados.
- Teste inicial do pacote criado e validado.
- Primeiro commit: `4563c5f` — `chore: initialize project foundation`.
- Repositório publicado em `iagocava/iagocava-genshin-dev-suite`.
- Documentação de continuidade adicionada no commit `2d54f24` — `docs: add project roadmap and session tracking`.

### Próxima tarefa

Sincronizar o `PROJECT_MASTER.md` com o estado real da Fase 0 e iniciar o Projeto 1.

---

## Sessão 003 — 27/10/2026

**Projeto:** Sincronização documental / Projeto 1  
**Objetivo:** alinhar a documentação ao estado real do GitHub e preparar o início do Genshin Pull Calculator.

### Concluído

- Publicação no GitHub verificada.
- Branch padrão `main` confirmada.
- Commits `4563c5f` e `2d54f24` verificados.
- Estrutura modular publicada confirmada.
- Fase 0 marcada como concluída no arquivo mestre.
- Próxima tarefa definida para o módulo reutilizável de conversão de recursos em pulls.

### Próxima tarefa

Criar a branch `feature/pull-calculator` e implementar no `core/currency` a conversão de primogemas e Destinos Entrelaçados em pulls, com testes unitários.
