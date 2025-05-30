import gooeypie as gp
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]

def check_password_length(event):
    password = password_input.text
    result_lbl_title.text = "Feedback:"
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char in symbols for char in password):

        level_of_password.text = "Password is strong."
    elif len(password) < 8:
        level_of_password.text = "Password is too short. \nMust be at least 8 characters."
    else:
        level_of_password.text = "Password is weak."
    check_common_passwords()

def check_common_passwords():
    f = open("common_passwords.txt")
    
    common_passwords = f.readlines()
    clean_passwords = []
 
    for password in common_passwords:
        password = password.replace("\n", "")
        clean_passwords.append(password)
    
    if password_input.text in clean_passwords:
        check_password.text = "Password is common. \nPlease choose a different one."
 
    # if "liverpool" in clean_passwords:
    #     print("Yes")
    # else:
    #     print("No")
    
    # f.close()

###### Create the app window ######

app = gp.GooeyPieApp("Passolution")
app.set_size(500, 300)

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


check_password = gp.Label(app, "")



###### set up a grid #######

app.set_grid(7, 3)

###### Add widgets to the grid ######
#app.add(title, 1, 1)
#app.add(intro_of_app, 2, 1, column_span=2)
app.add(intro_of_app, 1, 1, column_span=3, align='center')

app.add(password_input, 3, 2)
app.add(explain_procedure, 3, 1, align='right')
app.add(submit_bin, 4, 2, align='left')

app.add(result_lbl_title, 5, 1)
app.add(level_of_password, 6,1, column_span=2)

app.add(sep_v, 5, 2, row_span=3, align='center')

app.add(check_password,7,1)


###### run the app ######

app.run()


