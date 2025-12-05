from prefect import flow, task
import httpx


@task(log_prints=True)
def get_stars(repo: str):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")
    
@task(log_prints=True)
def test1():
    print("Bien")

@task(log_prints=True)
def test2():
    print("bien2")

@flow(name="GitHub Stars")
def github_stars(repos: list[str]):
    test1()
    for repo in repos:
        get_stars(repo)
    test2()


# run the flow!
if __name__ == "__main__":
    github_stars.deploy(
        name="testing",
        work_pool_name="vm-BI2",
        cron="* * * * *"
    )
