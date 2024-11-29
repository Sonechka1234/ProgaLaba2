from requests import RequestException
from result_repository import JsonResultRepository
from regex_service import RegexService



def main():
    repository = JsonResultRepository()
    service = RegexService(repository)

    while True:
        print("\nВыберите действие:")
        print("1. Получить СНИЛС из файла")
        print("2. Получить СНИЛС с веб-страницы")
        print("3. Найти СНИЛС в тексте")
        print("4. Выход")

        try:
            user_input = input("Введите номер действия: ").strip().lower()
            choice = int(user_input)

            match choice:
                case 1:
                    result = service.get_snils_in_file()
                        
                    print(f"Результат из файла: {result.snils}")

                case 2:
                    url = input("Введите URL веб-страницы: ")
                    result = service.get_snils_in_web(url)

                    print(f"Результат с веб-страницы: {result.snils}")

                case 3:
                    text = input("Введите текст: ")
                    snils_list = service.get_snils_in_text(text)

                    print(f"Результат из текста: {snils_list}")

                case 4:
                    print("Выход из программы.")
                    break

                case _:
                    print("Ошибка: выбрано недопустимое действие. Попробуйте снова.")

        except RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()