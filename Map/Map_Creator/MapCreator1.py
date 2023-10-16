def create_square_file(size, filename):
    with open(filename, 'w') as file:
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    file.write('1')
                else:
                    file.write('0')
                if j < size - 1:
                    file.write(',')
            file.write('\n')

# Taille du carré (par exemple, 3)
square_size = 16

# Nom du fichier à créer (par exemple, "carre_3.txt")
output_filename = f"carre_{square_size}.txt"

# Créer le fichier
create_square_file(square_size, output_filename)