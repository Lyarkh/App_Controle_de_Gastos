import streamlit as st

st.header('Distribuição valor')

# Valores iniciais para distribuição
valor_total = st.number_input('Valor Total')
choices = st.number_input('escolha a quantidade', 0)

# Criação de cada um dos cartões e sliders para a distribuição e escolha da porcentagem

cartoes_default = {
    0: "BagBank (Itau)",
    1: "DuoBank (C6)",
    2: "HomeBank (Inter)",
    3: "WishesBank (Next)",
    4: "InvestBank (XP)",
    5: "PigBank (NuBank)",
}

distribuicoes = []
max_value = 100
for i in range(choices):
    if max_value == 0:
        break
    col1, col2 = st.columns(2)
    with col1:
        if i in cartoes_default.keys():
            title_cartao = st.text_input('Nome cartao', cartoes_default[i])
        else:
            title_cartao = st.text_input('Nome cartao', f'Cartão {i}')

    with col2:
        value = st.number_input('Porcentagem',min_value=0, max_value=max_value, key=f' {i}')
    distribuicoes.append({title_cartao: value})
    max_value -= value

# Calculando a distribuição
valor_distribuido = 0
for cart in distribuicoes:
    for i in cart.keys():
        porcent = cart[i] / 100
        valor_separado = valor_total * porcent
    valor_distribuido += cart[i]
    cart['valor separado'] = round(valor_separado, 2)
    cart[i] = f'{cart[i]}%'


# Escrevendo o valor distribuido para cada cartão
with st.sidebar:
    st.write(f'Porcentagem total distribuida: {valor_distribuido}%')
    if valor_distribuido != 100:
        st.warning('Ainda falta porcentagem a ser distribuida')

    st.write(distribuicoes)
