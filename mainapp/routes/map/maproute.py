from flask import Flask, render_template, Blueprint
import folium
from mainapp.services import pins_svc

mapapp= Blueprint( 'maproute', __name__, 
            template_folder='templates', 
            static_folder='static')

@mapapp.route('/home', methods=['GET', 'POST'])
def home():
    mapObj = folium.Map(location=[42.361145, -71.057083], zoom_start=13, 
                        width=700, height=500)
    
    pins_list = pins_svc.pins_list()
    favorite_pins_list = pins_svc.pins_list_favorite()
    #print(pins_list)

    if pins_list:
        largest_pkid = pins_svc.get_last_pkid()
        print(largest_pkid)

        def avg_rating(person:str):
            # rating = 0
            score = 0
            for pin in pins_list:
                if pin[person]:
                    score += pin[person]
            rating = score / largest_pkid[0]['pkid']
            return rating

    if pins_list:
        for pin in pins_list:
            favorite_huh = 'Oh Yea' if pin['favorited'] == 'true' else 'ew'
            popup_content = f"""
            <b>Title:</b> {pin['title']}<br>
            <b>Address:</b> {pin['address']}<br>
            <b>Mayah's Rating:</b> {pin['rating1']}<br>
            <b>Jude's Rating:</b> {pin['rating2']}<br>
            <b>Description:</b> {pin['description']}<br>
            <b>Favorited?:</b> {favorite_huh}<br>
            """
            folium.Marker(
                [pin['latitude'], pin['longitude']],
                popup=folium.Popup(popup_content, max_width=300),
                tooltip=pin['title'] 
            ).add_to(mapObj)
    mayah_avg_rating = avg_rating('rating1') if pins_list else 0
    jude_avg_rating = avg_rating('rating2') if pins_list else 0
    
    mapObj.get_root().render()

    header = mapObj.get_root().header.render()
    body = mapObj.get_root().html.render()
    script = mapObj.get_root().script.render()

    return render_template('main.html', header=header, body=body, 
                           script=script, pins_list=pins_list, favorite_pins_list=favorite_pins_list, 
                           mayah_avg_rating=mayah_avg_rating, jude_avg_rating=jude_avg_rating)