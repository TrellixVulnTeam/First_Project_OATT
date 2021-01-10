###########In The NME oF Allah##########
# check if admin if it not make him admin **
# check passwd with for loop*
# terms between accept and refuse**
# check full name,age && country *
# if right welcome with zfill && launch the app*
# Advertisment for discount based on the user country *
# fill a form of abilites with dictionary*
# Ok based on your abilites we suggest you go to ......... department*
# Notes for user to add if he wants*
# Enter number for contacting him if it's good*
# Don't forget using functions in if's for's while's
# Thanking for using the app *
################################
#####In the name of Allah######
###############################

import time

admins = ["Osama", "Ahmed", "Ibrahim"]
countries1 = ["Egypt", "KSA", "Bahrin", "Quatar", "Iraq", "lybia"]
countries2 = ["USA", "Germany", "Italy", "France"]
skills = ["Programmer", "Buffer-overflower"]
skills1 = ["Pen-testing", "Threat-hunting", "Bug-hunting"]
skills2 = ["Network-administrator", "Cisco-administrator"]


# function1
def name_passwd():
    user = input("Enter your name please:# ").strip().capitalize()
    if user in admins:
        # Password checking
        password = input("Enter your password please:# ")
        time.sleep(2)
        tries = 3
        passwd = "osama_elzero"

        while passwd != password:
            tries -= 1
            print(f"Wrong password!! you have {'last one, BE CAREFUL' if tries == 0 else tries} try left")
            password = input("Enter your password, again:# ")
            time.sleep(2)

            if tries == 0:
                print("=" * 50)
                print("Ok, You have tried all the chances come back after 1 hour")
                print("=" * 50)
                time.sleep(2)
                break
        else:
            time.sleep(2)
            print(f"ok, welcome to our app Mr/{user}")
            terms = input(
                f"We are sorry Mr/{user}, but we have a short query To improve our app if you wanna accept it hit [yes] if you don't hit [no]").strip().capitalize()
            if terms == "Yes" or terms == "Y" or terms == "yes":
                # Gathering Info
                fname = input("Please Enter your first name:# ")
                sname = input("Please Enter your second name:# ")
                tname = input("Please Enter your Third name:# ")
                time.sleep(2)
                country = input("Please Enter your country:# ").strip().capitalize()

                def fullname(fname, sname, tname, country):
                    print(
                        f"Ok, your personal Info are: {fname.strip().capitalize()} {sname.upper():.1s} {tname.capitalize()} {country}")

                fullname(fname, sname, tname, country)

                # countries
                if country in countries1:
                    print(f"Ok Mr/{user}, Based on your country We have a specific discount for you")
                    print("=" * 50)
                    print("We have a offer for you *Take the pythoner or pythonesta with 30% discount")
                    print("If you want this discount please messege osamaabdella2003@gmail.com")
                    print("=" * 50)

                elif country in countries2:
                    print(f"Ok Mr/{user}, Based on your country We have a specific discount for you")
                    print("=" * 50)
                    print("We have a magnifiecent offer for you *Take the pythoner or pythonesta with 10% discount")
                    print("If you want discount please messege (osamaabdella2003@gmail.com)")
                    print("=" * 50)
                else:
                    print("Sorry, You have no discount")

                # age
                def inputNumber(message):
                    while True:
                        try:
                            userInput = int(input(message))
                        except ValueError:
                            print("Enter a valid Number. please, Try Again!")
                            continue
                        else:
                            return userInput
                            break

                            # MAIN PROGRAM STARTS HERE:

                age = inputNumber("How old are you?")
                if (age <= 18):
                    print(
                        "Ok, Forget about your country.based on your age,It is clear you are a student, So we have a 50% discount for you")
                    print("=" * 50)
                    print("Take this course with just 50$")
                    print("If you want discount please messege (osamaabdella2003@gmail.com)")
                    print("=" * 50)


                else:
                    # print("You will be able to vote in " + str(18-age) + " year(s).")
                    print(
                        "Ok, Forget about your country.based on your age,It is clear you are a student, So we have a 30% discount for you")
                    print("=" * 50)
                    print("Take this course with just 60$")
                    print("If you want discount please messege (osamaabdella2003@gmail.com)")
                    print("=" * 50)
                    time.sleep(2)

            def skiils():
                print("=" * 50)
                print(skills)
                print(skills1)
                print(skills2)
                print("=" * 50)

                ability = input(
                    "Please, insert your job from above, and we 'll see your abilites(case sensitive) please):# ")
                # tuple = ("html", "java", "osama")
                # def abilites(*ability):
                #    print("Ok, Your abilites are:")
                #    for skill in ability:
                #        print(f" - {skill}")
                # abilites(*ability)
                if ability in skills:
                    print(
                        "Ok, you can improve your programming language by understanding the concept of progrmming, algorithms && Data structure")
                    print("We suggest you going to Programmers department")
                    notes = input("If you wanna add some notes about you, add it here\n")
                elif ability in skills1:
                    print(
                        "Ok, you can improve your cyber security sence by improving your thinking and hunting in the right time")
                    print("We suggest you going to IT department")
                    notes = input("If you wanna add some notes about you, add it here\n")
                elif ability in skills2:
                    print("Ok, you can improve your Network administration by taking CCNA, CCNA security && CCNP")
                    print("We suggest you going to Red team department")
                    notes = input("If you wanna add some notes about you, add it here\n")
                else:
                    print("Please, check It again!!(Enter a job from the list) (case sensitive)")
                    skiils()

            skiils()

            if terms == "No" or terms == "N":
                print("Sorry you refused the query, exiting....")
                exit()

    elif user not in admins:
        choose = input(
            "Ok, you are not admin, If you wanna me to add you in admins hit [yes], if not [No]:# ").strip().capitalize()
        if choose == "Yes" or choose == "Y":
            thenewname = input("Enter the name you prefer to use please? ")
            admins.append(thenewname)
            print("Done!!")
            name_passwd()
        else:
            print("As you like sir. Have a nice day!!")


name_passwd()

happy = input("We are happy for using our app, Did you liked it [yes/no]").strip().capitalize()
if happy == "Yes" or happy == "Y":
    print("Thanks for trusting us")
elif happy == "No" or happy == "N":
    print(f"Thanks for alerting us!!")
    sad = input("What's the Wrong please to develop it:#\n")
print("Bye!! friend")



