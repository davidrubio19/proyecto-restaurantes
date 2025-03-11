from sqlalchemy import Column, Integer, String, Float, ForeignKey  # Asegúrate de importar ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    cuisine_type = Column(String, nullable=False)

    # Relación con la tabla Menu (un restaurante tiene muchos menús)
    menus = relationship('Menu', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant(name={self.name}, location={self.location}, cuisine_type={self.cuisine_type})>'

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    menu_type = Column(String, nullable=False)  # Ejemplo: 'daily', 'a la carta', etc.
    price = Column(Float, nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)  # Aquí usamos ForeignKey

    def __repr__(self):
        return f'<Menu(description={self.description}, menu_type={self.menu_type}, price={self.price})>'
