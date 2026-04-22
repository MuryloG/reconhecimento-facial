import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

def limpar_pastas_antigas(pasta_assets):
    pastas_para_limpar = ['olhos', 'nariz', 'boca']
    for pasta in pastas_para_limpar:
        caminho_pasta = os.path.join(pasta_assets, pasta)
        if os.path.exists(caminho_pasta):
            for arquivo in os.listdir(caminho_pasta):
                if arquivo.endswith('.png'):
                    os.remove(os.path.join(caminho_pasta, arquivo))

def criar_manequim_universal(pasta_assets):
    tamanho_canvas = (400, 400)
    canvas = Image.new('RGBA', tamanho_canvas, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    
    cor_pele_generica = (80, 80, 80, 255)
    draw.ellipse((60, 20, 340, 380), fill=cor_pele_generica)
    canvas = canvas.filter(ImageFilter.GaussianBlur(radius=5))
    
    caminho_salvar = os.path.join(pasta_assets, 'faces', 'rosto_base_universal.png')
    os.makedirs(os.path.dirname(caminho_salvar), exist_ok=True)
    canvas.save(caminho_salvar)

def extrair_e_salvar_componentes(caminho_imagem_origem, id_extracao):
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    pasta_assets = os.path.join(dir_atual, '..', 'assets')
    
    img_cv = cv2.imread(caminho_imagem_origem)
    if img_cv is None: return

    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if len(faces) == 0: return
    (x, y, w, h) = faces[0]
    
    y_exp = max(0, y - int(h * 0.2))
    h_exp = h + int(h * 0.3)
    rosto_recortado = img_cv[y_exp:y_exp+h_exp, x:x+w]
    
    img_pil = Image.fromarray(cv2.cvtColor(rosto_recortado, cv2.COLOR_BGR2RGB)).convert("RGBA")
    img_400 = img_pil.resize((400, 400))
    
    mask_oval = Image.new('L', (400, 400), 0)
    ImageDraw.Draw(mask_oval).ellipse((60, 20, 340, 380), fill=255)
    mask_oval = mask_oval.filter(ImageFilter.GaussianBlur(radius=5))
    
    def fatiar_suave(pasta_destino, nome_arquivo, poligono):
        mask_peca = Image.new('L', (400, 400), 0)
        ImageDraw.Draw(mask_peca).polygon(poligono, fill=255)
        
        mask_peca = mask_peca.filter(ImageFilter.GaussianBlur(radius=10))
        mask_final = ImageChops.multiply(mask_peca, mask_oval)
        
        img_final = img_400.copy()
        img_final.putalpha(mask_final)
        
        os.makedirs(os.path.join(pasta_assets, pasta_destino), exist_ok=True)
        img_final.save(os.path.join(pasta_assets, pasta_destino, nome_arquivo))

    poly_olhos  = [(0, 30), (400, 30), (400, 280), (270, 280), (230, 150), (170, 150), (130, 280), (0, 280)]
    poly_nariz  = [(160, 140), (240, 140), (270, 280), (130, 280)]
    poly_boca   = [(0, 260), (400, 260), (400, 400), (0, 400)]

    fatiar_suave('olhos', f'olhos_{id_extracao}.png', poly_olhos)
    fatiar_suave('nariz', f'nariz_{id_extracao}.png', poly_nariz)
    fatiar_suave('boca', f'boca_{id_extracao}.png', poly_boca)

if __name__ == "__main__":
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    pasta_assets = os.path.join(dir_atual, '..', 'assets')
    
    limpar_pastas_antigas(pasta_assets)
    criar_manequim_universal(pasta_assets)
    
    # Rodando na base inteira (1 a 40)
    for i in range(1, 41):
        img_path = os.path.join(dir_atual, '..', 'dataset', f's{i}', '1.pgm')
        if os.path.exists(img_path):
            extrair_e_salvar_componentes(img_path, f"sujeito_{i:02d}")
            
    print("Limpeza concluída e peças extraídas de toda a base criminal!")