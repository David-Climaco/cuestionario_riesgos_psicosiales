import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Autoevaluación CoPsoQ-istas 21 v2", page_icon="📊", layout="centered")

# Lógica de evaluación psicométrica según los baremos de la Versión 2
def evaluar_dimension_v2(puntuacion, verde, amarillo):
    es_escala_directa = verde[0] <= verde[1]
    
    if es_escala_directa:
        if verde[0] <= puntuacion <= verde[1]:
            return "FAVORABLE", "🟢"
        elif amarillo[0] <= puntuacion <= amarillo[1]:
            return "INTERMEDIA", "🟡"
        else:
            return "DESFAVORABLE", "🔴"
    else:
        if verde[1] <= puntuacion <= verde[0]:
            return "FAVORABLE", "🟢"
        elif amarillo[1] <= puntuacion <= amarillo[0]:
            return "INTERMEDIA", "🟡"
        else:
            return "DESFAVORABLE", "🔴"

# Diccionario completo de definiciones y orientaciones preventivas oficiales v2
info_oficial_v2 = {
    "Exigencias cuantitativas": {
        "definicion": "Son las exigencias psicológicas derivadas de la cantidad de trabajo. Se relacionan estrechamente con el ritmo y con el tiempo de trabajo.",
        "origen": "Falta de personal, incorrecta medición de los tiempos, mala planificación o herramientas inadecuadas.",
        "medida": "Adecuar la cantidad de trabajo al tiempo disponible aumentando personal o mejorando procesos."
    },
    "Doble presencia": {
        "definicion": "Son las exigencias sincrónicas y simultáneas del ámbito laboral y del ámbito doméstico-familiar.",
        "origen": "Exigencias cuantitativas altas, prolongación unilateral de la jornada o horarios incompatibles con el cuidado.",
        "medida": "Facilitar la compatibilización entre la vida laboral y familiar y garantizar horarios pactados."
    },
    "Exigencias emocionales": {
        "definicion": "Exigencias para no involucrarnos en la situación emocional derivada de las relaciones interpersonales que implica el trabajo.",
        "origen": "Naturaleza de las tareas en ocupaciones de servicios y alta exposición a situaciones conflictivas de terceros.",
        "medida": "Proporcionar formación en habilidades específicas y aportar tiempos de reposo o rotación."
    },
    "Ritmo de trabajo": {
        "definicion": "Constituye la exigencia psicológica referida específicamente a la intensidad del trabajo en relación con la cantidad y el tiempo.",
        "origen": "Variaciones de la plantilla, presión de tiempos o demandas de producción excesivas.",
        "medida": "Adecuar el ritmo a la capacidad real, evitando aceleraciones por falta de planificación organizativa."
    },
    "Influencia": {
        "definicion": "Margen de autonomía en el día a día del trabajo: sobre las tareas a realizar (el qué), el orden y los métodos a emplear (el cómo).",
        "origen": "Métodos de trabajo centralizados y directivas que limitan la participación básica.",
        "medida": "Potenciar la participación en las decisiones relacionadas con las tareas cotidianas."
    },
    "Posibilidades de desarrollo": {
        "definicion": "Oportunidades que ofrece el trabajo para poner en práctica conocimientos, habilidades y experiencia, así como para adquirir nuevos.",
        "origen": "Trabajo altamente estandarizado, monótono, rutinario y repetitivo.",
        "medida": "Incrementar las oportunidades diseñando contenidos complejos y variados."
    },
    "Sentido del trabajo": {
        "definicion": "Relación del trabajo con otros valores (utilidad, importancia social) y conocimiento de su contribución al servicio final.",
        "origen": "Fraccionamiento extremo de las tareas donde se desconoce el impacto real de lo que se realiza.",
        "medida": "Fomentar la claridad organizativa y dar visibilidad al valor de la labor de cada persona."
    },
    "Claridad de rol": {
        "definicion": "Conocimiento concreto sobre la definición de las tareas a realizar, objetivos, recursos y margen de autonomía.",
        "origen": "Ausencia de definiciones concisas de los puestos de trabajo o fallos de comunicación interna.",
        "medida": "Definir con precisión los puestos de trabajo y las tareas asignadas de antemano."
    },
    "Conflicto de rol": {
        "definicion": "Exigencias contradictorias que se presentan en el trabajo o aquellas que suponen un conflicto de carácter profesional o ético.",
        "origen": "Órdenes contrarias entre sí (ej. rapidez extrema versus calidad minuciosa sin recursos).",
        "medida": "Eliminar instrucciones contradictorias y asegurar procedimientos claros."
    },
    "Previsibilidad": {
        "definicion": "Disponer de la información adecuada, suficiente y a tiempo para realizar correctamente el trabajo y adaptarse a futuros cambios.",
        "origen": "Prácticas de comunicación empresarial deficientes o secretismo institucional.",
        "medida": "Entregar la información con antelación suficiente y proveer formación ante cambios."
    },
    "Inseguridad sobre las condiciones de trabajo": {
        "definicion": "Preocupación por el futuro en relación a cambios no deseados en condiciones fundamentales (puesto, tareas, horario, salario).",
        "origen": "Asignaciones arbitrarias de jornadas o turnos, y modificaciones unilaterales.",
        "medida": "Garantizar la estabilidad en las condiciones pactadas eliminando decisiones imprevistas."
    },
    "Inseguridad sobre el trabajo": {
        "definicion": "Preocupación por el futuro en relación a la estabilidad en el empleo o la pérdida del puesto de ocupación.",
        "origen": "Uso abusivo o sistemático de la contratación temporal sin justificación real.",
        "medida": "Garantizar la seguridad y estabilidad en el empleo reduciendo la temporalidad."
    },
    "Confianza vertical": {
        "definicion": "Seguridad de que la dirección actuará de manera adecuada, competente y justa sin sacar ventaja de su posición de poder.",
        "origen": "Falta de fiabilidad en la información de los mandos o historial de promesas incumplidas.",
        "medida": "Cambiar la cultura de mando hacia directivas transparentes, honestas y fiables."
    },
    "Justicia": {
        "definicion": "Medida en la que las personas trabajadoras son tratadas con equidad en su trabajo (reparto de tareas, resolución de conflictos).",
        "origen": "Arbitrariedad en la toma de decisiones diarias y favoritismos.",
        "medida": "Garantizar el respeto y la justicia organizacional mediante criterios objetivos."
    },
    "Calidad del liderazgo": {
        "definicion": "Valoración de la gestión, planificación y conducción de los equipos humanos que realizan los mandos inmediatos.",
        "origen": "Ausencia de principios claros de gestión o líderes enfocados únicamente en la presión.",
        "medida": "Proporcionar formación y habilidades directivas orientadas al apoyo mutuo."
    }
}

# Mapeos de puntuación (Versión 2)
opciones_frecuencia = {"Siempre": 4, "Muchas veces": 3, "A veces": 2, "Solo alguna vez": 1, "Nunca": 0}
opciones_frecuencia_inversa = {"Siempre": 0, "Muchas veces": 1, "A veces": 2, "Solo alguna vez": 3, "Nunca": 4}
opciones_medida = {"En gran medida": 4, "En buena medida": 3, "En cierta medida": 2, "En alguna medida": 1, "En ningún caso": 0}

# Título e interfaz de usuario
st.title("📋 CUESTIONARIO PARA LA AUTO-EVALUACIÓN DE RIESGOS PSICOSOCIALES EN EL TRABAJO")
st.subheader("CoPsoQ-istas 21 — Versión 2 (Sensibilización)")
st.write("Esta herramienta te ayudará a identificar las condiciones organizativas que impactan en tu salud.")

# Formulario unificado de 30 preguntas
with st.form("copsoq_v2_form"):
    
    st.header("Sección A: Exigencias y Contenidos del Trabajo (Frecuencia)")
    p1 = st.radio("1. ¿La distribución de tareas es irregular y provoca que se te acumule el trabajo?", list(opciones_frecuencia.keys()))
    p2 = st.radio("2. ¿Tienes tiempo suficiente para hacer tu trabajo?", list(opciones_frecuencia_inversa.keys()))
    p3 = st.radio("3. ¿Hay momentos en los que necesitarías estar en la empresa y en casa a la vez?", list(opciones_frecuencia.keys()))
    p4 = st.radio("4. ¿Sientes que tu trabajo te ocupa tanto tiempo que perjudica a tus tareas domésticas y familiares?", list(opciones_frecuencia.keys()))
    p5 = st.radio("5. ¿En el trabajo tienes que ocuparte de los problemas personales de otros?", list(opciones_frecuencia.keys()))
    p6 = st.radio("6. ¿Tienes que trabajar muy rápido?", list(opciones_frecuencia.keys()))
    p7 = st.radio("7. ¿Tienes mucha influencia sobre las decisiones que afectan a tu trabajo?", list(opciones_frecuencia.keys()))
    # CORREGIDO AQUÍ: Usa opciones_medida
    p8 = st.radio("8. ¿Tienes influencia sobre CÓMO realizas tu trabajo?", list(opciones_medida.keys()))

    st.markdown("---")

    st.header("Sección B: Contenidos del Trabajo (Intensidad)")
    p9 = st.radio("9. ¿Tu trabajo, en general, es desgastador emocionalmente?", list(opciones_medida.keys()))
    p10 = st.radio("10. ¿El ritmo de trabajo es alto durante toda la jornada?", list(opciones_medida.keys()))
    p11 = st.radio("11. ¿Tu trabajo permite que aprendas cosas nuevas?", list(opciones_medida.keys()))
    p12 = st.radio("12. ¿Tu trabajo permite que apliques tus habilidades y conocimientos?", list(opciones_medida.keys()))
    p13 = st.radio("13. ¿Tus tareas tienen sentido?", list(opciones_medida.keys()))
    p14 = st.radio("14. ¿Las tareas que haces te parecen importantes?", list(opciones_medida.keys()))

    st.markdown("---")

    st.header("Sección C: Definición de Tareas e Información")
    p15 = st.radio("15. ¿Tu trabajo tiene objetivos claros?", list(opciones_medida.keys()))
    p16 = st.radio("16. ¿Sabes exactamente qué se espera de ti en el trabajo?", list(opciones_medida.keys()))
    p17 = st.radio("17. ¿Se te exigen cosas contradictorias en el trabajo?", list(opciones_medida.keys()))
    p18 = st.radio("18. ¿Tienes que hacer tareas que tú crees que deberían hacerse de otra manera?", list(opciones_medida.keys()))
    p19 = st.radio("19. ¿En tu empresa se te informa con suficiente antelación de decisiones importantes, cambios y proyectos de futuro?", list(opciones_medida.keys()))
    p20 = st.radio("20. ¿Recibes toda la información que necesitas para realizar bien tu trabajo?", list(opciones_medida.keys()))

    st.markdown("---")

    st.header("Sección D: Preocupación por Cambios Futuros")
    st.markdown("**En estos momentos, ¿estás preocupado o preocupada por...**")
    p21 = st.radio("21. ...si te cambian el horario (turno, días de la semana, horas de entrada y salida) contra tu voluntad?", list(opciones_medida.keys()))
    p22 = st.radio("22. ...si te varían el salario (que no te lo actualicen, que te lo bajen, variable, etc.)?", list(opciones_medida.keys()))
    p23 = st.radio("23. ...si te despiden o no te renuevan el contrato?", list(opciones_medida.keys()))
    p24 = st.radio("24. ...lo difícil que sería encontrar otro trabajo en el caso de que te quedaras en paro?", list(opciones_medida.keys()))

    st.markdown("---")

    st.header("Sección E: Reconocimiento, Confianza y Justicia")
    p25 = st.radio("25. ¿Confía la dirección en que los trabajadores hacen un buen trabajo?", list(opciones_medida.keys()))
    p26 = st.radio("26. ¿Te puedes fiar de la información procedente de la dirección?", list(opciones_medida.keys()))
    p27 = st.radio("27. ¿Se solucionan los conflictos de una manera justa?", list(opciones_medida.keys()))
    p28 = st.radio("28. ¿Se distribuyen las tareas de una forma justa?", list(opciones_medida.keys()))
    p29 = st.radio("29. Tu actual jefe inmediato ¿planifica bien el trabajo?", list(opciones_medida.keys()))
    p30 = st.radio("30. Tu actual jefe inmediato ¿resuelve bien los conflictos?", list(opciones_medida.keys()))

    enviado = st.form_submit_button("📊 Analizar Resultados (Versión 2)")

# Procesamiento al enviar
if enviado:
    # Extracción de puntos individuales
    pts = {
        1: opciones_frecuencia[p1],          2: opciones_frecuencia_inversa[p2],
        3: opciones_frecuencia[p3],          4: opciones_frecuencia[p4],
        5: opciones_frecuencia[p5],          6: opciones_frecuencia[p6],
        7: opciones_frecuencia[p7],          8: opciones_medida[p8],
        9: opciones_medida[p9],              10: opciones_medida[p10],
        11: opciones_medida[p11],            12: opciones_medida[p12],
        13: opciones_medida[p13],            14: opciones_medida[p14],
        15: opciones_medida[p15],            16: opciones_medida[p16],
        17: opciones_medida[p17],            18: opciones_medida[p18],
        19: opciones_medida[p19],            20: opciones_medida[p20],
        21: opciones_medida[p21],            22: opciones_medida[p22],
        23: opciones_medida[p23],            24: opciones_medida[p24],
        25: opciones_medida[p25],            26: opciones_medida[p26],
        27: opciones_medida[p27],            28: opciones_medida[p28],
        29: opciones_medida[p29],            30: opciones_medida[p30]
    }

    # Estructura de Dimensiones con las preguntas que se suman asociadas
    dimensiones_v2 = {
        "Exigencias cuantitativas":              {"puntos": pts[1] + pts[2],   "preguntas": [1, 2],   "verde": [0, 1], "amarillo": [2, 3]},
        "Doble presencia":                       {"puntos": pts[3] + pts[4],   "preguntas": [3, 4],   "verde": [0, 3], "amarillo": [4, 5]},
        "Exigencias emocionales":                {"puntos": pts[5] + pts[9],   "preguntas": [5, 9],   "verde": [0, 3], "amarillo": [4, 5]},
        "Ritmo de trabajo":                      {"puntos": pts[6] + pts[10],  "preguntas": [6, 10],  "verde": [0, 1], "amarillo": [2, 3]},
        "Influencia":                            {"puntos": pts[7] + pts[8],   "preguntas": [7, 8],   "verde": [8, 6], "amarillo": [5, 4]},
        "Posibilidades de desarrollo":           {"puntos": pts[11] + pts[12], "preguntas": [11, 12], "verde": [8, 6], "amarillo": [5, 4]},
        "Sentido del trabajo":                   {"puntos": pts[13] + pts[14], "preguntas": [13, 14], "verde": [8, 7], "amarillo": [6, 6]},
        "Claridad de rol":                       {"puntos": pts[15] + pts[16], "preguntas": [15, 16], "verde": [8, 8], "amarillo": [7, 6]},
        "Conflicto de rol":                      {"puntos": pts[17] + pts[18], "preguntas": [17, 18], "verde": [0, 1], "amarillo": [2, 3]},
        "Previsibilidad":                        {"puntos": pts[19] + pts[20], "preguntas": [19, 20], "verde": [8, 7], "amarillo": [6, 5]},
        "Inseguridad sobre las condiciones de trabajo": {"puntos": pts[21] + pts[22], "preguntas": [21, 22], "verde": [0, 1], "amarillo": [2, 3]},
        "Inseguridad sobre el trabajo":          {"puntos": pts[23] + pts[24], "preguntas": [23, 24], "verde": [0, 2], "amarillo": [3, 4]},
        "Confianza vertical":                    {"puntos": pts[25] + pts[26], "preguntas": [25, 26], "verde": [8, 7], "amarillo": [6, 5]},
        "Justicia":                              {"puntos": pts[27] + pts[28], "preguntas": [27, 28], "verde": [8, 7], "amarillo": [6, 5]},
        "Calidad del liderazgo":                 {"puntos": pts[29] + pts[30], "preguntas": [29, 30], "verde": [8, 7], "amarillo": [6, 5]}
    }

    st.success("¡Análisis completado correctamente con transparencia de fórmulas!")
    st.header("📊 Tu Perfil de Exposición Psicosocial")

    for dim, baremo in dimensiones_v2.items():
        nivel, emoji = evaluar_dimension_v2(baremo["puntos"], baremo["verde"], baremo["amarillo"])
        info = info_oficial_v2[dim]
        
        idx_pA, idx_pB = baremo["preguntas"]
        puntos_pA = pts[idx_pA]
        puntos_pB = pts[idx_pB]

        with st.expander(f"{emoji} **{dim}** — Total: {baremo['puntos']} puntos"):
            st.markdown("⚙️ **Fórmula y desglose de puntuación:**")
            st.code(f"Dimensión Total = Pregunta {idx_pA} ({puntos_pA} pts) + Pregunta {idx_pB} ({puntos_pB} pts) = {baremo['puntos']} puntos")
            
            st.markdown(f"**¿Qué mide?**")
            st.write(info["definicion"])
            
            st.markdown(f"**Situación actual:**")
            if nivel == "FAVORABLE":
                st.success(f"🟢 **Favorable para la salud:** Nivel óptimo de exposición.")
            elif nivel == "INTERMEDIA":
                st.warning(f"🟡 **Nivel intermedio:** Exposición moderada, requiere vigilancia.")
            else:
                st.error(f"🔴 **Desfavorable para la salud:** Nivel nocivo que requiere intervención.")
                st.markdown(f"**Posible origen:** {info['origen']}")
                st.markdown(f"**Medida sugerida:** {info['medida']}")
            
            if baremo["verde"][0] <= baremo["verde"][1]:
                lim_text = f"Favorable (Verde): {baremo['verde'][0]}-{baremo['verde'][1]} | Intermedio (Amarillo): {baremo['amarillo'][0]}-{baremo['amarillo'][1]}"
            else:
                lim_text = f"Favorable (Verde): {baremo['verde'][1]}-{baremo['verde'][0]} | Intermedio (Amarillo): {baremo['amarillo'][1]}-{baremo['amarillo'][0]}"
            st.caption(f"Intervalos de referencia: {lim_text}")

    st.markdown("---")
    st.subheader("ACTÚA, DEFIENDE TU SALUD")
    st.write("Impedir que las condiciones psicosociales de trabajo dañen la salud es posible mediante la adopción de medidas preventivas organizacionales en la empresa.")
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray; font-style: italic; font-size: 1.1em;'>By. David Clímaco</p>", unsafe_allow_html=True)
    st.warning("⚠️ **Nota de privacidad:** Este entorno procesa tus respuestas en el navegador de manera local de forma anónima. by DC**")
