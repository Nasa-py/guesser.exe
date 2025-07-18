# import streamlit as st
# import random

# # Page config
# st.set_page_config(page_title="🎯 Guess The Number", layout="centered")

# # Setup session state
# if "num" not in st.session_state:
#     st.session_state.num = random.randint(1, 100)
# if "remaining" not in st.session_state:
#     st.session_state.remaining = 10
# if "message" not in st.session_state:
#     st.session_state.message = ""
# if "won" not in st.session_state:
#     st.session_state.won = False
# if "lost" not in st.session_state:
#     st.session_state.lost = False
# if "show_result" not in st.session_state:
#     st.session_state.show_result = False
# if "guesses" not in st.session_state:
#     st.session_state.guesses = 0
# if "anim_played" not in st.session_state:
#     st.session_state.anim_played = False
# if "input_key" not in st.session_state:
#     st.session_state.input_key = str(random.randint(1000, 9999))


# # Reset function
# def reset_game():
#     st.session_state.num = random.randint(1, 100)
#     st.session_state.remaining = 10
#     st.session_state.message = ""
#     st.session_state.won = False
#     st.session_state.lost = False
#     st.session_state.show_result = False
#     st.session_state.guesses = 0
#     st.session_state.anim_played = False
#     st.session_state.input_key = str(random.randint(1000, 9999))


# # Title
# st.title("🎯 Guess the Number Game")
# st.markdown("I’m thinking of a number between **1** and **100**.\nYou have **10 guesses**!")

# # Input
# if not st.session_state.show_result:
#     guess = st.text_input(
#         "Enter your guess:",
#         value="",
#         key=st.session_state.input_key,
#         placeholder="Your number..."
#     )

#     if st.button("Submit Guess"):
#         if guess.strip().isdigit():
#             num = int(guess.strip())
#             st.session_state.guesses += 1
#             if num == st.session_state.num:
#                 st.session_state.message = f"✅ You got it! It was {st.session_state.num}."
#                 st.session_state.won = True
#                 st.session_state.show_result = True
#                 st.rerun()

#             elif num < st.session_state.num:
#                 st.session_state.remaining -= 1
#                 st.session_state.message = "🔼 Too low!"
#             else:
#                 st.session_state.remaining -= 1
#                 st.session_state.message = "🔽 Too high!"

#             if st.session_state.remaining <= 0 and not st.session_state.won:
#                 st.session_state.message = f"❌ You lost! It was {st.session_state.num}."
#                 st.session_state.lost = True
#                 st.session_state.show_result = True
#                 st.rerun()

#         else:
#             st.warning("Please enter a valid number.")

#     st.markdown(f"🧠 Remaining guesses: **{st.session_state.remaining}**")

# # Show message
# if st.session_state.message:
#     if st.session_state.won:
#         st.success(st.session_state.message)
#     elif st.session_state.lost:
#         st.error(st.session_state.message)
#     else:
#         st.info(st.session_state.message)

# # Show result + animation
# if st.session_state.show_result and not st.session_state.anim_played:
#     if st.session_state.won:
#         st.balloons()
#     elif st.session_state.lost:
#         st.markdown("""
#             <style>
#             .loss-animation {
#                 position: fixed;
#                 top: 0;
#                 left: 0;
#                 width: 100vw;
#                 height: 100vh;
#                 background: radial-gradient(circle, #ff0000cc, #000000ee);
#                 z-index: 9999;
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 font-size: 3rem;
#                 font-weight: bold;
#                 color: white;
#                 animation: fadeout 2.5s ease forwards;
#             }
#             @keyframes fadeout {
#                 0% { opacity: 1; }
#                 100% { opacity: 0; visibility: hidden; }
#             }
#             </style>
#             <div class="loss-animation">💥 Game Over 💥</div>
#         """, unsafe_allow_html=True)
#     st.session_state.anim_played = True


# # Guesses used
# if st.session_state.show_result:
#     st.markdown(f"📦 You used **{st.session_state.guesses} guesses**.")
#     st.markdown("---")
#     if st.button("🔁 Play Again"):
#         reset_game()
#         st.rerun()


import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="🎯 Guess The Number", layout="centered")

# Setup session state
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
if "remaining" not in st.session_state:
    st.session_state.remaining = 10
if "message" not in st.session_state:
    st.session_state.message = ""
if "won" not in st.session_state:
    st.session_state.won = False
if "lost" not in st.session_state:
    st.session_state.lost = False
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "guesses" not in st.session_state:
    st.session_state.guesses = 0
if "anim_played" not in st.session_state:
    st.session_state.anim_played = False
if "input_key" not in st.session_state:
    st.session_state.input_key = str(random.randint(1000, 9999))
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
if "fastest_guess" not in st.session_state:
    st.session_state.fastest_guess = 10

# Reset function
def reset_game():
    st.session_state.num = random.randint(1, 100)
    st.session_state.remaining = 10
    st.session_state.message = ""
    st.session_state.won = False
    st.session_state.lost = False
    st.session_state.show_result = False
    st.session_state.guesses = 0
    st.session_state.anim_played = False
    st.session_state.input_key = str(random.randint(1000, 9999))

# Title
st.title("🎯 Guess the Number Game")
st.markdown("I’m thinking of a number between **1** and **100**.\nYou have **10 guesses**!")

# Input
if not st.session_state.show_result:
    guess = st.text_input(
        "Enter your guess:",
        value="",
        key=st.session_state.input_key,
        placeholder="Your number..."
    )

    if st.button("Submit Guess"):
        if guess.strip().isdigit():
            num = int(guess.strip())
            st.session_state.guesses += 1
            if num == st.session_state.num:
                st.session_state.message = f"✅ You got it! It was {st.session_state.num}."
                st.session_state.won = True
                st.session_state.show_result = True
                st.session_state.games_played += 1
                st.session_state.fastest_guess = min(st.session_state.fastest_guess, st.session_state.guesses)
                st.rerun()

            elif num < st.session_state.num:
                st.session_state.remaining -= 1
                st.session_state.message = "🔼 Too low!"
            else:
                st.session_state.remaining -= 1
                st.session_state.message = "🔽 Too high!"

            if st.session_state.remaining <= 0 and not st.session_state.won:
                st.session_state.message = f"❌ You lost! It was {st.session_state.num}."
                st.session_state.lost = True
                st.session_state.show_result = True
                st.session_state.games_played += 1
                st.rerun()

        else:
            st.warning("Please enter a valid number.")

    st.markdown(f"🧠 Remaining guesses: **{st.session_state.remaining}**")

# Show message
if st.session_state.message:
    if st.session_state.won:
        st.success(st.session_state.message)
    elif st.session_state.lost:
        st.error(st.session_state.message)
    else:
        st.info(st.session_state.message)

# Show result + animation
if st.session_state.show_result and not st.session_state.anim_played:
    if st.session_state.won:
        st.balloons()
        st.markdown("""
        <script>
        new Audio('https://www.myinstants.com/media/sounds/tuturu.mp3').play();
        </script>
        """, unsafe_allow_html=True)
    elif st.session_state.lost:
        st.markdown("""
            <style>
            .loss-animation {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: radial-gradient(circle, #ff0000cc, #000000ee);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 3rem;
                font-weight: bold;
                color: white;
                animation: fadeout 2.5s ease forwards;
            }
            @keyframes fadeout {
                0% { opacity: 1; }
                100% { opacity: 0; visibility: hidden; }
            }
            </style>
            <div class="loss-animation">💥 Game Over 💥</div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <script>
        new Audio('https://www.myinstants.com/media/sounds/wrong-answer-sound-effect.mp3').play();
        </script>
        """, unsafe_allow_html=True)
    st.session_state.anim_played = True

# Stats
if st.session_state.games_played > 0:
    st.markdown("## 📊 Game Stats")
    st.markdown(f"- Games Played: **{st.session_state.games_played}**")
    st.markdown(f"- Fastest Win: **{st.session_state.fastest_guess} guesses**")
    st.markdown(f"- Average Guesses per Game: **{round(st.session_state.guesses / st.session_state.games_played, 2)}**")

# Guesses used
if st.session_state.show_result:
    st.markdown(f"📦 You used **{st.session_state.guesses} guesses**.")
    st.markdown("---")
    if st.button("🔁 Play Again"):
        reset_game()
        st.rerun()

# Funny feedback
if not st.session_state.show_result:
    if st.session_state.guesses >= 7:
        st.caption("You're hotter than a CPU on Chrome. 😅")
    elif st.session_state.guesses > 0:
        st.caption("Try again, love, but softer… 💘")
