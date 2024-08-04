import timeit
import requests
import boyer_moore
import kmp
import rabin_karp

URLS = {
    "article1": "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh",
    "article2": "https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ",
}


def download_file(url):
    response = requests.get(url)
    response.raise_for_status()
    raw_data = response.content
    encoding = "windows-1251"
    return raw_data.decode(encoding)


text1 = download_file(URLS["article1"])
text2 = download_file(URLS["article2"])


def time_search(search_algorithm, text, pattern):
    return timeit.timeit(lambda: search_algorithm(text, pattern), number=10)


patterns1 = {
    "existing": "алгоритм сортування чисел",
    "non_existing": "якийсь вигаданий текст",
}
patterns2 = {
    "existing": "філософські роздуми",
    "non_existing": "якийсь вигаданий текст",
}

algorithms = {
    "Боєра-Мура": boyer_moore.boyer_moore_search,
    "Кнута-Морріса-Пратта": kmp.kmp_search,
    "Рабіна-Карпа": rabin_karp.rabin_karp_search,
}

results = {}

for text_name, text, patterns in [
    ("стаття 1", text1, patterns1),
    ("стаття 2", text2, patterns2),
]:
    results[text_name] = {}
    for algo_name, algo_func in algorithms.items():
        results[text_name][algo_name] = {}
        for pat_name, pattern in patterns.items():
            time_taken = time_search(algo_func, text, pattern)
            results[text_name][algo_name][pat_name] = time_taken

# Print results
for text_name, algo_results in results.items():
    print(f"Результати для {text_name}:")
    print(f"{'Алгоритм':<15} {'Існуючий підрядок (s)':<25} {'Неіснуючий підрядок (s)'}")
    print("-" * 50)
    for algo_name, times in algo_results.items():
        print(f"{algo_name:<15} {times['existing']:<25} {times['non_existing']}")
    print()
