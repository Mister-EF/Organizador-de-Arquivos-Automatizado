import os
import shutil

def organizar_pasta(caminho_diretorio):
    mapeamento_extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Arquivos_Compactados': ['.zip', '.rar', '.7z'],
        'Instaladores': ['.exe', '.msi'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Musicas': ['.mp3', '.wav']
    }

    if not os.path.exists(caminho_diretorio):
        print("Caminho não encontrado.")
        return

    for arquivo in os.listdir(caminho_diretorio):
        caminho_completo = os.path.join(caminho_diretorio, arquivo)

        if os.path.isdir(caminho_completo):
            continue

        extensao = os.path.splitext(arquivo)[1].lower()

        movido = False
        for categoria, extensoes in mapeamento_extensoes.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(caminho_diretorio, categoria)
                
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
                print(f"Movido: {arquivo} -> {categoria}")
                movido = True
                break
        
        if not movido:
            print(f"Ignorado (Sem categoria): {arquivo}")

if __name__ == "__main__":
    diretorio_alvo = "./meus_downloads_teste"
    
    organizar_pasta(diretorio_alvo)