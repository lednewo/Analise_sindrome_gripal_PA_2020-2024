import pandas as pd

input_file = 'src/extract/outputs_extraidos/sindrome_gripal_2020.xlsx'
output_file = 'src/treat/outputs/sindrome_gripal_2020.xlsx'


try: 

    df = pd.read_excel(input_file)
    

    df['dataNotificacao'] = pd.to_datetime(df['dataNotificacao']).dt.date

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dados tratados", index=False)

    print(f"Arquivo salvo em: {output_file}")

except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
