# -*- coding: utf-8 -*-
"""
Edu Radar - coleta e filtro de notícias educacionais.

O que este script faz:
1. Lê a lista de fontes em config.py
2. Para cada fonte, tenta buscar o feed RSS (com fallback entre candidatas)
3. Filtra cada item pelas palavras de inclusão/exclusão
4. Junta tudo, remove duplicatas e itens antigos
5. Salva o resultado em data/noticias.json (lido pelo site estático)

Roda tanto localmente (python scripts/fetch_news.py) quanto dentro do
GitHub Actions.
"""
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests

from config import FONTES, PALAVRAS_INCLUIR, PALAVRAS_EXCLUIR, DIAS_RETENCAO

ROOT = Path(__file__).resolve().parent.parent
SAIDA_JSON = ROOT / "data" / "noticias.json"
LOG_PATH = ROOT / "data" / "ultimo_log.txt"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; EduRadarBot/1.0; "
        "+https://github.com/) EduRadar-RSS-Reader"
    )
}
TIMEOUT_SEGUNDOS = 15


def log(msg, linhas_log):
    print(msg)
    linhas_log.append(msg)


def bate_filtro(texto):
    """Retorna True se o texto passa no filtro de inclusão/exclusão."""
    texto_lower = texto.lower()

    if any(palavra in texto_lower for palavra in PALAVRAS_EXCLUIR):
        return False

    return any(palavra in texto_lower for palavra in PALAVRAS_INCLUIR)


def buscar_feed(candidatas, linhas_log):
    """Tenta cada URL candidata até uma funcionar. Retorna (url_usada, feed) ou (None, None)."""
    for url in candidatas:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT_SEGUNDOS)
            if resp.status_code == 200:
                feed = feedparser.parse(resp.content)
                if feed.entries:
                    return url, feed
                else:
                    log(f"  [aviso] {url} respondeu 200 mas sem itens no feed.", linhas_log)
            else:
                log(f"  [aviso] {url} respondeu status {resp.status_code}.", linhas_log)
        except requests.RequestException as e:
            log(f"  [erro] falha ao buscar {url}: {e}", linhas_log)
    return None, None


def processar_fonte(fonte, linhas_log):
    nome = fonte["nome"]
    log(f"\n=== Fonte: {nome} (confiança: {fonte['confianca']}) ===", linhas_log)

    url_usada, feed = buscar_feed(fonte["candidatas"], linhas_log)
    if not feed:
        log(f"  [FALHOU] Nenhuma URL candidata funcionou para {nome}.", linhas_log)
        return []

    log(f"  [OK] Usando: {url_usada} ({len(feed.entries)} itens no feed)", linhas_log)

    itens_filtrados = []
    for entry in feed.entries:
        titulo = entry.get("title", "")
        resumo = entry.get("summary", "") or entry.get("description", "")
        texto_completo = f"{titulo} {resumo}"

        if not bate_filtro(texto_completo):
            continue

        link = entry.get("link", "")
        publicado = entry.get("published", "") or entry.get("updated", "")

        itens_filtrados.append(
            {
                "titulo": titulo.strip(),
                "resumo": resumo.strip()[:300],
                "link": link,
                "fonte": nome,
                "publicado": publicado,
            }
        )

    log(f"  -> {len(itens_filtrados)} itens passaram no filtro de palavras-chave.", linhas_log)
    return itens_filtrados


def carregar_noticias_existentes():
    if SAIDA_JSON.exists():
        try:
            with open(SAIDA_JSON, "r", encoding="utf-8") as f:
                return json.load(f).get("noticias", [])
        except (json.JSONDecodeError, OSError):
            return []
    return []


def main():
    linhas_log = []
    log(f"Edu Radar - execução iniciada em {datetime.now(timezone.utc).isoformat()}", linhas_log)

    novas_noticias = []
    for fonte in FONTES:
        novas_noticias.extend(processar_fonte(fonte, linhas_log))
        time.sleep(1)  # gentileza com os servidores das fontes

    existentes = carregar_noticias_existentes()

    # Junta novas + existentes, removendo duplicatas por link
    vistos = set()
    todas = []
    for item in novas_noticias + existentes:
        chave = item["link"]
        if chave and chave not in vistos:
            vistos.add(chave)
            todas.append(item)

    # (Opcional/simplificado) mantém só as últimas 300 notícias no arquivo,
    # já que datas em formatos variados entre feeds dificultam um corte
    # confiável só por DIAS_RETENCAO.
    todas = todas[:300]

    SAIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(SAIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(
            {
                "atualizado_em": datetime.now(timezone.utc).isoformat(),
                "total": len(todas),
                "noticias": todas,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    log(f"\nTotal final salvo em noticias.json: {len(todas)}", linhas_log)

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas_log))


if __name__ == "__main__":
    main()
