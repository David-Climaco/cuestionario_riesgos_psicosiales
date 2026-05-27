import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Autoevaluación CoPsoQ-istas 21", page_icon="📊", layout="centered")

# Funciones de lógica psicométrica
def evaluar_dimension(puntuacion, favorable, intermedia):
    if favorable[0] <= puntuacion <= favorable[1]:
        return "🟢 FAVORABLE (Nivel de exposición más saludable para la salud)"
    elif intermedia[0] <= puntuacion <= intermedia[1]:
        return "🟡 INTERMEDIA (Nivel de exposición intermedio)"
    else:
        return "🔴 DESFAVORABLE (Nivel de exposición más nocivo para la salud)"

# Mapeo de respuestas estándar a puntos
opciones_estandar = {
    "Siempre / Muy preocupado/a": 4,
    "Muchas veces / Bastante preocupado/a": 3,
    "Algunas veces / Más o menos preocupado/a": 2,
    "Sólo alguna vez / Poco preocupado/a": 1,
    "Nunca / Nada preocupado/a": 0
}

# Mapeo para preguntas inversas (P3, P27, P37)
opciones_inversas = {
    "Siempre": 0,
    "Muchas veces": 1,
    "Algunas veces": 2,
    "Sólo alguna vez": 3,
    "Nunca": 4
}

# Título de la aplicación
st.title("📋 Cuestionario de Auto-Evaluación de Riesgos Psicosociales")
st.write("**Versión corta del CoPsoQ-istas 21.** Instrumento diseñado para identificar y valorar la exposición a factores de riesgo para la salud de naturaleza psicosocial.")
st.info("Por favor, lee detenidamente cada pregunta y elige la opción que mejor describa tu situación actual en tu puesto de trabajo.")

# --- FORMULARIO DE STREAMLIT ---
with st.form("cuestionario_form"):
    
    # -------------------------------------------------------------------------
    st.header("1. Exigencias Psicológicas")
    # -------------------------------------------------------------------------
    p1 = st.radio("1) ¿Tienes que trabajar muy rápido?", list(opciones_estandar.keys()))
    p2 = st.radio("2) ¿La distribución de tareas es irregular y provoca que se te acumule el trabajo?", list(opciones_estandar.keys()))
    p3 = st.radio("3) ¿Tienes tiempo de llevar al día tu trabajo? *(Pregunta Inversa)*", list(opciones_inversas.keys()))
    p4 = st.radio("4) ¿Te cuesta olvidar los problemas del trabajo?", list(opciones_estandar.keys()))
    p5 = st.radio("5) ¿Tu trabajo, en general, es desgastador emocionalmente?", list(opciones_estandar.keys()))
    p6 = st.radio("6) ¿Tu trabajo requiere que escondas tus emociones?", list(opciones_estandar.keys()))

    st.markdown("---")

    # -------------------------------------------------------------------------
    st.header("2. Control sobre el Trabajo")
    # -------------------------------------------------------------------------
    p7 = st.radio("7) ¿Tienes influencia sobre la cantidad de trabajo que se te asigna?", list(opciones_estandar.keys()))
    p8 = st.radio("8) ¿Se tiene en cuenta tu opinión cuando se te asignan tareas?", list(opciones_estandar.keys()))
    p9 = st.radio("9) ¿Tienes influencia sobre el orden en el que realizas las tareas?", list(opciones_estandar.keys()))
    p10 = st.radio("10) ¿Puedes decidir cuándo haces un descanso?", list(opciones_estandar.keys()))
    p11 = st.radio("11) Si tienes algún asunto personal o familiar ¿puedes dejar tu puesto de trabajo al menos una hora sin tener que pedir un permiso especial?", list(opciones_estandar.keys()))
    p12 = st.radio("12) ¿Tu trabajo requiere que tengas iniciativa?", list(opciones_estandar.keys()))
    p13 = st.radio("13) ¿Tu trabajo permite que aprendas cosas nuevas?", list(opciones_estandar.keys()))
    p14 = st.radio("14) ¿Te sientes comprometido con tu profesión?", list(opciones_estandar.keys()))
    p15 = st.radio("15) ¿Tienen sentido tus tareas?", list(opciones_estandar.keys()))
    p16 = st.radio("16) ¿Hablas con entusiasmo de tu empresa a otras personas?", list(opciones_estandar.keys()))

    st.markdown("---")

    # -------------------------------------------------------------------------
    st.header("3. Inseguridad sobre el Futuro")
    st.subheader("En estos momentos, ¿estás preocupado/a...")
    # -------------------------------------------------------------------------
    p17 = st.radio("17) ...por lo difícil que sería encontrar otro trabajo en el caso de que te quedaras en paro?", list(opciones_estandar.keys()))
    p18 = st.radio("18) ...por si te cambian de tareas contra tu voluntad?", list(opciones_estandar.keys()))
    p19 = st.radio("19) ...por si te cambian el horario (turno, días, horas) contra tu voluntad?", list(opciones_estandar.keys()))
    p20 = st.radio("20) ...por si te varían el salario (bajas, actualizaciones, variable) contra tu voluntad?", list(opciones_estandar.keys()))

    st.markdown("---")

    # -------------------------------------------------------------------------
    st.header("4. Apoyo Social y Calidad de Liderazgo")
    # -------------------------------------------------------------------------
    p21 = st.radio("21) ¿Sabes exactamente qué margen de autonomía tienes en tu trabajo?", list(opciones_estandar.keys()))
    p22 = st.radio("22) ¿Sabes exactamente qué tareas son de tu responsabilidad?", list(opciones_estandar.keys()))
    p23 = st.radio("23) ¿En esta empresa se te informa con suficiente antelación de los cambios que pueden afectar tu futuro?", list(opciones_estandar.keys()))
    p24 = st.radio("24) ¿Recibes toda la información que necesitas para realizar bien tu trabajo?", list(opciones_estandar.keys()))
    p25 = st.radio("25) ¿Recibes ayuda y apoyo de tus compañeras o compañeros?", list(opciones_estandar.keys()))
    p26 = st.radio("26) ¿Recibes ayuda y apoyo de tu inmediato o inmediata superior?", list(opciones_estandar.keys()))
    p27 = st.radio("27) ¿Tu puesto de trabajo se encuentra aislado del de tus compañeros/as? *(Pregunta Inversa)*", list(opciones_inversas.keys()))
    p28 = st.radio("28) En el trabajo, ¿sientes que formas parte de un grupo?", list(opciones_estandar.keys()))
    p29 = st.radio("29) ¿Tus actuales jefes inmediatos planifican bien el trabajo?", list(opciones_estandar.keys()))
    p30 = st.radio("30) ¿Tus actuales jefes inmediatos se comunican bien con los trabajadores?", list(opciones_estandar.keys()))

    st.markdown("---")

    # -------------------------------------------------------------------------
    st.header("5. Doble Presencia")
    # -------------------------------------------------------------------------
    opciones_p31 = {
        "Soy el/la principal responsable y hago la mayor parte de tareas domésticas": 4,
        "Hago aproximadamente la mitad de las tareas familiares y domésticas": 3,
        "Hago más o menos una cuarta parte de las tareas familiares y domésticas": 2,
        "Sólo hago tareas muy puntuales": 1,
        "No hago ninguna o casi ninguna de estas tareas": 0
    }
    p31 = st.radio("31) ¿Qué parte del trabajo familiar y doméstico haces tú?", list(opciones_p31.keys()))
    p32 = st.radio("32) Si faltas algún día de casa, ¿las tareas domésticas que realizas se quedan sin hacer?", list(opciones_estandar.keys()))
    p33 = st.radio("33) Cuando estás en la empresa ¿piensas en las tareas domésticas y familiares?", list(opciones_estandar.keys()))
    p34 = st.radio("34) ¿Hay momentos en los que necesitarías estar en la empresa y en casa a la vez?", list(opciones_estandar.keys()))

    st.markdown("---")

    # -------------------------------------------------------------------------
    st.header("6. Estima")
    # -------------------------------------------------------------------------
    p35 = st.radio("35) Mis superiores me dan el reconocimiento que merezco", list(opciones_estandar.keys()))
    p36 = st.radio("36) En las situaciones difíciles en el trabajo recibo el apoyo necesario", list(opciones_estandar.keys()))
    p37 = st.radio("37) En mi trabajo me tratan injustamente *(Pregunta Inversa)*", list(opciones_inversas.keys()))
    p38 = st.radio("38) Si pienso en todo el trabajo y esfuerzo realizado, el reconocimiento me parece adecuado", list(opciones_estandar.keys()))

    # Botón de envío del formulario
    enviado = st.form_submit_button("📊 Calcular mis Resultados")

# --- PROCESAMIENTO DE RESULTADOS ---
if enviado:
    # Cálculo de puntuaciones sumando los valores numéricos correspondientes
    tot_exigencias = opciones_estandar[p1] + opciones_estandar[p2] + opciones_inversas[p3] + opciones_estandar[p4] + opciones_estandar[p5] + opciones_estandar[p6]
    tot_control = opciones_estandar[p7] + opciones_estandar[p8] + opciones_estandar[p9] + opciones_estandar[p10] + opciones_estandar[p11] + opciones_estandar[p12] + opciones_estandar[p13] + opciones_estandar[p14] + opciones_estandar[p15] + opciones_estandar[p16]
    tot_inseguridad = opciones_estandar[p17] + opciones_estandar[p18] + opciones_estandar[p19] + opciones_estandar[p20]
    tot_apoyo = opciones_estandar[p21] + opciones_estandar[p22] + opciones_estandar[p23] + opciones_estandar[p24] + opciones_estandar[p25] + opciones_estandar[p26] + opciones_inversas[p27] + opciones_estandar[p28] + opciones_estandar[p29] + opciones_estandar[p30]
    tot_doble = opciones_p31[p31] + opciones_estandar[p32] + opciones_estandar[p33] + opciones_estandar[p34]
    tot_estima = opciones_estandar[p35] + opciones_estandar[p36] + opciones_inversas[p37] + opciones_estandar[p38]

    # Estructura con baremos oficiales
    dimensiones = {
        "1. Exigencias Psicológicas":            {"puntos": tot_exigencias,   "fav": [0, 7],   "int": [8, 11]},
        "2. Control sobre el Trabajo":           {"puntos": tot_control,      "fav": [26, 40], "int": [19, 25]},
        "3. Inseguridad sobre el Futuro":        {"puntos": tot_inseguridad,  "fav": [0, 4],   "int": [5, 9]},
        "4. Apoyo Social y Calidad de Liderazgo": {"puntos": tot_apoyo,        "fav": [32, 40], "int": [25, 31]},
        "5. Doble Presencia":                    {"puntos": tot_doble,        "fav": [0, 2],   "int": [3, 6]},
        "6. Estima":                             {"puntos": tot_estima,       "fav": [13, 16], "int": [10, 12]}
    }

    # Despliegue visual de los resultados
    st.success("¡Cuestionario procesado con éxito! Aquí tienes tu reporte:")
    st.header("📊 Tu Diagnóstico Psicosocial")

    for dim, info in dimensiones.items():
        resultado = evaluar_dimension(info["puntos"], info["fav"], info["int"])
        
        # Crear cajas visuales (expander) para cada sección
        with st.expander(f"**{dim}** — Puntuación: {info['puntos']} pts"):
            st.write(f"**Situación:** {resultado}")
            st.caption(f"Rangos oficiales de referencia -> Favorable: {info['fav'][0]}-{info['fav'][1]} | Intermedia: {info['int'][0]}-{info['int'][1]} | Desfavorable: fuera de estos rangos.")

    st.warning("⚠️ **Nota de privacidad:** Este entorno web procesa los datos localmente en tu sesión. Al recargar la página, tus respuestas se borrarán y no quedarán guardadas en ninguna base de datos pública.")
