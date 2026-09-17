from pyscript import document, display

def place_order(e):
       document.getElementById("output1").innerHTML ="" 
       Main = document.getElementById("Main")
       Main_price = float(Main.value)
       display(Main_price, target="output1") 