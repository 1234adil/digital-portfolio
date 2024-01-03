from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Adil Ahmadzada"
PAGE_ICON = ":wave:"
NAME = "Adil Ahmadzada"
DESCRIPTION = """
Business Development Manager / Consultant, Lean Six Sigma Professional.
"""
EMAIL = "adilahmadzada5@gmail.com"
SOCIAL_MEDIA = {
    "YouTube":  "https://www.youtube.com/channel/UCWmMj6MDEvHmiad8FgGBVNQ",
    "LinkedIn": "https://www.linkedin.com/in/adil-ahmadzada-9375251b8/",
    "Personal": "https://adilahmadzada.dorik.io/"
}
# Achievement details
achievements = {
    "🏆 Lean Six Sigma Black Belt":  "https://gstudy.greycampus.com/certificate/201083566981",
    "🏆 Lean Six Sigma Green Belt": "https://www.coursera.org/account/accomplishments/specialization/BLH3RL6J9UZY",
    "🏆 Lean Six Sigma Yellow Belt": "https://www.coursera.org/account/accomplishments/specialization/GW4C7ZVXDL5U",
    "🏆 Leading People and Teams": "https://www.coursera.org/account/accomplishments/specialization/AJE98TJC84FG",
    "🏆 Engineering Project Management": "https://www.coursera.org/account/accomplishments/specialization/UB74MJZDL8R6",
    "🏆 International Business Essentials": "https://www.coursera.org/account/accomplishments/verify/QXJS6Y4Y4NT8",
    "🏆 Project Management Principles and Practices": "https://www.coursera.org/account/accomplishments/specialization/XBD64P5MGGSV",
    "🏆 Strategic Management and Innovation": "https://www.coursera.org/account/accomplishments/specialization/57A5P94YTCS6",
    "🏆 Corporate Entrepreneurship": "https://www.coursera.org/account/accomplishments/specialization/44PJTDL9QQ25",
    "🏆 Leadership Development for Engineers": "https://www.coursera.org/account/accomplishments/specialization/MK6WX72J49NW",
    "🏆 ICPM Certified Supervisor": "https://www.coursera.org/account/accomplishments/professional-cert/H8FM46X3PBVF",
    "🏆 International Marketing": "https://www.coursera.org/account/accomplishments/specialization/FKAGVXBLL278",
    "🏆 Management for Global Competitive Advantage": "https://www.coursera.org/account/accomplishments/specialization/GU74GKR3U4J4",
    "🏆 World Economy": "https://www.coursera.org/account/accomplishments/specialization/Z7ZCZXCRUHKP",
    "🏆Autodesk": "https://www.coursera.org/account/accomplishments/specialization/A3762XS9FKB4",
   }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Achievements")
st.write("---")
for achievements, link in achievements.items():
    st.write(f"[{achievements}]({link})")
