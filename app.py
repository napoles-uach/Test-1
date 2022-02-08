import streamlit as st
import os
import runpy


class stwidget:
  def __init__(self,kind,sidebar,name):
    self.kind = kind
    self.sidebar = sidebar
    self.name = name
  def get_code(self):
    if self.sidebar==True:
      code = f"st.sidebar.{self.kind}('{self.name}')"
    else:
      code = f"st.{self.kind}('{self.name}')"


    return code

st.set_page_config(page_title="Streamlit App", page_icon="🤖",layout="wide")
widgets = ['title','header','subheader','image','text','button','checkbox','slider','text_input','number_input','camera_input']


#if selection equal a number, then show that number
#code_list=[]
#two columns usint st.beta_columns
col1,col2 = st.columns([6,2])
select_widget=col2.selectbox('select',widgets)
if 'code_list' not in st.session_state:
    st.session_state.code_list = []
with col2.form('form'):
    is_sidebar = st.checkbox('sidebar')
    label = st.text_input('label or text')
    wid = stwidget(select_widget,is_sidebar,label)   
    subm= st.form_submit_button('submit')
    if subm:        
        st.session_state.code_list.append(wid.get_code())

code_lines = st.multiselect(
     'What are your favorite colors',
     st.session_state.code_list,
     st.session_state.code_list)
#write code_list to a file with each line as a code snippet
with open('code.py','w') as f:
    f.write('import streamlit as st\n')
    for code in #st.session_state.code_list:
        f.write(code+'\n')      

with col1:
    runpy.run_path('code.py')




#st.write('You selected:', options)
#code_string = '\n'.join(st.session_state.code_list)
#with st.expander("See your code"):
#    st.code(code_string, language='python')