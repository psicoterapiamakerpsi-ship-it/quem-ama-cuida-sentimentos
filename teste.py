# SCRIPT FINAL — Análise de sentimento dos tweets
import json
import re
import csv
from pysentimiento import create_analyzer

# Função de limpeza
def limpar_texto(texto):
    texto = re.sub(r'https?://\S+', '', texto)
    texto = re.sub(r'@\S+', '', texto)
    texto = re.sub(r'#\S+', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

# Carrega o modelo
print("Carregando modelo... aguarde!")
analisador = create_analyzer(task="sentiment", lang="pt")
print("Modelo carregado! Iniciando análise...\n")

# Lê os tweets e analisa
resultados = []
total = 0
erros = 0

with open("data.ndjson", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue
        try:
            tweet = json.loads(linha)
            legacy = tweet.get("legacy", {})
            texto_original = legacy.get("full_text", "")
            texto_limpo = limpar_texto(texto_original)

            if not texto_limpo:
                continue

            # Analisa o sentimento
            resultado = analisador.predict(texto_limpo)

            resultados.append({
                "id": tweet.get("rest_id", ""),
                "data": legacy.get("created_at", ""),
                "texto_original": texto_original,
                "texto_limpo": texto_limpo,
                "sentimento": resultado.output,
                "prob_positivo": round(resultado.probas["POS"], 4),
                "prob_negativo": round(resultado.probas["NEG"], 4),
                "prob_neutro": round(resultado.probas["NEU"], 4),
                "likes": legacy.get("favorite_count", 0),
                "retweets": legacy.get("retweet_count", 0),
            })

            total += 1
            if total % 100 == 0:
                print(f"Analisados: {total} tweets...")

        except Exception as e:
            erros += 1

# Salva o CSV
with open("resultado_sentimentos.csv", "w", newline="", encoding="utf-8-sig") as f:
    campos = ["id","data","texto_original","texto_limpo","sentimento",
              "prob_positivo","prob_negativo","prob_neutro","likes","retweets"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(resultados)

print(f"\n✓ Análise concluída!")
print(f"  Tweets analisados: {total}")
print(f"  Erros: {erros}")
print(f"  Arquivo salvo: resultado_sentimentos.csv")