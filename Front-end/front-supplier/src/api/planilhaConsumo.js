export const planilhaConsumo = async (planilha) => {
  const formData = new FormData();
  formData.append("file", planilha);
  const res = await fetch("http://localhost:8000/api/v1/transform-file", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Erro ao processar");
  }

  const dados = await res.json();
  return dados.Result;
};
