def mainNumber():
    with open('main.txt') as file:
        passwd = file.readline()
        return passwd.strip()