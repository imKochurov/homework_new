a = [chr(i) for i in range(97, 123)] # генеруємо усі букви алфавіту
print(a)



def reverse_by_stack(array):
    stack = [] # створюємо порожній стек
    reversed_result = [] # порожній список для оберненого результату
    for element in array: # поелементно наповнюємо стек "знизу-договри", від букви "a" до "z"
        stack.append(element)

    while len(stack) != 0: # поки стек не стане порожнім
        reversed_result.append(stack.pop()) # видаляємо елементи зі стеку "згори-донизу" від "z" до "a" і записуємо видалені елементи результуючий список

    return reversed_result

print(reverse_by_stack(a))







# def reverse(array:list):
#     lenth = len(array)
#     while lenth > 0:
#         array.insert(lenth, array[0])
#         array.pop(0)
#         lenth -= 1

# reverse(a)
# print(a)




# def reverse_2(array:list):
#     start_element = 0
#     end_element = len(array) - 1

#     while start_element < end_element:
#         array[start_element], array[end_element] = array[end_element], array[start_element]
#         start_element += 1
#         end_element -=1

# reverse_2(a)
# print(a)