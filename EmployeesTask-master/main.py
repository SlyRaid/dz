import json



def employees_rewrite(sort_type):
    with open(file='employees.json', mode='r') as read_file:
        data = json.load(read_file)
        if sort_type == 'salary':
            sorted_data = sorted(data['employees'], key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])

    with open(f'employees_{sort_type.lower()}_sorted.json', 'w') as file:
        json.dump(sorted_data, file, indent=4)


employees_rewrite('salary')








#sorted_data = sorted(data, key=lambda x: x['salary'], reverse=True)

# with open(f'employees_{sort_type}_sorted.json', 'w') as file:
#     json.dump(sorted_data, file, indent=4)

