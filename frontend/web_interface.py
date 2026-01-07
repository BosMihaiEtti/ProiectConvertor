import streamlit as st
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.data_provider import RateProvider
from backend.forex_engine import ForexMarket

st.set_page_config(page_title="Convertor valutar & Forex", page_icon="💱")

css_file = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if 'market' not in st.session_state:
    provider = RateProvider()
    st.session_state.market = ForexMarket(provider.fetch_rates())

market = st.session_state.market

st.markdown('<div class="title-text">Convertor valutar', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([3, 3, 3])

    with c1:
        amount = st.number_input("Amount", value=1.0, min_value=0.01)

    currencies = sorted(list(market.rates.keys()))
    if "USD" in currencies: currencies.insert(0, currencies.pop(currencies.index("USD")))

    with c2:
        from_curr = st.selectbox("From", currencies, index=0)
    with c3:
        idx_to = currencies.index("EUR") if "EUR" in currencies else 1
        to_curr = st.selectbox("To", currencies, index=idx_to)

    if st.button("Convert"):
        res = market.convert(amount, from_curr, to_curr)
        unit_rate = market.convert(1, from_curr, to_curr)

        st.markdown("---")
        st.markdown(f"<div class='rate-info'>● Live rate: 1 {from_curr} = {unit_rate:.4f} {to_curr}</div>",
                    unsafe_allow_html=True)
        st.markdown(f"<div class='big-result'>{res:,.2f} {to_curr}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown("### 📉 Forex")

col_btn, col_info = st.columns([1, 2])

with col_btn:
    if st.button("Simulate Market Volatility"):
        with st.spinner("Updating market rates..."):
            market.simulate_volatility()
            time.sleep(0.5)
        st.success("Rates Updated!")
        time.sleep(0.5)
        st.rerun()

with col_info:
    st.info("Apasă pe butonul din stânga pentru a simula fluctuațiile pieței (+/- 0.5%).")
    st.write(f"**Current USD Rates:** EUR: {market.rates.get('EUR', 0):.4f} | RON: {market.rates.get('RON', 0):.4f}")