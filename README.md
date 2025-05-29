[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DpCY8B3G)
My program is for someone who has hobbies, summer courses, or any activity in general over the summer and wants to plan it over a week so that they can have an organized schedule to follow. The program has the user type out their activities and when the user is done, they get a summer schedule for the week that they can follow.
Here are a function, Loop, and List block
Function:
def get_activities():
    activity_list = []
    print("What events, activities, or hobbies do you want to do over the summer?")
    print("Type one thing out at a time. Type 'done' when you're finished and want your schedule.\n")
Loop: 
   while True:
        user_input = input("Give a hobby or activity: ")
        if user_input.lower() == "done":
            break
        activity_list.append(user_input)
    return activity_list
List is in the function block
