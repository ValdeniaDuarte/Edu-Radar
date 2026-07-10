const grade = document.getElementById("grade");
const busca = document.getElementById("busca");
const filtroFonte = document.getElementById("filtroFonte");
const statusEl = document.getElementById("statusAtualizacao");

let todasNoticias = [];

function formatarData(iso) {
  if (!iso) return "";
  const d = new Date(iso);
  if (isNaN(d)) return iso; // alguns feeds tem formatos diferentes; mostra cru se nao parsear
  return d.toLocaleDateString("pt-BR", { day: "2-digit", month: "short", year: "numeric" });
}

function renderizar() {
  const termo = busca.value.trim().toLowerCase();
  const fonteSelecionada = filtroFonte.value;

  const filtradas = todasNoticias.filter((n) => {
    const bateBusca =
      !termo ||
      n.titulo.toLowerCase().includes(termo) ||
      (n.resumo || "").toLowerCase().includes(termo);
    const bateFonte = !fonteSelecionada || n.fonte === fonteSelecionada;
    return bateBusca && bateFonte;
  });

  grade.innerHTML = "";

  if (filtradas.length === 0) {
    grade.innerHTML = '<p class="vazio">Nenhuma noticia encontrada com esse filtro.</p>';
    return;
  }

  for (const n of filtradas) {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <span class="fonte">${n.fonte}</span>
      <h3><a href="${n.link}" target="_blank" rel="noopener">${n.titulo}</a></h3>
      <p>${n.resumo || ""}</p>
      <span class="data">${formatarData(n.publicado)}</span>
    `;
    grade.appendChild(card);
  }
}

async function carregar() {
  try {
    const resp = await fetch("data/noticias.json?_=" + Date.now());
    const dados = await resp.json();

    todasNoticias = dados.noticias || [];

    const fontesUnicas = [...new Set(todasNoticias.map((n) => n.fonte))].sort();
    for (const f of fontesUnicas) {
      const opt = document.createElement("option");
      opt.value = f;
      opt.textContent = f;
      filtroFonte.appendChild(opt);
    }

    statusEl.textContent = dados.atualizado_em
      ? `Ultima atualizacao: ${new Date(dados.atualizado_em).toLocaleString("pt-BR")} · ${dados.total} noticias`
      : "";

    renderizar();
  } catch (e) {
    grade.innerHTML = '<p class="vazio">Ainda nao ha dados. Rode o script de coleta ou aguarde a primeira execucao automatica.</p>';
  }
}

busca.addEventListener("input", renderizar);
filtroFonte.addEventListener("change", renderizar);

carregar();
