from PIL import Image
import os

def gerar_retrato(componentes, output_path="retrato_falado_suspeito.png"):
    base_img = None
    
    ordem_camadas = ['face', 'cabelo', 'sobrancelhas', 'olhos', 'nariz', 'boca', 'barba']
    
    for camada in ordem_camadas:
        if camada in componentes and os.path.exists(componentes[camada]):
            img_camada = Image.open(componentes[camada]).convert("RGBA")
            
            if base_img is None:
                base_img = img_camada
            else:
                base_img = Image.alpha_composite(base_img, img_camada)
    
    if base_img:
        base_img.save(output_path)
        print(f"Retrato falado gerado com sucesso em: {output_path}")
    else:
        print("Erro: Nenhum componente válido selecionado.")

if __name__ == "__main__":
    meus_componentes = {
        'face': '../assets/faces/formato_padrao.png',
        'olhos': '../assets/olhos/olhos_v1.png',
        'nariz': '../assets/nariz/nariz_v1.png',
        'boca': '../assets/boca/boca_v1.png',
        'cabelo': '../assets/cabelo/cabelo_curto.png'
    }
    
    gerar_retrato(meus_componentes)