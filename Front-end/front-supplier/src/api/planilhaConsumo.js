export const planilhaConsumo = async (planilha) => {
  const formData = new FormData();
  formData.append("file", planilha);
  const res = await fetch("http://localhost:8000/api/v1/transform-file", {
    method: "POST",
    body: formData,
  });

  if (res.status == 400) {
    throw new Error(
      "Verifique se a sua planilha tem os campos com esses nomes: Solicitante, Matricula, Valor, Colaborador",
    );
  }

  if (!res.ok) {
    throw new Error("Erro ao processar");
  }

  const dados = await res.json();
  return dados.Result;
};
