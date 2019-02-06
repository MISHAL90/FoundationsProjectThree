# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Mishal"
my_age = 28
my_bio = " nothing"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    # your code goes here!
    print (" would you like to: ")
    print ("1) Create a new culb. ")
    print ("or")
    print ("2)Browse and join clubs")
    print ("or")
    print ("3) View existing clubs")
    print ("or")
    print ("4) Display members of a club")
    print ("or")
    print ("-1)Close application")
    user_input=input (" ")
    if int(user_input) == 1:
    	create_club()
    elif int(user_input)== 2:
    	join_clubs()
    elif int(user_input)==3:
    	view_clubs()
    elif int(user_input)==4:
    	view_club_members()
    elif int(user_input) == -1:
    	return

#population
    
def create_club():
    # your code goes here!
    print (" Pick a name for your new club: ")
    user_input_name = input (" ")
    print ( "what is your club about? ")
    user_input_desc = input (" ")
    
    new_club = Club(user_input_name ,user_input_desc) 
    print (" Enter the number of the people you would like to recruit to your new club (-1 to stop): ")
    print ("------------------------------------------------------")
    for item in population:
    	print ("%s ,%s " % (population.index(item)+1 , item.name )  )
    user_input_pop = input ("")
    while user_input_pop != "-1" :	
    	if population[int(user_input_pop)-1] in population:
    		new_club.recruit_member(population[int(user_input_pop)-1])
    		user_input_pop = input ("")
    print ("here's your club: ")
    print (user_input_name)
    print (user_input_desc)
    print ("Members: ")
    total_age = 0

    for member in new_club.members:
       print (" - %s (%s Years old) - %s" % (member.name , member.age , member.bio))
       print ("")
       total_age += member.age
    average = float(total_age) / len(new_club.name)
    print (" Average age in the club: %2f Years" % average)
    clubs.append(new_club)
    print ("Ok %s Club is successfully Created " % new_club.name)
    options() 

    

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print ("Name: %s" % club.name)
    	print (" Description: %s" % club.description)
    	print (" Members %s" % len(club.members))
    	print ("")

def view_club_members():
    # your code goes here!
    view_clubs()
    print ("")
    name_the_club_see_members = input (" Enter the name of the club whose members you'd like to see:")
    for club in clubs:
    	if (club.name.lower() == name_the_club_see_members.lower()):
    		club.print_member_list()
    	 #  obj_club = club
    		# print ("_ %s (%s Years old - %s" % (member.name , member.age , member.bio))
    		# print ("")


def join_clubs():
    # your code goes here!
    view_clubs()
    print  ("")
    name_the_club_join = input ("Enter the name of the club you'd like to join: ")
    obj_club = None
    for club in clubs:
    	if(club.name == name_the_club_join):
    	   obj_club = club
    	   obj_club.recruit_member(myself)
    	   break
    print ("%s just joined %s" % (myself.name , obj_club.name))
    options()


    

def application():
    introduction()
    # your code goes here!
    
