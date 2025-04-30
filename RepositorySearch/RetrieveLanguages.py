import json

import requests

from RepositorySearch.utils import write_json_file


def get_repository_with_language():


    params = {
    }

    response = requests.get("https://api.github.com/search/repositories", params=params)
    response_json = json.loads(response.text)

    results = []
    for repo in response_json["items"]:
        lang_res = requests.get(repo["languages_url"])
        lang_res_json = json.loads(lang_res.text)

        results += [{"name": repo["name"], "lang": lang_res_json}]


if __name__ == "__main__":
    results = get_repository_with_language()
    write_json_file("repositories-http-lang.json", results)
