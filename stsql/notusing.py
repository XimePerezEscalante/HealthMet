#"SELECT COUNT(*) FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:" +  str(todaycomplete.minute) + "%'"  '2024-11-24___:24%' "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';"
if (todaycomplete.minute - 1) < 10:
    cursor.execute("SELECT COUNT(*) as Total FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:0" +  str(todaycomplete.minute - 1) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
    datos = cursor.fetchall()
    df = pd.DataFrame(datos,columns=cursor.column_names)
    #st.dataframe(df)
else:
    cursor.execute("SELECT COUNT(*) as Total FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:" +  str(todaycomplete.minute - 1) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
    datos = cursor.fetchall()
    df = pd.DataFrame(datos,columns=cursor.column_names)
    #st.dataframe(df)


if df.iloc[0]['Total'] > 1:
        totalDatos = df.iloc[0]['Total']
        st.write(totalDatos)
        cont = 0
        while cont < totalDatos:
            if (todaycomplete.minute - 1) < 10:
                cursor.execute("SELECT humidity, temperature FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:0" +  str(todaycomplete.minute - 1) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
                datos = cursor.fetchall()
                df = pd.DataFrame(datos,columns=cursor.column_names)
                #st.dataframe(df)
                promedioHumedad = promedioHumedad + df.iloc[cont]['humidity']
                promedioTemperatura = promedioTemperatura + df.iloc[cont]['temperature']
            else:
                cursor.execute("SELECT humidity, temperature FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:" +  str(todaycomplete.minute - 1) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
                datos = cursor.fetchall()
                df = pd.DataFrame(datos,columns=cursor.column_names)
                #st.dataframe(df)
                promedioHumedad = promedioHumedad + df.iloc[cont]['humidity']
                promedioTemperatura = promedioTemperatura + df.iloc[cont]['temperature']
            cont = cont + 1

    promedioHumedad0 = promedioHumedad / totalDatos
    promedioTemperatura0 = promedioTemperatura / totalDatos

    st.title("Normal: " + str(promedioHumedad) + "   " + str(promedioTemperatura))
    st.title("0: " + str(promedioHumedad0) + "   " + str(promedioTemperatura0))

    time.sleep(30)

    if todaycomplete.minute < 10:
        cursor.execute("SELECT COUNT(*) as Total FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:0" +  str(todaycomplete.minute) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
        datos = cursor.fetchall()
        df = pd.DataFrame(datos,columns=cursor.column_names)
        #st.dataframe(df)
    else:
        cursor.execute("SELECT COUNT(*) as Total FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:" +  str(todaycomplete.minute) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
        datos = cursor.fetchall()
        df = pd.DataFrame(datos,columns=cursor.column_names)
        #st.dataframe(df)


    if df.iloc[0]['Total'] > 1:
        totalDatos = df.iloc[0]['Total']
        cont = 0
        st.write(totalDatos)
        while cont < totalDatos:
            if (todaycomplete.minute) < 10:
                cursor.execute("SELECT humidity, temperature FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:0" +  str(todaycomplete.minute) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
                datos = cursor.fetchall()
                df = pd.DataFrame(datos,columns=cursor.column_names)
                #st.dataframe(df)
                promedioHumedad = promedioHumedad + df.iloc[cont]['humidity']
                promedioTemperatura = promedioTemperatura + df.iloc[cont]['temperature']
            else:
                cursor.execute("SELECT humidity, temperature FROM sensores WHERE timestamp LIKE '" +  str(fecha) + "___:" +  str(todaycomplete.minute) + "%'" + "AND id_dispositivo = '" + st.session_state['deviceid1'] + "';")
                datos = cursor.fetchall()
                df = pd.DataFrame(datos,columns=cursor.column_names)
                #st.dataframe(df)
                promedioHumedad = promedioHumedad + df.iloc[cont]['humidity']
                promedioTemperatura = promedioTemperatura + df.iloc[cont]['temperature']
            cont = cont + 1

    promedioHumedad1 = promedioHumedad / totalDatos 
    promedioTemperatura1 = promedioTemperatura / totalDatos 

    st.title("Normal: " + str(promedioHumedad) + "   " + str(promedioTemperatura))

    st.title("1: " + str(promedioHumedad1) + "   " + str(promedioTemperatura1))

    diferenciaHumedad =  promedioHumedad1 - promedioHumedad0
    diferenciaTemperatura = promedioTemperatura1 - promedioTemperatura0

    colvacia1, coltemp, colhum, colvacia = st.columns(4)
    coltemp.metric("Temperatura", str(promedioTemperatura1) + " °C", str(diferenciaTemperatura) + " °C")
    colhum.metric("Humedad", str(promedioHumedad1) + "%", str(diferenciaHumedad) + "%")
