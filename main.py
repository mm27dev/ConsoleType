#imports modules needed
import time
import os
from wonderwords import RandomWord
global new
w = RandomWord()
#stores inbuilt tests into a dict
global random_words
def random_words():
    words = ""
    for i in range(10):
        generator =w.word(word_min_length=5 ,word_max_length=7)
        words = words + " " + generator
    random_test_data = words + "."
    return random_test_data.strip()



random_word = random_words()

def create_and_edit_leaderboard(wpm,text_type):
    type_text = text_type
    string_thing = str(wpm)
    allthescores_list = []
    try:
        open("allthescores_typingtest_python.txt", "x")
    except:
        pass
    with open("allthescores_typingtest_python.txt", "a") as allthescores:
        allthescores.write(string_thing+'\n')
    with open("allthescores_typingtest_python.txt", "r") as allthescores:
        for lines in allthescores.readlines():
            allthescores_list.append(int(lines))

    allthescores_list.sort(reverse=True)


    try:
        open("python_typing_leaderboard.txt", "x")
    except:
        pass
    with open("python_typing_leaderboard.txt", "w") as leaderboard:
        place_num = 0
        for thing in allthescores_list:
            place_num += 1
            leaderboard.write(str(place_num)+".    "+str(thing)+" WPM (User: "+username+", Test: "+type_text+")\n")









tests = {
    "The quick fox:" : "The quick brown fox jumps over the lazy dog.",
    "Random Words(Use this to improve WPM)" : random_word
}
#initiates just the test  in a func for reuse in other modes
def test(text,option,type_of_test):
    type_test =type_of_test
    #stores param
    test_data = text
    #shows opening for test
    os.system("cls")
    print("Test will start in:")
    time.sleep(1)
    os.system("cls")
    print("3")
    time.sleep(1)
    os.system("cls")
    print("2")
    time.sleep(1)
    os.system("cls")
    print("1")
    time.sleep(1)
    os.system("cls")
    #record start and end time
    time1 = time.time()
    type_it = input(test_data+"\n>")
    time2 = time.time()
    #minus times for final time
    true_time = time2 - time1
    #if input and test string are equal
    if type_it.strip() == test_data.strip():
        #find wpm and time
        print("You have perfect accuracy!")
        time.sleep(1.5)
        word_num = 0
        min_time = true_time/60
        for words in test_data.split():
            word_num += 1
        wpm = word_num/min_time
        print("This test took you "+str(true_time.__round__(1))+" seconds/"+str(min_time.__round__(3))+" minutes to complete!")
        print("You type at "+ str(wpm.__round__()) + " wpm!")
        rounded_wpm= wpm.__round__()
        create_and_edit_leaderboard(rounded_wpm,type_test)
        new_key = option
        if new_key == "2":
            quit()
        else:
            print("Would you like to quit the application(enter) or go back to the test start screen(y) ")
            continue_again = input(">")
            if continue_again == "y":
                start()
            else:
                quit()

    # or else
    else:
        #restart test
        print("Your accuracy was not good enough! Please all sure to type all the words, spaces, and punctuation correctly!")
        time.sleep(1.5)
        start()






print("Welcome to ConsoleType, a comprehensive typing text that runs right in your Python Console.")
global username
username = input("What is your username:  ")
def start():
    choose_option =input("Would you like to choose from our in-built library of test(l), load a .txt file(f), or view the leaderboard(g)\n>")
    #checks if option is valid
    while choose_option != "l" and choose_option != "f" and choose_option != "g":
        choose_option = input("Please choose a valid option!\n>")
    if choose_option == "l":
        key_num = 0
        for key in tests:
            key_num +=1
            print(str(key_num)+"." + key)
        test_choice = input("Enter the number of the test you would like to take :\n>")
        global new
        new = test_choice.strip()
        new_key_num = 0
        for key_dummy in tests:
            new_key_num+=1
            if str(new_key_num) == new and str(new_key_num) != "2" and new != "2":
                cus_text = tests[key_dummy]
                test(cus_text,False,"The quick fox")
            elif str(new_key_num) == new and str(new_key_num) == "2" and new == "2":
                test_text = tests[key_dummy]
                test(test_text, "2","Random Words")


    if choose_option == "f":
        #find path for file
        user = input("What is the name of the user in directory path\n>")
        folder = input("What is the name of the main folder the file is stored in\n>")
        file_name = input("What is the name of the file\n>")
        for dirs, path , files in os.walk("C:/Users/"+user+"/"+folder):
            if file_name in files:
                with open ("C:/Users/"+user+"/"+folder+"/"+file_name, "r") as file:
                    data = file.read()
            else:
                print("Not a valid file or path")
        textdata = data
        test(textdata,False,"Custom .txt File")
    # initiate game mode
    if choose_option == "g":
        with open ("python_typing_leaderboard.txt", "r") as leaderboard:
            data = leaderboard.read()
            os.system("cls")
            print(data)

print("Please wait...")
start()