import streamlit as st
import time

st.set_page_config(page_title="AI Profile Trust Analyzer", layout="wide")

st.title("🔍 AI Profile Trust Analyzer")
st.write("Analyze any profile using URL")

url = st.text_input("🌐 Enter Profile URL")

if st.button("🚀 Analyze Profile"):

    if url == "":
        st.warning("Please enter a URL")
    else:
        with st.spinner("Analyzing profile..."):
            time.sleep(2)

        # Dummy data (for now)
        followers = 120
        following = 300
        posts = 5
        reviews = 10
        account_age = 60

        score = 75

        col1, col2, col3 = st.columns(3)

        col1.metric("Followers", followers)
        col2.metric("Posts", posts)
        col3.metric("Account Age", account_age)

        st.divider()

        st.subheader("🔐 Trust Score")
        st.progress(score / 100)
        st.write(f"{score}%")

        if score > 70:
            st.success("✅ Real Profile")
        else:
            st.error("❌ Fake Profile")
