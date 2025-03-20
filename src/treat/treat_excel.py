import pandas as pd

input_file = 'src/extract/outputs_extraidos/sindrome_gripal_2020.xlsx'
output_file = 'src/treat/outputs/sindrome_gripal_2020.xlsx'


try: 
    substituicoes = {
        "CabeÃ§a": "Cabeça",
        "AssintomÃ¡tico": "Assintomático",
        "DistÃºrbios": "Distúrbios",
        "BelÃ©m": "Belém",
        "Santa BÃ¡rbara do ParÃ¡": "Santa Bárbara do Pará",
        "BraganÃ§a": "Bragança",
        "SantarÃ©m": "Santarém",
        "MarabÃ¡": "Marabá",
        "CametÃ¡": "Cametá",
        "TucuruÃ": "Tucuruí",
        "CapitÃ£o PoÃ§o": "Capitão Poço",
        "TucumÃ£": "Tucumã",
        "RurÃ³polis": "Rurópolis",
        "OurilÃ¢ndia do Norte": "Ourilândia do Norte",
        "MojuÃ­ dos Campos": "Mojuí dos Campos",
        "CanaÃ£ dos CarajÃ¡s": "Canaã dos Carajás",
        "SÃ£o Geraldo do Araguaia": "São Geraldo do Araguaia",
        "IgarapÃ©-AÃ§u": "Igarapé-Açu",
        "SÃ£o SebastiÃ£o da Boa Vista": "São Sebastião da Boa Vista",
        "TomÃ©-AÃ§u": "Tomé-Açu",
        "SÃ£o Miguel do GuamÃ¡": "São Miguel do Guamá",
        "SÃ£o FÃ©lix do Xingu": "São Félix do Xingu",
        "CuruÃ¡": "Curuá",
        "MedicilÃ¢ndia": "Medicilândia",
        "ConceiÃ§Ã£o do Araguaia": "Conceição do Araguaia",
        "Cachoeira do PiriÃ¡": "Cachoeira do Ararí",
        "OurilÃ¢ndia do Norte": "Ourilândia do Norte",
        "PiÃ§arra": "Piçarra",
        "Aurora do ParÃ¡": "Aurora do Pará",
        "MÃ£e do Rio": "Mãe do Rio",
        "RedenÃ§Ã£o": "Redenção",
        "SÃ£o JoÃ£o de Pirabas": "São João de Pirabas",
        "GurupÃ¡": "Gurupá",
        "SÃ£o Caetano de Odivelas": "São Caetano de Odivelas",
        "Augusto CorrÃªa": "Augusto Corrêa",
        "IvaiporÃ£": "Ivaiporã",
        "UruarÃ¡": "Uruará",
        "CurionÃ³polis": "Curionópolis",
        "UlianÃ³polis": "Ulianópolis",
        "TailÃ¢ndia": "Tailândia",
        "Ãgua Azul do Norte": "Água Azul do Norte",
        "VitÃ³ria do Xingu": "Vitória do Xingu",
        "Santa Maria do ParÃ¡": "Santa Mara do Pará",
        "ConcÃ³rdia do ParÃ¡": "Concórdia do Pará",
        "GarrafÃ£o do Norte": "Garrafão do Norte",
        "AfuÃ¡": "Afuá",
        "Ipixuna do ParÃ¡": "ipixuna do Pará",
        "Nova EsperanÃ§a do PiriÃ¡": "Nova Esperança do Piriá",
        "PacajÃ¡": "Pacajá",
        "Senador JosÃ© PorfÃ­rio": "Senador José Porfírio",
        "Palestina do ParÃ¡": "Palestina do Pará",
        "MaracanÃ£": "Maracanã",
        "OurÃ©m": "Ourém",
        "SÃ£o Domingos do Araguaia": "São Domingos do Araguaia",
        "SÃ£o Paulo": "São Paulo",
        "CuruÃ§Ã¡": "Curuçá",
        "MelgaÃ§o": "Melgaço",
        "Ã“bidos": "Óbidos",
        "JacundÃ¡": "Jacundá",
        "MuanÃ¡": "Muaná",
        "Santa Izabel do ParÃ¡": "Santa Izabel do Pará",
        "OriximinÃ¡": "Oriximiná",
        "AnajÃ¡s": "Anajáis",
        "AcarÃ¡": "Aracá",
        "Eldorado do CarajÃ¡s": "Eldorado do Carajás",
        "Santo AntÃ´nio dos Lopes": "Santo Antônio dos Lopes",
        "CatalÃ£o": "Catalão",
        "SalinÃ³polis": "Salinópolis",
        "BaiÃ£o": "Baião",
        "Santo AntÃ´nio do TauÃ¡": "Santo Antônio do Tauá",
        "TrairÃ£o": "Trairão",
        "Oeiras do ParÃ¡": "Oeiras do Pará",
        "Santa Luzia do ParÃ¡": "Santa Luiza do Pará",
        "SÃ£o Francisco do ParÃ¡": "São Francisco do Pará",
        "IgarapÃ©-Miri": "Igarapé-Miri",
        "GoianÃ©sia do ParÃ¡": "Goianésia do Pará",
        "SÃ£o Domingos do Capim": "São Domingos do Capim",
        "Rondon do ParÃ¡": "Rondon do Pará",
    }

    df = pd.read_excel(input_file)
    df = df.replace(substituicoes, regex=True)

    df['dataNotificacao'] = pd.to_datetime(df['dataNotificacao']).dt.date

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dados tratados", index=False)

    print(f"Arquivo salvo em: {output_file}")

except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
