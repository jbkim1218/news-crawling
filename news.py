import requests
from bs4 import BeautifulSoup
import time

def get_all_news_titles(url):
    all_news_titles = []
    current_page = 1

    while True:
        full_url = f'{url}&page={current_page}'
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        news_elements = soup.find_all('dd', class_='articleSubject')

        for element in news_elements:
            news_title = element.find('a').text.strip()
            all_news_titles.append(news_title)


        current_page += 1

        if not news_elements:
            break

    return all_news_titles

def main():
    urls = [
        'https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=401',
        'https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=402',
        'https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=406'
    ]

    while True:
        for url in urls:
            all_news_titles = get_all_news_titles(url)


            for title in all_news_titles:
                print(title)

        time.sleep(3600)

if __name__ == "__main__":
    main()
