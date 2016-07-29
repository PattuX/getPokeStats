import argparse
from pgoapi import pgoapi

parser = argparse.ArgumentParser()
parser.add_argument("login_name")
parser.add_argument("password")
parser.add_argument("service", help="ptc or google")
parser.add_argument("lat")
parser.add_argument("long")
args = parser.parse_args()

pokemon_list = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","NidoranF","Nidorina","Nidoqueen","NidoranM","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]

pokeapi = pgoapi.PGoApi()
login_name = args.login_name
password = args.password
service = args.service
lat = args.lat
long = args.long

pokeapi.login(service, login_name, password, float(lat), float(long), 10)
pokeapi.get_inventory()
request = pokeapi.create_request()
request.get_inventory()
response = request.call()
items = response['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']

print "nickname;species;attack_IV;defense_IV;stamina_IV;percent;cp"
for item in items:
    if 'pokemon_data' in item['inventory_item_data']:
        # Eggs are treated as pokemon by Niantic.
         if 'is_egg' not in item['inventory_item_data']['pokemon_data']:
            pokedata = item['inventory_item_data']['pokemon_data']
            attack_IV = pokedata.get('individual_attack', 0)
            defense_IV = pokedata.get('individual_defense', 0)
            stamina_IV = pokedata.get('individual_stamina', 0)
            percent = float(attack_IV + defense_IV + stamina_IV)/45. * 100.
            percent = "%.2f" % percent
            cp = str(pokedata.get('cp', 0))
            species = pokemon_list[int(pokedata.get('pokemon_id', 0))-1]
            nickname = pokedata.get('nickname', 'no_nickname')
            print "%s;%s;%s;%s;%s;%s;%s" %(nickname, species, str(attack_IV), str(defense_IV), str(stamina_IV), percent, cp)
            
            
