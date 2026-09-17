from pyscript import document, display

def place_order(e):
       document.getElementById("output1").innerHTML ="" 
       Main = document.getElementById("Main")
       Appetize = document.getElementById("Appetize")
       Drink = document.getElementById("Drink")
       Main_price = float(Main.value)
       Appe_price = float(Appetize.value)
       Drink_price = float(Drink.value)
       total = Main_price + Appe_price + Drink_price
       VAT = total * 0.12
       SuperTotal = total + VAT
       display(f"[[Thank you For your Order!]]", target="output1") 
       display(f"[[Receipt]]", target="output1") 
       display(f"Subtotal: {total}", target="output1") 
       display(f"VAT: {VAT}", target="output1") 
       display(f"Total: {SuperTotal}", target="output1") 
       display(f"Please come back again!(with more money.)", target="output1") 