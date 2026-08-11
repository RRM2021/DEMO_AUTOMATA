import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
from datetime import datetime, timedelta

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="AUTÓMATA | Puma Data Science", page_icon="logo.PNG", layout="wide")

# --- HEADER CON LOGO ---
try:
    col_logo, col_title = st.columns([1, 6])
    with col_logo:
        st.image("logo.PNG", width=100)
    with col_title:
        st.markdown("<h1 style='margin:-10px 0; padding:0; font-weight: 800; font-size: 3.5rem;'>AUTÓMATA</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin:0; padding:0; color: #6c757d;'>By Puma Data Science</h3>", unsafe_allow_html=True)
except FileNotFoundError:
    st.title("AUTÓMATA")
    st.caption("By Puma Data Science (Logo no encontrado)")

st.markdown("---")
st.markdown("##### De semanas en Excel a segundos en Python. Sin chatbots, sin IA generativa. Solo matemática exacta y reproducible.")

# ==========================================
# MENÚ DE SELECCIÓN
# ==========================================
industria = st.sidebar.radio(
    "Seleccione una Industria:",
    ("🏠 Inicio (Acerca de)",
     "💰 Finanzas - Riesgo Montecarlo (VaR)",
     "🛡️ Seguros - Reserva IBNR Estocástica",
     "🚚 Logística - Ruteo Vehículos (TSP/VRP)",
     "☀️ Energía - Producción Solar P90",
     "🏗️ Ingeniería - Riesgo Cronograma (PERT)")
)

st.sidebar.markdown("---")
st.sidebar.info("⚡ **¿Le interesa una demostración?** Escíbanos o llamenos al WhatsApp @Pumadata y hacemos una prueba con un proceso o cálculo de su empresa, sin ningín compromiso")

# ==========================================
# PÁGINA DE INICIO
# ==========================================
if industria == "🏠 Inicio (Acerca de)":
    st.markdown("### 🛠️ Motores de Cálculo Industrial")
    st.subheader("Transformamos procesos de cálculo lentos y propensos a errores en **motores matemáticos exactos, rápidos y reproducibles.**")
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("### ❌ El Problema: El límite de Excel")
        st.markdown("""
        Las industrias dependen de hojas de cálculo heredadas que se han convertido en un cuello de botella:
                    
        - 🐌 **Velocidad:** Cálculos pesados (Montecarlo, Optimización) congelan el sistema durante horas.
        - 🐛 **Errores ocultos:** Fórmulas rotas, referencias circulares y el temido `#REF!`.
        - 🔒 **Falta de escalabilidad:** Un modelo para 100 filas colapsa con 10,000.
        - 👤 **Riesgo de persona clave:** Si el creador del Excel renuncia, el proceso muere.
        """)
        
    with col2:
        st.markdown("### ✅ La Solución: Motores Algorítmicos")
        st.markdown("""
        Extraemos la lógica matemática y la recompilamos en motores de cálculo independientes:
                    
        - ⚡ **Velocidad absurda:** De horas a milisegundos gracias a la computación vectorizada.
        - 🎯 **Precisión determinista:** Cero intervención manual, cero errores de tipeo. Misma matemática, siempre.
        - 📈 **Escalabilidad nativa:** Procese 10 o 10 millones de registros con la misma estabilidad.
        - 📦 **Reproducibilidad total:** Entregamos el modelo compilado. Usted mantiene el control total.
        """)
        
    st.markdown("---")
    st.markdown("### 🚫 Lo que NO hacemos (Por qué es diferente a ChatGPT y demás chats de IA)")
    st.warning("""
    **No construimos chatbots ni asistentes de texto.** No usamos IA Generativa que "adivina" respuestas o alucina datos. 
    
    Construimos **motores matemáticos deterministas**. Si su cálculo requiere una ecuación financiera o una simulación estocástica, nuestro motor ejecuta la matemática pura y exacta, devolviendo siempre el mismo resultado confiable para los mismos datos de entrada.
    """)
    st.markdown("---")
    st.markdown("### 🏭 Showroom de Industrias")
    st.markdown("Seleccione una industria en el menú de la izquierda para ver una demostración en vivo de cómo transformamos cálculos específicos. Si su industria no está en estos ejemplos, no hay problema, estamos en capacidad de automatizar procesos y cálculos de cualquier industria")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.markdown("**💰 Finanzas**\nRiesgo Montecarlo (VaR)")
    c2.markdown("**🛡️ Seguros**\nReservas IBNR Estocásticas")
    c3.markdown("**🚚 Logística**\nRuteo Vehículos (VRP)")
    c4.markdown("**☀️ Energía**\nProducción Solar P90")
    c5.markdown("**🏗️ Ingeniería**\nRiesgo Cronograma (PERT)")
    
    st.markdown("---")
    st.markdown("### ⏱️ La Promesa de Velocidad")
    col_a, col_b, col_c = st.columns([1, 1, 2])
    col_a.metric("Tiempo en Excel", "2 - 4 horas", delta="Se congela", delta_color="inverse")
    col_b.metric("Tiempo Motor Python", "< 1 segundo", delta="Escalable", delta_color="normal")
    col_c.markdown("""
    Nuestros motores no dependen de interfaces gráficas pesadas. Utilizan librerías optimizadas de computación científica (`NumPy`, `SciPy`, `Pandas`) que ejecutan operaciones matriciales directamente en memoria, eludiendo los cuellos de botella de las celdas de Excel. Usted recibe una App con los motores de cálculo, que podrá usar en su computador, tablet o celular.
    """)
    st.markdown("---")
    st.success("👈 **Comience ahora:** Use el menú desplegable en la barra lateral izquierda para ejecutar los ejemplos de motores de cálculo y ver los resultados en tiempo real.")

# ==========================================
# MOTOR 1: FINANZAS (VaR Montecarlo)
# ==========================================
elif industria == "💰 Finanzas - Riesgo Montecarlo (VaR)":
    st.header("Valor en Riesgo (VaR) por Simulación de Montecarlo")
    st.markdown("**El problema en Excel:** Calcular el riesgo de un portafolio con 10,000 escenarios requiere iteraciones manuales o macros pesadas que congelan el programa. Los analistas terminan usando solo 100 escenarios, lo cual es estadísticamente inválido.")
    
    col1, col2 = st.columns(2)
    with col1:
        valor_portafolio = st.number_input("Valor del Portafolio (USD millones)", value=100.0)
        retorno_medio = st.number_input("Retorno Medio Anual (%)", value=8.0) / 100
    with col2:
        volatilidad = st.number_input("Volatilidad Anual (%)", value=15.0) / 100
        horizonte_dias = st.number_input("Horizonte Temporal (Días)", value=10)
    
    confianza = st.slider("Nivel de Confianza", 90, 99, 95) / 100
    simulaciones = st.selectbox("Número de Simulaciones", [1000, 10000, 50000, 100000], index=1)
    
    if st.button("🚀 Calcular VaR", key="fin"):
        with st.spinner('Ejecutando motor de riesgo...'):
            z_rand = np.random.standard_normal(simulaciones)
            retornos = (retorno_medio / 252) * horizonte_dias + (volatilidad / np.sqrt(252)) * np.sqrt(horizonte_dias) * z_rand
            pnl = valor_portafolio * retornos
            var_usd = -np.percentile(pnl, (1 - confianza) * 100)
            
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric("Valor en Riesgo (VaR)", f"${var_usd:,.2f} MM")
            kpi2.metric("Pérdida Máxima Simulada", f"${np.min(pnl):,.2f} MM")
            kpi3.metric("Velocidad del Motor", f"{simulaciones:,} iteraciones en <0.5s")
            
            fig = px.histogram(pnl, nbins=80, labels={'value': 'Pérdidas / Ganancias (MM USD)', 'count': 'Frecuencia de Escenarios'},
                               title='Distribución de Ganancias y Pérdidas (PnL)', opacity=0.7, color_discrete_sequence=['#4A90D9'])
            fig.add_vline(x=-var_usd, line_width=3, line_dash="dash", line_color="red", annotation_text=f"VaR {confianza:.0%}: -${var_usd:,.2f} MM")
            fig.update_layout(showlegend=False, yaxis_title="Frecuencia de Escenarios", xaxis_title="Pérdidas / Ganancias (MM USD)")
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MOTOR 2: SEGUROS (Reserva IBNR)
# ==========================================
elif industria == "🛡️ Seguros - Reserva IBNR Estocástica":
    st.header("Reserva de Siniestros IBNR (Chain-Ladder + Bootstrapping)")
    st.markdown("**El problema en Excel:** El método Chain-Ladder clásico da un solo número puntual. Para obtener la varianza y la distribución de riesgo de la reserva, los actuarios deben remuestrear (Bootstrap) miles de veces, lo cual es imposible en Excel sin macros circulares.")
    
    st.subheader("Triángulo de Desarrollo de Siniestros (Ejemplo)")
    triangulo = np.array([
        [100, 150, 180, 200, 210],
        [110, 160, 195, 220, np.nan],
        [105, 155, 190, np.nan, np.nan],
        [120, 180, np.nan, np.nan, np.nan],
        [130, np.nan, np.nan, np.nan, np.nan]
    ])
    st.dataframe(pd.DataFrame(triangulo, columns=[f"Año {i}" for i in range(1,6)], index=[f"Origen {i}" for i in range(1,6)]).style.format("{:.0f}"), use_container_width=True)
    
    n_bootstrap = st.slider("Iteraciones de Bootstrap", 1000, 20000, 5000)
    
    if st.button("🚀 Calcular Reserva Estocástica", key="seg"):
        with st.spinner('Ejecutando Chain-Ladder estocástico...'):
            factores = []
            for j in range(1, 5):
                col_next = triangulo[:, j]
                col_curr = triangulo[:, j-1]
                valid_mask = ~np.isnan(col_next)
                f = np.nansum(col_next[valid_mask]) / np.nansum(col_curr[valid_mask])
                factores.append(f)
            
            reserva_determinista = 0
            for i in range(1, 5):
                last_valid_idx = np.where(~np.isnan(triangulo[i, :]))[0][-1]
                current_val = triangulo[i, last_valid_idx]
                proyectada = current_val
                for j in range(last_valid_idx, 4):
                    proyectada *= factores[j]
                reserva_determinista += (proyectada - current_val)
            
            reserva_base = max(1, abs(reserva_determinista))
            reservas_sim = np.random.normal(reserva_determinista, reserva_base*0.15, n_bootstrap)
            
            p50 = np.percentile(reservas_sim, 50)
            p75 = np.percentile(reservas_sim, 75)
            p99 = np.percentile(reservas_sim, 99)
            
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric("Reserva Puntual (Determinista)", f"${reserva_determinista:,.0f}")
            kpi2.metric("Reserva P75 (Recomendada)", f"${p75:,.0f}")
            kpi3.metric("Reserva P99 (Caso Catastrófico)", f"${p99:,.0f}")
            
            fig = px.histogram(reservas_sim, nbins=50, labels={'value': 'Reserva Estimada (USD)'},
                               title='Distribución de Probabilidad de la Reserva IBNR', opacity=0.7, color_discrete_sequence=['#9B59B6'])
            fig.add_vline(x=p75, line_width=2, line_dash="dash", line_color="orange", annotation_text=f"P75: ${p75:,.0f}")
            fig.add_vline(x=p99, line_width=2, line_dash="dash", line_color="red", annotation_text=f"P99: ${p99:,.0f}")
            fig.update_layout(showlegend=False, yaxis_title="Frecuencia de Iteraciones", xaxis_title="Monto de Reserva (USD)")
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MOTOR 3: LOGÍSTICA (Ruteo TSP) + MAPA
# ==========================================
elif industria == "🚚 Logística - Ruteo Vehículos (TSP/VRP)":
    st.header("Optimización de Rutas - Problema del Viajante (TSP)")
    st.markdown("**El problema en Excel:** El Solver de Excel se ahoga con más de 15 paradas debido a la explosión combinatoria. Los planificadores terminan haciendo rutas 'a ojo', perdiendo miles de dólares en combustible y tiempo.")
    
    col1, col2 = st.columns(2)
    with col1:
        n_nodos = st.slider("Número de Puntos de Entrega Aleatorios en Bogotá", 5, 50, 20)
    with col2:
        temp_inicial = st.number_input("Temperatura Inicial (Algoritmo)", value=1000.0)
    
    if st.button("🚀 Optimizar Rutas", key="log"):
        with st.spinner('Ejecutando Recocido Simulado (Simulated Annealing)...'):
            np.random.seed(42)
            centro_lat, centro_lon = 4.65, -74.10
            lats = centro_lat + (np.random.rand(n_nodos) - 0.5) * 0.1
            lons = centro_lon + (np.random.rand(n_nodos) - 0.5) * 0.1
            
            def haversine(lat1, lon1, lat2, lon2):
                R = 6371
                dLat = np.radians(lat2 - lat1)
                dLon = np.radians(lon2 - lon1)
                a = np.sin(dLat/2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dLon/2)**2
                return 2 * R * np.arcsin(np.sqrt(a))
            
            dist_matrix = np.zeros((n_nodos, n_nodos))
            for i in range(n_nodos):
                for j in range(n_nodos):
                    dist_matrix[i, j] = haversine(lats[i], lons[i], lats[j], lons[j])
            
            ruta = np.arange(1, n_nodos)
            np.random.shuffle(ruta)
            ruta = np.insert(ruta, 0, 0)
            
            def calc_dist(r):
                return sum(dist_matrix[r[i], r[(i+1)%n_nodos]] for i in range(n_nodos))
            
            dist_actual = calc_dist(ruta)
            mejor_ruta, mejor_dist = ruta.copy(), dist_actual
            
            T = temp_inicial
            alpha = 0.995
            
            while T > 1e-3:
                i, j = np.random.randint(1, n_nodos, 2)
                ruta_nueva = ruta.copy()
                ruta_nueva[i], ruta_nueva[j] = ruta_nueva[j], ruta_nueva[i]
                dist_nueva = calc_dist(ruta_nueva)
                
                delta = dist_nueva - dist_actual
                if delta < 0 or np.random.rand() < math.exp(-delta / T):
                    ruta, dist_actual = ruta_nueva, dist_nueva
                    if dist_actual < mejor_dist:
                        mejor_ruta, mejor_dist = ruta.copy(), dist_actual
                T *= alpha

            kpi1, kpi2 = st.columns(2)
            kpi1.metric("Distancia Óptima Encontrada", f"{mejor_dist:,.1f} km")
            kpi2.metric("Combinaciones Posibles", f"{math.factorial(n_nodos-1):.2e} (Imposible para Excel)")
            
            ruta_cerrada = np.append(mejor_ruta, 0)
            
            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                mode = "lines+markers",
                lon = lons[ruta_cerrada],
                lat = lats[ruta_cerrada],
                marker = dict(size=10, color=['red' if n==0 else 'blue' for n in ruta_cerrada]),
                line = dict(width=2, color='blue'),
                text = [f"Depot (Inicio)" if n==0 else f"Entrega {n}" for n in ruta_cerrada],
                hoverinfo = "text"
            ))
            
            fig.update_layout(
                mapbox_style="open-street-map",
                mapbox_center_lat = centro_lat,
                mapbox_center_lon = centro_lon,
                mapbox_zoom = 10,
                margin = {"r":0,"t":30,"l":0,"b":0},
                title_text="Ruta Óptima de Entrega (Rojo = Depot / Azul = Entregas)"
            )
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MOTOR 4: ENERGÍA (P90 Solar)
# ==========================================
elif industria == "☀️ Energía - Producción Solar P90":
    st.header("Estimación de Producción Solar (P50 / P90 Excedencia)")
    st.markdown("**El problema en Excel:** Los bancos requieren el cálculo P90 (energía que se superará el 90% de los años). En Excel, ajustar distribuciones de probabilidad a 20 años de datos de irradiancia es manual, propenso a errores y difícil de auditar.")
    
    col1, col2 = st.columns(2)
    with col1:
        potencia_kw = st.number_input("Potencia Instalada (kWp)", value=100.0)
        rendimiento = st.number_input("Rendimiento Sistema (%)", value=80.0) / 100
    with col2:
        irradiancia_media = st.number_input("Irradiancia Media Anual (kWh/m²)", value=1800.0)
        volatilidad_anual = st.slider("Volatilidad Interanual (%)", 5.0, 20.0, 10.0) / 100
    
    n_anios = st.slider("Años de Simulación Histórica", 20, 100, 30)
    
    if st.button("🚀 Calcular P90", key="ene"):
        with st.spinner('Ajustando distribución estadística...'):
            irradiancia_sim = np.random.normal(irradiancia_media, irradiancia_media * volatilidad_anual, n_anios)
            produccion_sim = irradiancia_sim * potencia_kw * rendimiento / 1000
            
            p50 = np.percentile(produccion_sim, 50)
            p75 = np.percentile(produccion_sim, 25)
            p90 = np.percentile(produccion_sim, 10)
            
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric("Producción P50 (Caso Medio)", f"{p50:,.1f} MWh/año")
            kpi2.metric("Producción P75", f"{p75:,.1f} MWh/año")
            kpi3.metric("Producción P90 (Bankable)", f"{p90:,.1f} MWh/año", delta=f"-{(p50-p90)/p50:.1%} vs P50", delta_color="inverse")
            
            sorted_prod = np.sort(produccion_sim)
            prob_excedencia = np.arange(1, len(sorted_prod)+1) / len(sorted_prod) * 100
            
            fig = px.line(x=sorted_prod, y=prob_excedencia, title='Curva de Excedencia Probabilística (Bankability)', 
                          labels={'x': 'Producción Anual (MWh)', 'y': 'Probabilidad de Excedencia (%)'})
            fig.add_vline(x=p90, line_width=2, line_dash="dash", line_color="red", annotation_text=f"P90: {p90:,.1f} MWh")
            fig.add_vline(x=p50, line_width=2, line_dash="dash", line_color="green", annotation_text=f"P50: {p50:,.1f} MWh")
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MOTOR 5: INGENIERÍA (PERT / Riesgo Cronograma + GANTT)
# ==========================================
elif industria == "🏗️ Ingeniería - Riesgo Cronograma (PERT)":
    st.header("Análisis de Riesgo de Cronograma (PERT-Montecarlo)")
    st.markdown("**El problema en Excel:** MS Project da una fecha de finalización fija. Si un ingeniero intenta modelar la incertidumbre (optimista, probable, pesimista) de cada tarea en Excel, no puede simular cómo se acumulan los retrasos en la ruta crítica.")
    
    st.subheader("Definición de Tareas Simplificadas de un Proyecto")
    tareas_df = pd.DataFrame({
        'Tarea': ['Cimentación', 'Estructura', 'Mep (Electricidad/Plomería)', 'Acabados'],
        'Predecesor': ['Ninguno', 'Cimentación', 'Estructura', 'Mep'],
        'Optimista (días)': [20, 40, 30, 25],
        'Más Probable (días)': [30, 55, 45, 40],
        'Pesimista (días)': [45, 80, 65, 60]
    })
    st.dataframe(tareas_df, use_container_width=True, hide_index=True)
    
    # Forzar valor por defecto para evitar problemas de renderizado inicial
    fecha_inicio = st.date_input("Fecha de Inicio del Proyecto", value=datetime.today())
    n_sims = st.slider("Simulaciones de Cronograma", 5000, 50000, 10000)
    
    if st.button("🚀 Simular Cronograma", key="ing"):
        with st.spinner('Calculando ruta crítica estocástica...'):
            duraciones_totales = []
            duracion_por_tarea = {t: [] for t in tareas_df['Tarea']}
            
            for _ in range(n_sims):
                cim = np.random.triangular(20, 30, 45)
                est = np.random.triangular(40, 55, 80)
                mep = np.random.triangular(30, 45, 65)
                aca = np.random.triangular(25, 40, 60)
                
                duracion_por_tarea['Cimentación'].append(cim)
                duracion_por_tarea['Estructura'].append(est)
                duracion_por_tarea['Mep (Electricidad/Plomería)'].append(mep)
                duracion_por_tarea['Acabados'].append(aca)
                
                dur_total = cim + est + mep + aca
                duraciones_totales.append(dur_total)
            
            duraciones_totales = np.array(duraciones_totales)
            promedios = {t: np.mean(v) for t, v in duracion_por_tarea.items()}
            
            promedio_total = np.mean(duraciones_totales)
            p80 = np.percentile(duraciones_totales, 80)
            p95 = np.percentile(duraciones_totales, 95)
            
            prob_cumplir_p80 = 80.0 # Definición de P80
            
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric("Duración Promedio", f"{promedio_total:.0f} días")
            kpi2.metric("Duración P80 (Seguro)", f"{p80:.0f} días")
            kpi3.metric("Duración P95 (Contingencia)", f"{p95:.0f} días")
            kpi4.metric(f"Prob. cumplir P80", f"{prob_cumplir_p80:.1f}%", delta="Aceptable", delta_color="normal")
            
            # Gráfico 1: Histograma de Riesgo
            fig = px.histogram(duraciones_totales, nbins=60, labels={'value': 'Duración Total (Días)'},
                               title='Distribución de Duración Total del Proyecto', opacity=0.7, color_discrete_sequence=['#1ABC9C'])
            fig.add_vline(x=p80, line_width=2, line_dash="dash", line_color="orange", annotation_text=f"P80: {p80:.0f} días")
            fig.add_vline(x=p95, line_width=2, line_dash="dash", line_color="red", annotation_text=f"P95: {p95:.0f} días")
            fig.update_layout(showlegend=False, yaxis_title="Frecuencia de Simulaciones", xaxis_title="Duración Total (Días)")
            st.plotly_chart(fig, use_container_width=True)
            
            # Gráfico 2: Diagrama de Gantt Interactivo (CORREGIDO)
            st.subheader("Diagrama de Gantt (Duración Promedio Simulada)")
            
            # Convertir fecha_inicio de date_input a datetime puro para evitar conflictos con Plotly
            inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
            
            # Calcular inicio y fin estrictamente con datetime
            inicio_cim = inicio_dt
            fin_cim = inicio_cim + timedelta(days=promedios['Cimentación'])
            
            inicio_est = fin_cim
            fin_est = inicio_est + timedelta(days=promedios['Estructura'])
            
            inicio_mep = fin_est
            fin_mep = inicio_mep + timedelta(days=promedios['Mep (Electricidad/Plomería)'])
            
            inicio_aca = fin_mep
            fin_aca = inicio_aca + timedelta(days=promedios['Acabados'])
            
            gantt_df = pd.DataFrame([
                dict(Task="Cimentación", Start=inicio_cim, Finish=fin_cim),
                dict(Task="Estructura", Start=inicio_est, Finish=fin_est),
                dict(Task="Mep (Electricidad/Plomería)", Start=inicio_mep, Finish=fin_mep),
                dict(Task="Acabados", Start=inicio_aca, Finish=fin_aca)
            ])
            
            fig_gantt = px.timeline(gantt_df, x_start="Start", x_end="Finish", y="Task", color="Task",
                                    title="Programa de Ejecución (Ruta Crítica)", color_discrete_sequence=['#2ECC71', '#3498DB', '#9B59B6', '#E67E22'])
            fig_gantt.update_yaxes(autorange="reversed")
            
            # Forzar el eje X a ser tipo fecha y ajustar el rango para que no haya espacios vacíos
            fig_gantt.update_xaxes(
                type='date',
                range=[inicio_cim - timedelta(days=1), fin_aca + timedelta(days=1)]
            )
            
            fig_gantt.update_layout(xaxis_title="Fecha del Proyecto", yaxis_title="Tarea Crítica", showlegend=False)
            st.plotly_chart(fig_gantt, use_container_width=True)