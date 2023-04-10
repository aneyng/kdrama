class KoreanDrama:
    def __init__(self, name, rating, releaseYear, genre):
        self.name = name
        self.rating = float(rating)
        self.releaseYear = int(releaseYear)
        self.genre = int(genre)

    def __repr__(self): # KoreanDrama -> String
        return str(self.name, self.rating, self.releaseYear, self.genre)