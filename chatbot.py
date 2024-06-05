import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-image: url('file:///D:/children-education/Children/EducationWallpaper.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
"""
<style>
    .title
    {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .text_input
    {
        font-size:20px;
    }
</style>
""",unsafe_allow_html=True)
st.markdown('<div class="title">Question Answering Application</div>', unsafe_allow_html=True)
st.sidebar.success('Home')
st.markdown(
    """
    <label style='font-size: 25px; color: black;font-weight:bold;'>
        Enter URL
    </label>
    """,
    unsafe_allow_html=True
)
url = st.text_input("")
col1, col2, col3 = st.columns(3)
with col1:
    class_option = st.selectbox(
        "Select Class",
        ("Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12")
    )
with col2:
    subject_option = st.selectbox(
        "Select Subject",
        ("Math", "Science", "History", "Geography", "English", "Physics", "Chemistry", "Biology", "Economics", "Computer Science")
    )
with col3:
    chapter_option = st.selectbox(
        "Select Chapter",
        ("Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7", "Chapter 8", "Chapter 9", "Chapter 10")
    )
c1,c2= st.columns(2)  
with c1:
    question_type = st.selectbox(
    "Select Question Type",
    ("Low", "Medium", "High")
)
with c2:
    question_type1 = st.selectbox(
    "Select Question type",
    ("Subjective", "MCQ","Fill_the_Blank")
)
 
question = st.chat_input("Ask The Question")


