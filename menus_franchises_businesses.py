# Classes - Menus, Franchises and Businesses

# The restaurant has been growing well.  Use python to keep things organised.

# KEY CONCEPTS
# Classes, Methods
# List filtering and aggregation
# Representing objects as strings

# CREATE MENUS
# There are four different menus: brunch, early-bird, dinner, and kids.

class Menu:
  def __init__ (self, name, items, start_time, end_time):
    self.name = name 
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#  string representation method for menu name and availability.
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " - " + str(self.end_time)


# Brunch is served from 11am to 4pm. 
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
# print(brunch_menu.name)
# Output
# Brunch
print(brunch_menu)
# Output
# Brunch menu available from 1100 - 1600

# Early-bird Dinners are served from 3pm to 6pm. 
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
print(early_bird_menu)
# Output
# Early Bird menu available from 1500 - 1800

# Dinner served from 5pm to 11pm. 
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
print(dinner_menu)
# Output
# Dinner menu available from 1700 - 2300

# Kids Dinners are served from 11am to 9pm. 
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 2100)
print(kids_menu)
# Output
# Kids menu available from 1100 - 2100


# CREATE FRANCHISES




# CREATE BUSINESSES






