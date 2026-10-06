import streamlit as st

# Configuracao da pagina
st.set_page_config(
    page_title="Validador de Apolice - TLOG",
    page_icon="🛡",
    layout="centered"
)

# Tabela completa e revisada de Limites de Garantia (LMG) por Produto / Condicao Especial
tabela_regras = {
    "Aco e ferro em geral": 150000.00,
    "GLUCOSE / MALTOSE; CHOCOLATE LÍQUIDO OU EM MASSA; ÁCIDO CÍTRICO; GELATINA; AMIDOS": 450000.00,
    "Álcool etílico e para fins medicinais / farmacêuticos": 150000.00,
    "Aluminio em geral": 150000.00,
    "Algodão em geral": 1000000.00,
    "Artigos de higiene e limpeza, cosmeticos e perfumaria": 150000.00,
    "Artigos esportivos": 150000.00,
    "Autopecas em geral, inclusive para motocicleta": 200000.00,
    "Balas, chocolates, chicletes e doces em geral": 150000.00,
    "Baterias automotivas": 150000.00,
    "Bebidas em geral, exceto cervejas e refrigerantes": 150000.00,
    "Bobinas de papel": 150000.00,
    "Brinquedos e bicicletas, partes, pecas e acessorios": 150000.00,
    "Café (qualquer tipo)": 4000000.00,
    "Café de qualquer tipo (Geral)": 150000.00,
    "Calçados (tênis, sapatos, chinelos, sandálias), solados, palmilhas e correias": 150000.00,
    "Cartuchos para impressoras e copiadoras": 150000.00,
    "Câmeras e Artigos fotograficos em geral": 150000.00,
    "Carne congelada, in natura, charque, pescados e leite (inclusive em pó/condensado)": 900000.00,
    "Carnes in natura e Charque de origem animal": 150000.00,
    "Carne de frango congelada": 170000.00,
    "Cassiterita": 150000.00,
    "CD's, DVD's, LD's e Blue Ray": 150000.00,
    "Computadores em Geral, Notebooks, Desktops, Tablets, Teclados, Monitores, CPU, Processadores, Memórias, Kit Multimídia, Jogos e Semelhantes, Demais Periféricos e Demais Partes e Peças destes produtos": 150000.00,
    "Cervejas e Refrigerantes": 150000.00,
    "Cobre de qualquer tipo": 150000.00,
    "Confeccoes, tecidos, fios têxteis e roupas prontas": 150000.00,
    "Defensivos agrícolas - Embarcador CHDS DO BRASIL": 2500000.00,
    "Eletrônicos em Geral e Eletrodomésticos": 200000.00,
    "Embarcador Hexion Química do Brasil": 160000.00,
    "Embarcador CNH (somente pra partes e peças de máquinas e implementos agrícolas)": 150000.00,
    "Embarques de mercadorias em Pick-up abertas": 100000.00,
    "Empilhadeiras de qualquer tipo": 150000.00,
    "Equipamentos e aparelhos de ginastica": 150000.00,
    "Equipamento médico hospitalar": 150000.00,
    "Fechaduras, ferragens em geral e": 150000.00,
    "Farinha de peixe": 450000.00,
    "Ferramentas manuais ou elétricas (por exemplo, furadeiras, serras elétricas, lixadeiras, etc)": 200000.00,
    "Fertilizantes e defensivos agrícolas": 150000.00,
    "Frango Congelado (Operação GT Foods - Percurso Paranaguá x Terra Boa/Maringá/Paranavaí/Cambé/Apucarana/Paraíso do Norte)": 550000.00,
    "Frangos Congelados em geral": 450000.00,
    "Frango e Porco Congelados transportados em containers": 750000.00,
    "Fraldas descartáveis": 150000.00,
    "Fibra óptica": 150000.00,
    "Grãos, farinhas, farelos e sementes em geral (exceto café qualquer tipo)": 150000.00,
    "Lâmpadas, inclusive reatores, luminárias e periféricos": 150000.00,
    "Leite de qualquer tipo": 150000.00,
    "Máquinas e Equipamentos Agrícolas, Colheitadeiras, Pá Carregadeira": 1500000.00,
    "Máquinas e Equipamentos com dimensões excepcionais/pesados": 500000.00,
    "Materiais elétricos e montagem de rede de distribuição, painéis solares /fotovoltaicos": 150000.00,
    "Materiais elétricos, inclusive ferramentas, fios e cabos em geral (exceto cobre)": 150000.00,
    "Materiais de escritório e escolar livros e revistas em geral": 150000.00,
    "Metal Group Participacoes Ltda (Origem/Destino Brasil, exceto RJ)": 2500000.00,
    "Óleos lubrificantes": 150000.00,
    "Óleos Comestíveis, Óleos Vegetais, (Inclusive Azeites), Óleos de Origem Animal, Óleos Minerais ou Óleos Sintéticos, Degomados ou Não Degomados do embarcador AAK DO BRASIL INDUSTRIA E COMERCIO DE OLEOS VEGETAIS LTDA": 200000.00,
    "Oleos Comestiveis, Oleos Vegetais, Azeites": 200000.00,
    "Operação Embarcador RENAULT DO BRASIL, VOLVO e SCANIA": 10000000.00,
    "Papel e celulose em geral (Exceto bobina de papel)": 150000.00,
    "Partes e peças de máquinas e implementos agrícolas - Embarcador CNH": 2500000.00,
    "Pilhas e baterias (exceto aparelhos de telefones celulares)": 150000.00,
    "Pisos Cerâmicos, Vasilhames e Garrafas de Vidro, Vidros de Qualquer Tipo": 200000.00,
    "Pneus e câmaras de ar": 200000.00,
    "Pneus e câmaras de ar e suas matérias primas": 1000000.00,
    "Produtos alimenticios em geral": 170000.00,
    "Produtos farmaceuticos (exceto medicamentos)": 150000.00,
    "Produtos ópticos em geral": 150000.00,
    "Produtos quimicos em geral (exceto de uso veterinário)": 150000.00,
    "Produtos siderúrgicos, latão e folha de flandres": 150000.00,
    "Polímeros em geral": 150000.00,
    "Racks para transporte de mercadorias": 250000.00,
    "Rolamentos em geral": 200000.00,
    "Suco Congelado transportado em containers": 400000.00,
    "Tintas, vernizes, corantes, pigmentos e similares": 150000.00,
    "Transformadores/geradores pesados": 200000.00,
    "Tratores de quaisquer tipos, máquinas e implementos agrícolas": 150000.00,
    "Zinco": 150000.00,
    "Bens Gerais / Outros (Limite Máximo Padrão da Apólice)": 6000000.00
}

def obter_regras_gerenciamento(valor, lmg_limite):
    """Retorna as exigências de Gerenciamento de Risco (Regras Gerais)."""
    if valor <= lmg_limite:
        return [
            "Consulta e liberação do motorista, ajudante e veículo."
        ]
    elif valor <= 600000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 1200000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca) OU Rastreador Redundante RF OU Escolta Armada OU Imobilizador Inteligente.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 2000000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Rastreador Redundante RF OU Escolta Armada OU Imobilizador Inteligente.",
            "Proibido Rodagem entre 22h às 05h.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 2500000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca).",
            "Rastreador Redundante RF OU Imobilizador Inteligente.",
            "Trava de 5° Roda ou Bloqueador de carreta.",
            "Proibido Rodagem entre 22h às 05h.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 4000000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca) E/OU Rastreador Redundante RF OU Imobilizador Inteligente.",
            "Escolta Armada OU POS adicional de 10% caso não tenha sido utilizado Escolta Armada.",
            "Trava de 5° Roda ou Bloqueador de carreta.",
            "Proibido Rodagem entre 22h às 05h.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    else:
        return [
            "⚠️ **Valor acima do limite padrão:** Requer aviso prévio por escrito à Seguradora com antecedência mínima de 3 dias úteis."
        ]

def obter_regras_farinha_peixe(valor):
    """Retorna as exigências específicas de GR para Farinha de Peixe (Exceto RJ)."""
    if valor <= 200000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo e motorista Frota ou agregado."
        ]
    elif valor <= 450000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo e motorista Frota ou agregado.",
            "Rastreamento / Monitoramento."
        ]
    else:
        return [
            "⚠️ **Valor acima do limite da condição especial:** Requer aviso prévio por escrito à Seguradora com antecedência mínima de 3 dias úteis."
        ]

def obter_regras_container_pr(valor, lmg_limite):
    """Retorna as exigências de GR para Container com Origem e Destino no Paraná (PR)."""
    if valor <= lmg_limite:
        return [
            "Consulta e liberação do motorista, ajudante e veículo."
        ]
    elif valor <= 600000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 1200000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca) OU Rastreador Redundante RF OU Escolta Armada OU Imobilizador Inteligente.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 2500000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca) OU Rastreador Redundante RF OU Escolta Armada OU Imobilizador Inteligente.",
            "Rastreador Redundante RF OU Escolta Armada OU Imobilizador Inteligente.",
            "Proibido rodagem entre 22h e 05h.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    elif valor <= 6000000.00:
        return [
            "Consulta e liberação do motorista, ajudante e veículo.",
            "Rastreamento / Monitoramento.",
            "Um (01) Rastreador Móvel (Isca) OU Rastreador Redundante RF OU Imobilizador Inteligente.",
            "Rastreador Redundante RF OU Trava Eletrônica.",
            "Imobilizador Inteligente OU Trava Eletrônica OU Escolta Armada.",
            "Trava de 5ª Roda OU Bloqueador de carreta OU Cadeado Inteligente OU Trava de porta de container.",
            "Proibido rodagem entre 22h e 05h.",
            "Proibido utilização de equipamento em modo 'sleep'.",
            "Pernoite deverá ser monitorado a cada 30 minutos."
        ]
    else:
        return [
            "⚠️ **Valor acima de R$ 6.000.000,00:** Requer aviso prévio por escrito à Seguradora com antecedência mínima de 3 dias úteis."
        ]

st.title("🛡 Validador de Regras de Apolice - TLOG")
st.markdown("Consulte os limites de **LMG e Exigências de Gerenciamento de Risco**.")

with st.form("form_com_regras_pr"):
    cliente = st.text_input("Cliente (Opcional)", placeholder="Ex: Empresa Exemplo S.A.")
    
    col1, col2 = st.columns(2)
    with col1:
        cidade_inicio = st.text_input("Cidade de Inicio (Origem)")
    with col2:
        destino = st.text_input("Cidade de Destino")
        
    container_pr = st.checkbox("Mercadorias em Container com Origem e Destino no Estado do Paraná (PR)")
        
    lista_produtos = sorted(list(tabela_regras.keys()))

    produto = st.selectbox(
        f"Produto / Condição Especial ({len(lista_produtos)} opções):", 
        options=lista_produtos, 
        index=0
    )
    
    valor_mercadoria = st.number_input("Valor da Mercadoria (R$)", min_value=0.0, format="%.2f", step=1000.0)

    submitted = st.form_submit_button("Consultar Apolice e Regras de GR")

if submitted:
    if not cidade_inicio or not destino or not produto:
        st.warning("⚠️ Por favor, preencha as cidades de origem, destino e selecione o produto.")
    else:
        lmg_limite = tabela_regras.get(produto, 150000.00)
        ultrapassou = valor_mercadoria > lmg_limite
        
        if produto == "Farinha de peixe":
            regras_gr = obter_regras_farinha_peixe(valor_mercadoria)
            tipo_regra_txt = "Farinha de Peixe (Exceto RJ)"
        elif container_pr:
            regras_gr = obter_regras_container_pr(valor_mercadoria, lmg_limite)
            tipo_regra_txt = "Container (Origem e Destino no Paraná - PR)"
        else:
            regras_gr = obter_regras_gerenciamento(valor_mercadoria, lmg_limite)
            tipo_regra_txt = "Regras Gerais"
        
        st.divider()
        titulo_relatorio = f"📊 Relatorio de Analise"
        if cliente:
            titulo_relatorio += f": {cliente}"
        st.subheader(titulo_relatorio)
        
        st.info(f"**Rota:** {cidade_inicio} -> {destino} \n\n **Produto / Condição:** {produto} \n\n **Tipo de Tabela GR:** {tipo_regra_txt}")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric(label="Valor Informado da Carga", value=f"R$ {valor_mercadoria:,.2f}")
        with col_b:
            st.metric(label="LMG Limite da Apolice", value=f"R$ {lmg_limite:,.2f}")
            
        if ultrapassou:
            st.error("🚨 **ALERTA CRITICO DE LMG:** O valor da mercadoria **ULTRAPASSA** o limite máximo fixado pela apólice!")
            st.warning("⚠️ **Importante:** Nas operações que ultrapassarem os limites estabelecidos, o Segurado obriga-se a dar aviso, por escrito, à Seguradora, com **antecipação mínima de 3 (três) dias úteis**, contados da data de embarque.")
        else:
            st.success("✅ **Status LMG:** O valor da carga esta dentro do limite fixado para esta mercadoria.")
            
        st.markdown("---")
        st.subheader("📋 Exigências de Gerenciamento de Risco (GR)")
        for regra in regras_gr:
            st.markdown(f"- {regra}")