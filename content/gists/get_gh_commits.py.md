+++
title = "get_gh_commits.py"
description = "A Python script for exporting a GitHub user's daily commit counts to a CSV file."
date = 2023-08-05
draft = false

[taxonomies]
tags = ["python", "scripting", "data extraction"]

[extra]
+++

A Python script for exporting a GitHub user's daily commit counts to a CSV file.

```txt
# requirements.txt
# Do `pip install beautifulsoup4 pandas`
beautifulsoup4
pandas
```

```python
def get_gh_commit_data(github_username: str) -> list:
    """
    Get GitHub commit data for a given username by scraping the GitHub
    contribution calendar heatmap for each year of activity.

    This function returns a list of dictionaries with the following keys:
    - date: The date of the commit
    - commits: The number of commits on that date

    Parameters
    ----------
    github_username : str
        The GitHub username to get commit data for.

    Returns
    -------
    list
        A list of dictionaries with the commit data.
    """
    # Import the requests and BeautifulSoup libraries
    import requests
    import datetime
    from bs4 import BeautifulSoup

    _r1 = requests.get(f"https://github.com/{github_username}/")

    # Parse HTML and save to BeautifulSoup object
    html = BeautifulSoup(_r1.text, "html.parser")

    # Select the "year" links
    year_list = html.select("a.js-year-link")

    # Get the page links for each year
    pages = []
    for year in year_list:
        pages.append("https://github.com" + year.attrs["href"])

    # Get the commit data for each year
    commits = []
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for page in pages:
        # Get the page HTML for a given year
        _r = requests.get(page)
        html = BeautifulSoup(_r.text, "html.parser")

        # Get all the "rect" elements in the Calendar heatmap
        days = html.find_all("td", class_="ContributionCalendar-day")

        # Get the commit data for each day
        for day in days:
            # Check if the rect element has a "data-date" and "data-count" attribute
            if ("data-date" in day.attrs):
                # Check if the date is in the past
                if datetime.datetime.strptime(day["data-date"], "%Y-%m-%d") < today:
                    # Append the commit data to the list commits
                    commit_count = day.text.split(" ")[0]
                    if commit_count == "No":
                        commit_count = 0
                    commits.append(
                        {"date": day["data-date"], "commit_count": commit_count}
                    )

    return commits


def main(args=None):
    import pandas as pd

    # Get the GitHub username from the user
    username = input("Enter GitHub username: ")

    # Get the commit data and save to a pandas DataFrame
    df = pd.DataFrame(get_gh_commit_data(username))
    df.date = pd.to_datetime(df.date)
    df = df.sort_values(by="date")

    # Save the commit data to a CSV file
    df.to_csv(f"{username}_commit_data.csv", index=False)


# Check if the script is being run directly and run the main function
if __name__ == "__main__":
    main()
```