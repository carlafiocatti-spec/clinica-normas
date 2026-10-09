import streamlit as st

# Configuración de la página (Interfaz limpia, moderna y corporativa neutral)
st.set_page_config(
    page_title="Gestión de Normativas",
    page_icon="▪️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS con estética corporativa ultra-limpia y sobria
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .header-container {
        padding: 15px 0px 5px 0px;
        border-bottom: 1px solid #E5E7EB;
        margin-bottom: 25px;
    }
    .header-title {
        color: #111827;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 500;
        font-size: 18px;
        letter-spacing: -0.3px;
    }
    .header-subtitle {
        color: #6B7280;
        font-size: 13px;
        margin-top: 2px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: 500;
        font-size: 14px;
        border-radius: 4px;
        padding: 0.5rem;
        border: none;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #1E40AF;
        color: white;
    }
    .result-box {
        background-color: #F9FAFB;
        padding: 22px;
        border-radius: 6px;
        border: 1px solid #E5E7EB;
        margin-top: 20px;
        font-size: 14px;
        color: #374151;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado minimalista institucional
st.markdown("""
    <div class="header-container">
        <div class="header-title">Módulo de Validación y Normativas</div>
        <div class="header-subtitle">Consulta de directivas, coberturas y reglas de facturación</div>
    </div>
""", unsafe_allow_html=True)

# Base de datos estructurada con toda la información exacta de tus fuentes
normas_db = {
    "Acindar": {
        "vencimiento_orden": "30 Días",
        "sistema_validacion": "Presentación de bono autorizado o validación vía AMR.",
        "coseguro": "⛔ **NO COBRAR COSEGURO AL PACIENTE.** La obra social lo debita directamente de su cuenta.",
        "practicas": {
            "Consultas Médicas": "🟡 **Validación AMR / Bono:** Validación mediante sistema AMR o presentación de bono impreso de Acindar.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟡 / 🟢 **Viene Autorizado de origen:** RMN y TAC (incluye contraste).\n\n🟡 **Requiere Validación AMR / Bono:** Ecografías, Eco Doppler y Mamografías digitales.",
            "Ecografías y Eco Doppler": "🟡 **Requiere Validación AMR / Bono:** Ecografías y Eco Doppler con validación previa.",
            "Odontología": "🟡 **Requiere autorización previa / AMR:** Tomografías Cone Beam (Código 34) con autorización previa.",
            "Ginecología / IVE": "🟡 **Requiere autorización previa:** Consulta Inicial, Presentación 1 y Presentación 3.",
            "Oftalmología / Otras": "🟡 **Verificar sistema AMR:** Consultar cobertura específica según plan."
        }
    },
    "Amr": {
        "vencimiento_orden": "30 Días",
        "sistema_validacion": "Validación online a través del sistema AMR.",
        "coseguro": "Consultar según cartilla y plan vigente.",
        "practicas": {
            "Consultas Médicas": "🟢 **Validación AMR:** Ingresar al sistema para verificar habilitación de consulta de forma directa.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟡 **Verificar cobertura:** Consultar normas específicas por código en sistema AMR.",
            "Ecografías y Eco Doppler": "🟢 **Sin inconvenientes:** Ecografías ambulatorias habituales con validación de credencial.",
            "Odontología": "🟡 **Autorización:** Sujeto a auditoría y validación previa en portal.",
            "Ginecología / IVE": "🟡 **Auditoría:** Consultar normas vigentes en sistema.",
            "Oftalmología / Otras": "🟢 **Prácticas habituales:** Validadas por sistema."
        }
    },
    "Amur": {
        "vencimiento_orden": "30 Días",
        "sistema_validacion": "Portal web Amur / Token de validación.",
        "coseguro": "Aplica según plan del afiliado.",
        "practicas": {
            "Consultas Médicas": "🟢 **Token / Credencial:** Presentación de credencial digital o física con token activo generado en el momento.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟡 **Auditoría:** Verificar requerimiento de autorización web según alta o baja complejidad.",
            "Ecografías y Eco Doppler": "🟢 **Sin autorización previa:** Ecografías convencionales.",
            "Odontología": "🟡 **Autorización previa:** Sujeto a plan.",
            "Ginecología / IVE": "🟡 **Normativa específica:** Verificar por portal.",
            "Oftalmología / Otras": "🟢 **Atención habitual:** Según cartilla."
        }
    },
    "Luis Pasteur": {
        "vencimiento_orden": "60 Días",
        "sistema_validacion": "Copia de credencial o autorización previa (Asociación de Clínicas / Docsys).",
        "coseguro": "Consultar sistema Docsys.",
        "practicas": {
            "Consultas Médicas": "🟢 **Sin autorización previa:** Imprimir orden de consulta directamente desde Docsys y adjuntar fotocopia de la credencial del paciente.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟢 **Sin autorización previa** (fotocopia de credencial) para RMN menor/mayor convencional y TAC convencional.\n\n🟡 **Requiere autorización previa:** Resonancia con Espectroscopia y Tomógrafo Multislice.",
            "Ecografías y Eco Doppler": "🟢 **Sin autorización previa** con fotocopia de credencial y orden de Docsys.",
            "Odontología": "🟢 **Sin autorización previa** (fotocopia de credencial): Ortopantomografía, Seriada y Bitewing.",
            "Ginecología / IVE": "🟡 **Requiere autorización previa:** Colocación y Extracción de DIU.\n\nℹ️ **Modalidad Especial:** IVE por presupuesto.",
            "Oftalmología / Otras": "🟢 **Sin autorización previa:** Campo Visual y Paquimetría.\n\n🟡 **Requiere autorización previa:** OCT."
        }
    },
    "Osdop": {
        "vencimiento_orden": "30 días",
        "sistema_validacion": "Autorización de obra social o sistema F5.",
        "coseguro": "Aplica según plan (verificar en sistema).",
        "practicas": {
            "Consultas Médicas": "🟡 **Bono de Consulta:** Presentar bono oficial de Osdop debidamente habilitado y firmado.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟡 **Autorización Obligatoria:** RMN y TAC requieren autorización previa de Osdop o validación por F5.",
            "Ecografías y Eco Doppler": "🟡 **Autorización previa:** Indispensable auditoría de la obra social.",
            "Odontología": "🟡 **Autorización previa:** Requiere bono y sello correspondiente.",
            "Ginecología / IVE": "🟡 **Requiere autorización:** Auditoría previa.",
            "Oftalmología / Otras": "🟡 **Validación F5 obligatoria.**"
        }
    },
    "Prevencion": {
        "vencimiento_orden": "60 días + 30 de autorización",
        "sistema_validacion": "Gored (Elegibilidad obligatoria)",
        "coseguro": "Según cartilla del plan.",
        "practicas": {
            "Consultas Médicas": "🟢 **Elegibilidad Gored:** Verificar estado del afiliado en el sistema previo a la atención.",
            "Diagnóstico por Imágenes (RMN / TAC)": "🟢 **Sin autorización previa:** RMN comunes, TAC convencional y multislice en planes habilitados.\n\n🟡 **Con autorización:** Angioresonancia y Colangiografía.",
            "Ecografías y Eco Doppler": "🟢 **Sin autorización previa** en todos los planes habilitados (A2 a A6 e IÓN).",
            "Odontología": "🟡 **Requiere autorización:** Tomografía Cone Beam en todos los planes.",
            "Ginecología / IVE": "🟢 **Elegibilidad Gored** previa.",
            "Oftalmología / Otras": "🟢 **Sin autorización previa** para prácticas de baja complejidad."
        }
    }
}

# Selectores en pantalla distribuidos en dos columnas limpias
col1, col2 = st.columns(2)

with col1:
    obra_social_seleccionada = st.selectbox(
        "Obra Social / Prepaga",
        options=list(normas_db.keys())
    )

with col2:
    practicas_disponibles = list(normas_db[obra_social_seleccionada]["practicas"].keys())
    practica_seleccionada = st.selectbox(
        "Área / Práctica / Estudio",
        options=practicas_disponibles
    )

st.markdown("<br>", unsafe_allow_html=True)

# Botón central de consulta
if st.button("Consultar requisitos"):
    datos_os = normas_db[obra_social_seleccionada]
    resultado_practica = datos_os["practicas"][practica_seleccionada]
    
    # Tarjeta de resultado con diseño corporativo sobrio y limpio
    st.markdown(f"""
        <div class="result-box">
            <strong style="color: #1E3A8A; font-size: 15px;">Resultado para: {obra_social_seleccionada} — {practica_seleccionada}</strong>
            <hr style="border: 0; border-top: 1px solid #E5E7EB; margin: 12px 0;">
            <div style="margin-bottom: 15px; line-height: 1.6;">
                {resultado_practica}
            </div>
            <div style="background-color: #F3F4F6; padding: 10px; border-radius: 4px; font-size: 13px; color: #4B5563;">
                <b>📌 Reglas generales de la prepaga:</b><br>
                • Vencimiento de orden: {datos_os['vencimiento_orden']}<br>
                • Sistema de validación: {datos_os['sistema_validacion']}<br>
                • Coseguro: {datos_os['coseguro']}
            </div>
        </div>
    """, unsafe_allow_html=True)