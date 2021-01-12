#Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don’t know yet if they’re going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
price = 3

little_mermaid = 3
brother_bear = 5
hercules = 1

total = (little_mermaid + brother_bear + hercules) * 3

print(total)


#Suppose you’re working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350

total_pay = (facebook * 10) + (google * 6) + (amazon * 4)

print (total_pay)


#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_has_space = True
schedule_works = False
can_be_enrolled = class_has_space and schedule_works
can_be_enrolled

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

premium_member = True

number_of_items = 5

offer_not_expired = True

can_apply_offer = (number_of_items > 2 or premium_member) and offer_not_expired

can_apply_offer

#Class Review

is_premium_member = False
purchasing_more_than_two_items = True
offer_valid = True
offer_can_be_applied = offer_valid and (is_premium_member or purchasing_more_than_two_items)
offer_can_be_applied


#Use the following code to follow the instructions below:
    #username = ‘codeup’
    #password = ‘notastrongpassword’


#Create a variable that holds a boolean value for each of the following conditions:
    #the password must be at least 5 characters
    #the username must be no more than 20 characters
    #the password must not be the same as the username
    #bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_is_at_least_5_characters = len(password) >= 5
username_less_than_twenty_characters = len(username) <= 20
password_different_than_username = username != password

#bonus

password_has_no_whitespace = password == password.strip()
username_has_no_whitespace = username == username.strip()

is_valid_username_and_password = (password_is_at_least_5_characters
                            and username_less_than_twenty_characters
                            and password_different_than_username
                            and password_has_no_whitespace
                            and username_has_no_whitespace)

is_valid_username_and_password