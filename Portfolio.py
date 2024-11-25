import streamlit as st
import info
import pandas as pd

#About Me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write('---')
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height ="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt = "Github" width ="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href = "mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width ="75" height ="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"
    }, hide_index=True)
    st.write("---")

education_section(info.education_data, info.course_data)

#Internship/Work Experience
def IW_experience_section(IW_experience_data):
    st.header("Internship/Work Experience")
    for IW_title, (IW_description, image) in IW_experience_data.items():
        expander = st.expander(f"{IW_title}")
        expander.image(image, width=250)
        for bullet in IW_description:
            expander.write(bullet)
    st.write("---")
IW_experience_section(info.IW_experience_data)

#Healthcare Experience
def healthcare_experience_section(healthcare_experience_data):
    st.header("Healthcare Experience")
    for healthcare_title, (healthcare_description, image) in healthcare_experience_data.items():
        expander = st.expander(f"{healthcare_title}")
        expander.image(image, width=250)
        for bullet in healthcare_description:
            expander.write(bullet)
    st.write("---")
healthcare_experience_section(info.healthcare_experience_data)

#Honors
def research_section(honors_data):
    st.header("Honors")
    for honors_name, data in honors_data.items():
        expander = st.expander(f"{honors_name}")
        if isinstance(data, tuple) and len(data) == 2:
            honors_description, image = data
            if image:
                expander.image(image, width=250)
        else:
            honors_description = data
        for bullet in honors_description:
            expander.write(bullet)
    st.write("---")
research_section(info.honors_data)

#Research
def research_section(research_data):
    st.header("Research")
    for research_name, data in research_data.items():
        expander = st.expander(f"{research_name}")
        if isinstance(data, tuple) and len(data) == 2:
            research_description, image = data
            if image:
                expander.image(image, width=250)
        else:
            research_description = data
        for bullet in research_description:
            expander.write(bullet)
    st.write("---")
research_section(info.research_data)


#Skills
def skills_section(skills_data, course_data):
    st.header("Skills")
    st.write(f"**Language:** {skills_data['Language']}")
    st.write(f"**Lab Skills:** {skills_data['Lab Skills']}")
    st.write(f"**Software Proficiency:** {skills_data['Software Proficiency']}")
    st.write(f"**Administrative/Financial:** {skills_data['Administrative/Financial']}")
    st.write(f"**Certifications:** {skills_data['Certifications']}")
    st.write("---")

skills_section(info.skills_data, info.course_data)

#Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, details in leadership_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, (details, image) in activity_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data, info.activity_data)
