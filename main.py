class WeDeliver:
  
  def __init__(self):
    self.drivers = []
    self.cities = {
        "Akkar": ["Jbeil","Beirut"],
        "Jbeil": ["Akkar","Beirut","Saida"],
        "Beirut": ["Akkar","Jbeil","Saida","Zahle"],
        "Saida": ["Jbeil","Beirut","Zahle"],
        "Zahle": ["Beirut","Saida"]
    }
    self.driver_id_counter = 1
    
  def main_menu(self):
    while True:
      print("Hello! Please enter:")
      print("1. To go to the drivers'menu")
      print("2. To go to the cities menu")
      print("3. To exit the system")
      choice = input("Your choice:")
      if choice == "1":
        self.drivers_menu()     
      elif choice == "2":
        self.cities_menu()
      elif choice == "3":
        print("Exiting the system. Goodbye")
        break
      else:
        print("Invalid choice. Please try again")
        
  def drivers_menu(self):
    while True:
      print("\nDRIVERS' MENU")
      print("1. To view all the drivers")
      print("2. To add a driver")
      print("3. To go back to main menu")
      choice = input("Your choice:")
      if choice == "1":
        self.view_all_drivers()
      elif choice == "2":
        self.add_driver()
      elif choice == "3":
        break  # Move break inside the if block
      else:
        print("Invalid choice. Please try again")
        
  def view_all_drivers(self):
    if not self.drivers:
      print("No drivers in the system")
    else:
      for driver in self.drivers:
        print(f"ID{driver['id']:03d},{driver['name']},{driver['city']}")
        
  def add_driver(self):
    name = input("Enter driver's name")
    city = input("Enter driver's start city")
    if city not in self.cities:
      print("City not recognized. Driver not added")
      return
    reachable_drivers = set()
    for driver in self.drivers:
      if self.can_reach_city(driver["city"],city):
        reachable_drivers.add(driver["name"])
    if reachable_drivers:
      print(f"Drivers delivering to {city}: {','.join(reachable_drivers)}")
    else:
      print(f"No drivers can deliver to {city}.")
      
  def can_reach_city(self,start_city, target_city):
    visited = set()
    queue = [start_city]
    while queue:
      current_city = queue.pop(0) 
      if current_city == target_city:
        return True
      if current_city not in visited:
        visited.add(current_city)
        queue.extend(self.cities[current_city])
        return False

if __name__ == "__main__":
  system = WeDeliver()
  system.main_menu()



      




      
