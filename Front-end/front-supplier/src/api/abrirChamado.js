const URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const abrirChamado = async (dados) => {
  const res = await fetch(`${URL}/api/v1/open-desk`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dados),
  });

  if (!res.ok) {
    throw new Error("Erro ao abrir chamado");
  }

  const valores = await res.json();
  return valores.RITM;
};
