import re
def response(hey_bob):
    all_uppercase = hey_bob.isupper()
    if (hey_bob == ""):
        return "Fine. Be that way!"

    if (hey_bob.isspace() == False):
        hey_bob_joined = hey_bob.replace(" ", "")
    else:
        hey_bob_joined = hey_bob
        
    if all_uppercase:
        if(hey_bob_joined[-1] == '?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif (hey_bob_joined[-1] == '?'):
        return 'Sure.'
    elif(hey_bob.isspace()):
        return "Fine. Be that way!"
    else:
        return "Whatever."
