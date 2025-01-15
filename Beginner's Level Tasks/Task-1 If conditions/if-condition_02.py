#2. Write a program to determine which country a city belongs to. Given list of cities per country. Ask the user to enter a city name and print the corresponding country.
def determine_country():
    Australia = ["Sydney","Melbourne","Brisbane","Perth"]
    UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
    India = ["Mumbai","Bangalore","Chennai","Delhi"]
    #Getting input city from the user
    city = input("Enter a city name: ")
    if city in Australia:
        print(f"{city} is in Australia")
    elif city in UAE:
        print(f"{city} is in UAE")
    elif city in India:
        print(f"{city} is in India")
    else:
        print("Invalid city")
        
determine_country()
