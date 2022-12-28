from tkinter import * 

window = Tk()

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg = 'cyan')

#adding widgets 

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight / (height*height)
    bmi = round(bmi, 1)
    print(bmi)

    name = username.get()
    msg = ''
    if bmi < 18.5: 
        msg = 'You are underweight!'
    elif bmi > 18.5 and bmi <=24.9:
        msg = 'Congratulations.You are in normal weight range!'
    elif bmi > 25 and bmi <= 29.9:
        msg = 'You are overweight!'
    elif bmi > 30:
        msg = 'You are obese!'
    else: 
        msg = 'Something has gone wrong.'

    output_msg = Label(result_frame, text = name+", your BMI is "+ str(bmi) + "\n"+ msg, bg = "cyan", font=("Calibri", 10), width=32)
    output_msg.place(x = 10, y = 40)
    output_msg.pack()

    
app_label = Label(window, text = "BMI Calculator", fg = "black", bg = "cyan", font=("Calibri", 20),bd=5)
app_label.place(x = 50, y =20)

name_label = Label(window, text = "Your Name: ", fg = "black", bg = "cyan", font=("Calibri", 12),bd=1)
name_label.place(x = 20, y = 90)

username = Entry(window, text='', bd = 2, width = 22)
username.place(x = 150, y =92)

weight_label = Label(window, text = "Enter weight (kgs) : ", fg = "black", bg = "cyan", font=("Calibri", 12),bd=1)
weight_label.place(x = 20, y = 140)

weight_entry = Entry(window, text='', bd = 2, width = 15)
weight_entry.place(x = 150, y =142)

height_label = Label(window, text = "Enter height (cms) : ", fg = "black", bg = "cyan", font=("Calibri", 12),bd=1)
height_label.place(x = 20, y = 190)

height_entry = Entry(window, text='', bd = 2, width = 15)
height_entry.place(x = 150, y =192)

calculate_button = Button(window, text = "Calculate BMI", fg = "black", bg = "cyan", bd = 4, command = calculate_bmi)
calculate_button.place(x = 20, y = 250)

result_frame = LabelFrame(window, text = "Result",bg = "cyan", font=("Calibri", 12))
result_frame.pack(pady = 5)
result_frame.place(x = 20, y = 300)

result_label = Label(result_frame, text = "", fg = "black", bg = "cyan", font=("Calibri", 10), width = 40)
result_label.place(x = 10, y = 20)
result_label.pack()




#mainloop () that is used when your application is ready to run. mainloop () is an infinite loop used to run the application, 
#wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()