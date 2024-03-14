import streamlit as st
import base64


def display_pdf(file_name):
    """
    Displays pdf 
    """
    # Read file as bytes:
    with open(file_name, "rb") as f:
        bytes_data = f.read()

    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode("utf-8")

    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
    
    st.markdown(pdf_display, unsafe_allow_html=True)


st.title("Embedded PDF Viewer")
st.markdown("""---""")

display_pdf("orac.pdf")

st.markdown("""---""")
