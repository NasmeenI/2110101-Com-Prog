import math

def mosteller(w, h):
    return math.sqrt(w*h)/60
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Mosteller formula
 
def du_bois(w, h):
    return 0.007184 * w**0.425 * h**0.725
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Du Bois formula
 
def fujimoto(w, h):
    return 0.008883 * w**0.444 * h**0.663
    # return the body surface area of a person
    # based on body weight (w) and height (h)
    # using Fujimoto formula
 
def main():
    weight = float(input())
    height = float(input())

    print("Mosteller =", round(mosteller(weight ,height), 5))
    print("Du Bois =", round(du_bois(weight ,height), 5))
    print("Fujimoto =", round(fujimoto(weight ,height),5))

exec(input()) # DON'T remove this line