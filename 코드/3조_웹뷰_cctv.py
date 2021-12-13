import streamlit as st
import base64


# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

file1= open("영상2.gif", "rb")
contents = file1.read()
data_url = base64.b64encode(contents).decode("utf-8")
file1.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="700" height="700" alt="cat gif">',
    unsafe_allow_html=True,
)

# st.markdown('---')

# file2= open("영상2.gif", "rb")
# contents = file2.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file2.close()

# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" width="700" height="700" alt="cat gif">',
#     unsafe_allow_html=True,
# )