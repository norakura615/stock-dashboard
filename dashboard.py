import streamlit as st
import yfinance as yf

st.title("株価チェッカー")

# サイドバーに設定を移動
with st.sidebar:
    st.header("設定")
    ticker = st.text_input("ティッカーシンボル", value="AAPL")
    period = st.selectbox("期間", ["1mo", "3mo", "6mo", "1y"])

if st.button("取得"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)

    if hist.empty:
        st.error("データが取得できませんでした")
    else:
        # 基本情報
        info = stock.info
        st.subheader(info.get("longName", ticker))

        col1, col2, col3 = st.columns(3)
        col1.metric("最新終値", f"{hist['Close'].iloc[-1]:.2f}")
        col2.metric("期間最高値", f"{hist['High'].max():.2f}")
        col3.metric("期間最安値", f"{hist['Low'].min():.2f}")

        # チャート
        st.line_chart(hist["Close"])