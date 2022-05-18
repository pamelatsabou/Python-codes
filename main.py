import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    title_label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    elif reps % 2 == 1:
        title_label.config(text="Working Time", fg=GREEN, bg=YELLOW)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    #if count_sec == 0:
     #   count_sec = "00"
    if count_min < 10:
       count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks, bg=YELLOW, font=("Times new roman", 10))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Times new roman", 35))
title_label.grid(column=1, row=0)

start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

check_mark = Label(text="", bg=YELLOW, font=("Times new roman", 10))
check_mark.grid(column=1, row=3)

window.mainloop()
