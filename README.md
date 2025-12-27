# Supplier Automation

## Visão Geral

O Supplier Automation é um sistema web para automação de processos envolvendo fornecedores e clientes, com foco na integração dos dados entre rotinas automatizadas em Python e interfaces HTML/CSS. O sistema gera páginas HTML dinâmicas a partir das informações processadas em Python, e transfere dados (como dados de clientes e fornecedores) para um banco de dados interno, facilitando consultas, edições e automatização de rotinas. Também utiliza dataframes para organizar e manipular dados de forma eficiente.

---

## Estrutura do Projeto

- **scripts/**  
  Scripts Python para automação, geração de páginas HTML dinâmicas, manipulação de dados com dataframes e interface principal.
- **assets/**  
  Arquivos CSS e HTML usados para estilização e exibição das páginas.
- **doc/**  
  Documentação explicativa sobre os módulos, requisitos funcionais (RF) e não funcionais (RNF), e orientações de uso.

---

## Ferramentas Utilizadas

<p>
  <img src="https://skillicons.dev/icons?i=py" alt="Python" height="48">
  <img src="https://skillicons.dev/icons?i=vscode" alt="VSCode" height="48">
  <img src="https://skillicons.dev/icons?i=html" alt="HTML" height="48">
  <img src="https://skillicons.dev/icons?i=css" alt="CSS" height="48">
  <img src="https://skillicons.dev/icons?i=js" alt="CSS" height="48">
</p>

---

## Funcionalidades

1. **Cadastro de Fornecedores e Clientes**
   - Interface HTML para registro de dados de fornecedores e clientes.
   - Campos para empresa, contato, produtos, prazos, observações, cliente, endereço, etc.

2. **Automação de Processos**
   - Scripts Python para importar, processar e exportar dados entre HTML e banco de dados.
   - Rotinas integradas que facilitam o transporte das informações do HTML para o banco.

3. **Geração de Relatórios Dinâmicos**
   - Uso de dataframes (Pandas) para criar relatórios e dashboards automatizados.
   - Visualizações exportáveis ou exibidas direto no HTML.

4. **Consulta e Atualização**
   - Busca por nome, CNPJ, produto, cliente etc.
   - Edição ágil dos registros existentes via formulários HTML dinâmicos.

5. **Interface Amigável**
   - Navegação intuitiva com menus laterais e formulários responsivos.
   - Personalização visual via CSS.

---

## Fluxo do Usuário

1. Usuário acessa o sistema web.
2. Realiza cadastro ou login (se aplicável).
3. Escolhe operação no menu (cadastrar, consultar, automatizar, relatar).
4. Preenche formulários ou aciona rotinas automáticas.
5. Informações são transferidas via scripts Python para HTML e para o banco de dados.
6. Relatórios podem ser visualizados ou exportados através do HTML.
7. Encerra sessão.

---

## Banco de Dados

- **Fornecedor:** id_fornecedor, empresa, contato, produto, prazo_entrega, observações
- **Cliente:** id_cliente, nome, contato, endereço, produto, status
- Outros dados exportados dos formulários/relatórios HTML são mantidos no banco via rotinas Python.

Scripts de criação e manutenção dos dados estão disponíveis em `scripts/`.

---

## Instruções de Uso

1. Instale as dependências principais com `pip install -r requirements.txt`.
2. Configure os arquivos de ambiente e banco conforme especificado na documentação.
3. Execute o sistema Python principal para iniciar a automação, integração HTML/banco, ou gerar relatórios.

---

## Observações Importantes

- Não foi utilizado Figma ou modelagem formal de dados.
- Tudo é gerado e manipulado dinamicamente via scripts Python.
- Dataframes facilitam a automação e análise dos dados.

---

## Contribuições

O Supplier Automation resolve gargalos comuns na comunicação e automação com fornecedores e clientes.  
A equipe recebe sugestões para novas funcionalidades, integrações ou melhorias. Para contato profissional ou customizações, veja abaixo.

---

**Equipe Supplier Automation**  
<p style="text-align: left;">
  <a href="https://www.linkedin.com/in/arthur-resende-gomes-3312bb305" target="_blank" style="box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5); display: inline-block; margin: 10px; border-radius: 8px; overflow: hidden;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" height="48" width="48" alt="LinkedIn" style="border-radius: 8px; background: #fff; padding: 4px; box-shadow: 2px 2px 8px #000;" />
  </a>
</p>
