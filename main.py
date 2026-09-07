import string 

STOP_WORDS = ["the", "is", "at", "which", "and", "to",
              "a", "an", "for", "my", "i"]

TECHNICAL_KEYWORDS = ["crash", "bug", "broken", "error"]

BILLING_KEYWORDS = ["bill", "charged", "payment", "subscription"]


def classify_message(message):
    message = message.lower()

    words = message.split()

    words = [word.strip(string.punctuation) for word in words]

    filtered_words = [word for word in words if word  not in STOP_WORDS]

    its_technical = False
    its_billing = False

    for word in filtered_words:

        if word in TECHNICAL_KEYWORDS:
            its_technical = True 

        if  word in BILLING_KEYWORDS:
            its_billing = True 


    if  its_technical:
        return "Technical Support"

    elif its_billing:
        return "Billing Support" 
    else:
        return "General Inquiry" 

message = input("enter your message :-")
result = classify_message(message)    
print(result)           


    
