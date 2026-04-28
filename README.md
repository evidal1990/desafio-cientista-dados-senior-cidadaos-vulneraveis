# Desafio Técnico - Cientista de Dados Sênior (PIC)

Este repositório contém a resolução do desafio com notebooks para análise exploratória de chamados do 1746.

## Estrutura do projeto

```text
.
├── README.md
├── notebooks/
│   ├── 01_analise_apis_clima.ipynb
├── data/
│   └── .gitkeep
├── results/
│   └── figures/
└── requirements.txt
```

## Pré-requisitos

- Python 3.11+ (recomendado)
- Conta/projeto GCP com acesso ao BigQuery
- Credenciais configuradas para leitura via `basedosdados`
- Conexão com internet para APIs externas:
  - Nager.Date (feriados)
  - Open-Meteo (clima)

## Como executar

### 1) Clonar e entrar no repositório

```bash
git clone <url-do-repositorio>
cd desafio-cientista-dados-senior-cidadaos-vulneraveis
```

### 2) Criar e ativar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependências

```bash
pip install -r requirements.txt
```

### 4) Abrir os notebooks

```bash
jupyter lab
```

Ou, se preferir:

```bash
jupyter notebook
```


## Configuração de acesso aos dados

Para consultas via `basedosdados`, utilize um projeto de faturamento válido no BigQuery e autentique conforme orientação da biblioteca.

Exemplo de uso nos notebooks:

```python
import basedosdados as bd

df = bd.read_sql(
    "SELECT * FROM `datario.adm_central_atendimento_1746.chamado` LIMIT 100",
    billing_project_id="SEU_PROJETO_GCP",
)
```

## Observações importantes

- A tabela de chamados é grande; sempre aplique filtro de partição (`data_particao`) para reduzir custo/tempo.
- Algumas células dependem de chamadas HTTP para APIs externas; falhas de rede podem afetar resultados.