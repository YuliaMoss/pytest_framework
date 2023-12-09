import json
import requests
from requests.exceptions import RequestException


def make_a_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except RequestException as request_error:
        raise f'Request error: {request_error}. Something went wrong with the request.'
    except Exception as other_error:
        raise f'Some error occurred: {other_error}. Please check your code for issues.'


def get_ship_data():
    url = "https://swapi.dev/api/starships/10/"
    return make_a_request(url)


def get_pilots_data(pilot_url):
    return make_a_request(pilot_url)


def get_planet_data(planet_url):
    return make_a_request(planet_url)


def collect_pilots_data(data_pilot):
    pilot_keys = ['name', 'height', 'mass', 'homeworld']
    pilot_dict = {key: data_pilot[key] for key in pilot_keys if key in data_pilot}

    planets_url = data_pilot['homeworld']

    data_planet = get_planet_data(planets_url)
    planet_keys = ['name']
    planet_values = [data_planet[key] for key in planet_keys if key in data_planet]
    if planet_values:
        pilot_dict['planet'] = planet_values[0]
    else:
        pilot_dict['planet'] = None
    return pilot_dict


def collect_starship_data():
    starship_data = get_ship_data()
    starship_info = ['name', 'max_atmosphering_speed', 'model', 'pilots']
    starship_dict = {key: starship_data[key] for key in starship_info if key in starship_data}

    pilots_list = []
    pilots_url = starship_data.get('pilots', [])

    for _url in pilots_url:
        pilot_data = get_pilots_data(_url)
        pilot_dict = collect_pilots_data(pilot_data)
        pilots_list.append(pilot_dict)

    starship_dict['pilots'] = pilots_list
    return starship_dict


def save_to_json_file(starship_dict=None):
    with open('millennium_falcon.json', 'w') as json_file:
        json.dump(starship_dict, json_file, indent=2)


if __name__ == '__main__':
    data_to_save = collect_starship_data()
    save_to_json_file(data_to_save)
