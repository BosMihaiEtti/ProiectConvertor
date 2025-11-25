import streamlit as st

st.set_page_config(page_title="Currency converter", layout="wide")

with open("style.css") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown('<div class="converter-card">Proiect</div>', unsafe_allow_html=True)

col_amount, col_from, col_switch, col_to = st.columns([1.5, 2.5, 0.7, 2.5])

with col_amount:
    st.markdown('<div class="field-label">Amount</div>', unsafe_allow_html=True)
    st.markdown('<div class="converter-amount">', unsafe_allow_html=True)
    amount = st.text_input(label="", value="1.00")
    st.markdown('</div>', unsafe_allow_html=True)

with col_from:
    st.markdown('<div class="field-label">From</div>', unsafe_allow_html=True)
    st.markdown('<div class="converter-selectbox">', unsafe_allow_html=True)
    from_currency = st.selectbox(
        label="",
        options=[
            "USD - US Dollar",
            "EUR - Euro",
            "RON - Romanian Leu",
            "GBP - British Pound",
        ],
        index=0,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_switch:
    st.write("")
    st.write("")
    st.markdown('<div class="switch-button">', unsafe_allow_html=True)
    switch = st.button("⇄")
    st.markdown('</div>', unsafe_allow_html=True)


with col_to:
    st.markdown('<div class="field-label">To</div>', unsafe_allow_html=True)
    st.markdown('<div class="converter-selectbox">', unsafe_allow_html=True)
    to_currency = st.selectbox(
        label="",
        options=[
            "EUR - Euro",
            "USD - US Dollar",
            "RON - Romanian Leu",
            "GBP - British Pound",
        ],
        index=1,
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")
col_empty, col_convert = st.columns([6, 2])
with col_convert:
    st.markdown('<div class="convert-button">', unsafe_allow_html=True)
    convert = st.button("Convert", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # închidem converter-card
