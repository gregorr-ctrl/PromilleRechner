
import streamlit as st

st.set_page_config(page_title="Promille-Rechner", layout="centered")

st.title("🍹 Promille-Rechner Deluxe")

st.markdown("""
Berechne deine geschätzte Blutalkoholkonzentration (in ‰) basierend auf Getränken, Menge, Alkoholgehalt, Trinkdauer und Körperdaten.
""")

# Körperdaten
st.sidebar.header("🧍 Körperdaten")
gewicht = st.sidebar.number_input("Körpergewicht (kg)", min_value=30.0, max_value=200.0, value=75.0, step=0.5)
geschlecht = st.sidebar.selectbox("Geschlecht", ["Männlich", "Weiblich"])
r = 0.7 if geschlecht == "Männlich" else 0.6

trinkdauer = st.sidebar.number_input("Dauer des Trinkens (in Stunden)", min_value=0.0, step=0.5, value=1.0)

st.markdown("### 🥂 Getränk auswählen oder individuell eingeben")

getraenke = {
    "Bier": (0.5, 5),
    "Wein": (0.2, 12),
    "Sekt": (0.1, 11),
    "Vodka (Shot)": (0.04, 40),
    "Whiskey-Cola": (0.3, 10),
    "Gin Tonic": (0.3, 12),
    "Caipirinha": (0.3, 13),
    "Pina Colada": (0.3, 15),
    "Vodka Bull": (0.3, 12),
    "Vodka Wellness": (0.3, 10),
    "Long Island Iced Tea": (0.4, 22),
    "Mojito": (0.3, 12),
    "Tequila Sunrise": (0.3, 13),
    "Sex on the Beach": (0.3, 14),
    "Selbst eingeben...": None
}

auswahl = st.selectbox("Getränk wählen", list(getraenke.keys()))

if auswahl != "Selbst eingeben...":
    default_menge_l, default_vol = getraenke[auswahl]
    menge_l = st.number_input("Getränkemenge (in Litern)", value=default_menge_l, min_value=0.01, step=0.05)
    vol_prozent = st.number_input("Alkoholgehalt (% Vol.)", value=default_vol, min_value=0.0, step=0.1)
else:
    menge_l = st.number_input("Getränkemenge (in Litern)", min_value=0.01, step=0.05)
    vol_prozent = st.number_input("Alkoholgehalt (% Vol.)", min_value=0.0, step=0.1)

anzahl = st.number_input("Anzahl der Getränke", min_value=1, step=1, value=1)

if menge_l > 0 and vol_prozent > 0:
    gesamt_menge = menge_l * anzahl
    alkohol_g = gesamt_menge * vol_prozent / 100 * 0.8 * 1000
    promille_roh = alkohol_g / (gewicht * r)

    # Abbau berücksichtigen
    abgebaut = trinkdauer * 0.15
    promille_effektiv = max(0, promille_roh - abgebaut)

    # Ausgabe
    st.markdown("### 📊 Ergebnis")
    st.write(f"**Getrunkene Menge insgesamt:** {gesamt_menge:.2f} l")
    st.write(f"**Reiner Alkohol:** {alkohol_g:.1f} g")
    st.write(f"**Ungefähre Promille (ohne Abbau):** {promille_roh:.2f} ‰")
    st.write(f"**Abgezogen durch {trinkdauer:.1f} h Trinkzeit:** {abgebaut:.2f} ‰")
    st.success(f"**→ Geschätzte aktuelle Promille: {promille_effektiv:.2f} ‰**")

st.markdown("---")
st.caption("Hinweis: Dies ist nur eine Schätzung. Kein medizinischer Wert. Kein Trinken & Fahren!")
