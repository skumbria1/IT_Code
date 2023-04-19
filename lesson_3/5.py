shopping_list: list[str] = ['eggs', 'bread', 'waffles', 'soap', 'tea']
for item in shopping_list:
    if len(item) % 2 == 0:
        print(item, end=' ')
