def element_is_in_array(element, array): 
  len_seredin = len(array) // 2
  if len(array) == 0:
    return False
  if element == array[len_seredin]:
    return True 
  if element > array[len_seredin]:
    if len_seredin == 0:
      len_seredin = 1
    return element_is_in_array(element, array[len_seredin:]) 
  if element < array[len_seredin]:
    return element_is_in_array(element, array[:len_seredin])
tests = [
    (5, [1,2,3,4,5], True),
    (6, [1,2,3,4,5], False),
    (0, [1,2,3,4,5], False),
    (-1, list(range(10000)), False),
    (3578, list(range(10000)), True),
    (100, [], False),
    (100, [100], True)
]
all_ok = True
for element, array, result in tests:
  print(element_is_in_array(element, array))
