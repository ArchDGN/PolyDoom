class Map:
    def __init__(self):
        self.map = []

    def load_map(self, path):

        # Chargement de la map depuis un fichier texte

        with open(path, "r") as file:
            for line in file:
                if line[0] == '#':
                    continue
                else:
                    square_row = line.strip().split(',')
                    square_row = [int(num) for num in square_row]
                    self.map.extend(square_row)

        return self.map

    def get_map_info(self, path):

        # Retourne la taille de la map
        data = []
        with open(path, "r") as file:
            data = ((file.readline()[1:].split(',')))
            data[-1] = data[-1][:-1]
            data = [int(num) for num in data]
            return data

        return 0