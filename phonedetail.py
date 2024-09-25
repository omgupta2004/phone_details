import phonenumbers 
import customtkinter as cst
from phonenumbers import timezone, geocoder,carrier

number=input("enter yout number with +__")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")#en is for company name in english
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)

