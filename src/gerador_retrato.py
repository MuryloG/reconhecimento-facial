from PIL import Image, ImageDraw, ImageFilter, ImageChops
import os

def gerar_retrato(componentes, output_path="../retrato_falado_suspeito.png"):
    tamanho = (400, 400)
    
    if 'face' in componentes and os.path.exists(componentes['face']):
        bg = Image.open(componentes['face']).convert("RGBA")
    else:
        bg = Image.new('RGBA', tamanho, (80, 80, 80, 255))
        
    fg = Image.new('RGBA', tamanho, (0, 0, 0, 0))
    base_mask = Image.new('L', tamanho, 0)
    draw_mask = ImageDraw.Draw(base_mask)
    
    poligonos = {
        'olhos': [(0, 30), (400, 30), (400, 280), (270, 280), (230, 150), (170, 150), (130, 280), (0, 280)],
        'nariz': [(160, 140), (240, 140), (270, 280), (130, 280)],
        'boca':  [(0, 260), (400, 260), (400, 400), (0, 400)]
    }
    
    ordem_camadas = ['olhos', 'nariz', 'boca']
    
    for camada in ordem_camadas:
        if camada in componentes and os.path.exists(componentes[camada]):
            img_camada = Image.open(componentes[camada]).convert("RGBA")
            fg = Image.alpha_composite(fg, img_camada)
            draw_mask.polygon(poligonos[camada], fill=255)
            
    # A MÁGICA ESTÁ AQUI: Desfocamos a máscara de delimitação em 10px!
    # Se uma peça estiver faltando, a borda vira um degradê pro cinza, e não uma linha de estilete.
    base_mask = base_mask.filter(ImageFilter.GaussianBlur(radius=10))
            
    mask_oval = Image.new('L', tamanho, 0)
    ImageDraw.Draw(mask_oval).ellipse((60, 20, 340, 380), fill=255)
    
    final_mask = ImageChops.multiply(base_mask, mask_oval)
    
    fg_alpha = fg.split()[3] 
    clipped_alpha = ImageChops.multiply(fg_alpha, final_mask) 
    fg.putalpha(clipped_alpha) 
    
    resultado = Image.alpha_composite(bg, fg)
    resultado.save(output_path)

if __name__ == "__main__":
    pass