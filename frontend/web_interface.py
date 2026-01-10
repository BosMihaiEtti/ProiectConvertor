import sys
import os
import streamlit as st
import plotly.graph_objects as go

# --- FIX IMPORT ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.data_provider import RateProvider
from backend.forex_engine import ForexMarket

# --- CONFIGURARE ---
st.set_page_config(page_title="FX Converter", page_icon="💱", layout="centered")


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def initialize_backend():
    if 'market' not in st.session_state:
        provider = RateProvider()
        rates = provider.fetch_rates()
        st.session_state['market'] = ForexMarket(rates)
    return st.session_state['market']


def plot_candlestick_chart(df, from_curr, to_curr):
    """Grafic curat, fara fundal."""
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        increasing_line_color='#26a69a',  # Verde 
        decreasing_line_color='#ef5350'  # Rosu 
    )])

    fig.update_layout(
        title=None,  # Fara titlu in grafic, il punem in HTML
        xaxis_rangeslider_visible=False,
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent
        font=dict(color="#333"),  # Text inchis la culoare
        xaxis=dict(showgrid=True, gridcolor='#e0e0e0'),
        yaxis=dict(showgrid=True, gridcolor='#e0e0e0')
    )
    return fig


def main():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    load_css(css_path)
    market = initialize_backend()
    currency_list = market.available_currencies

    # --- HEADER (Pe zona albastra) ---
    st.markdown('<h1 class="hero-title">Convertor Valutar</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Cursuri în timp real și analiză de piață</p>', unsafe_allow_html=True)

    # --- INPUTURI (Direct pe pagina, sub semicerc) ---
    c1, c2, c3, c4 = st.columns([2, 2, 0.5, 2])

    with c1:
        st.markdown('<div class="field-label">Sumă</div>', unsafe_allow_html=True)
        amount = st.number_input("Sum", value=100.0, step=10.0, label_visibility="collapsed")

    with c2:
        st.markdown('<div class="field-label">Din</div>', unsafe_allow_html=True)
        idx_from = currency_list.index("EUR") if "EUR" in currency_list else 0
        from_curr = st.selectbox("From", currency_list, index=idx_from, label_visibility="collapsed")

    with c3:
        st.markdown('<div class="arrow-container">➝</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="field-label">În</div>', unsafe_allow_html=True)
        idx_to = currency_list.index("RON") if "RON" in currency_list else 1
        to_curr = st.selectbox("To", currency_list, index=idx_to, label_visibility="collapsed")

    # --- BUTON & REZULTAT ---
    if st.button("CALCULEAZĂ", use_container_width=True):
        res = market.convert(amount, from_curr, to_curr)
        st.markdown(f"""
            <div class="result-box">
                <div class="rate-text">{amount:.2f} {from_curr} =</div>
                <div class="result-text">{res:,.4f} {to_curr}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.write("")
        st.write("")

    # --- GRAFIC  ---
    st.markdown("---")

    if from_curr != to_curr:
        st.markdown(f'<div class="chart-header">Evoluție {from_curr} - {to_curr} (Candlestick)</div>',
                    unsafe_allow_html=True)
        ohlc_data = market.get_ohlc_data(from_curr, to_curr, days=30)
        fig = plot_candlestick_chart(ohlc_data, from_curr, to_curr)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.caption("Alege monede diferite pentru a vedea graficul.")


if __name__ == "__main__":
    main()
