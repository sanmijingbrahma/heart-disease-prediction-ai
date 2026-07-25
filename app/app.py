import streamlit as st

from predict import predict
from utils import (
    validate_input,
    get_risk_label,
    format_probability,
)


st.set_page_config(
    page_title="Heart Disease Risk Prediction",
    page_icon="❤️",
    layout="centered",
)


st.title("❤️ Heart Disease Risk Prediction")

st.write(
    "Predict the likelihood of heart disease using a machine learning model."
)

st.markdown("---")

st.subheader("Patient Information")


col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50,
    )

    sex = st.selectbox(
        "Sex",
        options=[0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male",
    )

    cp = st.selectbox(
        "Chest Pain Type",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Typical Angina",
            2: "Atypical Angina",
            3: "Non-anginal Pain",
            4: "Asymptomatic",
        }[x],
    )

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120,
    )

    chol = st.number_input(
        "Cholesterol (mg/dl)",
        min_value=50,
        max_value=700,
        value=200,
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
    )

    restecg = st.selectbox(
        "Resting ECG",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Normal",
            1: "ST-T Wave Abnormality",
            2: "Left Ventricular Hypertrophy",
        }[x],
    )

with col2:
    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150,
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
    )

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Upsloping",
            2: "Flat",
            3: "Downsloping",
        }[x],
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        options=[0, 1, 2, 3, 4],
    )

    thal = st.selectbox(
        "Thal",
        options=[3, 6, 7],
        format_func=lambda x: {
            3: "Normal",
            6: "Fixed Defect",
            7: "Reversible Defect",
        }[x],
    )


patient = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal,
}

st.markdown("---")


if st.button("Predict Risk", use_container_width=True):

    valid, message = validate_input(patient)

    if not valid:
        st.error(message)
    else:
        prediction, probability = predict(patient)

        risk = get_risk_label(prediction)
        prob = format_probability(probability)

        st.subheader("Prediction")

        if prediction == 0:
            st.success(f"🟢 {risk}")
        else:
            st.error(f"🔴 {risk}")

        st.metric("Risk Probability", prob)


with st.expander("📖 Feature Guide"):
    st.markdown("""
### Chest Pain Type
- **1** = Typical Angina
- **2** = Atypical Angina
- **3** = Non-anginal Pain
- **4** = Asymptomatic

### Fasting Blood Sugar
- **0** = ≤ 120 mg/dl
- **1** = > 120 mg/dl

### Resting ECG
- **0** = Normal
- **1** = ST-T Wave Abnormality
- **2** = Left Ventricular Hypertrophy

### Exercise Induced Angina
- **0** = No
- **1** = Yes

### Slope of Peak Exercise ST Segment
- **1** = Upsloping
- **2** = Flat
- **3** = Downsloping

### Number of Major Vessels (ca)
- Number of major vessels colored by fluoroscopy (0–4)

### Thal
- **3** = Normal
- **6** = Fixed Defect
- **7** = Reversible Defect
""")


st.markdown("---")

st.caption(
    "⚠️ This tool is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment."
)
