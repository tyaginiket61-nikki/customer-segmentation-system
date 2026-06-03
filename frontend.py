import streamlit as st
import requests

st.set_page_config(page_title="Customer Segmentation", layout="centered")

st.title("🧠 Customer Segmentation App")
st.write("Enter customer details to predict cluster")

age = st.slider("Age", 18, 70, 25)
income = st.slider("Annual Income", 10, 150, 50)
score = st.slider("Spending Score", 1, 100, 50)

if st.button("Predict Cluster"):
    
    data = {
        "age": age,
        "annual_income": income,
        "spending_score": score
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            cluster = result["predicted_cluster"]

            st.success(f"🎯 Predicted Cluster: {cluster}")

            if cluster == 0:
                st.info("💡 Low income, low spending")
            elif cluster == 1:
                st.info("💡 High income, high spending")
            elif cluster == 2:
                st.info("💡 Average customers")
            else:
                st.info("💡 Other segment")

        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")

        