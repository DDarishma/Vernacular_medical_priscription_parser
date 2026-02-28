import streamlit as st
from ocr import extract_text
from llm import analyze_prescription
from tts import generate_audio

st.set_page_config(page_title="Vernacular Prescription Parser", layout="wide")

st.title("🩺 Vernacular Medical Prescription Parser")
st.write("Upload a prescription and get explanation in English, Telugu & Hindi")

uploaded_file = st.file_uploader("Upload Prescription Image", type=["png", "jpg", "jpeg"])

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Prescription")

    if st.button("Analyze Prescription"):

        with st.spinner("Processing..."):

            text = extract_text(uploaded_file)
            result = analyze_prescription(text)

        st.subheader("📋 Extracted Medicines")

        for med in result.get("medicines", []):

            st.markdown(f"### 💊 {med.get('name','')}")
            st.write("**Dosage:**", med.get("dosage",""))
            st.write("**English:**", med.get("english_explanation",""))

            st.success("Telugu Explanation")
            st.write(med.get("telugu_explanation",""))

            st.info("Hindi Explanation")
            st.write(med.get("hindi_explanation",""))

            # Telugu Audio
            if med.get("telugu_explanation"):
                audio_file = generate_audio(med["telugu_explanation"], lang="te")
                st.audio(audio_file)

        if result.get("warnings"):
            st.error("⚠ Safety Warnings")
            for w in result["warnings"]:
                st.write("-", w)