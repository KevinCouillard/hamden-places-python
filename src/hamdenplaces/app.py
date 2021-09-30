"""
Gives information on certain locations in Hamden that fall under the categories of Gas Stations, Park or Restaurant.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HamdenPlaces(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        title_lable = toga.Label(
            'Hamden Places',
            style=Pack(padding=(0, 5))
        )
        
        start_button = toga.Button(
            'Start App',
            on_press=self.next_screen,
            style=Pack(height=100, width=600, padding=5)
        )
        
        appImage = toga.ImageView(id="startImage", image = "hamden_places_app_logo.jpg")
        
        start_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        image_box = toga.Box(style=Pack(direction=COLUMN, padding=5, height=575, width=600))
        image_box.add(appImage)
        start_box.add(title_lable)
        start_box.add(start_button)
        
        main_box.add(image_box)
        main_box.add(start_box)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
        
    def next_screen(self, widget):
        outer_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        gas_station_button = toga.Button(
            'Gas Stations',
            on_press=self.next_screen,
            style=Pack(height=100, width=600, padding=15)
        )
        
        restaurant_button = toga.Button(
            'Restaurants',
            on_press=self.next_screen,
            style=Pack(height=100, width=600, padding=15)
        )
        
        park_button = toga.Button(
            'Parks',
            on_press=self.next_screen,
            style=Pack(height=100, width=600, padding=15)
        )
        
        outer_box.add(gas_station_button)
        outer_box.add(restaurant_button)
        outer_box.add(park_button)
        
        self.second_window = toga.Window(title='Services')
        self.windows.add(self.second_window)
        self.second_window.content = outer_box
        self.second_window.show()
    
def main():
    return HamdenPlaces()
