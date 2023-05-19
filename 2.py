import requests

def get_movie_details(movie_name):
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
            title = first_result["title"]
            overview = first_result["overview"]
            print(f"Title: {title}")
            print(f"Overview: {overview}")
        else:
            print("No se encontraron detalles de la película.")
    else:
        print("No se encontraron detalles de la película.")

movie_name = input("Ingresa el nombre de la película a buscar: ")
get_movie_details(movie_name)

