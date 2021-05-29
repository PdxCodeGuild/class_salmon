filename = 'contacts_output.csv'
def open_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        # print("lines: ", lines)
        print(file)
    print(lines)


def thisthis():
    print('this')

thisthis()
open_file(filename)


print(lines)
print(file)