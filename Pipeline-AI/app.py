import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Digite seu email")
    data = st.date_input("Data da Venda", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9, 0))  # valor padrão: 09:00
    valor = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Campo para escolher o produto vendido", ["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):  # printa as informações para o usuario
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro: {e}")

if __name__ == "__main__":
    main()

    # Comentários removidos para clareza
    # st.write("**Dados da Venda:**")
    # st.write(f"Email do Vendedor: {email}")
    # st.write(f"Data e Hora da Compra: {data_hora}")
    # st.write(f"Valor da Venda: R$ {valor:.2f}")
    # st.write(f"Quantidade de Produtos: {quantidade}")
    # st.write(f"Produto: {produto}")
