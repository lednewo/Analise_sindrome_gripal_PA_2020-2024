import pandas as pd
import unicodedata

input_file = 'src/treat/outputs/sindrome_gripal_2024.xlsx'
output_file = 'src/treat/sindrome_gripal_2024.xlsx'

def normalize_text(text):
    """Remove acentos e normaliza texto para minúsculas e sem espaços extras."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if unicodedata.category(c) != 'Mn'
    ).strip().lower()

try:
    df = pd.read_excel(input_file)
    
    df['dataNotificacao'] = pd.to_datetime(df['dataNotificacao']).dt.date
    
    coluna_cidade = "municipio"
    df[coluna_cidade] = df[coluna_cidade].astype(str).apply(normalize_text)
    
    cidades_desejadas = [
        'ananindeua', 'barcarena', 'belem', 'benevides', 
        'castanhal', 'marituba', 'santa barbara do para', 'santa izabel do para'
    ]
    
    df_filtrado = df[df[coluna_cidade].isin(cidades_desejadas)].copy()
    
    sexo_counts = df_filtrado.groupby(["municipio", "sexo"]).size().reset_index(name="contagem")
    
    sintomas_conhecidos = [
        "outros", "dispneia", "febre", "dor de garganta", "distúrbios olfativos", 
        "distúrbios gustativos", "tosse", "dor de cabeça", "assintomático", "coriza"
    ]    
    
    if "sintomas" in df_filtrado.columns and df_filtrado["sintomas"].notna().any():
        
        df_filtrado["sintomas"] = df_filtrado["sintomas"].fillna("none").str.strip()
        
        for sintoma in sintomas_conhecidos:
            df_filtrado[sintoma] = df_filtrado["sintomas"].apply(
                lambda x: sintoma if sintoma in [s.strip().lower() for s in x.split(",")] else None
            )
        df_filtrado.drop(columns=["sintomas"], inplace=True)
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df_filtrado.to_excel(writer, sheet_name="Dados Filtrados", index=False)
        sexo_counts.to_excel(writer, sheet_name="Contagem Sexo por Município", index=False)
    
    print(f"Arquivo salvo em: {output_file}")
    
except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
