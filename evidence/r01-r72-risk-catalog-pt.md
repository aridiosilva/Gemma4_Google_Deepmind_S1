# Catálogo R01–R72: problemas da plataforma e do ambiente que dificultam o atendimento ao desafio Gemma 4

**Author:** Aridio Silva · Independent Researcher, Brazil · ORCID 0009-0008-2411-6995  
**Preferred citation:** Silva, Aridio  
**Copyright:** © 2026 Aridio Silva  
**Assistência documental:** Claude Code (Claude Opus 5.5), a pedido do autor; sem coautoria.  
**Disponibilidade:** cópia pública para avaliação do paper. A classificação do original é interna. © 2026 Aridio Silva. Sem licença pública atribuída.  
**Created:** 2026-11-06 18:52 · **Last Updated:** 2026-11-06 19:10 (inclusão das ocorrências W01–W25 de [4]) · America/Sao_Paulo (UTC−03:00)  
**Versão anterior preservada:** `docs/historico/2026-11-06-1852-catalogo-R01-R72-antes-ocorrencias-W.md`  
**Status:** REVIEW. Consolidação documental de catálogos existentes; nenhum risco foi reproduzido ou testado nesta consolidação.  
**Status normativo:** não normativo. Não substitui o catálogo canônico R01–R64 [1], não incorpora R65–R72 a ele e não autoriza execução, retry, tarefas adicionais nem ações Kaggle.  

## 1. Finalidade e escopo

Este documento reúne, numa única lista, os 72 riscos registrados pelo projeto que dificultam produzir e avaliar patches no desafio Gemma 4 Developer Agent. Os itens R01–R64 vêm do catálogo do documento de arquitetura [1, §5]. Os itens R65–R72 vêm da análise do fórum oficial feita em 04/11/2026 [2, §4]. A finalidade é servir de referência ao paper da Paper Track, que precisa separar falhas do algoritmo P de falhas do ambiente, da cadeia de inferência e do harness.

Três limites precisam ficar claros desde o início.

Primeiro, nem todo item é defeito da plataforma. O catálogo original reúne restrições da competição, defeitos de bibliotecas, comportamentos do modelo e também riscos de planejamento do próprio projeto, como confiar em estimativas de memória ou em benchmarks gerais. A coluna "Natureza" da seção 3 separa essas origens. Essa classificação é uma interpretação deste documento; ela não existe nas fontes e não foi revisada pelo autor.

Segundo, R65–R72 continuam sendo uma proposta. O catálogo canônico declara, nas suas seções 24 a 26, que não criou R65 e que mantém o total em 64 [1]. A análise do fórum propõe os oito itens novos [2], e documentos posteriores já os citam [3]. A decisão de incorporá-los ao catálogo canônico cabe ao autor. O título da análise do fórum fala em "R65–R74", mas a sua tabela só define R65–R72 [2, §1 e §4]. R73 e R74 não têm conteúdo em nenhum documento localizado, e R75 não aparece no repositório.

Terceiro, as descrições de R01–R64 condensam o texto original; o texto integral está nas linhas indicadas na seção 5. Os defeitos concretos dos recursos da plataforma — wheels, bibliotecas, servidor de inferência e verificador — estão registrados como ocorrências W01–W25 na análise de bugs dos recursos [4] e na seção 26 de [1]. Cada ocorrência W é vinculada a uma ou mais classes R; ela não cria classe nova. A seção 4.11 resume essas ocorrências, e a última coluna da tabela-resumo mostra quais classes R têm ocorrência W registrada. É nessas ocorrências que está a evidência reproduzida dos problemas da plataforma; as classes R descrevem o tipo de risco.

Quarto, R65 e W01 descrevem o mesmo defeito do parser `gemma4` da vLLM 0.19.1. A análise de recursos [4] e a seção 26 de [1] o enquadraram em classes existentes (R06, R20, R22, R27, R35, R37, R44, R48 e R62) e declararam que não havia motivo para R65. A análise do fórum [2], dois dias depois, propôs R65 para o mesmo mecanismo. Este documento mantém as duas leituras visíveis e não escolhe entre elas.

## 2. Siglas das fontes citadas dentro dos itens

As siglas abaixo aparecem nas descrições de R01–R50. A descrição completa de cada fonte, com hashes e limites de leitura, está em [1, §2.1 e §17].

| Sigla | Fonte | Observação |
|---|---|---|
| G1 | Conversa com o Gemini sobre restrições, limitações e erros, PDF de 34 páginas | Material de terceiro; "p. X" é a ordem física das páginas |
| G1-R1, G1-R3 | Trechos da conversa G1 recuperados pelo autor | Continuam sendo respostas do Gemini, não regulamento |
| G2 | `advanced_implementation_risks_safeguards.md` | Guia avançado gerado na mesma conversa |
| G4 | Material de documentação Gemma usado na seção 5.9 de [1] | Origem de R51–R64, com as fontes B2 e B11–B14 |
| A1 | Proposta de arquitetura de 18/10/2026 | Referência histórica |
| U1 | Instruções e relatos do autor no chat de 19/10/2026 | Inclui a falha vivida com links simbólicos |
| O1 | Visão geral e avaliação da competição [5] | Fonte oficial |
| O3 | Anúncio dos modelos 12B, E4B e E2B [6] | Equipe Kaggle e comentários de participantes |
| O4 | Notebook oficial "Getting Started" e dados de entrada [7] | Fonte oficial |
| O5, O5a | Comentários da equipe Kaggle e discussão sobre perda de pensamentos [8], [9] | Confirmações de defeitos e correções anunciadas |

Os itens R65–R72 citam números de tópicos do fórum oficial da competição (por exemplo, 746336). O endereço de cada tópico segue o padrão `https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/<número>`; os tópicos foram lidos em 04/11/2026 conforme [2, §1] e não foram reconsultados nesta consolidação.

## 3. Tabela-resumo

Legenda da coluna "Natureza" (classificação interpretativa deste documento):

- **A** — plataforma e regras do Kaggle: sandbox offline, empacotamento, imagem, fila, quota, prazo e variantes admitidas.
- **B** — framework de agente e submissão: ADK, `adk_submission`, compilador do agente e registro de ferramentas.
- **C** — cadeia de inferência e modelo: vLLM, parser, Gemma 4, pensamento, KV cache e adaptadores.
- **D** — harness, ferramentas e tarefas da competição: sandbox de execução, verificador, prompt gerado e repositórios das tarefas.
- **E** — planejamento e método do projeto. Não é defeito da plataforma; é risco de decisão ou de interpretação do próprio trabalho.

Um item pode ter duas naturezas quando as fontes indicam causa compartilhada.

| ID | Problema | Natureza | Seção de origem | Ocorrências W [4] |
|---|---|---|---|---|
| R01 | Execução sem internet | A | [1] §5.1 | — |
| R02 | Links simbólicos e fronteira de caminhos | A | [1] §5.1 | — |
| R03 | Organização e conteúdo do ZIP | A | [1] §5.1 | — |
| R04 | Diretivas de inclusão e sintaxe YAML | B | [1] §5.1 | — |
| R05 | Registro e disponibilidade das ferramentas | B | [1] §5.1 | — |
| R06 | Schema de ferramentas Python | B | [1] §5.1 | W01, W08, W09, W13 |
| R07 | Subagentes e passagem de controle | B | [1] §5.1 | — |
| R08 | Controle por prompt e controle obrigatório | B | [1] §5.1 | — |
| R09 | Acúmulo de logs e código irrelevante | E | [1] §5.2 | — |
| R10 | Compactação com perda do retorno das ferramentas | B | [1] §5.2 | W06 |
| R11 | Perda de pensamentos entre chamadas | B+C | [1] §5.2 | W02, W06, W14 |
| R12 | Flags que alteram o modo de pensamento | B+C | [1] §5.2 | W02, W06, W14 |
| R13 | Orçamento de pensamento e seed não propagados | B+C | [1] §5.2 | W02, W06, W14 |
| R14 | Limite por resposta confundido com limite por tarefa | E | [1] §5.2 | W06 |
| R15 | Janela útil e margem para a resposta | C | [1] §5.2 | W06 |
| R16 | Busca semântica vazia ou pouco útil | D | [1] §5.3 | W21 |
| R17 | Dados de grafo ausentes ou incompatíveis | D | [1] §5.3 | W21 |
| R18 | Saídas de busca excessivas | D | [1] §5.3 | W21 |
| R19 | Falha de correspondência em edição | C+D | [1] §5.3 | W04 |
| R20 | Codificação duplicada de retornos | B+C | [1] §5.3 | W01, W02, W09, W14, W17 |
| R21 | Quebras de linha e codificação do arquivo | D | [1] §5.3 | — |
| R22 | Repetição e buscas sem progresso | C+E | [1] §5.3 | W01 |
| R23 | Mistura de variantes do modelo | A | [1] §5.4 | — |
| R24 | Seleção do modelo por rótulos de qualidade | E | [1] §5.4 | — |
| R25 | Estimativas de VRAM dos pesos | E | [1] §5.4 | — |
| R26 | LoRA reduzindo o KV cache | C | [1] §5.4 | W10, W19 |
| R27 | Travamentos em prompts longos | C | [1] §5.4 | W01, W10, W11, W12, W19 |
| R28 | Descoberta e identidade de adaptadores | A+C | [1] §5.4 | W19 |
| R29 | Multiplicidade e rank de adaptadores | E | [1] §5.4 | W19 |
| R30 | Paralelismo presumido | E | [1] §5.4 | — |
| R31 | Dependências indisponíveis | A | [1] §5.5 | W03 |
| R32 | Wheels binárias incompatíveis | A | [1] §5.5 | W03, W05, W07, W10, W13, W15, W16, W20 |
| R33 | Divergência de interpretador e ambiente virtual | A | [1] §5.5 | W03, W04, W16, W23, W24 |
| R34 | Vendorização e instalação antes do harness | A | [1] §5.5 | W03, W04 |
| R35 | Mistura de versões da plataforma | A | [1] §5.5 | 20 ocorrências (ver §4.11) |
| R36 | Comandos que excedem o saldo de tempo | A+D | [1] §5.6 | — |
| R37 | Descendentes órfãos e cancelamento incompleto | D | [1] §5.6 | W01, W11, W12, W22, W23, W24 |
| R38 | Limites de sistema e isolamento | D | [1] §5.6 | — |
| R39 | Acúmulo de disco e logs | D | [1] §5.6 | — |
| R40 | Memória do host e da GPU | A+C | [1] §5.6 | — |
| R41 | Limpeza destrutiva | E | [1] §5.7 | — |
| R42 | Patch vazio ou não capturado | D | [1] §5.7 | — |
| R43 | Testes extensos e testes no ambiente errado | D+E | [1] §5.7 | W03 |
| R44 | Aprovação local confundida com resolução oficial | D | [1] §5.7 | W01, W03, W04, W05, W16, W18, W23, W24, W25 |
| R45 | Persistência e desaparecimento da evidência | D | [1] §5.7 | — |
| R46 | Mocks e simulações confundidos com o modelo real | E | [1] §5.7 | — |
| R47 | Fila prolongada e consumo de quota | A | [1] §5.8 | — |
| R48 | Erro opaco e estado divergente da interface | A | [1] §5.8 | W01, W07, W08, W11, W12, W13, W15, W20, W22, W23, W24 |
| R49 | Velocidade local sem paridade com o scorer | A+E | [1] §5.8 | — |
| R50 | Limite global e política de encerramento | A | [1] §5.8 | — |
| R51 | Confundir memória dos pesos com pico de execução | E | [1] §5.9 | — |
| R52 | Inferir memória apenas pelos parâmetros efetivos ou ativos | E | [1] §5.9 | — |
| R53 | Transportar GGUF/Q4_0/mobile para o caminho W4A16-CT | C | [1] §5.9 | — |
| R54 | Misturar templates, tokens ou tokenizers Gemma 3/4 | C | [1] §5.9 | — |
| R55 | Remover contexto necessário dentro de um turno de ferramentas | B | [1] §5.9 | — |
| R56 | Tratar instrução de concisão como timeout ou limite de thinking | E | [1] §5.9 | — |
| R57 | Presumir a existência de ferramenta pelo nome no YAML | B | [1] §5.9 | — |
| R58 | Copiar parâmetros de sampling sem aplicação comprovada | C | [1] §5.9 | — |
| R59 | Produzir LoRA em formato incompatível com o scorer | A | [1] §5.9 | — |
| R60 | Importar pressupostos online/JAX/TPU para o sandbox | A | [1] §5.9 | — |
| R61 | Depender de MTP sem suporte ou ganho demonstrado | C | [1] §5.9 | — |
| R62 | Aceitar resultado de ferramenta com interpretação errada | C+E | [1] §5.9 | W01, W04, W07, W09, W17, W18, W19, W22, W23, W24, W25 |
| R63 | Usar benchmark geral como previsão de resolução das issues | E | [1] §5.9 | — |
| R64 | Usar amostra qualitativa como validação de treinamento | E | [1] §5.9 | — |
| R65 | Parser `gemma4_tool_parser` do vLLM 0.19.1 congela o servidor com array malformado | C | [2] §3.1 e §4 | mesmo mecanismo de W01 |
| R66 | String em aspas JSON chega com as aspas dentro do valor | C | [2] §3.2 e §4 | — |
| R67 | Argumento fechado por crase faz `edit_file` perder `old_string`/`new_string` | C | [2] §3.3 e §4 | — |
| R68 | Reset anti-adulteração dos testes inoperante antes do `test_patch` | D | [2] §3.6 e §4 | — |
| R69 | Testes dependentes da rede mudam de comportamento sem internet | D | [2] §3.8 e §4 | — |
| R70 | Requisitos com skips mutuamente exclusivos tornam a tarefa insolúvel | D | [2] §3.9 e §4 | — |
| R71 | Convenções do verificador reprovam correções válidas | D | [2] §3.10 e §4 | — |
| R72 | Prompt gerado pelo harness induz o modelo ao erro | D | [2] §3.11 e §4 | — |

A contagem de itens por natureza está na seção 6.

## 4. Descrição dos 72 problemas

Em cada item, "Aceite futuro" descreve a evidência que mostraria o risco controlado, caso a execução venha a ser autorizada. Ele não registra testes realizados [1, §5].

### 4.1 Submissão e contratos de integração (R01–R08)

**R01 — Execução sem internet (A).** O sandbox de avaliação não tem rede. Downloads, documentação remota e instalação pela internet não podem ser dependências do agente. Fontes: G1, p. 3-4, 14, 16 e 19; G2, §1; O1. Proposta: usar apenas recursos existentes e acessíveis pelo contrato oficial. Aceite futuro: iniciar, localizar código, editar e finalizar sem chamadas externas.

**R02 — Links simbólicos e fronteira de caminhos (A).** O autor já viveu falhas com symlinks (U1). Um `../` legítimo dentro da árvore precisa ser distinguido de um caminho que escapa da raiz autorizada. Fontes: G1, p. 4, 14, 16 e 19; U1. Proposta: pacote com arquivos reais e referências relativas permitidas, sem depender de links simbólicos. Aceite futuro: caminhos resolvidos permanecem na árvore admitida e compilam no validador oficial.

**R03 — Organização e conteúdo do ZIP (A).** O pacote exige `agent.yaml` na raiz e não deve levar resíduos `.pyc`, `.git` ou temporários. A recomendação "apenas texto/YAML" de G1, p. 30, conflita com o suporte a scripts e adaptadores. Fontes: G1, p. 3, 5, 15 e 30. Proposta: empacotar por lista explícita de arquivos, compatível com a allowlist oficial. Aceite futuro: validação oficial do pacote exato que será enviado.

**R04 — Diretivas de inclusão e sintaxe YAML (B).** Nomes incorretos, indentação e base de resolução dos includes podem impedir a construção do agente. Fontes: G1, p. 6-8, 12-15 e 31. Proposta: mapear cada include ao arquivo de origem e ao destino final dentro do pacote. Aceite futuro: compilação completa a partir de uma extração limpa, sem arquivos externos de apoio.

**R05 — Registro e disponibilidade das ferramentas (B).** Os nomes de ferramentas variam entre exemplos; aparecem inclusive `subgraph_retrieval` e nomes de APIs diferentes. Fontes: G1, p. 4, 7 e 28. Proposta: catálogo único derivado do registro efetivamente oferecido, com nome, argumentos, retorno e disponibilidade. Aceite futuro: nenhuma chamada depende de ferramenta não declarada ou inexistente.

**R06 — Schema de ferramentas Python (B).** O Gemini atribui falhas a parâmetros com valores padrão e a problemas de tipagem, sem reprodução anexada que sustente uma proibição universal. Fontes: G1, p. 13 e 31. Proposta: usar ferramentas oficiais e, se houver extensão admitida, explicitar e validar seu schema. Aceite futuro: argumentos e erros reais são interpretáveis, sem convenções inventadas.

**R07 — Subagentes e passagem de controle (B).** Delegação simples não garante cooperação, isolamento de histórico nem retorno estruturado. Fontes: G1, p. 2, 7, 12-13, 17 e 20. Proposta: uma chamada delimitada ao localizador e um retorno de evidências, sem rede de negociações. Aceite futuro: entrada, saída, retorno ao principal e orçamento compartilhado comprovados no mecanismo oficial.

**R08 — Controle por prompt e controle obrigatório (B).** O compilador examinado não recebia o registro de callbacks, e skills não obrigavam a passagem por uma guarda. Fontes: A1, §2 e §4-5. Proposta: declarar quais limites o harness impõe e quais decisões dependem do modelo. Aceite futuro: se controle determinístico de todas as transições for indispensável, demonstrar sua interface permitida antes de programar.

### 4.2 Contexto e inferência (R09–R15)

**R09 — Acúmulo de logs e código irrelevante (E).** Saídas extensas competem com o contexto útil e podem estimular repetições. Fontes: G1, p. 13, 15, 17, 19 e 21. Proposta: leituras por intervalo, buscas delimitadas e retorno curto do localizador. Aceite futuro: medir tokens de entrada, volume de saída e perda de informação relevante.

**R10 — Compactação com perda do retorno das ferramentas (B).** O Gemini atribui loops à preservação insuficiente de eventos na compactação; a equipe Kaggle registra investigação do tema, sem anúncio de correção. Fontes: G1, p. 27 e 32; O5. Proposta: reduzir a necessidade de compactar e preservar um estado curto da tarefa. Aceite futuro: continuidade após compactação, sem repetir indefinidamente uma busca já concluída.

**R11 — Perda de pensamentos entre chamadas (B+C).** Há confirmação oficial de incompatibilidade entre ADK e vLLM nesse ponto e anúncio de correção na wheelhouse. Fontes: G1, p. 27-28; O5a. Proposta: registrar a versão da cadeia de inferência e medir o comportamento após a correção. Aceite futuro: observar o caminho realmente servido, sem usar o arquivo de configuração como prova.

**R12 — Flags que alteram o modo de pensamento (B+C).** Ocultar pensamentos pode desativar o raciocínio em certas versões. Fontes: G1, p. 6, 9, 17 e 27-28; atualização em [2, §3.4], que registra a mudança intencional de `include_thoughts:false` no `adk_submission` 0.2.13. Proposta: distinguir ativação do modo, orçamento gerado, inclusão no histórico e exibição do resumo. Aceite futuro: parâmetros aceitos e propagados, com efeito observável na versão usada.

**R13 — Orçamento de pensamento e seed não propagados (B+C).** Parâmetros pedidos podem não chegar ao servidor; os 4.096 tokens sugeridos pelo Gemini não são um ótimo demonstrado. Fontes: G1, p. 27; O5. Proposta: calibrar a geração dentro do prazo e conferir a propagação. Aceite futuro: identificar configuração solicitada, configuração efetiva e tokens usados. A seed, sozinha, não assegura reprodução bit a bit.

**R14 — Limite por resposta confundido com limite por tarefa (E).** `max_output_tokens: 8192` não fixa o custo total de várias respostas. Fontes: G1, p. 6, 8 e 18. Proposta: planejar a soma de chamadas, entradas, geração e ferramentas. Aceite futuro: nenhuma análise usa só o teto de uma resposta para estimar a tarefa inteira.

**R15 — Janela útil e margem para a resposta (C).** Memória suficiente para carregar os pesos não garante espaço para histórico e geração. Fontes: G1, p. 10-12 e 27. Proposta: reservar espaço para a resposta seguinte, esquemas de ferramentas e retomadas. Aceite futuro: completar casos de contexto longo no perfil efetivo, sem depender de compactação que dispara tarde demais.

### 4.3 Busca e edição (R16–R22)

**R16 — Busca semântica vazia ou pouco útil (D).** O material alterna recomendação de grafos e relatos de benefício nulo. Fontes: G1, p. 1-2, 9 e 28. Proposta: começar com símbolos, mensagens de erro, arquivos e busca textual. Aceite futuro: comparar tempo até o arquivo relevante e resolução, com e sem a ferramenta.

**R17 — Dados de grafo ausentes ou incompatíveis (D).** Dataset opcional não garante cobertura de toda tarefa nem retorno com caminho correto. Fontes: G1, p. 1, 4 e 28. Proposta: tratar ausência como condição recuperável e não repetir a mesma consulta vazia. Aceite futuro: o fallback textual funciona sem embeddings ou grafos.

**R18 — Saídas de busca excessivas (D).** Resultados grandes ocupam a janela de contexto. Fontes: G1, p. 13 e 15; O5. Proposta: resultados limitados e leitura só dos candidatos relevantes. Aceite futuro: a saída não ocupa a janela inteira, e o corte não remove os dados de identificação do símbolo.

**R19 — Falha de correspondência em edição (C+D).** Indentação, espaços e trecho impreciso causam `old_string not found`. Fontes: G1, p. 9, 13-15 e 21; G2, §4. Proposta: reler o trecho atual, usar âncora curta e única e conferir o diff. Aceite futuro: falha de edição leva a diagnóstico e releitura, sem repetição idêntica ilimitada.

**R20 — Codificação duplicada de retornos (B+C).** Aspas e quebras de linha chegam com escapes duplicados; a equipe anunciou correção. Fontes: G1, p. 27 e 32; O5. Proposta: usar a cadeia oficial compatível e não aplicar desescape geral. Aceite futuro: leituras e edições com aspas, barras e novas linhas mantêm o conteúdo literal.

**R21 — Quebras de linha e codificação do arquivo (D).** CRLF e LF podem alterar a correspondência de edição. Fontes: G1, p. 14-15 e 31; G2. Proposta: observar o arquivo real e evitar normalizar toda a base. Aceite futuro: o diff contém só a alteração intencional. Diferença de newline não demonstra, por si só, "corrupção de cache".

**R22 — Repetição e buscas sem progresso (C+E).** O agente pode repetir buscas e ações sem obter evidência nova. Fontes: G1, p. 2, 13-14 e 27-28; G2, §3. Proposta: manter hipótese, ações recentes e motivo de cada consulta, e suspender a estratégia que repete a mesma evidência. Aceite futuro: um limite global encerra a sessão, e o trace distingue insistência útil de loop.

### 4.4 Modelos e memória da GPU (R23–R30)

**R23 — Mistura de variantes do modelo (A).** A regra da competição exige a mesma variante para todos os agentes, mesmo que duas caibam na memória. Fontes: G1, p. 4, 12 e 20; G1-R1; O3. Proposta: uma variante admitida para raiz, especialistas e adaptadores. Aceite futuro: nenhuma mistura de 31B com 12B.

**R24 — Seleção do modelo por rótulos de qualidade (E).** "Estado da arte" e "execução instantânea" não vêm com benchmark reproduzível. Fontes: G1, p. 9-12, 16-17 e 20. Proposta: comparar resolução no prazo, falhas de ferramenta e custo total. Aceite futuro: decisão baseada no mesmo conjunto, orçamento e cadeia de avaliação.

**R25 — Estimativas de VRAM dos pesos (E).** As faixas do Gemini (18-22 GB para 31B, 7-9 GB para 12B, 3,5-4,5 GB para E4B e 2,5-3 GB para E2B) não são medições do ambiente nem incluem caches, ativações e adaptadores. Fonte: G1. Proposta: não usá-las como prova de capacidade nem tratar 96 GB agregados como memória única. Aceite futuro: uso e margem observados no serviço efetivo.

**R26 — LoRA reduzindo o KV cache (C).** Adaptadores consomem memória que limitaria histórico e simultaneidade. Fontes: G1, p. 27-28 e 32; O5. Proposta: candidato de referência sem LoRA; adaptador só após benefício mensurável. Aceite futuro: capacidade de contexto preservada e prazo cumprido nos casos longos.

**R27 — Travamentos em prompts longos (C).** O servidor de inferência pode travar em entradas longas. Fonte: G1, p. 27. Proposta: limitar contexto e geração, definir encerramento da sessão e registrar a última operação. Aceite futuro: falha de inferência produz resultado identificável e não impede a continuidade do conjunto. Reduzir logs não prova que o servidor não travará. R65 detalha um mecanismo específico desse risco.

**R28 — Descoberta e identidade de adaptadores (A+C).** Nome do diretório, referência YAML, configuração PEFT e base do adaptador precisam corresponder. Fontes: G1, p. 29. Proposta: verificar a identidade completa e isolar primeiro o caminho sem adaptadores. Aceite futuro: o adaptador é carregado e altera a execução, sem confundir presença de arquivo com aplicação de pesos.

**R29 — Multiplicidade e rank de adaptadores (E).** Quantidade e rank aumentam reservas, custo e superfície de falha. Fontes: G1, p. 28 e 30. Proposta: adiar múltiplos adaptadores e fine-tuning. Aceite futuro: ganho em tarefa real que compense a carga adicional dentro do orçamento.

**R30 — Paralelismo presumido (E).** Quatro GPUs não implicam quatro tarefas independentes simultâneas, e há alerta sobre `ParallelAgent`. Fontes: G1; O3. Proposta: execução sequencial por tarefa, com um único escritor. Aceite futuro: qualquer concorrência posterior exige suporte comprovado e benefício no tempo total.

### 4.5 Python e dependências offline (R31–R35)

**R31 — Dependências indisponíveis (A).** Sem rede, bibliotecas ausentes não podem ser instaladas. Dependências do repositório avaliado e dependências de auxiliares do agente são inventários distintos. Fontes: G1, p. 26 e 31; G2, §1. Proposta: preferir biblioteca padrão e recursos oficiais. Aceite futuro: as duas camadas se resolvem offline.

**R32 — Wheels binárias incompatíveis (A).** A existência de uma `.whl` não comprova compatibilidade com Python, ABI, Linux, arquitetura ou bibliotecas nativas. Fonte: G2, §1. Proposta: registrar esses vínculos e não substituir pacotes centrais isoladamente. Aceite futuro: importação e uso no ambiente alvo, com versões do manifesto.

**R33 — Divergência de interpretador e ambiente virtual (A).** `python` e `pytest` no PATH podem apontar para ambientes diferentes; a imagem pública usa Python 3.13 com shims para módulos antigos. Fontes: G2, §1; O4. Proposta: usar a invocação prevista pelo interpretador fornecido à tarefa. Aceite futuro: comandos e testes rodam no mesmo ambiente pretendido.

**R34 — Vendorização e instalação antes do harness (A).** `vendor/`, dataset privado e `pip --no-index` são alternativa condicionada ao contrato, não permissão geral. Fonte: G2. Proposta: demonstrar montagem, importação, transitivas e licenças, sem presumir transferência do notebook ao sandbox. Aceite futuro: dependência acessível no scorer pelo caminho permitido.

**R35 — Mistura de versões da plataforma (A).** "Atualizar tudo" sem controle cria outras incompatibilidades. Fontes: G1, p. 28 e 31; A1, §6 e §8. Proposta: um conjunto oficial coerente, com dataset, wheels e hashes registrados. Aceite futuro: correções necessárias presentes, sem troca de biblioteca central por conveniência.

### 4.6 Processos e recursos do sandbox (R36–R40)

**R36 — Comandos que excedem o saldo de tempo (A+D).** Um timeout de comando maior que o tempo restante não protege o conjunto. Fontes: G1, p. 13-14; G2, §2. Proposta: limite por comando subordinado ao saldo da sessão, reservando a finalização. Aceite futuro: comando demorado é interrompido de modo controlado e o patch ainda é capturado.

**R37 — Descendentes órfãos e cancelamento incompleto (D).** Timeout do Python, cancelamento assíncrono e término de todos os descendentes não são equivalentes. Fontes: G2, §2; A1, §2, §5 e §8. Proposta: evitar tarefas de fundo e usar a supervisão nativa. Aceite futuro: término dos processos próprios e persistência do resultado observados.

**R38 — Limites de sistema e isolamento (D).** Namespaces, seccomp e AppArmor são citados sem configuração concreta. Fonte: G2. Proposta: tratar limites de processos, memória, disco e permissões como restrições a verificar no contrato real. Aceite futuro: auxiliares funcionam com os privilégios disponíveis, sem atribuir toda falha a um mecanismo de segurança sem diagnóstico.

**R39 — Acúmulo de disco e logs (D).** Arquivos temporários e capturas crescem ao longo do lote. Fontes: G2, §2; G1, p. 31. Proposta: limitar captura e temporários e salvar evidência mínima antes da limpeza. Aceite futuro: consumo não cresce sem limite. Guardar só as últimas 100-200 linhas pode perder a causa inicial do erro.

**R40 — Memória do host e da GPU (A+C).** Excesso de stdout, RAM do container e KV cache são problemas diferentes. Fontes: G1, p. 27 e 31; G2, §4. Proposta: tratar cada orçamento separadamente. Aceite futuro: o diagnóstico registra qual recurso esgotou, sem atribuir toda falha à VRAM.

### 4.7 Patch e verificação (R41–R46)

**R41 — Limpeza destrutiva (E).** `git clean -fd` e `git checkout .` podem apagar arquivos novos necessários e o próprio patch candidato. Fontes: G2, §2-3. Proposta: não usar restauração global como fallback padrão. Aceite futuro: a limpeza não apaga candidato válido nem arquivos novos necessários.

**R42 — Patch vazio ou não capturado (D).** Texto final do modelo não substitui o artefato extraído, e arquivos não rastreados podem ficar fora do diff. Fontes: G1, p. 3, 14 e 19; A1, §2. Proposta: usar a extração oficial e conferir os caminhos incluídos. Aceite futuro: o patch persistido corresponde ao estado intencional, inclusive para arquivos novos.

**R43 — Testes extensos e testes no ambiente errado (D+E).** Testes longos consomem o prazo, e teste que não coletou casos não equivale a aprovação. Fontes: G1, p. 6-7 e 15; G2, §3. Proposta: teste pertinente, com prazo e ambiente conhecidos. Aceite futuro: comando, resultado e relação com o patch atual registrados.

**R44 — Aprovação local confundida com resolução oficial (D).** Patch produzido, teste local, aplicação em cópia limpa e veredito oficial são estados distintos; o tempo dos testes pedidos pelo agente consome a geração. Fontes: G1, p. 14; A1, §2 e §7; O1. Atualização em [2, §3.12]: o verificador só roda os testes do `test_patch`, de modo que "resolvida" não significa ausência de regressão. Aceite futuro: estados separados e nenhum PASS inferido da ausência de erro visível.

**R45 — Persistência e desaparecimento da evidência (D).** O caminho `evaluate_task` analisado não acrescentava a persistência de `Evaluator.run`, e a limpeza podia remover artefatos como o JUnit. Fonte: A1, §5. Proposta: identificar a gravação real e o instante da coleta. Aceite futuro: resultado, patch e diagnóstico mínimo sobrevivem à limpeza.

**R46 — Mocks e simulações confundidos com o modelo real (E).** Contratos e testes históricos não são taxa de resolução do Gemma. Fonte: A1, §3 e §9. Aceite futuro: a evidência separa simulação, modelo substituto, modelo oficial e avaliação de competição.

### 4.8 Operação no Kaggle e interpretação dos resultados (R47–R50)

**R47 — Fila prolongada e consumo de quota (A).** Há relatos de espera de 15-30 horas e de bloqueio de nova submissão; a quota L4x4 é consumida em taxa ampliada. Fontes: G1, p. 28-30; O1. Proposta: margem de calendário e nenhuma submissão gasta para descobrir falha estática de pacote. Aceite futuro: distinguir espera, execução e cobrança observadas.

**R48 — Erro opaco e estado divergente da interface (A).** Há relatos de `Kaggle Error`, exceções sem trace e notebook exibido como ativo após o backend encerrar. Fontes: G1, p. 29-30. Proposta: preservar identificador da submissão, horários e logs; tratar fila, configuração, inferência e testes como classes diferentes. Aceite futuro: o agente não é alterado por inferência a partir de mensagem genérica.

**R49 — Velocidade local sem paridade com o scorer (A+E).** Latências de 3,8-8,7 s por chamada em RTX 4090/A100 são relatos sem protocolo reproduzível. Fontes: G1, p. 28-29. Proposta: tratar esses números como relatos e planejar variação de latência. Aceite futuro: medir a cadeia efetiva, sem extrapolar da GPU local.

**R50 — Limite global e política de encerramento (A).** O risco certo para o planejamento é não produzir todos os artefatos no prazo de 12 horas; a afirmação de que qualquer timeout zera a submissão não foi demonstrada. Fontes: G1, p. 1-4, 9, 14, 19 e 30; G2; O1. Proposta: finalizar cedo o que já é entregável. Aceite futuro: comportamento de timeout e de captura documentado na versão escolhida.

### 4.9 Riscos extraídos da documentação Gemma (R51–R64)

Estes itens decorrem de G4 e das fontes B2 e B11–B14 citadas em [1, §5.9]. Detalham riscos de integração e acrescentam contratos de protocolo, exportação e MTP. Não são falhas reproduzidas.

| ID | Risco | Aceite futuro |
|---|---|---|
| R51 | Confundir memória dos pesos com pico de execução | Dimensionamento inclui KV cache, buffers, adaptadores e margem |
| R52 | Inferir consumo de memória só pelos parâmetros efetivos/ativos | Distinguir parâmetros totais, ativos e formato real do checkpoint |
| R53 | Transportar GGUF/Q4_0/mobile para o caminho W4A16-CT | Artefato e loader correspondem à variante admitida e à versão do servidor |
| R54 | Misturar templates, tokens ou tokenizers Gemma 3/4 | Serialização inspecionada, sem BOS ou template duplicados |
| R55 | Remover contexto necessário dentro de um turno de ferramentas | Fronteiras de eventos e política de histórico documentadas e verificáveis |
| R56 | Tratar instrução de concisão como timeout ou limite de thinking | Limites rígidos têm mecanismo conhecido; orientações de prompt são identificadas como comportamentais |
| R57 | Presumir a existência de ferramenta pelo nome no YAML | Registro e schema efetivos correspondem às chamadas e respostas |
| R58 | Copiar parâmetros de sampling sem aplicação comprovada | Configuração efetiva e custos registrados em cada comparação |
| R59 | Produzir LoRA em formato incompatível com o scorer | Exportação, arquitetura e carregamento compatíveis antes de investir em treinamento |
| R60 | Importar pressupostos online/JAX/TPU para o sandbox | Matriz offline e de recursos distingue os ambientes e versões |
| R61 | Depender de MTP sem suporte ou ganho demonstrado | Artefatos, admissibilidade, suporte e custo líquido comprovados |
| R62 | Aceitar resultado de ferramenta com interpretação errada | Evidência confrontada com a hipótese, a operação e o estado do repositório |
| R63 | Usar benchmark geral como previsão de resolução das issues | Avaliação do fluxo completo e do prazo pelo protocolo pertinente |
| R64 | Usar amostra qualitativa ou exemplo incompleto como validação de treinamento | Evidência de benefício e caminho de exportação completos, sem extrapolar demos |

### 4.10 Falhas do ambiente relatadas no fórum oficial (R65–R72, proposta)

Estes itens foram propostos em [2] depois da leitura de cerca de 40 tópicos do fórum e do confronto com o código V11R6 e com a wheelhouse v08 (vLLM 0.19.1, swegemma 0.2.11, `adk_submission` 0.2.13, google-adk 1.36.1). Relatos de participantes só valem como fato para o projeto quando foram conferidos no código ou reproduzidos [2, §1]. A coluna "Situação em 04/11" vem de [2]; a coluna "Atualização" vem do relatório da rodada 2 V12 [3].

**R65 — Parser do vLLM 0.19.1 congela o servidor com array malformado (C).** Um array cujo elemento não usa o delimitador `<|"|>` e contém `]`, como `args:["Fix list[str] handling"]`, faz `_parse_gemma4_array` parar de avançar. O laço roda no event loop do servidor, que deixa de responder às tarefas seguintes. A correção upstream só existe a partir do vLLM 0.21.0. Tópicos 746336, 753973 e 745138. Os três gatilhos foram reproduzidos em 04/11 contra o vLLM 0.19.1 real: sem correção, nenhum retorna; com `gemma4_parser_compat`, viram erro `MALFORMED_GEMMA4_ARGUMENT_NO_PROGRESS` [2, §3.1].

**R66 — String em aspas JSON chega com as aspas no valor (C).** `skill_name:"my-skill"` chega como `"\"my-skill\""`. Se o modelo escrever um caminho assim, a ferramenta procura um arquivo inexistente, gasta chamadas e pode alimentar R22. Tópico 745138, com referência a vllm#51284 e vllm#51307; confirmado no teste local de [2, §3.2].

**R67 — Argumento fechado por crase faz `edit_file` perder argumentos (C).** O Gemma 4 31B às vezes fecha uma string com `` ` `` (backtick), o parser junta tudo num único argumento, e `old_string`/`new_string` desaparecem. Um participante relatou 107 falhas de `edit_file` em 246 chamadas (43 %). Tópicos 747923, 744272 e 745003. Para o paper, parte do que parece falha de P pode ser falha de serialização da chamada [2, §3.3].

**R68 — Reset anti-adulteração dos testes inoperante (D).** O `git checkout` abortava por pathspec inexistente, e um teste editado pelo agente fazia o `test_patch` falhar mesmo com a correção certa. Tópico 744825. O swegemma 0.2.11 usa `git ls-tree … | xargs git checkout`; o risco fica registrado porque produz falso negativo silencioso se a versão regredir [2, §3.6].

**R69 — Testes dependentes da rede mudam sem internet (D).** Oito tarefas de `requests` falham com o gold patch quando não há rede, porque o teste espera timeout e recebe `Network is unreachable` na hora. Tópico 754586. `requests_7433` e `requests_7502` estão nas 33 tarefas da amostra. O ensaio local R3 não isolou a rede e não prova o comportamento no Kaggle [2, §3.8].

**R70 — Skips mutuamente exclusivos tornam a tarefa insolúvel (D).** Requisitos com condições de skip contraditórias impedem qualquer patch de passar. Tópicos 754586, 751487 e 755554 (este último aberto pelo próprio projeto sobre a tarefa 16) [2, §3.9].

**R71 — Convenções do verificador reprovam correções válidas (D).** `-p no:anyio`, sobrescrita do `pytest.ini`, arquivos `.py` de dados tomados como alvo e JUnit acima de 10 MiB podem reprovar patches corretos. Tópico 751707. Os outros problemas de dependência de teste relatados no mesmo grupo foram cobertos por `offline-test-wheels` [2, §3.10].

**R72 — Prompt gerado pelo harness induz o modelo ao erro (D).** A árvore `find … | head -150` corta o pacote-fonte em 115 de 129 tarefas; `read_file` é limitado a 150 linhas; 18 de 129 enunciados trazem só título e link, inacessível sem rede. Tópicos 745220, 755291 e 746944. P não altera esse texto; para o paper, são causas de falha externas ao algoritmo [2, §3.11].

| ID | Situação em 04/11 [2] | Atualização da rodada 2 V12, 06/11 [3] |
|---|---|---|
| R65 | Mitigado pela compat; a parada do lote por erro de parser é residual | Os parsers `gemma4` funcionaram nas 18 respostas da rodada, sem travamento; entradas malformadas não foram exercitadas, então a ausência do defeito não está demonstrada |
| R66 | Aberto (diagnóstico offline) | Sem registro em [3] |
| R67 | Aberto (subclasse offline proposta) | O relatório associa a R20/R67 o caso de 3 das 4 chamadas `edit_file` com `old_string` duplamente escapado; as três foram aplicadas pela estratégia `unescaped` da ferramenta, sem falha de edição |
| R68 | Mitigado (swegemma 0.2.11) | Sem registro em [3] |
| R69 | Aberto; afeta `requests_7433` e `requests_7502` | Pendente: a rodada não chegou a essas tarefas |
| R70 | Mitigado (tarefa 16 adiada pelo autor) | Sem registro em [3] |
| R71 | Sem caso na amostra; latente | Sem registro em [3] |
| R72 | Só interpretação | Manifestou-se: o enunciado da tarefa trazia apenas "Fix ZWJ and edge cases" e dois links inacessíveis sem rede, e o agente registrou que não podia abri-los |

### 4.11 Defeitos dos recursos da plataforma: ocorrências W01–W25

A análise de bugs dos recursos [4] confrontou fontes originais de 34 componentes prioritários do harness, do servidor e das dependências diretas, os metadados das wheels locais e o código das fronteiras centrais de P. O manifesto de wheels tem 246 entradas; a análise não é auditoria exaustiva delas nem de todas as issues publicadas [4, "Escopo e proveniência"]. As ocorrências W23–W25 foram acrescentadas depois, a partir das execuções V11R2, V11R3 e V11R4 [4; 1, §26.5].

O grau de evidência segue a escala de [1, §26.2]: relato, inspeção, reprodução local, integração e Kaggle. "Reproduzido" significa reprodução local com os bytes pinados, em sondas sintéticas, sem GPU e sem tarefa científica. Nenhuma dessas reproduções demonstra que o defeito já tenha alterado um resultado das 33 tarefas [4, "Resultado para a decisão"].

| W | Componente e versão | Defeito | Evidência | Classes R | Situação e mitigação |
|---|---|---|---|---|---|
| W01 | vllm 0.19.1 (parser `gemma4`) | Entrada malformada faz o parser parar de avançar e travar o servidor | Reproduzido: 4 de 7 entradas sem progresso | R06, R20, R22, R27, R35, R37, R44, R48, R62 | **Bloqueio de liberação científica** em [1, §26.1]. Proposta própria rejeita a entrada malformada; a PR oficial 41991 corrige a família de defeitos. Ver R65 e o teste de 04/11 em [2, §3.1] |
| W02 | adk-submission 0.2.13 / ADK / vLLM | Pensamentos (reasoning) perdidos entre chamadas | Confirmado pela equipe Kaggle; ponte presente na wheel; 6 sondas puras | R11–R13, R20, R35 | P usa thinking desativado; validar a serialização se o caminho mudar |
| W03 | swegemma 0.2.11 / ambiente de testes | Dependências de teste ausentes no sandbox | Relatos no fórum | R31–R35, R43, R44 | Conferir dependências de cada snapshot no interpretador efetivo; erro de preparação não é falha científica de P |
| W04 | swegemma 0.2.11 | Teste importa a wheel instalada em vez do repositório editado (falso PASS por shadowing) | Relato | R19, R33–R35, R44, R62 | Exigir a origem do módulo sob teste; ocorrência no runtime de P não demonstrada |
| W05 | Wheels em geral | Mesma versão com conteúdo diferente | Inspeção de hashes | R32, R35, R44 | Usar SHA-256 da wheel e do arquivo carregado; a identidade do scorer não foi conferida |
| W06 | google-adk 1.36.1 | `ParallelAgent` e compactação | Issue oficial ADK 7324 | R10–R15, R35 | Condicional; P é sequencial. Não migrar para ADK 2.x, porque adk-submission exige ADK < 2 |
| W07 | FastAPI 0.141.1 / Starlette 0.52.1 / prometheus-fastapi-instrumentator 7.1.0 | `AttributeError` no roteamento das métricas; o backport de P deixa rótulos incorretos em 2 de 3 cenários | Reproduzido | R32, R35, R48, R62 | Proposta com `root_path` passou nos três cenários; não integrada. Rótulo errado é falha de observação, não de resposta do modelo |
| W08 | requests 2.34.2 | `NameError` na introspecção de tipos (issue 7456) | Reproduzido em 4 classes | R06, R35, R48 | Incidência nas funções de P não demonstrada; não aplicar monkeypatch global |
| W09 | pydantic 2.14.1 / pydantic-core 2.50.1 | Validação indevida: campo por nome errado ignorado, chave extra aceita, alias de TypedDict sobrescrito | Reproduzido: 3 comportamentos | R06, R20, R35, R62 | Mapear schema e API antes de alterar; atualização só coordenada e testada (avisos dos mantenedores; release 2.14.2) |
| W10 | torch 2.10.0+cu128 / transformers 5.13.1 / triton 3.6.0 | Erros de cuBLAS e SDPA | Relatos com as mesmas versões | R26, R27, R32, R35 | Condicional; registrar bibliotecas carregadas e erro de kernel no alvo |
| W11 | grpcio 1.84.0 | Chamada aio não cancelada pela coleta de lixo | Relato | R27, R37, R48 | Condicional; P usa HTTP local |
| W12 | uvicorn 0.54.0 | Reset no shutdown com reciclagem de workers | Relato | R27, R37, R48 | Condicional; não autoriza retry científico |
| W13 | pyyaml 6.0.3 | CDumper reentrante pode causar segfault | Relato | R06, R32, R48 | Precondição não encontrada em P |
| W14 | litellm 1.85.7 | Serialização de reasoning com Groq e streaming | Relato | R11–R13, R20, R35 | Outro provedor; não remover campos de reasoning globalmente |
| W15 | httpx 0.28.1 | Remoção do argumento `proxies=` | Reproduzido (rejeição do argumento) | R32, R35, R48 | Nenhum consumidor encontrado em P |
| W16 | Ambiente local Windows × Linux | Versões diferentes de Pydantic, LiteLLM, SDK OpenAI e instrumentator | Medição local | R32, R33, R35, R44 | Risco do ambiente de desenvolvimento, não da plataforma; sondas Linux usam as wheels pinadas |
| W17 | httpx2 2.15.1 | Política de cookies corrigida só em versão posterior | Relato de correção | R20, R35, R62 | Uso por P não demonstrado |
| W18 | swegemma 0.2.11 (`verification.py`) | Correspondência JUnit permissiva aceita teste de outro módulo, prefixo semelhante e outro parâmetro | Reproduzido: 3 aceitações indevidas em 9 casos | R44, R62 | **Bloqueio de liberação científica** em [1, §26.3]. P reutiliza o helper em `unit_evaluation.py:116`; comparação estrita proposta, não integrada. Não comprova falso PASS real |
| W19 | LoRA na vLLM | Adaptador e memória de CUDA graphs | Relatos e orientação da equipe | R26–R29, R35, R62 | Condicional; P usa 31B sem LoRA |
| W20 | Variante 12B | Carregamento do modelo 12B | Correção anunciada pela equipe | R32, R35, R48 | Condicional; P usa 31B |
| W21 | Ferramentas de grafo | Revisões das buscas em grafo | Relatos | R16–R18, R35 | Condicional; P não usa essas ferramentas |
| W22 | Harness próprio de P (`audited_runtime.py`) | `_close_async_generator` suprime a exceção do fechamento | Reproduzido: 3 sondas | R37, R48, R62 | Falha do próprio projeto. Mitigação especificada, não implementada |
| W23 | Harness próprio de P (guardião V11R2) | Import isolado da política falhou antes da preparação do sandbox | Confirmado no Kaggle e reproduzido localmente | R33, R35, R37, R44, R48, R62 | Falha do próprio projeto. Corrigida por caminho explícito na V11R3; zero tarefas avaliadas |
| W24 | swegemma 0.2.11 × classificador próprio | `rm -f /tmp/setup.py` do swegemma rejeitado pelo classificador de P | Confirmado na execução V11R3 | R33, R35, R37, R44, R48, R62 | Interação entre o recurso e a guarda do projeto. Mitigação na V11R4 reconhece só o comando exato; autorização V11R3 consumida, sem retry |
| W25 | Comparador próprio de P × coleta do pytest | Identidade `tests/test_cells.py::…` do manifesto não casa com `test_cells.py::…` coletado | Confirmado por artefatos e reprodução pura | R35, R44, R62 | Falha do próprio projeto. Veredito upstream preservado (`resolved=false`); correção e ensaio integrado pendentes |

Dois pontos dessa tabela importam diretamente para o desafio. Primeiro, W01 e W18 são os bloqueios de recursos registrados contra a liberação científica: o parser pode travar o servidor, e o verificador pode aceitar como aprovado um teste que não é o exigido [1, §26.1 e §26.3]. O arquivo de gate é documental e, em 02/11, ainda não era um bloqueio programado no runner [4]. A situação desses bloqueios nas versões V11R6, V12 e V12R1 não foi reavaliada nesta consolidação. Segundo, W16, W22, W23 e W25 são falhas do próprio projeto ou do ambiente local, e W24 é uma interação entre um recurso e uma guarda do projeto. Elas foram mantidas porque o catálogo as registra, mas não devem ser apresentadas como defeitos da plataforma.

A mesma análise registra 13 correções E01–E13 já aplicadas aos controles V10 [4, "Correções já aplicadas aos controles V10"]. Elas corrigem o harness do projeto, não a plataforma, e por isso não entram neste catálogo.

**Subcasos de relatos de competidores (27/10/2026).** A seção 24.1 de [1] enquadrou em classes existentes relatos que também dificultam o desafio: média prática de cerca de 5,5 minutos por tarefa (`12 h / 129 = 5,58 min`), que é média de planejamento e não timeout oficial (R36, R43, R49, R50); fila de validação relatada acima de 48 horas (R47, R48); consumo de quota L4x4 em taxa maior que T4x2/P100 (R47); `dirty_equals`, `inline_snapshot` ou `pytest` ausentes no ambiente de teste (R31–R35, R43); log `error (exit 0)` ao fim do orçamento (R44, R62); adaptador anunciado sem pesos LoRA aplicados (R28, R35, R59, R62); e `include_thoughts` alterando a geração ou só a exposição dos pensamentos (R11–R13, R35, R58).

**Pendências da tentativa 11 (27/10/2026).** A seção 25.2 de [1] registra como pendentes: o `GeneratorExit` convertido em `MODEL_REQUEST_FAILED_WITHOUT_AUDITABLE_USAGE` (R44, R62); a divergência entre o cleanup interno `VLLM_PROCESS_GROUP_NOT_GONE` e o supervisor externo, que registrou árvore encerrada e GPU ociosa (R37); e o `FileExistsError` de reentrada (R39, R45). A mesma seção registra que a consulta daquela data não encontrou confirmação oficial de patch que resolvesse o `GeneratorExit` ou a divergência de cleanup.

## 5. Onde está o texto integral

| Faixa | Arquivo | Localização |
|---|---|---|
| R01–R50 | `docs/arquitetura/2026-10-19-analise-gemini-e-proposta-arquitetura.md` | §5.1–§5.8, linhas 176–288 |
| R51–R64 | mesmo arquivo | §5.9, linhas 290–309 |
| Subcasos de 27/10 e pendências da tentativa 11 | mesmo arquivo de R01–R64 | §24.1 e §25.2 de [1] |
| Ocorrências W01–W25, fontes primárias, hashes e recibos | `docs/2026-11-02-analise-bugs-recursos-P.md` e mesmo arquivo de R01–R64 | [4] inteiro; §26 de [1] |
| Evidências das sondas W | `experimentos/2026-11-01-p3-bug33-correcoes-v01/v10-audit/wheel-research-20261102/` | Recibos JSON listados em [4], "Continuidade e localização das evidências" |
| R65–R72 | `Analises_Criticas/2026-11-04-forum-competicao/2026-11-04-2045-impacto-forum-no-harness-V11R6.md` | §3 e §4 |

As linhas citadas correspondem ao arquivo de [1] no working tree em 06/11/2026, que tinha alterações locais não commitadas nessa data.

## 6. Limitações desta consolidação

Este documento não testou nenhum risco, não reconsultou as fontes externas e não reavaliou o status de R01–R64 nem das ocorrências W. A tabela da seção 4.11 resume [4] e [1, §26] como estavam em 06/11/2026; não confere se as mitigações propostas para W01, W07, W18, W22 e W25 foram integradas nas versões V11R6, V12 ou V12R1. As fontes primárias de cada ocorrência (issues, releases e avisos dos mantenedores) estão em [4] e não foram reabertas. As descrições de R01–R50 são condensações e podem omitir nuances do texto original. A coluna "Natureza" é interpretação deste documento e pode ser contestada; em especial, os itens de natureza E não são defeitos da plataforma, mas riscos de decisão do projeto, mantidos aqui porque também dificultam o atendimento ao desafio. A tabela-resumo atribui natureza E pura a 13 itens (R09, R14, R24, R25, R29, R30, R41, R46, R51, R52, R56, R63 e R64) e natureza E combinada a outros 4 (R22, R43, R49 e R62); os demais 55 itens têm pelo menos uma origem externa ao projeto (A, B, C ou D). Contando os itens mistos em cada natureza que contêm, há 18 itens com natureza A, 12 com B, 19 com C e 18 com D.

A incorporação de R65–R72 ao catálogo canônico, a conciliação entre R65 e W01, o tratamento de R73–R74 anunciados no título de [2] e a revisão da coluna "Natureza" dependem de decisão de Aridio Silva.

## Bibliography / References

[1] Silva, Aridio. *Restrições do desafio Gemma 4 e proposta de revisão da arquitetura*. `docs/arquitetura/2026-10-19-analise-gemini-e-proposta-arquitetura.md`. Criado em 19/10/2026; última atualização declarada em 02/11/2026. Usado somente como catálogo de riscos, conforme `AGENTS.md` §16. Consultado em 06/11/2026: §5 e §24.1, §25 e §26 lidos para esta consolidação.

[2] Silva, Aridio. *Falhas do ambiente da competição relatadas no fórum: impacto no harness V11R6 e proposta R65–R74*. `Analises_Criticas/2026-11-04-forum-competicao/2026-11-04-2045-impacto-forum-no-harness-V11R6.md`. 04/11/2026. Consultado em 06/11/2026.

[3] Silva, Aridio. Relatório da rodada 2 V12. `Analises_Criticas/2026-11-05-implementacao-V12/kaggle-rodada2/2026-11-06-1425-relatorio-rodada2-V12.md`. 06/11/2026. Consultado em 06/11/2026.

[4] Silva, Aridio. *Análise de bugs conhecidos dos recursos e do harness do algoritmo P*. `docs/2026-11-02-analise-bugs-recursos-P.md`. 02/11/2026, com adendos W23–W25 do mesmo dia. Lido integralmente em 06/11/2026, no working tree, que tinha alterações locais não commitadas.

[5] Kaggle. Gemma 4 Developer Agent — Overview (O1). https://www.kaggle.com/competitions/gemma-4-developer-agent/overview. URL conforme [1]; não reconsultada em 06/11/2026.

[6] Holbrook, Ryan (Kaggle Staff). New Gemma 4 Models Available 12B E4B and E2B (O3). https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/748287. URL conforme [1]; não reconsultada em 06/11/2026.

[7] Holbrook, Ryan. Getting Started Gemma 4 Developer Agent — Input (O4). https://www.kaggle.com/code/ryanholbrook/getting-started-gemma-4-developer-agent/input. URL conforme [1]; não reconsultada em 06/11/2026.

[8] Holbrook, Ryan. Comentários no Kaggle (O5). https://www.kaggle.com/ryanholbrook/discussion. Índice mutável. URL conforme [1]; não reconsultada em 06/11/2026.

[9] Discussão sobre perda de pensamentos entre chamadas (O5a). https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/744354. URL conforme [1]; não reconsultada em 06/11/2026.

---

**Contagem de palavras:** 8447 palavras. Método: contagem conservadora local de todos os tokens separados por espaço em branco do arquivo inteiro, incluindo metadados, tabelas, bibliografia e esta nota, feita com PowerShell (`-split '\s+'`) após a gravação final. Não há texto em imagens. Este documento não é manuscrito da Paper Track e não está sujeito ao limite de 3.000 palavras do Writeup.
