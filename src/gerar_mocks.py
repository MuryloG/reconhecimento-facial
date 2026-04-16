from PIL import Image, ImageDraw
import os

def criar_mocks():
    # Pega a pasta exata onde este script (gerar_mocks.py) está salvo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Sobe um nível e entra em assets (ex: C:/.../projeto-a3-reconhecimento/assets)
    pasta_assets = os.path.join(diretorio_atual, '..', 'assets')

    pastas = [
        'faces', 'olhos', 'nariz', 'boca', 'cabelo', 'sobrancelhas'
    ]
    
    # Cria as pastas garantindo o caminho absoluto
    for subpasta in pastas:
        caminho_completo = os.path.join(pasta_assets, subpasta)
        os.makedirs(caminho_completo, exist_ok=True)

    # Caminhos absolutos para salvar cada arquivo
    face_path = os.path.join(pasta_assets, 'faces', 'formato_padrao.png')
    img_face = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_face)
    draw.ellipse((100, 50, 300, 350), fill=(255, 220, 170, 255))
    img_face.save(face_path)

    olhos_path = os.path.join(pasta_assets, 'olhos', 'olhos_v1.png')
    img_olhos = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_olhos)
    draw.ellipse((140, 150, 180, 180), fill=(0, 0, 255, 255))
    draw.ellipse((220, 150, 260, 180), fill=(0, 0, 255, 255))
    img_olhos.save(olhos_path)

    nariz_path = os.path.join(pasta_assets, 'nariz', 'nariz_v1.png')
    img_nariz = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_nariz)
    draw.polygon([(200, 180), (180, 240), (220, 240)], fill=(255, 100, 100, 255))
    img_nariz.save(nariz_path)

    boca_path = os.path.join(pasta_assets, 'boca', 'boca_v1.png')
    img_boca = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_boca)
    draw.rectangle((160, 280, 240, 300), fill=(255, 100, 150, 255))
    img_boca.save(boca_path)

    cabelo_path = os.path.join(pasta_assets, 'cabelo', 'cabelo_curto.png')
    img_cabelo = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_cabelo)
    draw.arc((90, 30, 310, 200), start=180, end=0, fill=(139, 69, 19, 255), width=40)
    img_cabelo.save(cabelo_path)
    
    print(f"Arquivos de teste gerados com sucesso na pasta: {pasta_assets}")

if __name__ == "__main__":
    criar_mocks()