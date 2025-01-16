import os


def renomear_para_caixa_alta(diretorio):
    try:
        for arquivo in os.listdir(diretorio):
            caminho_antigo = os.path.join(diretorio, arquivo)

            if os.path.isfile(caminho_antigo):
                nome, extensao = os.path.splitext(arquivo)
                novo_nome = f"{nome.upper()}{extensao}"
                caminho_novo = os.path.join(diretorio, novo_nome)

                os.rename(caminho_antigo, caminho_novo)
                print(f"Renomeado: {arquivo} -> {novo_nome}")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")


directory_path = "INSERT PATH"
renomear_para_caixa_alta(directory_path)
