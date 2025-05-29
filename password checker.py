import gooeypie as gp
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]



def check_password_length(event):
    password = password_input.text
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char in symbols for char in password):
        result_lbl.text = "Password is strong."
    elif len(password) < 8:
        result_lbl.text = "Password is too short. Must be at least 8 characters."
    else:
        result_lbl.text = "Password is weak."


def give_full_feedback(event):
    pass


###### Create the app window ######

app = gp.GooeyPieApp("Password Checker")
app.set_size(500, 300)

##### Create widgets ######

prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
password_input.width = 25
password_input.height = 1
submit_bin = gp.Button(app, "Check password", check_password_length)
test_new = gp.Label(app, "4, 4")
result_lbl = gp.Label(app, "")
sep_v = gp.Separator(app, 'vertical')

explain_procedure = gp.Label(app, "Enter password:")

intro_of_app = gp.Label(app, "Only the fittest passwords survive.")

title = gp.Label(app, "Passolution")



###### set up a grid #######

app.set_grid(7, 3)

###### Add widgets to the grid ######
#app.add(title, 1, 1)
#app.add(intro_of_app, 2, 1, column_span=2)
app.add(intro_of_app, 2, 1, column_span=3, align='center')
app.add(title, 1, 1, column_span=3, align='center')

app.add(password_input, 3, 2)
app.add(explain_procedure, 3, 1, align='right')
app.add(submit_bin, 4, 2, align='left')
app.add(result_lbl, 4, 3)
app.add(sep_v, 5, 2, row_span=3)


###### run the app ######

app.run()


