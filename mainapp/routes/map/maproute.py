from flask import Flask, render_template, Blueprint
import folium

mapapp= Blueprint( 'maproute', __name__, 
            template_folder='templates', 
            static_folder='static')

@mapapp.route('/home', methods=['GET', 'POST'])
def home():
    mapObj = folium.Map(location=[42.361145, -71.057083], zoom_start=15, 
                        width=800, height=500)
    
    mapObj.get_root().render()

    header = mapObj.get_root().header.render()
    body = mapObj.get_root().html.render()
    script = mapObj.get_root().script.render()

    return render_template('main.html', header=header, body=body, script=script)