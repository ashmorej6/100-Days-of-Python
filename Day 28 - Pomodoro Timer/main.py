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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="✔")
    timer_label.config(text="Timer")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 48, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 48, "bold"), fg=PINK, bg=YELLOW)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    count_min = math.floor(counter / 60)
    count_sec = counter % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    else:
        start_timer()
        tick = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            tick += "✔"
        tick_label.config(text=tick)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 105, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)



timer_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
tick_label = Label(text="✔", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
tick_label.grid(row=4, column=1)


start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)
window.mainloop()