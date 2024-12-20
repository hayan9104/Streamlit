import streamlit as st
import random

# Set the page title
st.title('Heart Disease Detection')

# Function to calculate disease chances
def calculate_disease_chances():
    diseases = {
        'Coronary Artery Disease (CAD)': random.randint(0, 100),
        'Heart Arrhythmias': random.randint(0, 100),
        'Heart Failure': random.randint(0, 100),
        'Heart Valve Disease': random.randint(0, 100),
        'Congenital Heart Defects': random.randint(0, 100),
        'Rheumatic Heart Disease': random.randint(0, 100),
        'Heart Muscle Disease (Cardiomyopathy)': random.randint(0, 100),
        'Myocardial Infarction (Heart Attack)': random.randint(0, 100),
    }
    return diseases

# Display the diseases and their chances
diseases = calculate_disease_chances()

# Display disease information in Streamlit
st.subheader("Disease Detection Results")
for disease, chance in diseases.items():
    st.markdown(f"**{disease}**: {chance}%")

# Button to trigger the calculation (this is optional as we are calculating on load)
if st.button("Recalculate Chances"):
    diseases = calculate_disease_chances()
    for disease, chance in diseases.items():
        st.markdown(f"**{disease}**: {chance}%")
