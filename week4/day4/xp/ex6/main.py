def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

show_magicians(magician_names)

make_great(magician_names)

print("\nAfter make_great():")
show_magicians(magician_names)
