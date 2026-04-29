## Como Executar
1. Instale as dependências executando: `pip install -r requirements.txt`
2. Execute o extrator para fatiar toda a base de dados e popular a pasta assets (necessário apenas na primeira execução ou caso atualize o dataset): `python src/extrator_automatico.py`

### Interface Desktop
3. Inicie o painel desktop: `python src/interface.py`

### Interface Web (dois PCs em rede)
3. Inicie o servidor web: `python src/app.py`
4. **Testemunha:** acessa `http://IP_DO_SERVIDOR:5000` para montar o retrato falado.
5. **Investigador:** acessa `http://IP_DO_SERVIDOR:5000/investigador` em outro PC para receber os suspeitos em tempo real.