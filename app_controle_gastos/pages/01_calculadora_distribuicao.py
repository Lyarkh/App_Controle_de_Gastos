import streamlit as st

import app_controle_gastos.utils.constants as constants

st.header('Distribuição valor')

# Valores iniciais para distribuição
valor_total = st.number_input('Valor Total')
choices = st.number_input('escolha a quantidade', 6)

# Criação de cada um dos cartões e sliders para a distribuição e escolha da porcentagem
distribuicoes = []
for i in range(choices):
    value_num = 0
    col1, col2 = st.columns(2)
    with col1:
        if i in constants.cartoes_default.keys():
            title_cartao = st.text_input(
                'Nome cartao', constants.cartoes_default[i]
            )
        else:
            title_cartao = st.text_input('Nome cartao', f'Cartão {i}')

    with col2:
        value_perc = st.number_input(
            'Porcentagem', min_value=0, max_value=100, key=f'{i}-b'
        )
    distribuicoes.append(
        {title_cartao: value_num if value_num else value_perc}
    )

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
    if valor_distribuido < 100:
        st.warning('Ainda falta porcentagem a ser distribuida')
        st.warning(f'Porcentagem faltante: {100 - valor_distribuido}%')
    if valor_distribuido > 100:
        st.warning('Ultrapassou porcentagem máxima, favor redestribuir')

    st.write(distribuicoes)
