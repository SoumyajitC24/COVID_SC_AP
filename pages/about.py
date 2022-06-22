"""This create About me page"""

# Import necessary module
import streamlit as st

def app():
    st.balloons()
    st.title('Contact Us')
    st.markdown('''#### Name:
    Soumyajit Chakraborty''')
    st.markdown('''#### Email:
    soumyajitc24.170@gmail.com''')
    st.markdown('''#### Name:
    Anmol S. Patel''')
    st.markdown('''#### Email:
    anmolpatel2112000@gmail.com''')
    #with st.echo():
    st.markdown('''<p>
                    <h4>Soumyajit's GitHub:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                        <p style="padding:10px">
                            <a href = "https://github.com/SoumyajitC24/COVID_19_Detection" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New' , stroke='currentColor';"> 
                                        You can find this project here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)
    st.markdown('''<p>
                <h4>Anmol's GitHub:</h4>
                <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                    <p style="padding:10px">
                        <a href = "https://github.com/patelanmol" 
                                    target="_blank"
                                    style="text-decoration:None; 
                                        color:black;
                                        padding:1rem;
                                        font-family:'Courier New' , stroke='currentColor';"> 
                                    You can check out my Github page here!
                        </a>
                    </p>
                </div>
                </p>''', unsafe_allow_html=True)
    st.markdown('''<p>
                    <h4>Soumyajit's LinkedIn:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                        <p style="padding:10px">
                            <a href = https://www.linkedin.com/in/soumyajit-chakraborty-64a9b022/" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New' , stroke='currentColor';"> 
                                        Check out my LinkedIn profile here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)
    st.markdown('''<p>
                    <h4>Anmol's LinkedIn:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px , stroke='currentColor';">
                        <p style="padding:10px">
                            <a href = https://www.linkedin.com/in/anmolp/" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New' , stroke='currentColor';"> 
                                        Check out my LinkedIn profile here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)                    