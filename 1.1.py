count_int = int(input())
sum_el = []

while len(sum_el) < count_int:
    input_integer = int(input())
    sum_el.append(input_integer)

print(sum(sum_el))
