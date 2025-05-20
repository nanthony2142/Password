import gooeypie as gp
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]

colors = ['CornflowerBlue', 'LimeGreen', 'Orchid', 'DarkSlateGray']
fonts = ['times new roman', 'comic sans ms', 'verdana', 'chiller']
styles = ['italic', 'normal']


def check_password_length(event):
    password = password_input.text
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(symbols() in password) and any(char in symbols for char in password):
        result_lbl.text = "Password is strong."
    elif len(password) < 8:
        result_lbl.text = "Password is too short. Must be at least 8 characters."
    else:
        result_lbl.text = "Password is weak."

###### Create the app window ######

app = gp.GooeyPieApp("Password Checker")
app.set_size(500, 300)

##### Create widgets ######

prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Textbox(app)
password_input.width = 25
password_input.height = 1
submit_bin = gp.Button(app, "Check", check_password_length)
test_new = gp.Label(app, "4, 4")
result_lbl = gp.Label(app, "")
title = gp.Label(app, "                                   Passolution")
intro_of_app = gp.Label(app, "Only the fittest passwords survive.")


###### set up a grid #######

app.set_grid(4, 3)

###### Add widgets to the grid ######
app.add(title, 1, 2)
app.add(intro_of_app, 2, 2, column_span=2)


app.add(password_input, 3, 2)
app.add(submit_bin, 4, 1, column_span=2)
app.add(result_lbl, 4, 3)

###### run the app ######

app.run()


