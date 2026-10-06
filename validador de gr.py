import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Validador de LMG e GR - Apólice Sompo",
    page_icon="🛡️",
    layout="wide",
)

# Título da Aplicação
st.title("🛡️ Validador de LMG e Gerenciamento de Risco (GR)")
st.markdown(
    "Ferramenta profissional de validação baseada nos limites específicos,"
    " limites máximos por mercadoria e regras da apólice Sompo."
)

# 1. Dicionário de EMBARCADORES ESPECÍFICOS
embarcadores_especificos = {
    "Selecione o Embarcador...": {"lmg_base": 0.00, "lmg_maximo": 0.00},
    "Operação Embarcador RENAULT DO BRASIL, VOLVO E SCANIA": {
        "lmg_base": 3000000.00,
        "lmg_maximo": 10000000.00,
    },
    (
        "Embarcador CNH (somente para partes e peças de máquinas e implementos"
        " agrícolas)"
    ): {"lmg_base": 2500000.00, "lmg_maximo": 2500000.00},
    (
        "Defensivos agrícolas do Embarcador CHDS DO BRASIL COMERCIO DE INSUMOS"
        " AGRICOLAS LTDA."
    ): {"lmg_base": 2500000.00, "lmg_maximo": 2500000.00},
    (
        "Embarcador METAL GROUP PARTICIPACOES LTDA (exceto Região Metropolitana"
        " do RJ)"
    ): {"lmg_base": 2500000.00, "lmg_maximo": 2500000.00},
    (
        "Operação de Frango Congelado do Embarcador GT Foods nos Percursos"
        " (Paranaguá x Terra Boa/ Maringá/ Paranavaí/ Cambé/ Apucarana/ Paraíso"
        " do Norte x Paranaguá)"
    ): {"lmg_base": 550000.00, "lmg_maximo": 550000.00},
    "Embarcador Hexion Química do Brasil": {
        "lmg_base": 160000.00,
        "lmg_maximo": 6000000.00,
    },
}

# 2. Dicionário COMPLETO de Mercadorias com Limites Fixos da Relação (Pág. 13)
mercadorias_gerais = {
    "Selecione a Mercadoria...": {"lmg_base": 0.00, "lmg_maximo": 0.00},
    "Aço e ferro em geral": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    (
        "GLUCOSE / MALTOSE; CHOCOLATE LÍQUIDO OU EM MASSA; ÁCIDO CÍTRICO;"
        " GELATINA; AMIDOS"
    ): {"lmg_base": 450000.00, "lmg_maximo": 6000000.00},
    "Álcool etílico e para fins medicinais / farmacêuticos": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Alumínio em geral": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Artigos de higiene e limpeza, cosméticos e perfumaria": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Artigos esportivos": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Autopeças em geral, inclusive para motocicleta": {
        "lmg_base": 200000.00,
        "lmg_maximo": 6000000.00,
    },
    "Balas, chocolates, chicletes e doces em geral": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Baterias automotivas": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Bebidas em geral, exceto cervejas e refrigerantes": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Bobinas de papel": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Brinquedos e bicicletas, partes, peças e acessórios": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Café de qualquer tipo": {"lmg_base": 150000.00, "lmg_maximo": 4000000.00},
    (
        "Calçados (tênis, sapatos, chinelos, sandálias), solados, palmilhas e"
        " correias"
    ): {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Cartuchos para impressoras e copiadoras": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Câmeras e Artigos fotográficos em geral": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Carnes 'in natura' e Charque de qualquer origem animal": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Carne de frango congelada": {
        "lmg_base": 170000.00,
        "lmg_maximo": 6000000.00,
    },
    "Cassiterita": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "CD´s, DVD´s, LD´s e Blue Ray": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    (
        "Computadores em Geral, Notebooks, Desktops, Tablets, Teclados,"
        " Monitores, CPU, Processadores, Memórias, Kit Multimídia, Jogos e"
        " Semelhantes, Demais Periféricos e Demais Peças"
    ): {"lmg_base": 150000.00, "lmg_maximo": 1000000.00},
    "Cervejas e Refrigerantes": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Cobre de qualquer tipo": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Confecções, tecidos, fios têxteis e roupas prontas": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Eletrônicos em Geral e Eletrodomésticos": {
        "lmg_base": 200000.00,
        "lmg_maximo": 1000000.00,
    },
    "Embarcador Hexion Química do Brasil": {
        "lmg_base": 160000.00,
        "lmg_maximo": 6000000.00,
    },
    "Embarcador CNH (partes e peças)": {
        "lmg_base": 150000.00,
        "lmg_maximo": 2500000.00,
    },
    "Empilhadeiras de qualquer tipo": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Equipamentos e aparelhos de ginástica": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Equipamento médico hospitalar": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Fechaduras, ferragens em geral": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    (
        "Ferramentas manuais ou elétricas (furadeiras, serras, lixadeiras)"
    ): {"lmg_base": 200000.00, "lmg_maximo": 6000000.00},
    "Fertilizantes e defensivos agrícolas": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Fraldas descartáveis": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Fibra óptica": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Grãos, farinhas, farelos e sementes em geral": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Lâmpadas, inclusive reatores, luminárias e periféricos": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Leite de qualquer tipo": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    (
        "Materiais elétricos e montagem de rede de distribuição, painéis"
        " solares"
    ): {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    (
        "Materiais elétricos, inclusive ferramentas, fios e cabos (exceto cobre)"
    ): {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Materiais de escritório e escolar, livros e revistas": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Óleos lubrificantes": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    (
        "Óleos Comestíveis, Vegetais, Minerais ou Sintéticos (Embarcador AAK)"
    ): {"lmg_base": 200000.00, "lmg_maximo": 6000000.00},
    "Papel e celulose em geral (Exceto bobina de papel)": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Pilhas e baterias (exceto celulares)": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Pneus e câmaras de ar": {"lmg_base": 200000.00, "lmg_maximo": 6000000.00},
    "Produtos alimentícios em geral": {
        "lmg_base": 170000.00,
        "lmg_maximo": 6000000.00,
    },
    "Produtos farmacêuticos (exceto medicamentos)": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Produtos ópticos em geral, óculos": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Produtos químicos em geral (exceto uso veterinário)": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Produtos siderúrgicos, latão e folha de flandres": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Polímeros em geral": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Rolamentos em geral": {"lmg_base": 200000.00, "lmg_maximo": 6000000.00},
    "Tintas, vernizes, corantes, pigmentos e similares": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Transformadores/geradores pesados": {
        "lmg_base": 200000.00,
        "lmg_maximo": 6000000.00,
    },
    "Tratores de quaisquer tipos, máquinas e implementos agrícolas": {
        "lmg_base": 150000.00,
        "lmg_maximo": 6000000.00,
    },
    "Zinco": {"lmg_base": 150000.00, "lmg_maximo": 6000000.00},
    "Algodão em geral": {"lmg_base": 1000000.00, "lmg_maximo": 1000000.00},
    "Farinha de peixe": {"lmg_base": 450000.00, "lmg_maximo": 450000.00},
    (
        "Demais Mercadorias Cobertas (Não listadas acima - Regra Geral)"
    ): {"lmg_base": 1500000.00, "lmg_maximo": 6000000.00},
}


# Função auxiliar para verificar isenção de rota (Paranaguá x Curitiba e Região Metropolitana)
def verificar_isencao_rota(origem, destino, valor):
    origem_limpa = origem.upper()
    destino_limpo = destino.upper()

    rota_parinova = ("PARANAGUÁ" in origem_limpa or "PARANAGUA" in origem_limpa) and (
        "CURITIBA" in destino_limpo
        or "SÃO JOSÉ DOS PINHAIS" in destino_limpo
        or "PINHAIS" in destino_limpo
        or "COLOMBO" in destino_limpo
        or "ARAUCÁRIA" in destino_limpo
        or "CAMPO LARGO" in destino_limpo
    )
    rota_invers = (
        "CURITIBA" in origem_limpa
        or "SÃO JOSÉ DOS PINHAIS" in origem_limpa
        or "PINHAIS" in origem_limpa
        or "COLOMBO" in origem_limpa
        or "ARAUCÁRIA" in origem_limpa
        or "CAMPO LARGO" in origem_limpa
    ) and ("PARANAGUÁ" in destino_limpo or "PARANAGUA" in destino_limpo)

    if (rota_parinova or rota_invers) and valor <= 1500000.00:
        return True
    return False


# Regra Padrão de Gerenciamento de Risco (Conforme Pág. 15 da Apólice)
def obter_regras_gr_padrao_tabela(valor, lmg_fixo):
    regras = []
    connector_avisos = []

    if valor <= lmg_fixo:
        regras.append("Consulta e liberação do motorista, ajudante e veículo[cite: 18].")
    elif valor <= 600000.00:
        regras.extend([
            "Consulta e liberação do motorista, ajudante e veículo[cite: 18].",
            "Rastreamento / Monitoramento[cite: 18].",
        ])
        connector_avisos.extend([
            "Proibido utilização de equipamento em modo “sleep”[cite: 18].",
            "Pernoite deverá ser monitorado a cada 30 minutos[cite: 18].",
        ])
    elif valor <= 1200000.00:
        regras.extend([
            "Consulta e liberação do motorista, ajudante e veículo[cite: 18].",
            "Rastreamento / Monitoramento[cite: 18].",
            (
                "Um (01) Rastreador Móvel (Isca) OU Rastreador Redundante RF OU"
                " Escolta Armada OU Imobilizador Inteligente[cite: 18]."
            ),
        ])
        connector_avisos.extend([
            "Proibido utilização de equipamento em modo “sleep”[cite: 18].",
            "Pernoite deverá ser monitorado a cada 30 minutos[cite: 18].",
        ])
    elif valor <= 2000000.00:
        regras.extend([
            "Consulta e liberação do motorista, ajudante e veículo[cite: 18].",
            "Rastreamento / Monitoramento[cite: 18].",
            (
                "Rastreador Redundante RF OU Escolta Armada OU Imobilizador"
                " Inteligente[cite: 18]."
            ),
        ])
        connector_avisos.extend([
            "Proibido Rodagem entre 22h às 05h[cite: 18].",
            "Proibido utilização de equipamento em modo “sleep”[cite: 18].",
            "Pernoite deverá ser monitorado a cada 30 minutos[cite: 18].",
        ])
    elif valor <= 2500000.00:
        regras.extend([
            "Consulta e liberação do motorista, ajudante e veículo[cite: 18].",
            "Rastreamento / Monitoramento[cite: 18].",
            "Um (01) Rastreador Móvel (Isca)[cite: 18].",
            "Rastreador Redundante RF OU Imobilizador Inteligente[cite: 18].",
            "Trava de 5ª Roda ou Bloqueador de carreta[cite: 18].",
        ])
        connector_avisos.extend([
            "Proibido Rodagem entre 22h às 05h[cite: 18].",
            "Proibido utilização de equipamento em modo “sleep”[cite: 18].",
            "Pernoite deverá ser monitorado a cada 30 minutos[cite: 18].",
        ])
    else:
        regras.extend([
            "Consulta e liberação do motorista, ajudante e veículo[cite: 18].",
            "Rastreamento / Monitoramento[cite: 18].",
            (
                "Um (01) Rastreador Móvel (Isca) + Rastreador Redundante RF OU"
                " Imobilizador Inteligente[cite: 18]."
            ),
            (
                "Escolta Armada OU POS adicional de 10% caso não tenha sido"
                " utilizado Escolta Armada[cite: 18]."
            ),
            "Trava de 5ª Roda ou Bloqueador de carreta[cite: 18].",
        ])
        connector_avisos.extend([
            "Proibido Rodagem entre 22h às 05h[cite: 18].",
            "Proibido utilização de equipamento em modo “sleep”[cite: 18].",
            "Pernoite deverá ser monitorado a cada 30 minutos[cite: 18].",
        ])
    return regras, connector_avisos


# Layout do Formulário de Entrada na Barra Lateral
st.sidebar.header("🔍 Parâmetros de Embarque")

local_coleta = st.sidebar.text_input("Local de Coleta (Origem):", "")
local_entrega = st.sidebar.text_input("Local de Entrega (Destino):", "")

tipo_container = st.sidebar.selectbox(
    "Tipo de Operação em Container:",
    [
        "Não é Container",
        "Container (Origem e Destino no PR)",
        "Container (Outras Regiões - Exceto PR e RJ)",
    ],
)

tipo_selecao = st.sidebar.radio(
    "Tipo de Seleção:", ["Embarcador Específico", "Mercadoria Geral"]
)

if tipo_selecao == "Embarcador Específico":
    commodity_selecionada = st.sidebar.selectbox(
        "Selecione o Embarcador:", list(embarcadores_especificos.keys())
    )
    dados_commodity = embarcadores_especificos[commodity_selecionada]
else:
    commodity_selecionada = st.sidebar.selectbox(
        "Selecione a Mercadoria:", list(mercadorias_gerais.keys())
    )
    dados_commodity = mercadorias_gerais[commodity_selecionada]

valor_carga = st.sidebar.number_input(
    "Valor Informado da Carga (R$):",
    min_value=0.0,
    value=0.0,
    step=10000.0,
    format="%.2f",
)

# Botão de Consulta
consultar_clicado = st.sidebar.button(
    "📋 Consultar Apólice", type="primary", use_container_width=True
)

# Comportamento Inicial da Tela
if not consultar_clicado:
    st.info(
        "👈 Preencha os parâmetros de embarque na barra lateral e clique em"
        " **'Consultar Apólice'** para iniciar a validação."
    )
else:
    if "Selecione" in commodity_selecionada or valor_carga <= 0:
        st.warning(
            "⚠️ Por favor, selecione uma opção válida e informe um valor de"
            " carga superior a zero."
        )
    else:
        lmg_base = dados_commodity["lmg_base"]
        lmg_maximo = dados_commodity["lmg_maximo"]

        st.markdown(f"### 📍 Rota: `{local_coleta}` ➔ `{local_entrega}`")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Valor Informado da Carga",
                value=f"R$ {valor_carga:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
            )

        with col2:
            st.metric(
                label="Limite Base (Relação GR)",
                value=f"R$ {lmg_base:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
            )

        with col3:
            st.metric(
                label="Limite Máximo da Categoria",
                value=f"R$ {lmg_maximo:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
            )

        st.markdown("---")

        st.info(
            f"🔍 **Consulta Realizada para:** {commodity_selecionada} | Tipo:"
            f" {tipo_container} | Rota: {local_coleta} ➔ {local_entrega}"
        )

        # Validação cruzando com o limite máximo específico
        if valor_carga > lmg_maximo:
            st.error(
                f"🚨 **ALERTA CRÍTICO:** O valor da mercadoria (R$"
                f" {valor_carga:,.2f}) **ULTRAPASSA** o limite máximo permitido"
                f" de R$ {lmg_maximo:,.2f} para esta categoria na apólice!"
            )
        elif valor_carga > lmg_base:
            st.warning(
                f"⚠️ **ATENÇÃO (Acima do Limite Base da Relação - R$"
                f" {lmg_base:,.2f}):**\n"
                "- O valor está acima do limite fixo da relação, mas dentro do"
                " limite máximo aceito.\n"
                "- **Regra de Prazo e Aceitação Tácita:** O Segurado obriga-se"
                " a dar aviso, por escrito, à Seguradora, com **antecipação"
                " mínima de 3 (três) dias úteis**, contados da data de"
                " embarque.\n"
                "- A Seguradora deverá se pronunciar no prazo de até **3 (três)"
                " dias úteis**, após o recebimento, sobre a aceitação ou não do"
                " risco.\n"
                "- A **ausência de manifestação por escrito** da Seguradora"
                " caracterizará a **aceitação tácita** do risco proposto."
            )

            exigencias_gr, avisos_gr = obter_regras_gr_padrao_tabela(
                valor_carga, lmg_base
            )
            st.markdown(
                "### 📋 Exigências de Gerenciamento de Risco (GR) - Tabela Geral"
            )

            st.markdown(
                f"*Regras aplicadas para a faixa de valor de R$"
                f" {valor_carga:,.2f}:*"
            )

            for req in exigencias_gr:
                st.markdown(f"- {req}")

            if avisos_gr:
                st.markdown("#### 🛑 Restrições e Monitoramento Operacional:")
                for aviso in avisos_gr:
                    st.markdown(f"- {aviso}")
        else:
            st.success(
                "✅ **Dentro do limite base da relação** estabelecido na"
                " apólice."
            )

            exigencias_gr, avisos_gr = obter_regras_gr_padrao_tabela(
                valor_carga, lmg_base
            )
            st.markdown(
                "### 📋 Exigências de Gerenciamento de Risco (GR) - Tabela Geral"
            )

            st.markdown(
                f"*Regras aplicadas para a faixa de valor de R$"
                f" {valor_carga:,.2f}:*"
            )

            for req in exigencias_gr:
                st.markdown(f"- {req}")

            if avisos_gr:
                st.markdown("#### 🛑 Restrições e Monitoramento Operacional:")
                for aviso in avisos_gr:
                    st.markdown(f"- {aviso}")

# Nota Geral de Rodapé da Apólice
st.markdown("---")
st.caption(
    "📌 **NOTA 1:** Proibido o uso do aplicativo de frete para contratação de"
    " motoristas, exceto FRETEBRAS e PX."
)