import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image

image = Image.open('img/unicorn.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
logo_path = os.path.join(os.path.dirname(__file__), "img", "small-deer-svgrepo-com.svg")

pages = ["Home", "Project1", "Project2", "Project3"]

styles = {
    "nav": {
        "background-color": "rgba(30, 144, 255, 0.9)",
        "display": "flex",
        "justify-content": "center",
        "padding": "0.5rem 1rem",
        "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)",
    },
    "img": {
        "position": "absolute",
        "bottom": "1%",
        "top": "1px",
        "left": "-2px",
        "width": "55px",
        "height": "55px",
        "object-fit": "contain",
        "border-radius": "10px"
    },
    "div": {
        "max-width": "960px",
        "margin": "0 auto",
    },
    "span": {
        "border": "2px solid rgba(255, 215, 0, 0.8)",
        "border-radius": "4px",
        "color": "rgba(255, 255, 255, 0.9)",
        "margin": "0 0.5rem",
        "padding": "0.5rem 1rem",
        "font-weight": "500",
        "transition": "background-color 0.3s ease, color 0.3s ease",
        "cursor": "pointer",
    },
    "active": {
        "background-color": "rgba(255, 215, 0, 0.8)",
        "color": "#2c3e50",
        "font-weight": "600",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",
        "color": "#f1c40f",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = st_navbar(pages, styles=styles, logo_path=logo_path, options=options)

if page == 'Home':
    Home.Home().app()
elif page == 'Project1':
    Project1.Project1().app()
elif page == 'Project2':
    Project2.Project2().app()
elif page == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()
