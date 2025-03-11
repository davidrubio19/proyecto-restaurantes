from flask import Flask, render_template, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Restaurant, Menu  # Asegúrate de que tus modelos están importados correctamente

app = Flask(__name__)

# Configura tu base de datos (Asegúrate de que esta configuración sea correcta)
engine = create_engine('sqlite:///restaurants.db')  # O la URL de tu base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Ruta para la página principal (donde mostramos el formulario de búsqueda)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la búsqueda de restaurantes
@app.route('/search', methods=['GET'])
def search():
    location = request.args.get('location')
    cuisine_type = request.args.get('cuisine_type')

    query = session.query(Restaurant).join(Menu)

    if location:
        query = query.filter(Restaurant.location == location)
    if cuisine_type:
        query = query.filter(Restaurant.cuisine_type == cuisine_type)

    restaurants = query.distinct().all()

    # Construir la respuesta JSON para el frontend
    result = []
    for restaurant in restaurants:
        restaurant_data = {
            "restaurant_name": restaurant.name,
            "location": restaurant.location,
            "cuisine_type": restaurant.cuisine_type,
            "menus": [{"description": menu.description, "menu_type": menu.menu_type, "price": menu.price} for menu in restaurant.menus]
        }
        result.append(restaurant_data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
