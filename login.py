import customtkinter
import CTkMessagebox
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

#Defining the button Action
def login():
    print("Logged in")
    inputUser = usernameText.get()
    inputPass = passwordText.get()

    if inputUser == "admin" and inputPass == "root":
        print("Logged in")
        message = CTkMessagebox.CTkMessagebox(title="Login Confirmation" , message="You have successfully logged in to the system", icon="check",fade_in_duration=.1)
        response = message.get()
        if response == "OK":
            loginRoot.destroy()
        
    else:
        message = CTkMessagebox.CTkMessagebox(title="Login Error" , message="Invalid Login Details!", icon="cancel",fade_in_duration=.1)

#Creating the main window
loginRoot = customtkinter.CTk()
loginRoot.geometry('500x300')
loginRoot.title("System Login")

#Creating the elements within the login Page
frame = customtkinter.CTkFrame(loginRoot)
label = customtkinter.CTkLabel(frame, text="System Login", font=('Roboto', 24))
usernameText = customtkinter.CTkEntry(frame, placeholder_text="Username")
passwordText = customtkinter.CTkEntry(frame,placeholder_text="Password", show="*")
rememberCheck = customtkinter.CTkCheckBox(frame, text="Remember Me")
loginButton = customtkinter.CTkButton(frame, text="Login",command=login)


#Packing the elements within the login Page
frame.pack(pady=12, padx=10,expand=True, fill="both")
label.pack(pady=12, padx=10)
usernameText.pack(pady=12, padx=10)
passwordText.pack(pady=12, padx=10)
rememberCheck.pack(pady=0, padx=0)
loginButton.pack(pady=12, padx=10)


loginRoot.mainloop()