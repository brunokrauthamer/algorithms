# Referência: Course Trybe
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/73f2a1d5-7d77-440b-a9f2-3ea9750db228/day/346e18ae-25d8-47a5-bd59-0e4d9cd2a2d2/lesson/9b22b10c-1e8a-4f00-bab8-edac69573b6b


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:  # se não reduzi o suficiente, continua
        mid = (start + end) // 2  # encontrando o meio
        merge_sort(numbers, start, mid)  # dividindo as listas
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)  # unindo as listas


# função auxiliar que realiza a mistura dos dois arrays


def merge(numbers, start, mid, end):
    left = numbers[start:mid]  # indexando a lista da esquerda
    right = numbers[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início
    # percorrer sobre a lista inteira como se fosse uma
    for general_index in range(start, end):
        # se os elementos da esquerda acabaram,
        # preenche o restante com a lista da direita
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        # se os elementos da direita acabaram,
        # preenche o restante com a lista da esquerda
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        # se o elemento do topo da esquerda for menor que o da direita,
        # ele será o escolhido
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            # caso o da direita seja menor, ele será o escolhido
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def string_sort(string):
    list_of_letters = []
    for letter in string:
        list_of_letters.append(letter)
    merge_sort(list_of_letters)
    return list_of_letters


def is_anagram(first_string, second_string):
    first_string_lower_case = first_string.lower()
    second_string_lower_case = second_string.lower()
    first_list_sorted = string_sort(first_string_lower_case)
    second_list_sorted = string_sort(second_string_lower_case)
    first_string_sorted = ''
    second_string_sorted = ''
    for letter in first_list_sorted:
        first_string_sorted += letter
    for letter in second_list_sorted:
        second_string_sorted += letter
    if first_string == '' or second_string == '':
        return (first_string_sorted, second_string_sorted, False)
    answer = first_string_sorted == second_string_sorted
    return (first_string_sorted, second_string_sorted, answer)
