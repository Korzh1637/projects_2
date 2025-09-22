from fuzzywuzzy import fuzz, process
import argparse

def find_duplicates(words):

    """
    Основная функция для нахождения дубликатов.
    
    Args:
        words ([str]): Список слов
        
    Returns:
        duplicates ([[str, str, int]]): Список, содержащий пары схожих слов и процент схожести
    """

    duplicates = []

    for i in range(len(words)):
        for j in range(i + 1, len(words)):

            w1, w2 = words[i], words[j]
            ratio = fuzz.ratio(w1, w2)

            #порог схожести
            if ratio >= 80:
                duplicates.append([w1, w2, ratio])
    
    return duplicates


def print_result(duplicates):

    """
    Функция для вывода результата.
    
    Args:
        duplicates ([[str, str, int]]): Список, содержащий пары схожих слов и процент схожести
    """

    for i in range(len(duplicates)):
        w1, w2, ratio = duplicates[i][0], duplicates[i][1], duplicates[i][2]
        print(f"{w1} <-> {w2} ({ratio}%)")


def main():

    """
    Основная функция для запуска из командной строки.
    
    Raises:
        parser.error: Если передано меньше двух слов
    """

    parser = argparse.ArgumentParser(description='Поиск нечётких дубликатов')
    parser.add_argument('input_list', help='список слов с опечатками')
    args = parser.parse_args()

    words = args.input_list.split(", ") #создание списка слов

    if not words or len(words) < 2:
        parser.error("Нужно передать как минимум два слова через запятую")

    duplicates = find_duplicates(words)
    print_result(duplicates)


if __name__ == "__main__": 
    main()