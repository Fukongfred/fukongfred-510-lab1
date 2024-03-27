import streamlit as st

st.title('Hi! This is Fukong~ : sunglasse : 💜')

pic = st.toggle('See my picture')
if pic:
    st.image("C:\Users\86138\Desktop\xhs\Group 1576.png", caption=None, width=2, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.subheader('', divider='rainbow')

bar = st.select_slider(
    'Select a color of the rainbow',
    options=['About', 'Education', 'Work Experience', 'Hobbies and Interests', 'Interesting Projects'])

if bar == 'About Me':
    st.subheader('About')
    about= '''
    I am working on my **startup**,.
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
    - 💪🏀🏈🎱🎿🥏🎮🔮🎲🕹️🀄♠️
    '''
    st.markdown(hobbies)

if bar == 'Interesting Projects':
    st.subheader('Interesting Projects')
    proj= '''
    - **Project 1** : GAC Metaverse Mobility Competition
    - **Project 2** : TAURUS Service&UX Redesign
    '''
    st.markdown(proj)