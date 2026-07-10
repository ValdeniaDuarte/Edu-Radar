# -*- coding: utf-8 -*-
"""
Roda isso primeiro para saber quais feeds funcionam de verdade:

    python scripts/verificar_feeds.py

Não altera nenhum arquivo - só imprime um relatório na tela.
"""
import feedparser
import requests

from config import FONTES

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; EduRadarBot/1.0)"}


def testar_url(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return f"status HTTP {resp.status_code}"
        feed = feedparser.parse(resp.content)
        if not feed.entries:
            return "respondeu, mas 0 itens (provavelmente não é um feed RSS válido)"
        return f"OK - {len(feed.entries)} itens encontrados"
    except requests.RequestException as e:
        return f"erro de conexão: {e}"


def main():
    print("Testando feeds configurados...\n")
    for fonte in FONTES:
        print(f"### {fonte['nome']} ###")
        for url in fonte["candidatas"]:
            resultado = testar_url(url)
            marcador = "✅" if resultado.startswith("OK") else "❌"
            print(f"  {marcador} {url}")
            print(f"     -> {resultado}")
        print()


if __name__ == "__main__":
    main()
