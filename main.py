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
real_timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global real_timer
    window.after_cancel(real_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="T I M E R")
    global reps
    reps = 0
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    short_brake = SHORT_BREAK_MIN * 60
    long_brake = LONG_BREAK_MIN * 60
    work_time = WORK_MIN * 60

    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_brake)
        timer.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_brake)
        timer.config(text="Short Break", fg="red")
    else:
        count_down(work_time)
        timer.config(text="W o r k", fg="green")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global real_timer
        real_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔️"
        check_mark.config(text=mark)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro Study Technique')
window.config(padx=200, pady=150, bg=YELLOW)

canvas = Canvas(width=222, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Button(command=start_timer)
start.grid(row=2, column=0)
start.config(text="START", font=(FONT_NAME, 15, "bold"))

reset = Button(command=reset_timer)
reset.grid(row=2, column=2)
reset.config(text="RESET", font=(FONT_NAME, 15, "bold"))

check_mark = Label(text="")
check_mark.grid(row=3, column=1)
check_mark.config(font=(FONT_NAME, 10, "normal"), bg=YELLOW, fg=GREEN)

timer = Label(text="T I M E R")
timer.grid(row=0, column=1)
timer.config(font=(FONT_NAME, 35, "italic"), bg=YELLOW)

window.mainloop()
