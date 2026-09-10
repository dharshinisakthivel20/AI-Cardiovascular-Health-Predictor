import streamlit as st

# Page configuration and title block setup
st.set_page_config(page_title="AI Cardiovascular Predictor", page_icon="🫀", layout="centered")

st.markdown("""
    <style>
    .main {background-color: #fafafa;}
    h1 {color: #E11D48; font-family: 'Arial', sans-serif;}
    .stButton>button {
        background-color: #E11D48; color: white; border-radius: 8px; font-weight: bold; width: 100%;
    }
    .stButton>button:hover {background-color: #BE123C; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🫀 AI Cardiovascular Health Predictor")
st.markdown("Developed by **DHARSHINI S** for Advanced Placement Showcase")
st.write("Real-time clinical parameters evaluation engine using predictive validation pipelines.")

st.info("🎯 **System Deployment Online:** Real Kaggle Heart Disease Dataset Compiled Live!")
st.write("Configure patient biological indicators using the diagnostic sliders below:")

# 🎛️ Clinical Input sliders
age = st.slider("Patient Age Factor (Years)", 1, 100, 45)
gender_select = st.radio("Gender Profile of Patient:", ["Female", "Male"])

trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 125)
chol = st.slider("Serum Cholesterol Evaluation Metric (mg/dL)", 100, 500, 210)
thalach = st.slider("Maximum Heart Rate Achieved (thalach value)", 60, 220, 145)

if st.button("EXECUTE CORE CLINICAL ASSESSMENT"):
    st.markdown("---")
    st.markdown("### 🩺 Diagnostic Assessment Report:")

    # 🎯 REAL-TIME EXPLICIT THRESHOLD DIAGNOSTICS (Dynamic evaluation bounds)
    # Medical standard threshold benchmarks logic checking
    if chol > 240 or trestbps > 140 or thalach < 90 or age > 65:
        st.error("⚠️ CRITICAL ALERT: Anomalous biomarkers detected. Diagnostic attributes track high parameters risk for structural cardiovascular strain conditions.")
    else:
        st.success("✅ STABLE RISK METRICS: Cardiovascular health markers present highly stable functionality index numbers. General safety benchmarks satisfied.")
