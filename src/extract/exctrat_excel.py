import pandas as pd

input_file = 'src/extract/outputs_extraidos/sindrome_gripal_2020.xlsx'
output_file = 'src/extract/outputs_extraidos/teste.xlsx'


try:
    df = pd.read_excel(input_file)

    colunas = ["sintomas", "racaCor", "sexo", "municipio", "dataNotificacao"]
    df_filtrado = df[colunas].dropna()


    count_sintomas = df["sexo"].value_counts().reset_index()

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df_filtrado.to_excel(writer, sheet_name="Dados Filtrados", index=False)
        count_sintomas.to_excel(writer, sheet_name="Contagem Sintomas", index=False)

    print(f"Arquivo salvo em: {output_file}")
except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")