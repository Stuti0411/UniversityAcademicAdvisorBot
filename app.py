import streamlit as st
from rag.rag_pipeline import load_pdfs
from router.smart_router import route_question

st.set_page_config(page_title="University Academic Advisor Bot", layout = "centered")
st.title("University Academic Advisor Bot")

st.write("Ask anything about:")
st.write("Student Records")
st.write("University Policies")
st.write("Holiday Schedules")
st.write("Scholarships /  Internships / Admissions")

#load rag PDFs
load_pdfs()

question = st.text_input("Enter you question")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        answer = route_question(question)
        st.success("Answer Generated!")
        st.write(answer)    