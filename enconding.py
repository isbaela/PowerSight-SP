import chardet

# Caminho para o arquivo CSV
file_path = 'C:/Users/isabe/Downloads/interrupcoes-energia-eletrica-2022 (1).csv'

# Ler as primeiras 1000 bytes do arquivo para detecção de codificação
with open(file_path, 'rb') as f:
    sample = f.read(1000)  # Ler apenas os primeiros 1000 bytes

# Detectar a codificação da amostra
result = chardet.detect(sample)
encoding = result['encoding']
confidence = result['confidence']

print(f"Codificação detectada: {encoding}")
print(f"Confiança: {confidence}")
