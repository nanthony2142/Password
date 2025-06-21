import gooeypie as gp
import hashlib
import requests
import math
from random import choice
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
fonts = ['verdana']
styles = ['italic']
colours = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'yellow', 'cyan']
capital = [letter.upper() for letter in letters]
length_points = 1
character_points = 1
points_common = 1
total_points = 1
points_common = 0
points_words = 0
points_breaches = 0

def check_breaches():        
        sha1_password = hashlib.sha1(password_input.text.encode('utf-8')).hexdigest().upper()
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f"Error fetching: {res.status_code}")

        hashes = (line.split(':') for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)  # Number of times password was found
        return 0  # Password not found

def check_password_length(event):
    global length_points
    result_lbl_title.text = "Feedback:"
    password = password_input.text
    if len(password) >= 12:
        level_of_password.text = "Your password length is great and secure."
        length_points = 5 

    elif len(password) >=8:
        level_of_password.text = "Your password is a bit too short. \nIt's recommended to be at least 12 characters long."
        length_points = 4

    elif len(password) >=6:
        level_of_password.text = "Your password is weak. \nIt's recommended to be at least 12 characters long."
        length_points = 3

    elif len(password) >=4:
        level_of_password.text = "Your password is extremely weak. \nIt's recommended to be at least 12 characters long."
        length_points = 2

    else:
        level_of_password.text = "Your password length is inadequate,\nIt needs to be much longer."
        length_points = 1
    

    check_characters()

def check_characters():
    global character_points
    password = password_input.text
    if any(char.isdigit() for char in password) and any(char in symbols for char in password) and any(char in letters for char in password) and any(char in capital for char in password):
        password_strength.text = "Your password has a diverse range of characters."
        character_points = 5
    
    elif any(char.isdigit() for char in password) and any(char in symbols for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password has a substantial range of characters.\n It would be even better if it included a capital letter."
        character_points = 4

    elif any(char.isdigit() for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password would be safer\nif it included symbols such as '@'."
        character_points = 3
    
    elif any(char in symbols for char in password) and any(char in letters for char in password):
        password_strength.text = "Your password would be safer\nif it included numbers such as '1'."
        character_points = 3

    elif any(char.isdigit() for char in password) and any(char in symbols for char in password):
        password_strength.text = "Your password would be safer if it\nincluded letters such as the letter 'a'."
        character_points = 3

    elif any(char.isdigit() for char in password):
        password_strength.text = "Your password is weak it would be\nsafer if it also included letters and symbols."
        character_points = 1
    
    elif any(char in symbols for char in password):
        password_strength.text = "Your password is weak it would be\nsafer if it also included letters and numbers."
        character_points = 1
    
    elif any(char in letters for char in password):
        password_strength.text = "Your password is weak it would be\nsafer if it also included numbers and symbols."
        character_points = 1
    
    check_common_passwords()
  
def check_common_passwords():
    global total_points, points_common, points_words, points_breaches

    points_common = 0
    points_words = 0
    points_breaches = 0

    f = open("common_passwords.txt")
    
    common_passwords = f.readlines()
    clean_passwords = []
   
 
    for password in common_passwords:
        password = password.replace("\n", "")
        clean_passwords.append(password)

    #print(clean_passwords)
    
    if password_input.text in clean_passwords:

        check_password.text = "Your password is commonly used. \nIt's highly recommended you don't use it."
    else:
        points_common = 1

    f = open("common_words.txt")

    common_words = f.readlines()
    clean_words = []

    for word in common_words:
        word = word.replace("\n", "")
        clean_words.append(word)
    
    if password_input.text in clean_words:
        check_password.text = "Your password is a common word.\nIt's recommended you don't use it."
    else:
        points_words = 1

    breach_count = check_breaches()

    if breach_count == 0:
        amount_of_breaches.text = "There are no known breaches with that password"
        points_breaches = 3
    else:
        amount_of_breaches.text = "There are {} known breaches with that password".format(breach_count)

    total_points = points_common + points_breaches + points_words
    

    visual_feedback()
    
def visual_feedback():
    global length_points, character_points, total_points

    if length_points == 5:
        points_length.text = "Length: ⭐️⭐️⭐️⭐️⭐️"
    elif length_points == 4:
        points_length.text = "Length: ⭐️⭐️⭐️⭐️"
    elif length_points == 3:
        points_length.text = "Length: ⭐️⭐️⭐️"
    elif length_points == 2:
        points_length.text = "Length: ⭐️⭐️"
    elif length_points == 1:
        points_length.text = "Length: ⭐️"

    if character_points == 5:
        points_character.text = "Characters: ⭐️⭐️⭐️⭐️⭐️"
    elif character_points == 4:
        points_character.text = "Characters: ⭐️⭐️⭐️⭐️"
    elif character_points == 3:
        points_character.text = "Characters: ⭐️⭐️⭐️"
    elif character_points == 2:
        points_character.text = "Characters: ⭐️⭐️"
    elif character_points == 1:
        points_character.text = "Characters: ⭐️"

    if total_points == 5:
        total_points_lbl.text = "Frequency: ⭐️⭐️⭐️⭐️⭐️"
    elif total_points == 4:
        total_points_lbl.text = "Frequency: ⭐️⭐️⭐️⭐️"
    elif total_points == 3:
        total_points_lbl.text = "Frequency: ⭐️⭐️⭐️"
    elif total_points == 2:
        total_points_lbl.text = "Frequency: ⭐️⭐️"
    elif total_points == 1:
        total_points_lbl.text = "Frequency: ⭐️"
    else:
        total_points_lbl.text = "Frequency: ⭐️"

    overall.text = str(math.floor((length_points + character_points + total_points) / 3))

    if overall.text == "5":
        overall.text = "Overall: ⭐️⭐️⭐️⭐️⭐️"
    elif overall.text == "4":
        overall.text = "Overall: ⭐️⭐️⭐️⭐️"
    elif overall.text == "3":
        overall.text = "Overall: ⭐️⭐️⭐️"
    elif overall.text == "2":
        overall.text = "Overall: ⭐️⭐️"
    elif overall.text == "1":
        overall.text = "Overall: ⭐️"

def toggle_mask(event):
    password_input.toggle()

def overall_mouse(event):
        overall.color = choice(colours)

def character_points_mouse(event):
    points_character.color = choice(colours)

def total_points_lbl_mouse_over(event):
    total_points_lbl.color = choice(colours)

def points_length_mouse_over(event):
    points_length.color = choice(colours)

###### Create the app window ######

app = gp.GooeyPieApp("Passolution")
app.set_size(880, 400)

##### Create widgets ######

result_lbl_title = gp.Label(app, "")
level_of_password = gp.Label(app, "")
prompt_lbl = gp.Label(app, "Enter your password:")
password_input = gp.Secret(app)
password_input.width = 25
password_input.height = 1
submit_bin = gp.Button(app, "Check password", check_password_length)
test_new = gp.Label(app, "4, 4")
sep_v = gp.Separator(app, 'vertical')
explain_procedure = gp.Label(app, "Enter password:")
check = gp.Checkbox(app, 'Show password')
check.add_event_listener('change', toggle_mask)
intro_of_app = gp.StyleLabel(app, "Only the fittest passwords survive!")
intro_of_app.font_name = 'Verdana' 
intro_of_app.font_size = 25            
intro_of_app.font_style = 'italic'      
password_strength = gp.Label(app, "")
check_password = gp.Label(app, "")
amount_of_breaches = gp.Label(app, "")
points_length = gp.StyleLabel(app, "")
points_length.font_name = 'Verdana'
points_length.font_size = 17
points_length.add_event_listener('mouse_over',points_length_mouse_over)
total_points_lbl = gp.StyleLabel(app, "")
total_points_lbl.font_name = 'Verdana'
total_points_lbl.font_size = 17
total_points_lbl.add_event_listener('mouse_over', total_points_lbl_mouse_over)
points_character = gp.StyleLabel(app, "")
points_character.font_name = 'Verdana'
points_character.font_size = 17
points_character.add_event_listener('mouse_over', character_points_mouse)
overall = gp.StyleLabel(app, "")
overall.font_name = 'Verdana'
overall.font_size = 25
overall.add_event_listener('mouse_over', overall_mouse)
link = gp.Hyperlink(app, "💀🥀","https://www.youtube.com/watch?v=xvFZjo5PgG0")
link.font_size = 5
tutorial = gp.Hyperlink(app, "A Demo of Passolution", "https://www.youtube.com/watch?v=DVi-sE-UwLw")

###### set up a grid #######

app.set_grid(8, 3)

###### Add widgets to the grid ######

app.add(intro_of_app, 1, 1, column_span=3, align='center')
app.add(password_input, 2, 2)
app.add(explain_procedure, 2, 1, align='right')
app.add(submit_bin, 3, 2, align='left')
app.add(result_lbl_title, 4, 1)
app.add(level_of_password, 5,1, column_span=2)
app.add(sep_v, 4,2, row_span=5, align='center')
app.add(password_strength, 6,1)
app.add(check_password,8,1)
app.add(points_length, 6,3)
app.add(points_character , 7,3)
app.add(total_points_lbl, 8,3)
app.add(overall, 4,3)
app.add(amount_of_breaches, 7,1)
app.add(check, 3, 1 , align='right')
app.add(link, 2, 3, align='right')
app.add(tutorial, 3, 3,)

###### run the app ######

app.run()
