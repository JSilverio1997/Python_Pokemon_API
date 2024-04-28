import requests
import json
import time
from datetime import datetime
import winsound
from Report.PokemonFile import PokemonFIle


class ApiExtractionPokemon:
    write_line = False
    pokemon_file = PokemonFIle

    def __init__(self):
        self.execute_api()

    def write_log(self, message):
        if self.write_line:
            print(message)

    def create_request(self, url):
        pokemon_data = {}
        try:
            response = requests.request("GET", url)

            if response.status_code == 200:
                json_file = json.loads(response.text)
                pokemon = json_file
                pokemon_data = dict(pokemon)
            else:
                self.write_log(f"Erro ao Tentar Consumir dados da API, veja o Status Code: {response.status_code}")

            return pokemon_data

        except:
            self.write_log(f"Erro em Geral ao Tentar Consumir Dados da API: {url}")

    def execute_api_pokemon_specific(self, url):
        try:
            response = self.create_request(url)
            moves_list = list()

            for moves_name in response["moves"]:
                moves_list.append(moves_name["move"]["name"])

            if response["is_default"]:
                primary_form = "Verdadeiro"
            else:
                primary_form = "Falso"

            pokemon = {"id": response["id"],
                       "nome": response["name"],
                       "height": response["height"],
                       "weight": response["weight"],
                       "is_default": primary_form,
                       "moves": moves_list
                       }

            move_qty = 0

            self.write_log("-" * 450)
            self.write_log(f"Id do Pokémon: {pokemon["id"]}")
            self.write_log(f"Nome do Pokémon: {pokemon["nome"]}")
            self.write_log(f"Altura do Pokémon: {pokemon["height"]}")
            self.write_log(f"Largura do Pokémon: {pokemon["weight"]}")
            self.write_log(f"Forma Primária do Pokémon: {pokemon["is_default"]}")

            for moves in pokemon["moves"]:
                move_qty += 1
                self.write_log(f"Golpe {move_qty}: {moves}")

            self.write_log("-" * 450)

            return pokemon

        except:
            print("Erro ao Tentar Executar a Extração de Dados de um Pokémon Específico. ")

    def execute_api_all_pokemons(self, url):
        try:
            list_names_pokemon = list()
            pokemon_qty_save = 0

            self.write_log("Criando Lista de Pokémon...")

            while url is not None:
                response = self.create_request(url)
                url = response["next"]

                for pokemons in response["results"]:
                    list_names_pokemon.append(pokemons)
                    pokemon_qty_save += 1

                    ''' self.write_log(f"Adicionando {pokemon_qty_save}º Pokémon a lista...")
                        self.write_log(f"Nome do Pokémon: {pokemons["name"]}")
                        self.write_log(f"URL demais Informação do Pokémon: {pokemons["url"]}")
                        self.write_log("-" * 250) '''

            self.write_log("Lista de Pokémon Criada...\n")
            winsound.Beep(1000, 500)

            return list_names_pokemon

        except:
            print("Erro ao Tentar Executar a Extração de Dados de Todos os Pokémons. ")

    def execute_api(self):
        dict_pokemon = dict()
        pokemon_list = list()

        # try:
        pokemon_name = input("\nDigite o Nome de Um Pokemon: ").strip()

        if pokemon_name == "":
            url = "https://pokeapi.co/api/v2/pokemon/"
            self.write_log("-" * 450)
            print(f"Data e Horário Inicial da Execução: {datetime.now().strftime("%d/%m/%Y  %H:%M:%S")}")
            list_names_pokemon = self.execute_api_all_pokemons(url)

            time.sleep(5)
            for find_pokemon_data in list_names_pokemon:
                dict_pokemon = self.execute_api_pokemon_specific(find_pokemon_data["url"])
                pokemon_list.append(dict_pokemon)
                self.pokemon_file.create_pokemon_file_specificy(dict_pokemon, find_pokemon_data["name"],
                "Pokemon")

            self.pokemon_file.create_pokemon_file_all(pokemon_list)
            print(f"Data e Horário Final da Execução: {datetime.now().strftime("%d/%m/%Y  %H:%M:%S")}")
            self.write_log("-" * 450)



        else:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
            dict_pokemon = self.execute_api_pokemon_specific(url)
            time.sleep(5)
            self.pokemon_file.create_pokemon_file_specificy(pokemon_datas=dict_pokemon,
                                                            pokemon_name=pokemon_name.lower(),
                                                            path_dir="SpecificyPokemon")

# except:
#  print("Erro em Geral ao tentar Executar Alguma Das APIs.")


# teste = ApiExtractionPokemon()
