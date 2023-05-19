import requests

def get_movie_actors(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    api_key = "6214f274c799ca74fd8a2e0fed65e704"  
    params = {
        "api_key": api_key,
        "query": movie_name
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" in data:
        results = data["results"]
        if len(results) > 0:
            first_result = results[0]
            movie_id = first_result["id"]
            movie_title = first_result["title"]
            print("Película encontrada:", movie_title)
            url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
            response = requests.get(url, params={"api_key": api_key})
            credits_data = response.json()
            if "cast" in credits_data:
                cast = credits_data["cast"]
                print("Actores:")
                for actor in cast:
                    name = actor["name"]
                    character = actor["character"]
                    print(f"Nombre: {name}")
                    print(f"Personaje: {character}")
                    print("-----")
            else:
                print("No se encontraron actores para la película.")
        else:
            print("No se encontraron actores para la película.")
    else:
        print("No se encontraron actores para la película.")

movie_name = input("Ingresa el nombre de la película a buscar: ")
get_movie_actors(movie_name)
