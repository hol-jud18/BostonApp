from flask import Flask, render_template, Blueprint
import folium
from mainapp.services import pins_svc

mapapp= Blueprint( 'maproute', __name__, 
            template_folder='templates', 
            static_folder='static')

@mapapp.route('/home', methods=['GET', 'POST'])
def home():
    mapObj = folium.Map(location=[42.361145, -71.057083], zoom_start=15, 
                        width=700, height=500)
    
    pins_list = pins_svc.pins_list()
    #print(pins_list)

    def avg_rating(person:str):
        rating = 0
        for pin in pins_list:
            score = 0
            if pin[person]:
                score += pin[person]
        rating = score / pin['pkid']
        return rating
    
    print(avg_rating('rating1'))

    if pins_list:
        for pin in pins_list:
            popup_content = f"""
            <b>Title:</b> {pin['title']}<br>
            <b>Address:</b> {pin['address']}<br>
            <b>Rating 1:</b> {pin['rating1']}<br>
            <b>Rating 2:</b> {pin['rating2']}<br>
            <b>Description:</b> {pin['description']}
            """
            folium.Marker(
                [pin['latitude'], pin['longitude']],
                popup=folium.Popup(popup_content, max_width=300),
                tooltip=pin['title'] 
            ).add_to(mapObj)
    
    mapObj.get_root().render()

    header = mapObj.get_root().header.render()
    body = mapObj.get_root().html.render()
    script = mapObj.get_root().script.render()

    return render_template('main.html', header=header, body=body, script=script, pins_list=pins_list)