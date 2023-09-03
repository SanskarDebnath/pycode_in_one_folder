def n_calc():
    num1 = float(input("Enter the first number : "))
    num2 = float (input("enter the second number : "))
    char = input("Enter the operation : ")
    if (char == '+'):
        result = num1+num2
    elif (char == '-'):
        result = num1-num2
    elif (char == '*'):
        result = num1*num2
    elif (char == '/'):
        if (num2==0):
            print("can not divide by zero")
            return
        else:
            result=num1/num2
    print("The required result is : ",result)


def Qr_gen():
    import qrcode
    import random
    string2="abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rand_string = ""
    length = 14
    for a in range(length):
        rand_string += random.choice(string2)
    string = input("Enter the string or the Name and the URL\n")
    image_qr = qrcode.make(string)
    var = image_qr.save(rand_string+".png")
    print("Final message : image has been saved named as: "+rand_string+".png")


def time_teller():
    import time
    loc_time = time.localtime()
    current_time = time.strftime("%H:%M:%S",loc_time)
    print (current_time)



def rand_str_gen():
    import random
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    length = int(input("enter the length of the Random String : "))
    random_string = ""
    for i in range(length):
        random_string = random_string + random.choice(string)
    print("The random string is : "+random_string)

def rand_num_gen():
    import random
    num = "0123456789"

    length = int(input("enter the size of the random number : "))

    rand_number = ""
    for i in range (length):
        rand_number += random.choice(num)
    print(rand_number)


def string_calculator():
    a = str(input("enter the string here : "))
    count=0
    for i in a:
        count=count+1
    print(count)



def random_password_gen():
    import time
    import random
    import datetime
    
    name = str(input("Enter the first name : "))
    count = 0
    for i in name:
        count = count + 1
    if (count>4):
        name = name[0:4]
    random_number = "1234567890"
    rand_num = ""
    num_length = 2
    for b in range (num_length):
        rand_num += random.choice(random_number)
    today  = datetime.date.today()
    current_year = today.year
    str_year = str(current_year)
    rand_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = 5
    old_password = ""
    for i in range (length):
        old_password = old_password + random.choice(rand_string)
    current_password = name+"-"+rand_num+"-"+old_password+"/"+str_year
    print(current_password)
    count_str = 0
    for i in current_password:
        count_str+=1
    print("Total length of the Password is : ",count_str)


def area_diff_shapes():
    choice = int(input("Enter the semi choioce : "))
    if (choice == 1):
        circle_area()
    elif (choice == 2):
        rectangle_area()
    elif (choice == 3):
        Square_area()
    elif (choice == 4):
        Trapezium()
    elif (choice == 5):
        Rhombos()
    else:
        print("error occured. The Choice are in between (1-5)")
        
def circle_area():
    #circle area
    import math
    rad = float(input("Enter the Radius of the Circle : "))
    circle_rad = math.pi*pow(2,rad)
    print ("the area of the circle is : %.3f"%circle_rad)

def rectangle_area():
    #rectangle area
    import math
    base,height  = map(float,input("Enter the Base of the rectangle : ").split())
    rect_area = base*height
    print("The total area of the rectangle is : %.2f"%rect_area)

def Square_area():
    
    base,height  = map(float,input("Enter the Base and the Height of the Square : ").split())
    squ_area = base*height
    print("The total area of the rectangle is : %.2f"%squ_area)


def Trapezium():
    #area for Trapezium
    a,b,height = map(float,input("Enter the two sides and the height : ").split())
    #print(a,b)
    trap_are = ((a+b)*height)/2
    print ("the area of the Trapezium is : %.2f"%trap_are)

def Rhombos():
    #area of Rhombos
    length,height = map(float, input("enter the Length and the height of the Rhombos : ").split())
    Rhombos_area = (length*height)/2
    print("The area Of th Rhombos is : %.2f"%Rhombos_area)


def alarm ():
    import time
    t = float(input("enter the time in minuites for a timer\n"))
    time.sleep(t*60)

    
    from winsound import Beep

    notes = {'C': 1635,
         'D': 1835,
         'E': 2060,
         'S': 1945,
         'F': 2183,
         'G': 2450,
         'A': 2750,
         'B': 3087,
         ' ': 37}


    melodie = 'CDEFG G AAAAG AAAAG FFFFE E DDDDC CDEFG G AAAAG AAAAG FFFFE E DDDDC CDEFG G AAAAG AAAAG FFFFE E DDDDC CDEFG G AAAAG AAAAG FFFFE E DDDDC CDEFG G AAAAG AAAAG FFFFE E DDDDC CDEFG G AAAAG AAAAG FFFFE E DDDDC'
    for i in melodie:
        Beep(notes[i], 500)




def factorial():
    a=int(input("Enter the number : "))
    before = a
    for i in range (1,a):
        a=a*i
    print("The factorial of ",before," is : ",a)


def weather_teller():
    import datetime as dt
    import requests
    BASE_URl = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open('api_key.txt', 'r').read()
    city = str(input("Enter the City name : "))

    def kelvin_cel_fahrenhite(temp_k):
        c = temp_k - 273.15
        f = c * (9/5) + 32
        return c, f
    
    url = BASE_URl+"appid="+API_KEY+"&q="+city
    response = requests.get(url).json()
    temp_k = response['main']['temp']
    temp_c, temp_f = kelvin_cel_fahrenhite(temp_k)
    feels_like_k = response['main']['feels_like']
    feels_like_c , feels_like_f = kelvin_cel_fahrenhite(feels_like_k)
    windspeed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    sun_rise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

    sun_set_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f"Tempreture In city {city} : {temp_c : .2f}°C or {temp_f : .2f}°F")

    print(f"Tempreture In city {city} Feels like : {feels_like_c : .2f}°C or{feels_like_f : .2f}°F")

    print(f"Wind Speed In city {city} : {windspeed} KM/H")

    print(f"General weather in city {city} : {description}")

    print(f"Sun rises time in city {city} at {sun_rise_time} local time.")
    
    print(f"Sun sets time in city {city} at {sun_set_time} local time.")

#n_calc()

#Qr_gen()

#time_teller()

#rand_str_gen()

#rand_num_gen()

#string_calculator()

#random_password_gen()

#area_diff_shapes()

#alarm ()

#factorial ()

#weather_teller ()

import random
import string
chars = string.ascii_letters + string.digits + string.punctuation
print(chars)
