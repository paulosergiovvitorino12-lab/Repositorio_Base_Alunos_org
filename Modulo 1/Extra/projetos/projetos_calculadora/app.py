import streamlit as st
import calculadora as calc


st.image("https://media.tenor.com/D8zWQW3ZduwAAAAe/math-calculator.png", width=600)
st.title("Calculadora")



numero1 = st.number_input("Digite o primeiro número: ", step=0.1,value=None)
numero2 = st.number_input("Digite o segundo número: ", step=0.1, value=None)
operacao = st.selectbox("Selecione a operação:",["+","-","/","*"])

if st.button("calcular"):
    resultado = calc.calcular(numero1, numero2, operacao)
    st.toast(f"O resultado é:{resultado}", duration=10)
    
    