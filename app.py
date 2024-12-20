import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Heart Disease Detection", layout="wide")

# Inject CSS styles
# Inject CSS styles
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #b33b29;
        margin: 0;
        padding: 20px;
    }

    .container {
        max-width: 600px;
        margin: auto;
        background: #b33b29;  /* Change the background color here */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }

    h1 {
        text-align: center;
        color: #090411;
        font-size: 1.8rem;
    }

    .disease-list {
        margin: 20px 0;
    }

    .disease {
        margin: 15px 0;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: #b33b29;
        color:#ffffff;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .disease:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .percentage {
        font-weight: bold;
        color: #2c3e50;
    }

    button {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: #b33b29;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    button:hover {
        background-color: #882212;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown("<h1>Heart Disease Detection</h1>", unsafe_allow_html=True)

# Navigation between pages
page = st.radio("Navigate", options=["Input Form", "Prediction Results"])

# Page 1: Input Form
if page == "Input Form":
    with st.container():  # Ensure this block is indented correctly
        # Layout for the form
        with st.form(key='input_form'):  # Added form block here

            # Age
            with st.expander("Age"):
                age = st.number_input("Age (in years)", min_value=0, max_value=120, value=40)
                st.caption("The number of years a person has lived. Older age increases heart disease risk.")

            # Sex
            with st.expander("Sex"):
                sex = st.radio("Select your sex:", options=["Male", "Female"])
                st.caption("1 = Male, 0 = Female. Men often develop heart disease earlier.")

            # Chest Pain Type
            with st.expander("Chest Pain Type"):
                cp = st.selectbox("Chest Pain Type:", options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
                st.caption("Indicates type of chest pain. 0 = Typical Angina.")

            # Resting Blood Pressure
            with st.expander("Resting Blood Pressure"):
                bp = st.slider("Resting Blood Pressure (mm Hg):", min_value=80, max_value=200, value=120)
                st.caption("High blood pressure can damage vessels and increase the risk.")

            # Cholesterol
            with st.expander("Cholesterol"):
                chol = st.slider("Serum Cholesterol (mg/dl):", min_value=100, max_value=400, value=233)
                st.caption("High cholesterol can lead to plaque buildup.")

            # Fasting Blood Sugar
            with st.expander("Fasting Blood Sugar"):
                fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:", options=["False", "True"])
                st.caption("1 = High blood sugar, 0 = Normal.")

            # Resting ECG
            with st.expander("Resting ECG"):
                restecg = st.selectbox("Resting ECG Results:", options=["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
                st.caption("Abnormal ECG results can indicate ischemia.")

            # Exercise Test
            with st.expander("Exercise Test"):
                thalach = st.slider("Maximum Heart Rate (bpm):", min_value=70, max_value=220, value=150)
                exang = st.radio("Exercise-induced angina:", options=["Yes", "No"])
                st.caption("Angina during activity can indicate significant heart issues.")

            # Additional Tests
            with st.expander("Additional Tests"):
                oldpeak = st.slider("ST Depression:", min_value=0.0, max_value=6.0, value=2.3, step=0.1)
                slope = st.selectbox("Slope of Peak Exercise ST Segment:", options=["Upsloping", "Flat", "Downsloping"])
                ca = st.selectbox("Number of Major Vessels:", options=["0", "1", "2", "3"])
                thal = st.selectbox("Thalassemia:", options=["Normal", "Fixed Defect", "Reversible Defect"])
                st.caption("Test to assess heart function under stress.")

            submit_button = st.form_submit_button("Calculate Disease Chances")

        if submit_button:
            # Store the input data for use in prediction page
            st.session_state.age = age
            st.session_state.sex = sex
            st.session_state.cp = cp
            st.session_state.bp = bp
            st.session_state.chol = chol
            st.session_state.fbs = fbs
            st.session_state.restecg = restecg
            st.session_state.thalach = thalach
            st.session_state.exang = exang
            st.session_state.oldpeak = oldpeak
            st.session_state.slope = slope
            st.session_state.ca = ca
            st.session_state.thal = thal

            # Redirect to prediction results page
            st.session_state.page = "Prediction Results"

# Page 2: Prediction Results
if page == "Prediction Results":
    # Fetch the stored input data from session
    if hasattr(st.session_state, 'age'):
        age = st.session_state.age
        sex = st.session_state.sex
        cp = st.session_state.cp
        bp = st.session_state.bp
        chol = st.session_state.chol
        fbs = st.session_state.fbs
        restecg = st.session_state.restecg
        thalach = st.session_state.thalach
        exang = st.session_state.exang
        oldpeak = st.session_state.oldpeak
        slope = st.session_state.slope
        ca = st.session_state.ca
        thal = st.session_state.thal
        
        st.markdown("<h3>Heart Disease Risk Prediction:</h3>", unsafe_allow_html=True)

        # Mock disease predictions (replace with actual model predictions)
        diseases = [
            {"id": "cad-percentage", "name": "Coronary Artery Disease (CAD)"},
            {"id": "arrhythmias-percentage", "name": "Heart Arrhythmias"},
            {"id": "heart-failure-percentage", "name": "Heart Failure"},
            {"id": "valve-disease-percentage", "name": "Heart Valve Disease"},
            {"id": "congenital-defects-percentage", "name": "Congenital Heart Defects"},
            {"id": "rheumatic-disease-percentage", "name": "Rheumatic Heart Disease"},
            {"id": "cardiomyopathy-percentage", "name": "Heart Muscle Disease (Cardiomyopathy)"},
            {"id": "heart-attack-percentage", "name": "Myocardial Infarction (Heart Attack)"}
        ]

        # Display predicted chances for each disease
        for disease in diseases:
            chance = random.randint(0, 100)  # Replace this with the model's prediction logic
            st.markdown(f"<div class='disease'><h2>{disease['name']}</h2><p class='percentage'>Chance: {chance}%</p></div>", unsafe_allow_html=True)
    else:
        st.error("No data found! Please go back to the input form and submit your details.")
