import git
import streamlit as st

st.title('Hi! This is Fukong~ 😎💜')

pic = st.toggle('See my picture')
if pic:
    st.image('./image/profile.png', width=300)

st.subheader('i', divider='rainbow')

bar = st.select_slider(
    'what do you want to know about me?',
    options=['About', 'Education', 'Work Experience', 'Hobbies and Interests', 'Interesting Projects'])

if bar == 'About':
    st.subheader('About')
    about= '''
    I am working on my **startup**.
    '''
    st.markdown(about)

if bar == 'Education':
    st.subheader('Education')
    education= '''
    - **University of Washington**  2023 - 2025
    
    Master of Science in Technology Innovation 💜 @ Golbal Innovation Exchange
    '''
    st.markdown(education)
    
if bar == 'Work Experience':
    st.subheader('Work Experience')
    work= '''
    - **SCUT HCI Design Lab**   2020 - 2023
    
    Researcher and Program Manager
    '''
    st.markdown(work)

if bar == 'Hobbies and Interests':
    st.subheader('Hobbies and Interests')
    hobbies= '''
    💪🏀🏈🎱🎿🥏🎮🔮🎲🕹️🀄♠️
    '''
    st.markdown(hobbies)

proj= '''
**Project 1** : GAC Metaverse Mobility Competition

**Project 2** : TAURUS Service&UX Redesign
'''

if bar == 'Interesting Projects':
    st.subheader('Interesting Projects')
    st.markdown(proj)