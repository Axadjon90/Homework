1)import threading
def check_numbers_substring(numbers_slice, substring, result_list, lock):
    """
    Berilgan raqamlar qatorida substring mavjudligini tekshiradi.
    Topilgan raqamlarni result_list ga qo'shadi (thread safe).
    """
    for number in numbers_slice:
        if substring in str(number):
            with lock:
                result_list.append(number)
def parallel_search(numbers, substring, num_threads=4):
    """
    numbers ro'yxatini num_threads qismga bo'lib, har bir qismni ipda tekshiradi.
    Natijada topilgan raqamlar ro'yxatini qaytaradi.
    """
    length = len(numbers)
    slice_size = length // num_threads
    threads = []
    result_list = []
    lock = threading.Lock()
    for i in range(num_threads):
        start = i * slice_size
        end = (start + slice_size) if i != num_threads - 1 else length
        slice_part = numbers[start:end]
        thread = threading.Thread(target=check_numbers_substring,
                                  args=(slice_part, substring, result_list, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return result_list
if __name__ == "__main__":
    numbers = [
        1234567890, 9876543210, 1122334455, 5566778899, 1010101010,
        9999999999, 123123123, 456456456, 789789789, 147258369,
        963852741, 111111111, 222222222, 333333333, 444444444,
        555555555, 666666666, 777777777, 888888888, 999999999
    ]
    substring = input("Qidiriladigan raqamni kiriting: ")
    found_numbers = parallel_search(numbers, substring, num_threads=4)
    print(f"\nSubstring '{substring}' ni o'z ichiga olgan raqamlar:")
    for num in found_numbers:
        print(num)
      Substring '5' ni o'z ichiga olgan raqamlar:
1234567890
9876543210
1122334455
5566778899
456456456
147258369
963852741
555555555

2)import threading
from collections import Counter
def count_words(text_chunk, local_counter):
    words = text_chunk.split()
    local_counter.update(words)
def read_file_chunks(filepath, num_threads):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    chunk_size = len(text) // num_threads
    return [text[i*chunk_size:(i+1)*chunk_size] if i != num_threads - 1 else text[i*chunk_size:]
            for i in range(num_threads)]
def parallel_word_count(filepath, num_threads=4)
    chunks = read_file_chunks(filepath, num_threads)
    threads = []
    counters = [Counter() for _ in range(num_threads)]
    for i in range(num_threads):
        thread = threading.Thread(target=count_words, args=(chunks[i], counters[i]))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    final_counter = Counter()
    for c in counters:
        final_counter.update(c)
    return final_counter
if __name__ == "__main__":
    filepath = input("Fayl yo‘lini kiriting: ")
    num_threads = 4
    result = parallel_word_count(filepath, num_threads)
    print("\n✅ So‘zlar soni:")
    for word, count in result.most_common(20):
        print(f"{word}: {count}")
      
