from textwrap import dedent

#dictionary /object holding menu items
items = {
  'Wings' : 0, 
  'Cookies' : 0,
  'Spring Rolls' : 0,
  'Salmon' : 0,
  'Steak' : 0,
  'Meat Tornado' : 0,
  'A Literal Garden' : 0,
  'Ice Cream' : 0,
  'Cake' : 0,
  'Pie' : 0,
  'Coffee' : 0,
  'Tea' : 0,
  'Unicorn Tears' : 0
}



def welcome():
  intro = '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
  '''
  print(dedent(intro))



def show_menu():
  menu = """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

  """
  print(menu)



def take_order():
  while True:
    order = input(dedent('''
      ***********************************
      ** What would you like to order? **
      ***********************************
      '''))

    if order == 'quit':
      break

    if order in items:
      items[order] += 1
      pre_amount = items[order]
      print(
        f'** {pre_amount} order of {order} have been added to your meal **'
      )



def main():
  welcome()
  show_menu()
  take_order()



if __name__ == "__main__":
  main()
