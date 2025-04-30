from github import Github

from RepositorySearch.utils import write_json_file


def get_repository_with_language():

    g = Github()
    results = []
    fetched_repositories = g.search_repositories(query="language:Java", sort='stars', order='desc')
    for i in range(20):
        repo = fetched_repositories[i]
        languages = repo.get_languages()
        results += [{"name": repo.name, "lang": languages}]

    return results


if __name__ == "__main__":
    results = get_repository_with_language()
    write_json_file("pygithub-search-lang.json", results)
