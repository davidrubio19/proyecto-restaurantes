from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Restaurant, Base  # Importa tus modelos

# Configura la base de datos
engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

# Eliminar restaurantes por nombre
restaurant_names_to_delete = ['Restaurante A']  # Cambia los nombres según necesites

# Usar el método filter para encontrar los restaurantes que coinciden con los nombres y luego eliminarlos
restaurants_to_delete = session.query(Restaurant).filter(Restaurant.name.in_(restaurant_names_to_delete)).all()

for restaurant in restaurants_to_delete:
    session.delete(restaurant)

# Confirmar los cambios
session.commit()

print(f"{len(restaurants_to_delete)} restaurantes eliminados correctamente.")

# Cerrar sesión
session.close()
