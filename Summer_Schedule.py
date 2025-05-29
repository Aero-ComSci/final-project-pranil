import random
def get_activities():
    activity_list = []
    print("What events, activities, or hobbies do you want to do over the summer?")
    print("Type one thing out at a time. Type out 'done' when you have your activities and want your schedule.\n")

    while True:
        user_input = input("Give a hobby or activity: ")
        if user_input.lower() == "done":
            break
        activity_list.append(user_input)
    return activity_list    
def create_schedule(activities):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_schedule = []    
    for day in days:
        random_activity = random.choice(activities)
        week_schedule.append([day, random_activity])
    return week_schedule    
def show_schedule(schedule):
    print("\nHere is the summer schedule\n")
    for item in schedule:
        print(item[0] + ": " + item[1])
my_activities = get_activities()
if len(my_activities) == 0:
    print("You didn't add any activities; please add something you plan to do over the summer")
else:
    my_schedule = create_schedule(my_activities)
    show_schedule(my_schedule)
print("\nSee you next week for your new scedule.")
