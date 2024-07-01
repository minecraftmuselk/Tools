f = 'todo.txt'
print('hijkio')
def show():
    todo_file = open(f, 'r')
    counter = 1
    for line in todo_file:
        line = line.strip('\n')
        print('  * (' + str(counter) + ') ' + line)
        counter += 1
    if counter == 1:
        print("Nothing in the list!")
    todo_file.close()

def add(item):
    todo_file = open(f, 'a')
    todo_file.write(item + '\n')
    todo_file.close()

def remove(number):
    todo_file = open(f, 'r')
    new_content = ''
    counter = 1
    for line in todo_file:
        if counter != number:
            new_content += line
        counter += 1
    todo_file.close()
    todo_file = open(f, 'w')
    todo_file.write(new_content)
    todo_file.close()

def main():
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove(number)
    print('Goodbye!')

main()