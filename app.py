import streamlit as st
from streamlit_webrtc import webrtc_streamer



x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.write('Hello, *World!* :sunglasses:')
webrtc_streamer(key="example")