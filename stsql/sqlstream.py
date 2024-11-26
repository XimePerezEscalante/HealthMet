import mysql.connector
import streamlit as st
import pandas as pd
import time
import datetime
import numpy as np

from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
from time import gmtime, strftime

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

connection = mysql.connector.connect(host = 'localhost', user='root', password = '', database = 'esp32_data')
cursor = connection.cursor()

def checarUsuario(user):
    cursor.execute("Select COUNT(*) as Total from datos_usuario WHERE nombre_usuario = '" + nombre_usuario + "';")
    datos = cursor.fetchall()
    df = pd.DataFrame(datos,columns=cursor.column_names)
    if df.iloc[0]['Total'] > 0:
        return True
    else:
        return False


registro_tab, inicio_tab, aboutus_tab = st.tabs(["Registrar cuenta","Iniciar sesión","Sobre nosotras"])

with registro_tab:
    #Título
    original_title = '<p style="font-family:Courier; font-size: 100px; align:center">HealthMet</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    with st.container(border = True):
        nombre_usuario = st.text_input("Nombre de usuario", "", key = "username1")
        if len(nombre_usuario) == 0:
            st.error("Introduce un nombre de usuario válido")
        pwd = st.text_input("Contraseña (Mínimo 8 caracteres)", "", type = "password")
        if len(pwd) < 8:
            st.error("Contraseña inválida: introduce mínimo 8 caracteres")
        nombre_real = st.text_input("Nombre", "")
        if len(nombre_real) == 0:
            st.error("Introduce tu nombre")
        apellido = st.text_input("Apellido (sólo uno)", "")
        if len(apellido) == 0:
            st.error("Introduce tu apellido")
        edad = st.number_input("Edad (15+)",15,100, value = None)
        if edad == None:
            st.error("Introduce tu edad")
        dispositivo = st.text_input("Escoge un nombre para tu casco", "HealthMet")
        if nombre_usuario and pwd and nombre_real and apellido and edad:
            if st.button("Registrar"):
                with st.spinner("Registrando..."):
                    time.sleep(1.5)
                    
                    if checarUsuario(nombre_usuario) == True:
                        st.error("Nombre de usuario no disponible")
                    else:
                        cursor.execute("INSERT INTO datos_usuario (nombre_usuario, contrasena, nombre, apellido, edad, dispositivo) VALUES('" + nombre_usuario + "','" + pwd + "','" + nombre_real + "','" + apellido + "'," + str(edad) + ",'" + dispositivo + "');")
                        connection.commit()
                        st.toast("Usuario registrado con éxito")
                        st.session_state['realname1'] = nombre_real

                #st.write("INSERT INTO datos_usuario (nombre_usuario, contrasena, nombre, apellido, edad, dispositivo) VALUES('" + nombre_usuario + "','" + pwd + "','" + nombre_real + "','" + apellido + "'," + str(edad) + ",'" + dispositivo + "');")
                #cursor.execute("INSERT INTO datos_usuario (edad) VALUES (" + str(edad) + ");")
                
                #cursor.execute("INSERT INTO datos_usuario (edad) VALUES (" + str(edad) + ");")

with inicio_tab:
    #Título
    original_title = '<p style="font-family:Courier; font-size: 100px; align:center">HealthMet</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    with st.container(border = True):
        nombre_usuario = st.text_input("Nombre de usuario", "", key = "username2")
        if len(nombre_usuario) == 0:
            st.error("Introduce un nombre de usuario válido")
        pwd = st.text_input("Contraseña (Mínimo 8 caracteres)", "", type = "password", key = "pwd2")
        if len(pwd) < 8:
            st.error("Contraseña inválida: introduce mínimo 8 caracteres")
        if nombre_usuario and pwd:
            if st.button("Iniciar sesión"):
                with st.spinner("Iniciando sesión..."):
                    time.sleep(1.5)
                    if checarUsuario(nombre_usuario) == True:
                        cursor.execute("SELECT contrasena FROM `datos_usuario` WHERE nombre_usuario = '" + nombre_usuario + "';")
                        datos = cursor.fetchall()
                        df = pd.DataFrame(datos,columns=cursor.column_names)
                        if df.iloc[0]['contrasena'] == pwd:
                            st.toast("Sesión iniciada con éxito", icon = "✅")
                        else:
                            st.error("Contraseña incorrecta")
        


with aboutus_tab:
    #Título
    original_title = '<p style="font-family:Courier; font-size: 100px; align:center">HealthMet</p>'
    st.markdown(original_title, unsafe_allow_html=True)


#Link al logo
image = "https://i.ibb.co/fCYXhLV/Helath-Met-Logo-Oficial.png"
#Poner logo
st.logo(image,link=None, icon_image=None)

#Registrar nuevo usuario
with st.sidebar:
    selected = option_menu("HealthMet", ["Inicio", 'Ajustes'], 
        icons=['house', 'gear'], menu_icon="bi bi-bicycle", default_index=1)
    



#if st.button("Say hello"):
#    st.write("Why hello there")
#else:
#    st.write("Goodbye")




#st.header("Hoy")

#today = datetime.datetime.now()
#d = st.date_input("",today)
#st.write(today)

#Toggle button
on = st.toggle("Activate feature")
#if on:
#    st.write("Feature activated!")



# AYUDA STREAMLIT
#st.write(dir(st))
# BALLOONS
#st.balloons()
#st.snow()



#connection = mysql.connector.connect(host = 'localhost', user='root', password = '', database = 'esp32_data')

#print('connected')

#cursor = connection.cursor()
#cursor.execute("Select * from datos_potenciometro")
#data = cursor.fetchall()




#st.title("Streamlit MySQL Connection")

#df = pd.DataFrame(data,columns=cursor.column_names)
#st.dataframe(df)


#cont = 0
#while (cont < 10):
#    time.sleep(5)
#    wind = df.iloc[cont]['valor']
#    st.write(wind)
#    cont = cont + 1
    

#col1, col2, col3 = st.columns(3)
#col1.metric("Temperature","11 °C", "1.2 °C")
#col2.metric("Wind", str(wind) + " km/h", "-8%")
#col3.metric("Humidity", "86%", "4%")
