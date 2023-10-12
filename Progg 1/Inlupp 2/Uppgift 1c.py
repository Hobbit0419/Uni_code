def delete(the_list, number):
      new_list = []        # Den nya listan sätts tom, initialt.
      for n in the_list:   # För varje element n i listan...
          if n == number:  # Om elementet är lika med number...
              continue     # Hoppa över resterande satser i detta loopvarv.
          new_list.append(n) # Annars, lägg till elementet i den nya listan
      the_list = new_list
      print('listan i delete', the_list) 

# Anropande kod
my_list = [2, 5, 1, 7, 12, 0, -5]
print('my_list före delete', my_list)
delete(my_list, 7)
print('my_list efter delete', my_list) # har 7 tagits bort från listan?

#the_list i funktionen är en lokal variabel i funktionen och ändrar inte den globala varabeln my_list