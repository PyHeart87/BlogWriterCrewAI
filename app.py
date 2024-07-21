import streamlit as st
from main_crewai import run_crew

st.title("CrewAI - AI Trends Blog Generator")

if st.button("Generate Blog Post"):
    with st.spinner("AI agents are working on your blog post..."):
        try:
            result = run_crew()
            st.success("Blog post generated successfully!")
            st.subheader("Generated Content:")
            st.markdown(result, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your console for more details.")

st.sidebar.header("About")
st.sidebar.info("This app uses CrewAI to generate a blog post about the latest AI trends. It employs a researcher agent to gather information and a writer agent to create the final content.") 