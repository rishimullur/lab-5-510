import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert resume coach and career advisor.

Please provide comprehensive resume advice and tips tailored to the given job description.

Please include the following details:
- Key skills and qualifications to highlight
- Relevant experience and accomplishments to emphasize
- Resume formatting and structure recommendations
- Any additional tips or advice to improve the chances of getting an interview

If you cannot provide any concrete answer or if you are not aware of the job, please respond with "I am not aware of this job and cannot advice you."

The job description is:
{prompt}
"""

def generate_resume_advice(prompt):
    response = model.generate_content(prompt_template.format(prompt=prompt))
    return response.text

st.title("📝 AI Resume Coach")

job_description = st.text_area("Enter the job description you want resume advice for:")

if st.button("Get Resume Advice"):
    advice = generate_resume_advice(job_description)
    st.write(advice)
