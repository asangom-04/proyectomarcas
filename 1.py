import requests

def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    api_key = "6214f274c799ca74fd8a2e0fed65e704"  
    params = {
        "api_key": api_key,
        "query": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" in data:
        results = data["results"]
        for result in results:
            title = result["title"]
            release_date = result["release_date"]
            print(f"Title: {title}")
            print(f"Release Date: {release_date}")
            print("-----")
    else:
        print("No se encontraron resultados.")

search_query = input("Ingresa el título o código de la película a buscar: ")
search_movies(search_query)
