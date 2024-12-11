import streamlit as st
import random
class Home:
    def __init__(self):
        pass
    def app(self):
        st.markdown("""
            <style>
            .main-title {
                font-family: 'Arial', sans-serif;
                color: #4A90E2;
                text-align: center;
            }
            .subheader {
                font-size: 20px;
                color: #FF6F61;
                text-align: center;
            }
            .fact-box {
                background-color: #F0F4F8;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
            }
            .button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 10px 0;
                border-radius: 5px;
                cursor: pointer;
            }
            </style>
            """, unsafe_allow_html=True)

        st.markdown("<h1 class='main-title'>About Me</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='subheader'>Hello! I am Danil.</h3>", unsafe_allow_html=True)
        st.write(
            "Welcome to my page! Here you will find information about me, my photos, videos and much more.")

        images = [
            "img/Photo.jpeg",
            "img/Photo2.jpeg",
            "img/Photo3.jpeg"
        ]
        if 'current_image' not in st.session_state:
            st.session_state.current_image = 0

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Back"):
                st.session_state.current_image = (st.session_state.current_image - 1) % len(images)
        with col3:
            if st.button("Next ➡️"):
                st.session_state.current_image = (st.session_state.current_image + 1) % len(images)

        st.image(images[st.session_state.current_image], use_column_width=True)

        # st.video("path_to_your_video.mp4")
        #
        # st.audio("path_to_your_audio.mp3")

        facts = [
            "I play drums and I'm into basketball!",
            "I love programming and create web applications.",
            "I once participated in a volunteer program to support the elderly."
        ]

        if st.button("✨ Find out an interesting fact!"):
            random_fact = random.choice(facts)
            st.write(random_fact)

        correct_age = 18
        st.markdown("<h1 class='main-title'>Guess my age!</h1>", unsafe_allow_html=True)

        st.write("Try to guess my age and check if you're right!")

        user_guess = st.number_input("Enter your own version:", min_value=15, max_value=25, step=1)

        if st.button("Check"):
            if user_guess == correct_age:
                st.markdown("<p class='success'>🎉 Right! You guessed my age.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='error'>❌ Wrong! Try again.</p>", unsafe_allow_html=True)





        name = st.text_input("What's your name?")
        if name:
            st.write(f"👋 Hello, {name}! I'm glad to see you on my page.")
        st.markdown("</div>", unsafe_allow_html=True)