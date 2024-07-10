from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="20 Min Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="5 Min Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work Timer", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,
                             count - 1)  # we have to assign the window.after a variable to we can cancel it after
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for session in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro Timer")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # was set according to the image size
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,
                    image=tomato_img)  # first arg is x and the second arg is y and values are the center of the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", width=10, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)

window.mainloop()
