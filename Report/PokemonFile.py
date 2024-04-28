import json
import winsound


class PokemonFIle:

    def create_pokemon_file_all(pokemon_datas=list):
        file_path = r"C:\Users\João\PycharmProjects\APIExtractionCourse\Report\ReportCreated\GeneralFileAllPokemons"
        file_name = "PokemonList.json"
        file_complete = file_path + '\\' + file_name

        try:
            with open(file_complete, "w") as report_file:
                for datas in pokemon_datas:
                    json.dump(datas, report_file)

            report_file.close()
            print("_" * 450)
            print(f"O Arquivo {file_name} foi gerado com sucesso no diretório: {file_path}")
            winsound.Beep(1000, 500)

        except:
            print(f"Erro ao tentar gerar o arquivo : {file_name} no diretório: {file_path}.")

    def create_pokemon_file_specificy(pokemon_datas=dict, pokemon_name="", path_dir=""):
        file_path = fr"C:\Users\João\PycharmProjects\APIExtractionCourse\Report\ReportCreated\{path_dir}"
        file_name = f"{pokemon_name}.json"
        file_complete = file_path + '\\' + file_name

        try:
            with open(file_complete, "w") as report_file:
                json.dump(pokemon_datas, report_file)

            report_file.close()
            print("_"*450)
            print(f"O Arquivo {file_name} foi gerado com sucesso no diretório: {file_path}")
            # winsound.Beep(1000, 500)

        except:
            print(f"Erro ao tentar gerar o arquivo : {file_name} no diretório: {file_path}.")


"""teste = PokemonFIle
teste.create_pokemon_file_all(pokemon_datas={"nome":"ditto"})
teste.create_pokemon_file_specificy(pokemon_datas={"nome":"ditto"}, pokemon_name="ditto", 
path_dir="SpecificyPokemon")"""

