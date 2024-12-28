import streamlit as st
import requests

responses = requests.get("https://randomuser.me/api/")

data = responses.json()

thumbnail = data["results"][0]["picture"]["medium"]

last_name = data["results"][0]["name"]["last"]
first_name = data["results"][0]["name"]["first"]

gender = data["results"][0]["gender"].title()

email = data["results"][0]["email"]

timezone = data["results"][0]["location"]["timezone"]["offset"]
city = data["results"][0]["location"]["city"]
state = data["results"][0]["location"]["state"]
country = data["results"][0]["location"]["country"]
postcode = data["results"][0]["location"]["postcode"]

col1, col2 = st.columns(2)

with col1:
    st.image(thumbnail, caption=f"{first_name} {last_name}", width=200)

    st.write(
        f"""
Name: {first_name} {last_name}\n
Gender: {gender}\n
Email: {email}\n
Lives in: {city}, {state}, {country}\n
Postcode: {postcode}\n
Timezone: GMT {timezone}
"""
)
