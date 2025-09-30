import streamlit as st

st.set_page_config(page_title="Smart Career Advisor", page_icon="🎓", layout="centered")

st.title("🎓 Smart Career Advisor")
st.markdown("Welcome! Let’s find the best career path for you based on your preferences.")

with st.form("career_form"):
    name = st.text_input("👤 Your Name")
    education = st.selectbox("🎓 Your Current Education Level", [
        "Matric", "Intermediate", "Diploma", "Bachelor's", "Master's", "PhD"
    ])
    interests = st.multiselect("💡 Your Interests", [
        "Science", "Technology", "Arts", "Business", "Healthcare", "Design", "Engineering", "Writing"
    ])
    goal = st.text_input("🎯 Your Future Goal (e.g., become a doctor, start a business, work in AI, etc.)")
    work_style = st.radio("💼 Preferred Work Style", [
        "Remote", "On-site", "Hybrid", "Freelance", "Entrepreneur"
    ])
    personality = st.selectbox("🧠 What best describes your personality?", [
        "Analytical", "Creative", "Social", "Organized", "Problem-solver", "Visionary"
    ])
    submitted = st.form_submit_button("Get Career Advice")

if submitted:
    st.header(f"👋 Hello {name}, here’s your Smart Career Report:")

    # 🎓 Suggested Career Paths
    st.subheader("🔍 Suggested Career Paths")
    if "Technology" in interests or "Engineering" in interests:
        st.markdown("- Software Engineering\n- Data Science\n- Cybersecurity\n- AI/ML Research")
    elif "Arts" in interests:
        st.markdown("- Graphic Design\n- Content Creation\n- Fashion Design\n- Film Making")
    elif "Healthcare" in interests:
        st.markdown("- Medicine\n- Nursing\n- Medical Technology\n- Psychology")
    elif "Business" in interests:
        st.markdown("- Marketing\n- E-commerce\n- Entrepreneurship\n- Finance")
    elif "Writing" in interests:
        st.markdown("- Journalism\n- Technical Writing\n- Blogging\n- Publishing")
    else:
        st.markdown("- General Management\n- Teaching\n- Public Administration")

    # 🧑‍💼 Job Roles
    st.subheader("🧑‍💼 Potential Job Roles")
    if personality == "Analytical":
        st.markdown("- Data Analyst\n- Financial Analyst\n- Engineer\n- Programmer")
    elif personality == "Creative":
        st.markdown("- Designer\n- Animator\n- Content Creator\n- Creative Director")
    elif personality == "Social":
        st.markdown("- HR Manager\n- Counselor\n- Teacher\n- Sales Manager")
    elif personality == "Organized":
        st.markdown("- Project Manager\n- Accountant\n- Admin Officer")
    elif personality == "Problem-solver":
        st.markdown("- Consultant\n- Engineer\n- AI Developer")
    elif personality == "Visionary":
        st.markdown("- Entrepreneur\n- Startup Founder\n- Innovation Manager")

    # 🎯 Future Goals
    st.subheader("🎯 Tailored Advice Based on Your Goal")
    st.markdown(f"You want to: **{goal}**")
    if "business" in goal.lower():
        st.info("Start exploring entrepreneurship, online business, and marketing tools like Shopify, SEO, and digital ads.")
    elif "doctor" in goal.lower():
        st.info("Pursue FSc Pre-Medical → MBBS or BDS → Specialization.")
    elif "ai" in goal.lower() or "machine learning" in goal.lower():
        st.info("Start with Python, then learn ML, DL, and explore platforms like Coursera, edX, and Hugging Face.")
    elif "design" in goal.lower():
        st.info("Practice on Figma, Adobe tools. Explore UI/UX or graphic design freelancing.")
    else:
        st.info("Stay focused, explore real-world experience through internships or self-learning platforms.")

    # 📚 Learning Resources
    st.subheader("📚 Recommended Learning Resources")
    st.markdown("""
- [Coursera](https://coursera.org)
- [edX](https://edx.org)
- [YouTube Channels](https://www.youtube.com) like Apna College, Simplilearn, CrashCourse
- [Kaggle](https://kaggle.com) for Data Science & ML
- [Fiverr](https://fiverr.com) & [Upwork](https://upwork.com) for freelancing ideas
    """)

    # 💡 Final Advice
    st.subheader("💡 Final Tips")
    st.success("Start small, be consistent, learn continuously — and don't be afraid to explore multiple paths. You're in charge of your future! 💪")

    st.markdown("---")
    st.caption("Made with ❤️ by Maheen Touqeer")
