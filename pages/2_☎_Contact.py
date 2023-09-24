import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.title("📞Contact")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name ) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

#load assests
lottie_coding = load_lottieurl("https://lottie.host/489acdbb-844c-4fa7-ae42-bcc317cd9630/5KceOv6YLa.json")
    

st.write("----")
st.header("Get In Touch With Me!")
st.write("##")

contact_form="""

       <form action="https://formsubmit.co/sharma.info25@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="Message" placeholder="Type your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """

left_column, right_column = st.columns(2)
with left_column:
 st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
 st.empty()
 st_lottie(lottie_coding, height=400, key="Contact_us")

    
   