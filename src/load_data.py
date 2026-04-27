import basedosdados as bd

# Para carregar o dado direto no pandas
df = bd.read_sql(
    "SELECT * FROM `datario.adm_central_atendimento_1746.chamado` LIMIT 100",
    billing_project_id="desafio-pic",
)

print(df.head())
