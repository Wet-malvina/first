with open("user.txt","a") as file:
    text=input("Введите текст: ")
    file.write(text+"\n")