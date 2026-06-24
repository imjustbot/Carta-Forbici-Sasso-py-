import random
import streamlit as st

WPLAYER = "Ha vinto il giocatore!"

WPC = "Ha vinto il computer!"

MOSSE = ["CARTA", "FORBICI", "SASSO"]

st.title("CARTA, FORBICI, SASSO")

mossa_utente = st.selectbox("SCEGLI LA TUA RISPOSTA:", MOSSE)

mossa_computer = random.choice(MOSSE)

st.write(f"Il computer ha scelto {mossa_computer}")

# VITTORIE DELL'UTENTE:

if mossa_utente == "CARTA" and mossa_computer == "SASSO":

    st.write(WPLAYER)

elif mossa_utente == "SASSO" and mossa_computer == "FORBICI":

    st.write(WPLAYER)

elif mossa_utente == "FORBICI" and mossa_computer == "CARTA":

    st.write(WPLAYER)

# VITTORIE DEL PC:

elif mossa_utente == "SASSO" and mossa_computer == "CARTA":

    st.write(WPC)

elif mossa_utente == "FORBICI" and mossa_computer == "SASSO":

    st.write(WPC)

elif mossa_utente == "CARTA" and mossa_computer == "FORBICI":

    st.write(WPC)

# IL PAREGGIO:

else:

    st.write("Pareggio!")


