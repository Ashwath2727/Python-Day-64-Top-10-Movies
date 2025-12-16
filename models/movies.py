from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id: Mapped[int] =mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String)
    img_url: Mapped[str] = mapped_column(String)


    def __repr__(self):
        return (f"Movie({self.title}, {self.year}, {self.description}, {self.rating}, {self.ranking},"
                f" {self.review}, {self.img_url})")