import streamlit as st
from gemini_api_openai import GeminiClient

# Set up Gemini API client
api_key = "YOUR_GEMINI_API_KEY"
client = GeminiClient(api_key)

def main():
    st.title("Resume Coach")
    st.write("This app provides personalized resume coaching based on a job description.")

    # Get job description from user
    job_description = st.text_area("Enter the job description here:")

    # Get user's resume
    resume_text = st.text_area("Enter your resume here:")

    if st.button("Get Resume Coaching"):
        if not job_description or not resume_text:
            st.warning("Please enter both the job description and your resume.")
        else:
            try:
                # Call Gemini API for resume coaching
                response = client.resume_coach(job_description, resume_text)
                st.success(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()