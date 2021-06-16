# Classes - Menus, Franchises and Businesses

# The restaurant has been growing well.  Use python to keep things organised.

# KEY CONCEPTS
# Classes, Methods
# List filtering and aggregation
# Representing objects as strings


# CREATE FRANCHISES
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

#  string representation method for franchise address.
  def __repr__(self):
    return self.address

# Time will dictate which menu is availabe for a customer order
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus


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

# Calculate bill method for purchased items.
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill


# Brunch is served from 11am to 4pm. 
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
# print(brunch_menu.name)
# Output
# Brunch
# print(brunch_menu)
# Output (before string representation method)
# <__main__.Menu object at 0x7f16b88eeb38>
# Output (after string representation method)
# Brunch menu available from 1100 - 1600

# Test calculate_bill with brunch menu.
# print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
# Output
# 13.5

# Early-bird Dinners are served from 3pm to 6pm. 
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
# print(early_bird_menu)
# Output (after string representation method)
# Early Bird menu available from 1500 - 1800

# Test calculate_bill with early_bird menu
# print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# Output
# 21.5

# Dinner served from 5pm to 11pm. 
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
# print(dinner_menu)
# Output (after string representation method)
# Dinner menu available from 1700 - 2300

# Kids Dinners are served from 11am to 9pm. 
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 2100)
# print(kids_menu)
# Output (after string representation method)
# Kids menu available from 1100 - 2100

# Franchises - flagship_store and new_installment
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# Test Franchise string representation for Franchise address
# print(flagship_store)
# Output (after Franchise string representation method)
# 1232 West End Road

# Test available_menus method (as time will dictate which menu is availabe for a customer order)
# print(flagship_store.available_menus(1200))
# Output
# [Brunch menu available from 1100 - 1600, Kids menu available from 1100 - 2100]

# print(flagship_store.available_menus(1700))
# Output
# [Early Bird menu available from 1500 - 1800, Dinner menu available from 1700 - 2300, Kids menu available from 1100 - 2100]


# CREATE BUSINESSES















