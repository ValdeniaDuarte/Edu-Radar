# -*- coding: utf-8 -*-
"""
Configuração central do Edu Radar.

FONTES: cada site pode ter mais de uma URL candidata de feed RSS.
O script tenta a primeira; se falhar, tenta a próxima da lista.
Marque o campo "confianca" para saber quais já foram confirmadas
e quais são "melhor palpite" (padrão comum de WordPress: /feed/).
"""

FONTES = [
    {
        "nome": "Na Prática",
        "confianca": "confirmada",
        "candidatas": [
            "https://www.napratica.org.br/feed/",
        ],
    },
    {
        "nome": "PEBSP",
        "confianca": "alta (WordPress confirmado)",
        "candidatas": [
            "https://www.pebsp.com/feed/",
        ],
    },
    {
        "nome": "Intercarreira",
        "confianca": "não confirmada - palpite padrão",
        "candidatas": [
            "https://www.intercarreira.com.br/feed/",
            "https://intercarreira.com.br/feed/",
        ],
    },
    {
        "nome": "InfoEducação",
        "confianca": "não confirmada - domínio precisa ser checado",
        "candidatas": [
            "https://www.infoeducacao.com.br/feed/",
            "https://infoeducacao.com.br/feed/",
        ],
    },
    {
        "nome": "CIEE",
        "confianca": "não confirmada - site institucional, pode não ter /feed/",
        "candidatas": [
            "https://www.ciee.org.br/feed/",
            "https://www.ciee.org.br/portal/feed/",
        ],
    },
    {
        "nome": "IFRS",
        "confianca": "não confirmada - portais de institutos federais variam muito",
        "candidatas": [
            "https://ifrs.edu.br/feed/",
            "https://www.ifrs.edu.br/feed/",
        ],
    },
    {
        "nome": "IFMG",
        "confianca": "não confirmada - portais de institutos federais variam muito",
        "candidatas": [
            "https://www.ifmg.edu.br/feed/",
            "https://ifmg.edu.br/feed/",
        ],
    },
    {
        "nome": "CPG Click Petróleo e Gás",
        "confianca": "alta (WordPress confirmado)",
        "candidatas": [
            "https://clickpetroleoegas.com.br/feed/",
        ],
    },
    {
        "nome": "CNN Brasil",
        "confianca": "não confirmada - feed geral, vai exigir filtro rígido",
        "candidatas": [
            "https://www.cnnbrasil.com.br/feed/",
        ],
    },
]

# --- Palavras-chave de inclusão -------------------------------------------
# Uma notícia passa no filtro se o título OU resumo contiver PELO MENOS
# UMA destas palavras/expressões (case-insensitive).
PALAVRAS_INCLUIR = [
    "vaga para curso",
    "vagas para curso",
    "vagas para cursos",
    "bolsa",
    "bolsas",
    "graduação",
    "pós-graduação",
    "pós graduação",
    "pos-graduacao",
    "mba",
    "especialização",
    "especializacao",
    "edital",
    "editais",
    "ead",
    "a distância",
    "a distancia",
    "gratuito online",
    "gratuita online",
    "curso gratuito",
    "curso gratuita",
    "remoto",
]

# --- Palavras-chave de exclusão -------------------------------------------
# Mesmo que uma notícia bata em PALAVRAS_INCLUIR, ela é descartada se
# também contiver qualquer uma destas expressões (para tirar vagas de
# emprego "puras", que não são sobre cursos/formação).
PALAVRAS_EXCLUIR = [
    "vaga de emprego",
    "vagas de emprego",
    "contratação imediata",
    "contrata-se",
    "clt",
    "estágio remunerado",
    "recrutamento e seleção",
    "processo seletivo simplificado para contratar",
    "carteira assinada",
]

# Quantos dias de notícias manter no arquivo final (evita acumular lixo antigo)
DIAS_RETENCAO = 30
