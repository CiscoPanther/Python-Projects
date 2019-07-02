def cs_service_bot():
    print("Hello! Welcome to the Panther Communications Company's Service Portal. Are you a new or existing customer? \n [1] New Customer \n [2] Existing Customer\n")
    user_selection = input("Please enter the number corresponding to your choice: ")
    if user_selection == "1":
        new_customer()
    elif user_selection == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection." )
        cs_service_bot()

def existing_customer():
    account_name = input("Please enter your account name: ")
    print("Welcome back " + account_name + "\n")
    print("What kind of support do you need? \n")
    print(" [1] Television Support \n [2] Internet Support \n [3] Speak to a support representative. \n")
    user_selection = input("Please enter the number corresponding to your choice: ")
    if user_selection == "1":
        television_suport()
    elif user_selection == "2":
        internet_support()
    elif user_selection == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection")
        existing_customer()

def new_customer():
    your_name = input("Please enter your name: ")
    print("Hi " + your_name + ", We're excited to have you join the JIGU family, how can we help you today? \n")
    print(" [1] Sign up for service. \n [2] Schedule a home visit. \n [3] Speak to a sales representative. \n")
    user_selection = input("Please enter the kind of support you need: ")
    if user_selection == "1":
        sign_up()
    elif user_selection == "2":
        home_visit()
    elif user_selection == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection")
        new_customer()

def television_support():
    print("What is the nature of your problem? \n [1] I can't access certain channels. \n [2] My picture is blurry. \n [3] I keep losing service. \n [4] Other issues. \n")
    user_selection = input("Please select an option that best describes your problem: ")
    if user_selection == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif user_selection == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif user_selection == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif user_selection == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection, please try again..")
        television_support()

def internet_support():
    # Replace `pass` with your code
    print("What is the nature of your problem? \n [1] I can't connect to the internet. \n [2] My connection is very slow. \n [3] Ican't access certain sites. \n")
    user_selection = input("Please select an option that best describes your problem: ")
    if user_selection == "1":
        print("Unplug your router, then plug it back in, then give it sometime.")
        did_that_help()
    elif user_selection == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    elif user_selection == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif user_selection == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection, please try again..")
        internet_support()

def did_that_help():
    print("Did the solution solve the problem? \n [1] Yes \n [2] No: ")
    user_response = input("Please select a number that corresponds to your answer: ")
    if user_response == "1":
        Print("Thank you for visiting us today. Do enjoy the rest of your day!")
        return cs_service_bot()
    elif user_response == "2":
        print("We are sorry, would you rather talk to a live representative or schedule a home visit to address this problem \n [1] Live Rep \n [2] Home Visit \n")
        response = input("Please enter a number that corresponds to your response: ")
        if response == "1":
            live_rep("support")
        elif response == "2":
            home_visit("support")
        else:
            print("Sorry, we do not understand your selection.")
            did_that_help()
    else:
        print("Sorry, we didn't understand your selection.")
        did_that_help()

def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for. \n [1] Bundle Deal (Internet + Cable) \n [2] Internet \n [3] Cable")
    user_selection = input("Please select the plan you wish to sign up for: ")
    if user_selection == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif user_selection == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif user_selection == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we do not understand your selection")
        return sign_up()

def home_visit(purpose = "none"):
    if purpose == "none":
        print("What is the purpose of the home visit? \n [1] New service installation. \n [2] Exisitng service repair. \n [3] Location scouting for unserviced region.")
        purpose = input("Please select the purpose of the home visit:" )
        if purpose == 1:
            home_visit("new_install")
        elif purpose == 2:
            home_visit("support")
        elif purpose == 3:
            home_visit("scout")
        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    if purpose == "new install":
        print("Please enter a date below when you are available for a technician to come to your home and install your new service.")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date
    if purpose == "support":
        print("Please enter a date below when you are available for a technician to come and inspect the problem:")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date
    if purpose == "scout":
        print("Please enter a date below when you are available for a technician to come scout your region for expansion:")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date

def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")

cs_service_bot()

