import time
from plyer import notification


if __name__ == '__main__':
    notification.notify(
        title = "Please Drink Water",
        message = "Water is essential to the human body and we need about 2.5 litres of water a day 1 Most of this will come from fluids but some from solid or liquid food the total of 2.5 litres per day is a rough estimate and depends on several factors.",
        app_icon =  r"C:\Users\saack\vs code projects\Healthy programmer\icon.ico",
        timeout=12
    )
    
