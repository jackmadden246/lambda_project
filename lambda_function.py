import requests
from bs4 import BeautifulSoup
import threading
import sqlite3

import time


def web_scrape(company=None, text=None):
    url = "https://realpython.github.io/fake-jobs/"
    web_page = requests.get(url)
    # print(web_page.text)
    soup = BeautifulSoup(web_page.content, 'html.parser')
    results = soup.find(id="ResultsContainer")
    # print(results.prettify())
    jobs = results.find_all("div", class_="card-content")
    for job in jobs:
        company_element = job.find("h3", class_="company")
        title_element = job.find("h2", class_="title")
        company_names = results.find_all("h3")
        keys = []
        values = []
        titles = results.find_all("h2")
    for company in company_names:
        python_titles = results.find_all("h2", string=lambda text: "python" in text.lower())
        company_1 = company.text
    keys.append(company_1)

    for titles in python_titles:
        titles_1 = titles.text
    values.append(titles_1)
    jobs_in_python = {}
    for i in range(0, len(values)):
        jobs_in_python[keys[i]] = values[i]
    # print(jobs_in_python)
    jobs_str = ""

    # Convert the dictionary to a string
    # using for loop and items() function
    for key, value in jobs_in_python.items():
        jobs_str += ' ' + key + ', ' + value + ' '
    # print(jobs_str)


def jobs_and_titles(target, arg):
    conn = sqlite3.connect('Python_jobs.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS JOBS(
                               JOB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                               JOB_TITLE VARCHAR(45),
                               COMPANY VARCHAR(45)); """)
    conn.commit()
    thread_connection_1 = threading.Thread(target=jobs_and_titles, args=['Savage-Bradley', 'Senior Python Developer'])
    thread_connection_2 = threading.Thread(target=jobs_and_titles, args=['Salazar-Meyers', 'Software Engineer (Python)'])
    thread_connection_3 = threading.Thread(target=jobs_and_titles, args=['Smith and Sons', 'Python Programmer (Entry-Level)'])
    thread_connection_1.start()
    thread_connection_2.start()
    thread_connection_3.start()
    thread_connection_1.join()
    thread_connection_2.join()
    thread_connection_3.join()


if __name__ == "__main__":
    start = time.time()
    web_scrape()
    end = time.time()

    print('Time took to execute:', end - start)
