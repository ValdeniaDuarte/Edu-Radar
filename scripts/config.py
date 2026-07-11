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
    {
        "nome": "Estudar Fora",
        "confianca": "alta (WordPress confirmado) - foco em bolsas no exterior",
        "candidatas": [
            "https://www.estudarfora.org.br/feed/",
        ],
    },
    {
        "nome": "Hora Brasil",
        "confianca": "confirmada - conteúdo muito alinhado (cursos gratuitos, EAD, editais)",
        "candidatas": [
            "https://www.horabrasil.com.br/feed/",
        ],
    },
    {
        "nome": "MEC (Ministério da Educação)",
        "confianca": "não confirmada - portais gov.br variam o padrão de RSS por ministério",
        "candidatas": [
            "https://www.gov.br/mec/pt-br/assuntos/noticias/RSS",
            "https://www.gov.br/mec/pt-br/assuntos/noticias/site-feed",
        ],
    },
]

# --- Palavras-chave "fortes" -----------------------------------------------
# Específicas o suficiente para valerem SOZINHAS, mesmo em sites de
# assunto geral (baixo risco de falso positivo).
PALAVRAS_FORTES = [
    "vaga para curso",
    "vagas para curso",
    "vagas para cursos",
    "graduação",
    "pós-graduação",
    "pós graduação",
    "pos-graduacao",
    "mba",
    "especialização",
    "especializacao",
    "curso gratuito",
    "curso gratuita",
    "cursos gratuitos",
    "curso ead",
    "cursos ead",
    "curso a distância",
    "cursos a distância",
    "bolsa de estudo",
    "bolsas de estudo",
    "bolsa de estudos",
    "bolsas de estudos",
    "bolsa integral",
    "bolsa parcial",
]

# --- Palavras-chave "fracas" ------------------------------------------------
# Ambíguas por natureza (tem outros significados comuns fora do contexto
# educacional). Só contam se o texto TAMBÉM tiver uma palavra de
# PALAVRAS_REFORCO por perto (veja bate_filtro em fetch_news.py).
PALAVRAS_FRACAS = [
    "bolsa",
    "bolsas",
    "edital",
    "editais",
    "ead",
    "gratuito",
    "gratuita",
    "online",
    "remoto",
    "a distância",
    "a distancia",
]

# Palavras que "confirmam" que uma palavra fraca está em contexto educacional.
PALAVRAS_REFORCO = [
    "curso",
    "cursos",
    "faculdade",
    "universidade",
    "instituto federal",
    "aluno",
    "alunos",
    "estudante",
    "estudantes",
    "matrícula",
    "matriculas",
    "matrículas",
    "aula",
    "aulas",
    "graduação",
    "professor",
    "ensino",
]

# --- Palavras-chave de exclusão -------------------------------------------
# Se qualquer uma destas aparecer, a notícia é descartada de qualquer
# forma - mesmo que também bata nas listas acima. Serve tanto para tirar
# vagas de emprego "puras" quanto os falsos positivos mais comuns
# (bolsa de valores, edital de licitação, etc).
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
    "bolsa de valores",
    "ibovespa",
    "b3",
    "pregão da bolsa",
    "ações da bolsa",
    "edital de licitação",
    "licitação",
    "pregão eletrônico",
    "trabalho remoto",
    "home office",
    "controle remoto",
]

# Quantos dias de notícias manter no arquivo final (evita acumular lixo antigo)
DIAS_RETENCAO = 30
