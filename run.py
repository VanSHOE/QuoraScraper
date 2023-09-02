import subprocess

if __name__ == '__main__':
    search_queries = [
        'Hyderabad',
        'ChatGPT',
        'COVID-19',
        'MachineLearning',
        'IndianElections',
    ]

    for search_query in search_queries:
        subprocess.call(['python', 'scraper.py', search_query, '1'])