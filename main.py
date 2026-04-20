import string
import getpass

def check_pwd() :
    password = getpass.getpass("Enter Password :")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    
    for char in list(password):
        if char in string.ascii_lowercase :
            lower_count +=1
       
        elif char in string.ascii_uppercase:
            upper_count +=1
        
        elif char in string.digits :
            num_count +=1
            
        elif char.isspace():
            wspace_count +=1
        
        else :
            special_count +=1
    
    
    length = len(password)
    
    
    #Score
    
    if lower_count >=1 :
        strength +=1
    if upper_count >=1 :
        strength +=1     
    if num_count >=1 :
        strength +=1
    if wspace_count >=1 :
        strength +=1
    if special_count>=1 :
        strength +=1
    if length >=12:
         strength +=1

    #Strength message 
    if strength == 1 :
        remarks = "Very Bad Password !! Change ASAP"
    elif strength == 2 :
        remarks= "Not A Good Password !! Change ASAP"
    elif strength == 3 :
        remarks = "It's a weak password, consider changing"
    elif strength == 4 :
            remarks = "It's a hard password, but can be better"
    else:
            remarks = "A very strong password"
    
    print('Your password has :')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    
    print (f"Password strength : {strength}")
    print(f"Hint : {remarks}")
 
 
    
def ask_pwd():
        while True :
            choice=input("Do you want to enter another pwd (y/n):")
        
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            else :
                print ('Invalid choice, Try Again')

if __name__ == "__main__":
    print('=== Password Strength Checker ===')
   
   
    while True :
        check_pwd()
        
        if not ask_pwd():
            print("Goodbye.")
            break
        