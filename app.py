import streamlit as st
import pickle
import numpy as np

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Student Stress Predictor",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------
# LOAD MODEL
# ---------------------------
with open("svm.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#4A148C;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.stButton > button {
    width:100%;
    background-color:#6A1B9A;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:3em;
}

.stButton > button:hover {
    background-color:#8E24AA;
    color:white;
}

.result-card {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:25px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown(
    '<div class="title">🧠 Student Stress Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a student is stressed based on lifestyle factors</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------
# INPUTS
# ---------------------------
col1, col2 = st.columns(2)

with col1:

    student_type = st.selectbox(
        "Student Type",
        [0, 1],
        help="0 = Day Scholar, 1 = Hosteller"
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=15.0,
        value=7.0
    )

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=20.0,
        value=5.0
    )

    social_media_hours = st.number_input(
        "Social Media Hours",
        min_value=0.0,
        max_value=15.0,
        value=2.0
    )

with col2:

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        80
    )

    exam_pressure = st.slider(
        "Exam Pressure",
        0,
        10,
        5
    )

    family_support = st.slider(
        "Family Support",
        0,
        10,
        5
    )

    month = st.slider(
        "Month",
        1,
        12,
        6
    )

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("🔍 Predict Stress Level"):

    input_data = np.array([[
        student_type,
        sleep_hours,
        study_hours,
        social_media_hours,
        attendance,
        exam_pressure,
        family_support,
        month
    ]])

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ Student is likely experiencing Stress")
        st.progress(85)

    else:
        st.success("😊 Student is likely Not Stressed")
        st.progress(25)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown(
    """
    <center>
    Developed using Streamlit • Scikit-Learn • SVM
    </center>
    """,
    unsafe_allow_html=True
)
