import csv
import re

def load_movies_data(file_path):
    movies_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies_data.append(row)
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    return movies_data

def save_movies_data(file_path, movies_data):
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=movies_data[0].keys())
            if file.tell() == 0:  # Якщо файл порожній, записати заголовки
                writer.writeheader()
            writer.writerows(movies_data)
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")

def search_movies_by_partial_input(movies_data, search_input, search_key):
    pattern = re.compile(search_input, re.IGNORECASE)
    results = [movie for movie in movies_data if pattern.search(movie[search_key])]
    return results

def display_search_results(results):
    if not results:
        print("Нічого не знайдено.")
        return

    print("Знайдені результати:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result['title']} ({result['year']})")

def view_movie_details(movie):
    print(f"\nОпис:\n{movie['description']}")
    print(f"\nТрейлер: {movie['trailer']}")

def main():
    file_path = 'films.csv'
    movies_data = load_movies_data(file_path)

    while True:
        print("\nВиберіть режим пошуку:")
        print("1. Пошук за назвою фільму")
        print("2. Пошук за жанром фільму")
        print("3. Пошук за роком випуску")
        print("4. Завантажити новий фільм")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            title_query = input("Введіть частину назви фільму: ")
            results = search_movies_by_partial_input(movies_data, title_query, 'title')
            display_search_results(results)

            if results:
                selected_index = int(input("Виберіть номер фільму для перегляду деталей (або 0, щоб повернутися): "))
                if 0 < selected_index <= len(results):
                    view_movie_details(results[selected_index - 1])

        elif choice == '2':
            genre_query = input("Введіть частину жанру фільму: ")
            results = search_movies_by_partial_input(movies_data, genre_query, 'gen')
            display_search_results(results)
            print(f"Знайдено фільмів у жанрі '{genre_query}': {len(results)}")

            if results:
                selected_index = int(input("Виберіть номер фільму для перегляду деталей (або 0, щоб повернутися): "))
                if 0 < selected_index <= len(results):
                    view_movie_details(results[selected_index - 1])

        elif choice == '3':
            year_query = input("Введіть частину року випуску фільмів: ")
            results = search_movies_by_partial_input(movies_data, year_query, 'year')
            display_search_results(results)
            print(f"Знайдено фільмів у роках, що містять '{year_query}': {len(results)}")

            if results:
                selected_index = int(input("Виберіть номер фільму для перегляду деталей (або 0, щоб повернутися): "))
                if 0 < selected_index <= len(results):
                    view_movie_details(results[selected_index - 1])

        elif choice == '4':
            new_movie = {
                'imdb_id': input("IMDb ID: "),
                'title': input("Назва: "),
                'year': input("Рік випуску: "),
                'popularity': input("Популярність: "),
                'description': input("Опис: "),
                'content_rating': input("Рейтинг вмісту: "),
                'movie_length': input("Тривалість: "),
                'rating': input("Рейтинг: "),
                'created_at': input("Дата створення: "),
                'trailer': input("Посилання на трейлер: "),
                'image_url': input("Посилання на зображення: "),
                'release': input("Дата випуску: "),
                'plot': input("Сюжет: "),
                'banner': input("Посилання на банер: "),
                'type': input("Тип: "),
                'more_like_this': input("Подібні фільми: "),
                'gen': input("Жанр: "),
                'keywords': input("Ключові слова: "),
            }
            movies_data.append(new_movie)
            save_movies_data(file_path, [new_movie])
            print("Фільм успішно додано.")

        elif choice == '0':
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()
