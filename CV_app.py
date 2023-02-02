from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic_Luka.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Luka Radosavljevic"
PAGE_ICON = ":wave:"
NAME = "Luka Radosavljevic"
DESCRIPTION = """
Stud. Cand. Merc. MAC. Med fokus på automatisering og optimering af processer, ved hjælp af Data Science.
"""
EMAIL = "luka.radosavljevic@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/luka-radosavljevic-9466bb168/",
    "GitHub": "https://github.com/LukaRado",
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
    st.image(profile_pic, width=250)

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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 1 Års erfaring med bogføring og adhoc opgaver i økonomiafdelingen
- ✔️ Omfangsrig erfaring og viden indenfor Python og Excel
- ✔️ God forståelse af statistiske principper og deres respektive anvendelser
- ✔️ Proaktiv og initiativrig teamspiller
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Supervised and unsupervised machine learning, exploratory data analysis, network analysis)
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Matplotlib, Altair
- 📚 Modeling: Logistic regression, linear regression, decision trees
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Erhvervserfaring")
st.write("---")

# --- JOB 1
st.write("🚧", "**Studiejob - Økonomiafdelingen | Strandfaraskip Landsins**")
st.write("06/2021 - 12/2021")
st.write(
    """
- ► Sommerferiejob, og sidenhen arbejdet hjemmefra resten af året
- ► Arbejdet med kreditor og debitor bogføring og adhoc opgaver som bl.a. udarbejdelse af økonomiske rapporter til intern brug

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Kasserer | Føroyingafelagid i Aalborg**")
st.write("03/2021 - 03/2022")
st.write(
    """
- ► Har stået for den samtlige økonomiske administration, heriblandt:
- ► Budgetlægning, udarbejdelse af årsrapport, bogføring, forhandle samarbejdsaftaler
"""
)




