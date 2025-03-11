from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Menu, Base  # Importamos los modelos que definimos en models.py

# Creamos la base de datos en un archivo SQLite (puedes cambiar esto si usas otra base de datos)
engine = create_engine('sqlite:///restaurants.db')

# Creamos las tablas en la base de datos
Base.metadata.create_all(engine)

# Creamos una sesión para insertar datos
Session = sessionmaker(bind=engine)
session = Session()

# Insertar restaurantes nuevos
restaurant4 = Restaurant(name="La cubana", location="Sevilla", cuisine_type="Mediterráneo")
restaurant5 = Restaurant(name="La conchita", location="Huelva", cuisine_type="Maritima")
restaurant6 = Restaurant(name="Revoltosa", location="Toledo", cuisine_type="Rica rica")

# Insertar menús para los restaurantes
menu4 = Menu(description="Menú del día: Ensalada, Paella", menu_type="daily", price=12.5, restaurant=restaurant4)
menu5 = Menu(description="Menú del día: Sopa de marisco, almejas en salsa", menu_type="daily", price=17.0, restaurant=restaurant5)
menu6 = Menu(description="Menú del día: Arroz con tomate", menu_type="daily", price=20.0, restaurant=restaurant6)

# Añadir restaurantes y menús a la sesión
session.add(restaurant4)
session.add(restaurant5)
session.add(restaurant6)

# Añadir menús a la sesión
session.add(menu4)
session.add(menu5)
session.add(menu6)

# Confirmar los cambios en la base de datos
session.commit()

# Cerrar sesión
session.close()

print("Datos insertados correctamente.")
