# Edu Radar

Site que agrega automaticamente notícias sobre **cursos, bolsas, graduação,
pós-graduação, MBA, especialização e EAD gratuitos**, filtrando fora vagas
de emprego comuns. Atualiza sozinho a cada 6 horas.

## 1. Testar os feeds antes de publicar (recomendado)

Se você tiver Python instalado na sua máquina:

```bash
cd edu-radar
pip install -r requirements.txt
python scripts/verificar_feeds.py
```

Isso mostra quais das URLs configuradas em `scripts/config.py` realmente
funcionam. Os feeds do **Na Prática**, **PEBSP** e **CPG Click Petróleo e
Gás** já foram confirmados. Os demais (Intercarreira, InfoEducação, CIEE,
IFRS, IFMG, CNN Brasil) estão como "melhor palpite" e podem precisar de
ajuste — se algum falhar, procure no próprio site por "RSS" ou "feed" no
rodapé, ou me mande o link que eu ajusto o `config.py`.

## 2. Subir para o GitHub

1. Crie um repositório novo no GitHub (pode ser público — assim o
   GitHub Actions roda com minutos ilimitados).
2. Suba todos os arquivos desta pasta para o repositório.
3. Vá em **Settings → Actions → General → Workflow permissions** e marque
   **"Read and write permissions"** (necessário para o robô conseguir
   salvar as notícias novas automaticamente).
4. Vá em **Settings → Pages**, em "Source" escolha **branch main, pasta /
   (root)**, e salve. Em alguns minutos seu site estará em
   `https://SEU-USUARIO.github.io/NOME-DO-REPO/`.

## 3. Rodar a primeira coleta manualmente

Não precisa esperar 6 horas: vá na aba **Actions** do repositório, clique
em "Atualizar noticias do Edu Radar" e depois em **"Run workflow"**. Em
menos de um minuto o `data/noticias.json` é atualizado e o site já mostra
as notícias.

## 4. Ajustar palavras-chave ou fontes

Tudo fica em `scripts/config.py`:
- `FONTES`: lista de sites e suas URLs de feed.
- `PALAVRAS_INCLUIR`: uma notícia só entra se bater com pelo menos uma.
- `PALAVRAS_EXCLUIR`: some se bater com qualquer uma dessas, mesmo que
  também bata em `PALAVRAS_INCLUIR` (é o que tira vagas de emprego puras).

Depois de editar, o próximo ciclo automático (ou um "Run workflow" manual)
já aplica as mudanças.

## Estrutura do projeto

```
edu-radar/
├── .github/workflows/update.yml   → agenda a coleta automática (cron)
├── scripts/
│   ├── config.py                  → fontes e palavras-chave
│   ├── fetch_news.py               → busca, filtra e salva o JSON
│   └── verificar_feeds.py          → testa as URLs sem alterar nada
├── data/noticias.json              → dados exibidos no site (gerado)
├── index.html / assets/            → o site em si (cards, busca, filtro)
└── requirements.txt
```
