import streamlit as st

from src.constants import CURRENCIES
from src.currency_convertor import convert_currency, get_exchange_rate

st.title(":dollar: Currency Converter")

st.markdown("""
    This tool allows you to instantly convert amounts between different currencies 🌍.
Enter the amount and choose the currencies to see the result. 
""")


base_currency = st.selectbox("From Currency (Base): ", CURRENCIES)
target_currency = st.selectbox("To Currency (Target): ", CURRENCIES)
amount = st.number_input('Enter amount: ', min_value=0.0, value=100.0)

if amount > 0 and base_currency and target_currency:
    try:
        exchange_rate = get_exchange_rate(
            base_currency=base_currency, target_currency=target_currency)
    except:
        st.error('Currency not support !')

    if exchange_rate:
        convert_amount = convert_currency(
            amount=amount, exchange_rate=exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.3f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Bace Currency",
                    value=f"{amount:.3f} {base_currency}")
        col2.markdown(
            "<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency",
                    value=f"{convert_amount:.3f} {target_currency}")
    else:
        st.error('Error fetching exchange rate.')

st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")
