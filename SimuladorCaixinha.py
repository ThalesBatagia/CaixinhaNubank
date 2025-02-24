import streamlit as st
import math

st.set_page_config(page_title="Simulador de Caixinha do Nubank", page_icon=":moneybag:", layout="wide")
st.title("Bem vindo ao simulador de caixinha do Nubank")
st.write("Aqui você pode simular quanto dinheiro você terá guardado em um determinado período de tempo se guardar um valor fixo todo mês na sua caixinha do Nubank")
st.write("Escolha abaixo se você deseja simular um aporte mensal ou um aporte único. Um aporte mensal é o valor que você coloca todo mês e o aporte único é o valor que você coloca uma única vez.")

tabs = st.tabs(["Aporte mensal", "Aporte único"])

with tabs[0]:
    st.write("Aqui você pode simular quanto dinheiro você terá guardado em um determinado período de tempo se guardar um valor fixo todo mês na sua caixinha do Nubank")
    def calcular_montante(P, A, r_a, n):
        # Converter taxa anual para taxa mensal
        r_m = (1 + r_a) ** (1/12) - 1

        # Fórmula dos juros compostos com aportes mensais
        M = P * (1 + r_m) ** n + A * ((1 + r_m) ** n - 1) / r_m

        return M
    
    P = st.number_input("Insira o aporte inicial:  ", min_value=0.0) # Investimento inicial
    A = st.number_input("Insira o aporte mensal:  ", min_value=0.0)  # Aporte mensal
    r_a = 0.12  # Taxa de juros anual (12%)
    n = st.number_input("Insira a quantidade de meses em que você deseja deixar a grana:", min_value= 0)  # Tempo em meses

    montante_final = calcular_montante(P, A, r_a, n)
    lucro = montante_final - (P + A*n)
    st.write(f"Dinheiro guardado após {n} meses: R$ {montante_final:.2f}")
    st.write(f"Lucro total: R$ {lucro:.2f}")

with tabs[1]:
    st.write("Aqui você pode simular quanto dinheiro você terá guardado em um determinado período de tempo se fizer um aporte único na sua caixinha do Nubank")
    valor_unico = st.number_input("Insira o valor do aporte único:  ", min_value=0.0) # Investimento inicial
    n = st.number_input("Insira a quantidade de dias em que você deseja deixar a grana:", min_value= 0)  # Tempo em dias

    def calcular_montante_unico(valor_unico, r, n):
        # Converter taxa anual para taxa diária
        r = (1 + 10.93/100)**(1/365) - 1

        # Fórmula dos juros compostos com aporte único
        M = valor_unico * ((1 + r) ** n)

        return M
    
    montante_final2 = calcular_montante_unico(valor_unico, r_a, n)
    lucro = montante_final2 - valor_unico
    st.write(f"Dinheiro guardado após {n} dias: R$ {montante_final2:.2f}")
    st.write(f"Lucro total: R$ {lucro:.2f}")

