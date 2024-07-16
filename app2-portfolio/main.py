import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpeg", width=650)

with col2:
    st.title("Prateek Mahajan")
    content = """
    Hi, My name is Prateek Mahajan, and I am currently pursuing a Bachelor of Technology (B.Tech) in Computer Science. My journey in this field has been driven by a profound interest in technology and its potential to transform the world. Through my academic experiences, I have developed a strong foundation in various programming languages, algorithms, and software development practices.
    Beyond my academic pursuits, I have a deep passion for sports. Engaging in different sports activities not only helps me stay physically fit but also teaches me valuable life skills such as teamwork, leadership, and perseverance. Balancing my studies with sports has instilled in me a sense of discipline and time management, which I believe are crucial for success in any field.
    """
    st.info(content)

content2 = """
        Below you can find of some of the Apps I have build in python.Feel free to contact me!
        """
st.write(content2)




