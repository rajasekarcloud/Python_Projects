# We are going to use the API
# https://v6.exchangerate-api.com/v6/24555bc969dd20c0a6aea6c8/latest/
# Create a API Key - 24555bc969dd20c0a6aea6c8
import requests;
import json;
# pycountry module to convert Country name to Code
import pycountry;
#print(pycountry.countries.get(name="India"));#
# Country(alpha_2='IN', alpha_3='IND', flag='🇮🇳', name='India', numeric='356', official_name='Republic of India')
from countryinfo import CountryInfo
# from countryinfo import CountryInfo - Get current information.
# https://www.geeksforgeeks.org/python-program-to-get-country-information/


def check_rate(currency_code):
    again_currency = ['GBP','EUR','USD'];
    base_url = "https://v6.exchangerate-api.com/v6/24555bc969dd20c0a6aea6c8/latest/";
    api_key = "24555bc969dd20c0a6aea6c8";
    payload: dict = {'access_key': api_key};
    #print(base_url+temp);
    data = requests.get(base_url+currency_code,params=payload);
    all_currency = data.json().get('conversion_rates');
    print(f'1 {currency_code}: ')
    for i in again_currency:
        print(f'{i} ->',all_currency.get(i));


country_name: str = input("Enter the country name: ");
country = CountryInfo(country_name);
currency_code = ''.join(country.currencies()); # Remove the space and []
country_code = country.iso(alpha=3);
check_rate(currency_code);
