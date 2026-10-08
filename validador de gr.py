import requests
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Validador de LMG, GR e Mercadorias - TLOG / Sompo",
    page_icon="🛡️",
    layout="wide",
)

# Título da Aplicação
st.title("🛡️ Validador de LMG, Gerenciamento de Risco (GR) e Contêineres")
st.markdown(
    "Ferramenta integrada de consulta de limites, regras de embarcadores,"
    " mercadorias específicas da apólice e exigências de segurança."
)


# Função para buscar Estados (UFs) do Brasil via API do IBGE
@st.cache_data
def carregar_estados():
  try:
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome"
    response = requests.get(url)
    if response.status_code == 200:
      dados = response.json()
      return {uf["sigla"]: uf["nome"] for uf in dados}
  except:
    pass
  return {
      "PR": "Paraná",
      "SP": "São Paulo",
      "SC": "Santa Catarina",
      "RS": "Rio Grande do Sul",
      "RJ": "Rio de Janeiro",
      "MT": "Mato Grosso",
      "MA": "Maranhão",
  }


# Função para buscar Cidades de um Estado via API do IBGE
@st.cache_data
def carregar_cidades(uf_sigla):
  try:
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf_sigla}/municipios?orderBy=nome"
    response = requests.get(url)
    if response.status_code == 200:
      dados = response.json()
      return [cidade["nome"] for cidade in dados]
  except:
    pass
  return []


# Lista de Embarcadores com Regras Específicas
embarcadores_especiais = [
    "Nenhum (Usar Mercadoria Geral)",
    "RENAULT DO BRASIL, VOLVO E SCANIA EM CONTAINER",
]


# Dicionário Completo de Mercadorias Específicas (Extraído da Planilha Oficial)
mercadorias_limites_especificos = {
    "Selecione a Mercadoria...": (0.00, 0.00),
    "Aço e ferro em geral": (150000.00, 6000000.00),
    (
        "GLUCOSE / MALTOSE; CHOCOLATE LÍQUIDO OU EM MASSA; ÁCIDO CÍTRICO;"
        " GELATINA; AMIDOS"
    ): (450000.00, 4000000.00),
    "Álcool etílico e para fins medicinais / farmacêuticos": (
        150000.00,
        6000000.00,
    ),
    "Alumínio em geral": (150000.00, 6000000.00),
    "Artigos de higiene e limpeza, cosméticos e perfumaria": (
        150000.00,
        6000000.00,
    ),
    "Artigos esportivos": (150000.00, 6000000.00),
    "Autopeças em geral, inclusive para motocicleta": (200000.00, 6000000.00),
    "Balas, chocolates, chicletes e doces em geral": (150000.00, 6000000.00),
    "Baterias automotivas": (150000.00, 6000000.00),
    "Bebidas em geral, exceto cervejas e refrigerantes": (150000.00, 6000000.00),
    "Bobinas de papel": (150000.00, 6000000.00),
    "Brinquedos e bicicletas, partes, peças e acessórios": (
        150000.00,
        6000000.00,
    ),
    "Café de qualquer tipo": (150000.00, 4000000.00),
    (
        "Calçados (tênis, sapatos, chinelos, sandálias), solados, palmilhas e"
        " correias"
    ): (150000.00, 6000000.00),
    "Cartuchos para impressoras e copiadoras": (150000.00, 6000000.00),
    "Câmeras e Artigos fotográficos em geral": (150000.00, 6000000.00),
    "Carnes “in natura” e Charque de qualquer origem animal": (
        150000.00,
        6000000.00,
    ),
    "Carne de frango e porco congelada transportada em container": (
        170000.00,
        750000.00,
    ),
    "Cassiterita": (150000.00, 6000000.00),
    "CD´s, DVD´s, LD´s e Blue Ray": (150000.00, 6000000.00),
    (
        "Computadores em Geral, Notebooks, Desktops, Tablets, Teclados,"
        " Monitores, CPU, Processadores, Memórias, Kit Multimídia, Jogos e"
        " Semelhantes, Demais Periféricos e Demais Partes e Peças"
    ): (150000.00, 6000000.00),
    "Cervejas e Refrigerantes": (150000.00, 6000000.00),
    "Cobre de qualquer tipo": (150000.00, 350000.00),
    "Confecções, tecidos, fios têxteis e roupas prontas": (150000.00, 300000.00),
    "Eletrônicos em Geral e Eletrodomésticos": (200000.00, 1000000.00),
    "Embarcador Hexion Química do Brasil": (160000.00, 6000000.00),
    (
        "Embarcador CNH (somente pra partes e peças de máquinas e implementos"
        " agrícolas)"
    ): (150000.00, 2500000.00),
    "Empilhadeiras de qualquer tipo": (150000.00, 6000000.00),
    "Equipamentos e aparelhos de ginastica": (150000.00, 6000000.00),
    "Equipamento médico hospitalar": (150000.00, 6000000.00),
    "Fechaduras, ferragens em geral": (150000.00, 6000000.00),
    (
        "Ferramentas manuais ou elétricas (furadeiras, serras elétricas,"
        " lixadeiras, etc)"
    ): (200000.00, 6000000.00),
    "Fertilizantes e defensivos agrícolas": (150000.00, 6000000.00),
    "Fraldas descartáveis": (150000.00, 6000000.00),
    "Fibra óptica": (150000.00, 6000000.00),
    "Grãos, farinhas, farelos e sementes em geral (exceto café qualquer tipo)": (
        150000.00,
        6000000.00,
    ),
    "Lâmpadas, inclusive reatores, luminárias e periféricos": (
        150000.00,
        6000000.00,
    ),
    "Leite de qualquer tipo": (150000.00, 6000000.00),
    (
        "Materiais elétricos e montagem de rede de distribuição, painéis solares"
        " /fotovoltaicos"
    ): (150000.00, 6000000.00),
    (
        "Materiais elétricos, inclusive ferramentas, fios e cabos em geral (exceto"
        " cobre)"
    ): (150000.00, 6000000.00),
    "Materiais de escritório e escolar livros e revistas em geral": (
        150000.00,
        6000000.00,
    ),
    "Óleos lubrificantes": (150000.00, 6000000.00),
    (
        "Óleos Comestíveis, Óleos Vegetais, Azeites, Óleos Animais/Minerais/Sintéticos"
        " (AAK DO BRASIL)"
    ): (200000.00, 6000000.00),
    "Papel e celulose em geral (Exceto bobina de papel)": (
        150000.00,
        6000000.00,
    ),
    "Pilhas e baterias (exceto celulares)": (150000.00, 6000000.00),
    "Pneus e câmaras de ar": (200000.00, 1000000.00),
    "Produtos alimentícios em geral": (170000.00, 6000000.00),
    "Produtos farmacêuticos (exceto medicamentos)": (150000.00, 6000000.00),
    "Produtos ópticos em geral": (150000.00, 6000000.00),
    "Produtos químicos em geral (exceto de uso veterinário)": (
        150000.00,
        6000000.00,
    ),
    "Produtos siderúrgicos, latão e folha de flandres": (150000.00, 6000000.00),
    "Polímeros em geral": (150000.00, 6000000.00),
    "Rolamentos em geral": (200000.00, 6000000.00),
    "Tintas, vernizes, corantes, pigmentos e similares": (
        150000.00,
        6000000.00,
    ),
    "Transformadores/geradores pesados": (200000.00, 6000000.00),
    "Tratores de quaisquer tipos, máquinas e implementos agrícolas": (
        150000.00,
        1500000.00,
    ),
    "Zinco": (150000.00, 6000000.00),
    "Frango congelado (Geral)": (170000.00, 450000.00),
    "Suco Congelado transportado em containers": (0.00, 400000.00),
    "Racks para transporte de mercadorias": (0.00, 250000.00),
    "Pisos Cerâmicos, Vasilhames Garrafas de Vidro, Vidros de Qualquer Tipo": (
        0.00,
        200000.00,
    ),
    "Embarques de mercadorias em Pickup abertas": (0.00, 100000.00),
    (
        "Carne congelada, in natura, charque, Pescados em geral, Leite (qualquer"
        " tipo/pó/condensado)"
    ): (0.00, 900000.00),
}


# Função de Regras de GR principal corrigida para tratar rotas interestaduais gerais
def obter_regras_gr(
    uf_origem,
    uf_destino,
    cidade_origem,
    cidade_dest,
    valor_carga,
    limite_fixo,
    teto_maximo,
    embarcador_selecionado,
):
  if valor_carga > teto_maximo:
    return {
        "status": "ERRO",
        "mensagem": (
            f"O valor da carga (R$ {valor_carga:,.2f}) ultrapassa o Teto"
            f" Máximo da apólice/embarcador (R$ {teto_maximo:,.2f}). Exige Carga"
            " Esporádica."
        ),
    }

  # --- TRATAMENTO PARA RENAULT, VOLVO E SCANIA EM CONTAINER ---
  if embarcador_selecionado == "RENAULT DO BRASIL, VOLVO E SCANIA EM CONTAINER":
    origem_up = uf_origem.upper()
    destino_up = uf_destino.upper()
    cidade_o_up = cidade_origem.upper()
    cidade_d_up = cidade_dest.upper()

    no_parana = origem_up == "PR" and destino_up == "PR"

    isencao_pr = False
    cidades_eixo = ["PARANAGUÁ", "CURITIBA", "SÃO JOSÉ DOS PINHAIS", "ADRIANÓPOLIS", "AGUDOS DO SUL", "ALMIRANTE TAMANDARÉ", "ARAUCÁRIA", "BALSA NOVA", "BOCAIÚVA DO SUL", "CAMPINA GRANDE DO SUL", "CAMPO DO TENENTE", "CAMPO LARGO", "CAMPO MAGRO", "CERRO AZUL", "COLOMBO", "CONTENDA", "DOUTOR ULYSSES", "FAZENDA RIO GRANDE", "ITAPERUÇU", "LAPA", "MANDIRITUBA", "PIÊN", "PINHAIS", "PIRAQUARA", "QUATRO BARRAS", "QUITANDINHA", "RIO BRANCO DO SUL", "RIO NEGRO", "TIJUCAS DO SUL", "TUNAS DO PARANÁ"]
    if no_parana and (
        cidade_o_up in cidades_eixo and cidade_d_up in cidades_eixo
    ):
      if valor_carga <= 1500000.00:
        isencao_pr = True

    if no_parana:
      if valor_carga <= 200000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": (
                "Não exigido"
                if not isencao_pr
                else "Isento (Até R$ 1.5M Paranaguá x Curitiba)"
            ),
            "isca": "Não exigido",
            "escolta": "Não exigido",
        }
      elif valor_carga <= 3000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": (
                "Sim"
                if not isencao_pr
                else "Isento (Até R$ 1.5M Paranaguá x Curitiba)"
            ),
            "isca": "Não exigido",
            "escolta": "Proibido modo Sleep | Pernoite a cada 30 min",
        }
      elif valor_carga <= 8000000.00:
        return {
            "status": "OK",
            "consulta": "Sim"
            if not isencao_pr
            else "Isento (Até R$ 1.5M Paranaguá x Curitiba)",
            "monitoramento": "Sim",
            "isca": (
                "1 Isca OU Eqpto. Fixo Redundante RF OU Rastr. Contingência"
                " OU Imobilizador"
            ),
            "escolta": (
                "Escolta Armada (ou opções da coluna anterior) | Pernoite a cada"
                " 30 min"
            ),
        }
      elif valor_carga <= 10000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "1 Isca / Eqpto. Móvel - Fixo Redundante RF",
            "escolta": (
                "Escolta Armada (substituível por Imobilizador, 1 Fiscal de"
                " Rota ou Trava de Porta Container)"
            ),
        }
      else:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "1 Isca / Eqpto. Móvel - Fixo Redundante RF",
            "escolta": (
                "Escolta Armada / Análise especial acima de R$ 10.000.000,00"
            ),
        }
    else:
      if valor_carga <= 200000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Não exigido",
            "isca": "Não exigido",
            "escolta": "Não exigido",
        }
      elif valor_carga <= 3000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "Não exigido",
            "escolta": (
                "🚨 **PROIBIDO AUTÔNOMO** | Pernoite a cada 30 min"
            ),
        }
      elif valor_carga <= 6000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": (
                "1 Isca OU Fixo Redundante RF OU Rastr. Contingência OU"
                " Imobilizador"
            ),
            "escolta": (
                "🚨 **PROIBIDO AUTÔNOMO** | Escolta Armada (ou opções da"
                " coluna anterior)"
            ),
        }
      elif valor_carga <= 8000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "1 Isca / Eqpto. Móvel - Fixo Redundante RF",
            "escolta": (
                "🚨 **PROIBIDO AUTÔNOMO** E Escolta Armada (substituível por"
                " Imobilizador Inteligente OU 1 Fiscal de Rota)"
            ),
        }
      elif valor_carga <= 10000000.00:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "1 Isca / Eqpto. Móvel - Fixo Redundante RF",
            "escolta": (
                "🚨 **PROIBIDO AUTÔNOMO** E Imobilizador Inteligente/Trava"
                " Eletrônica E Escolta Armada (substituível por Fiscal de Rota)"
            ),
        }
      else:
        return {
            "status": "OK",
            "consulta": "Sim",
            "monitoramento": "Sim",
            "isca": "1 Isca / Eqpto. Móvel",
            "escolta": (
                "Análise especial para valores acima de R$ 10.000.000,00"
            ),
        }

  # --- REGRAS PADRÃO POR MERCADORIA ESPECÍFICA (Aplica-se a PRxPR ou Interestadual Geral) ---
  is_pr_pr = uf_origem == "PR" and uf_destino == "PR"

  if is_pr_pr:
    if valor_carga <= limite_fixo:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Não exigido",
          "isca": "Não exigido",
          "escolta": "Não exigido",
      }
    elif valor_carga <= 600000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": "Não exigido",
          "escolta": "Proibido modo Sleep | Pernoite a cada 30 min",
      }
    elif valor_carga <= 1200000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": (
              "1 Isca OU Rastreador Redundante RF OU Escolta Armada OU"
              " Imobilizador Inteligente"
          ),
          "escolta": "Proibido modo Sleep | Pernoite a cada 30 min",
      }
    elif valor_carga <= 2500000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": (
              "1 Isca OU Rastreador Redundante RF OU Escolta Armada OU"
              " Imobilizador Inteligente"
          ),
          "escolta": (
              "+ Rastreador Redundante RF OU Escolta Armada OU Imobilizador"
              " Inteligente\n🚨 **PROIBIDA RODAGEM 22H ÀS 05H**"
          ),
      }
    else:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": (
              "1 Isca OU Rastreador Redundante RF OU Imobilizador"
              " Inteligente"
          ),
          "escolta": (
              "Rastreador Redundante RF OU Trava Eletrônica + Imobilizador"
              " OU Escolta Armada + Trava de 5ª Roda OU Bloqueador de Carreta"
              " OU Cadeado Inteligente\n🚨 **PROIBIDA RODAGEM 22H ÀS 05H**"
          ),
      }
  else:
    # Regra Interestadual Geral (inclui saídas do PR para outros estados como MA, SP, etc.)
    if valor_carga <= limite_fixo:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Não exigido",
          "isca": "Não exigido",
          "escolta": "Não exigido",
      }
    elif valor_carga <= 600000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": "Não exigido",
          "escolta": "PROIBIDO AUTÔNOMO | Modo Sleep proibido",
      }
    elif valor_carga <= 1200000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": (
              "1 Isca OU Redundante RF OU Escolta Armada OU Imobilizador"
          ),
          "escolta": "PROIBIDO AUTÔNOMO | Pernoite 30 min",
      }
    elif valor_carga <= 2000000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": (
              "Redundante RF OU Escolta Armada OU Imobilizador Inteligente"
          ),
          "escolta": (
              "PROIBIDO AUTÔNOMO\n🚨 **PROIBIDA RODAGEM 22H ÀS 05H**"
          ),
      }
    elif valor_carga <= 2500000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": "1 Isca (Rastreador Móvel)",
          "escolta": (
              "Redundante RF / Imobilizador + Trava de 5ª Roda / Bloqueador\n🚨"
              " **PROIBIDO AUTÔNOMO**\n🚨 **PROIBIDA RODAGEM 22H ÀS 05H**"
          ),
      }
    elif valor_carga <= 4000000.00:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": "1 Isca / Redundante RF OU Imobilizador",
          "escolta": (
              "Escolta Armada (OU POS Adicional de 10% sem Escolta) + Trava de"
              " 5ª Roda\n🚨 **PROIBIDO AUTÔNOMO**\n🚨 **PROIBIDA RODAGEM 22H ÀS"
              " 05H**"
          ),
      }
    else:
      return {
          "status": "OK",
          "consulta": "Sim",
          "monitoramento": "Sim",
          "isca": "1 Isca / Redundante RF OU Imobilizador",
          "escolta": (
              "Escolta Armada OU Fiscal de Rota + Trava de 5ª Roda\n🚨"
              " **PROIBIDO AUTÔNOMO**\n🚨 **PROIBIDA RODAGEM 22H ÀS 05H**"
          ),
      }


# Carregar estados do IBGE
estados_dict = carregar_estados()
lista_ufs = list(estados_dict.keys())

# Barra lateral
st.sidebar.header("🔍 Parâmetros da Consulta")

uf_origem = st.sidebar.selectbox(
    "UF de Coleta (Origem):",
    lista_ufs,
    index=lista_ufs.index("PR") if "PR" in lista_ufs else 0,
)
cidades_origem = carregar_cidades(uf_origem)
cidade_origem = st.sidebar.selectbox(
    "Cidade de Origem:", cidades_origem if cidades_origem else ["Selecione..."]
)

uf_destino = st.sidebar.selectbox(
    "UF de Entrega (Destino):",
    lista_ufs,
    index=lista_ufs.index("MA") if "MA" in lista_ufs else 0,
)
cidades_destino = carregar_cidades(uf_destino)
cidade_destino = st.sidebar.selectbox(
    "Cidade de Destino:",
    cidades_destino if cidades_destino else ["Selecione..."],
)

st.sidebar.markdown("---")
st.sidebar.subheader("🏢 Área de Embarcador")
embarcador_selecionado = st.sidebar.selectbox(
    "Selecione o Embarcador (Regra Especial):", embarcadores_especiais
)

if embarcador_selecionado != "Nenhum (Usar Mercadoria Geral)":
  limite_fixo, teto_maximo = 0.00, 10000000.00
  mercadoria_selecionada = embarcador_selecionado
  st.sidebar.info(f"Regra ativa para o embarcador: **{embarcador_selecionado}**")
else:
  mercadoria_selecionada = st.sidebar.selectbox(
      "Mercadoria Específica:", list(mercadorias_limites_especificos.keys())
  )
  if mercadoria_selecionada in mercadorias_limites_especificos:
    limite_fixo, teto_maximo = mercadorias_limites_especificos[
        mercadoria_selecionada
    ]
  else:
    limite_fixo, teto_maximo = 150000.00, 6000000.00

valor_carga = st.sidebar.number_input(
    "Valor Informado da Carga (R$):",
    min_value=0.0,
    value=2010000.0,
    step=10000.0,
    format="%.2f",
)

consultar = st.sidebar.button(
    "📋 Consultar Regras e GR", type="primary", use_container_width=True
)

if not consultar:
  st.info(
      "👈 Configure a rota, selecione o embarcador ou mercadoria específica,"
      " informe o valor da carga e clique em **'Consultar Regras e GR'**."
  )
else:
  st.markdown(
      f"### 📍 Rota: `{cidade_origem} / {uf_origem}` ➔"
      f" `{cidade_destino} / {uf_destino}` | Seleção:"
      f" `{mercadoria_selecionada}`"
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(label="Valor da Carga", value=f"R$ {valor_carga:,.2f}")
  with col2:
    st.metric(label="Limite Fixado", value=f"R$ {limite_fixo:,.2f}")
  with col3:
    st.metric(label="Teto Máximo", value=f"R$ {teto_maximo:,.2f}")

  st.markdown("---")

  resultado_gr = obter_regras_gr(
      uf_origem,
      uf_destino,
      cidade_origem,
      cidade_destino,
      valor_carga,
      limite_fixo,
      teto_maximo,
      embarcador_selecionado,
  )

  if resultado_gr["status"] == "ERRO":
    st.error(f"🚨 **ATENÇÃO:** {resultado_gr['mensagem']}")
  else:
    st.success(
        "✅ O valor da carga está dentro do Teto Máximo permitido para esta"
        " operação."
    )

    st.markdown("### 📋 Requisitos de Gerenciamento de Risco (GR)")

    col_a, col_b = st.columns(2)
    with col_a:
      st.markdown(
          f"* **Consulta Obrigatória:** `{resultado_gr['consulta']}`"
      )
      st.markdown(
          f"* **Monitoramento:** `{resultado_gr['monitoramento']}`"
      )
    with col_b:
      st.markdown(
          f"* **Isca / Eqpto. Móvel / Tecnologias:**"
          f" `{resultado_gr['isca']}`"
      )
      st.markdown(
          f"* **Escolta / Dispositivos Adicionais:**"
          f" `{resultado_gr['escolta']}`"
      )
