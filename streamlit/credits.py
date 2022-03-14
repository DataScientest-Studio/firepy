import streamlit as st 
import os
import base64
import streamlit.components.v1 as components
import os                      #+Deployment
import inspect                 #+Deployment

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url, size=50):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" height={size}px/>
        </a>'''
    return html_code


def app():

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    logo_dataScientest = get_img_with_href(os.path.join(currentdir, 'ressources/image4.png'), 'https://datascientest.com/')

    c1,c2 = st.columns([2,3])
    c1.markdown(logo_dataScientest, unsafe_allow_html=True) 
    st.write("")
    c1, c2  = st.columns([0.5, 1])
    with c1:
        st.markdown(f'''<u>FirePy Team</u> :''', unsafe_allow_html=True)  
    with c2:
        logo_linkedin = get_img_with_href(os.path.join(currentdir, 'ressources/linkedin.png'), 'https://www.linkedin.com/in/emmanuelle-cano-4b845940/', 20)
        st.markdown(f'''<a href="https://www.linkedin.com/in/emmanuelle-cano-4b845940/" style="text-decoration: none;color:ff4b4b">Emmanuelle CANO</a> {logo_linkedin}''', unsafe_allow_html=True) 
    
    c1, c2  = st.columns([0.5, 1])
    with c1:
        st.markdown(f'''''', unsafe_allow_html=True)  
    with c2:
        logo_linkedin = get_img_with_href(os.path.join(currentdir, 'ressources/linkedin.png'), 'https://www.linkedin.com/in/francois-faupin/', 20)
        st.markdown(f'''<a href="https://www.linkedin.com/in/francois-faupin/" style="text-decoration: none;color:ff4b4b">François FAUPIN</a> {logo_linkedin}''', unsafe_allow_html=True) 
 
    c1, c2  = st.columns([0.5, 1])
    with c1:
        st.markdown(f'''''', unsafe_allow_html=True)  
    with c2:
        logo_linkedin = get_img_with_href(os.path.join(currentdir, 'ressources/linkedin.png'), 'https://www.linkedin.com/in/gossartt/', 20)
        st.markdown(f'''<a href="https://www.linkedin.com/in/gossartt/" style="text-decoration: none;color:ff4b4b">Thomas GOSSART</a> {logo_linkedin}''', unsafe_allow_html=True) 
        
    c1, c2 = st.columns([0.5, 1])
    c1.markdown(f'''<u>Mentor :</u>''', unsafe_allow_html=True)  
    logo_linkedin = get_img_with_href(os.path.join(currentdir, 'ressources/linkedin.png'), 'https://www.linkedin.com/in/data-jesus/', 20)
    c2.markdown(f'''<a href="https://www.linkedin.com/in/data-jesus/" style="text-decoration: none;color:ff4b4b">Pierre ADEIKALAM</a> {logo_linkedin}''', unsafe_allow_html=True)    

