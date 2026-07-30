export const abrirChamado = async (dados) => {
  const res = await fetch("http://localhost:8000/api/v1/open-desk", {
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
