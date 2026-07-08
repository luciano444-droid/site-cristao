import streamlit as st
st.set_page_config(page_title="Site dos cultos virtuais")
st.title("Olá irmãs e irmãos")
st.divider()
st.write("Bem vindos ao nosso site, por favor nos informe seu nome logo abaixo: ")
#pergunta do nome do sapecoso
name = st.text_input("QUAL SEU NOME? ")
lista = ["LC", "Luciano", "Sunga", "Heloisa", "Emanuele", "Nana", "Akyla", "Susu"]
if name=="":
    pass
elif name in lista:
    st.success("vc é twin!!!!!!!🚀")
    st.balloons() # efeito de balões
    st.subheader("Bem-vindo ao site dos sapecosos do portelão, feito pelo mano LC (EU) rsrsrs")
    st.write(" A ideia dos cultos virtuais como desfarce foi uma ideia q tive de ultima hora.")
    st.write("Aqui é so pra resenha msm mas se os twins (vcs) quiserem q eu faça algo aqui é so falar")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWta7165TeCA-5z7PVcxKCxicCUKXV2ZqY3XZ-9hPjgbMq0tTVcPeBo5Sy&s=10", caption="***portelão sapecoso rsrsrs***")
    st.write("Enfm ne manos foi isso POR ENQUANTO, espero q tenham achado resenha😓, adios manos sapecosos ")
else:
    st.error("vc n é daqui abençoado🤨")
    st.error("Por favor se retire; Se vc tem acesso ao site, por favor fale com o dev")
