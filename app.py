import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from streamlit_folium import st_folium

st.title("📍 Phone Number Location Tracker")

number = st.text_input("+6285793451564")
key = st.secrets["OPENCAGE_API_KEY"]

if number:
    try:
        check_number = phonenumbers.parse(number)
        location = geocoder.description_for_number(check_number, "en")
        provider = carrier.name_for_number(check_number, "en")
        st.write("📍 Location:", location)
        st.write("📡 Provider:", provider)

        geocoder_oc = OpenCageGeocode(key)
        query = str(location)
        results = geocoder_oc.geocode(query)

        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']

            m = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(m)
            st_folium(m, width=700)
        else:
            st.warning("Lokasi tidak ditemukan.")
    except:
        st.error("Nomor tidak valid.")
