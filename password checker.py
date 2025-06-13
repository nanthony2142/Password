import gooeypie as gp
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]


def check_password_length(event):
    result_lbl_title.text = "Feedback:"
    password = password_input.text
    if len(password) >= 12:
        level_of_password.text = "Your password length is great and secure."

    elif len(password) >=8:
        level_of_password.text = "Your password is a bit too short. \nIt should be at least 12 characters long."

    elif len(password) >=6:
        level_of_password.text = "Your password is very weak. \nIt should be at least 12 characters long."

    elif len(password) >=4:
        level_of_password.text = "Your password is extremely weak. \nIt should be at least 12 characters long."

    else:
        level_of_password.text = "Your password length is terrible,\nIt needs to be so much longer."

    check_characters()

def check_characters():
    password = password_input.text
    if any(char.isdigit() for char in password) and any(char in symbols for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password has a very diverse range of characters."

    elif any(char.isdigit() for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password would be better\nif it included symbols such as @."
    
    elif any(char in symbols for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password would be better\nif it included numbers such as 1."

    elif any(char.isdigit() for char in password) and any(char in symbols for char in password):
        password_strength.text = "Your password would be better if it\nincluded letters such as the letter 'a'."

    elif any(char.isdigit() for char in password):
        password_strength.text = "Your password is very weak it would be\nbetter if it included letters and symbols."
    
    elif any(char in symbols for char in password):
        password_strength.text = "Your password is very weak it would be\nbetter if it included letters and numbers."
    
    elif any(char in letters for char in password):
        password_strength.text = "Your password is very weak it would be\nbetter if it included numbers and symbols."
    check_common_passwords()


    
   
def check_common_passwords():
    f = open("common_passwords.txt")
    
    common_passwords = f.readlines()
    clean_passwords = []
 
    for password in common_passwords:
        password = password.replace("\n", "")
        clean_passwords.append(password)
    
    if password_input.text in clean_passwords:
        check_password.text = "Your password is very commonly used. \nIt's highly recommended you don't use it."
    else:
        f = open("common_words.txt")
    
        common_words = f.readlines()
        clean_words = []
    
        for word in common_words:
            word = word.replace("\n", "")
            clean_words.append(word)
        
        if password_input.text in clean_words:
            check_password.text = "Your password contains very common words.\nIt's recommended you don't use it."
        else:
            check_password.text = ""

def visual_feedback():
    pass

###### Create the app window ######

app = gp.GooeyPieApp("Passolution")
app.set_size(600, 300)

##### Create widgets ######


result_lbl_title = gp.Label(app, "")

level_of_password = gp.Label(app, "")
prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
password_input.width = 25
password_input.height = 1
submit_bin = gp.Button(app, "Check password", check_password_length)
test_new = gp.Label(app, "4, 4")
sep_v = gp.Separator(app, 'vertical')
explain_procedure = gp.Label(app, "Enter password:")
intro_of_app = gp.Label(app, "Only the fittest passwords survive.")
password_strength = gp.Label(app, "")
check_password = gp.Label(app, "")

star_png = gp.Image(app, 'images/star.png')



###### set up a grid #######

app.set_grid(8, 3)

###### Add widgets to the grid ######
#app.add(title, 1, 1)
#app.add(intro_of_app, 2, 1, column_span=2)
app.add(intro_of_app, 1, 1, column_span=3, align='center')

app.add(password_input, 3, 2)
app.add(explain_procedure, 3, 1, align='right')
app.add(submit_bin, 4, 2, align='left')

app.add(result_lbl_title, 5, 1)
app.add(level_of_password, 6,1, column_span=2)

app.add(sep_v, 5,2, row_span=4, align='center')

app.add(password_strength, 7,1)

app.add(check_password,8,1)

app.add(star_png, 7, 3)


###### run the app ######

app.run()


# problem: line is not working to seperate the two columns

# unperadictablity: the password is not being checked for length, symbols, and numbers correctly.