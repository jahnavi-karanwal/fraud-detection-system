import streamlit as st
import joblib
import pandas as pd

import streamlit as st
import joblib
import pandas as pd

model = joblib.load("./models/fraud_model.pkl")

st.title("Fraud Detection System")

transaction_type = st.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"]
)

amount = st.number_input("Amount", min_value=0.0)

oldbalanceOrg = st.number_input("Old Balance Sender", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Sender", min_value=0.0)

oldbalanceDest = st.number_input("Old Balance Receiver", min_value=0.0)
newbalanceDest = st.number_input("New Balance Receiver", min_value=0.0)

if st.button("Predict"):

    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest],
        "balanceDiffOrig": [balanceDiffOrig],
        "balanceDiffDest": [balanceDiffDest]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.write(f"Fraud Probability: {probability:.2%}")

    if prediction == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Legitimate Transaction")