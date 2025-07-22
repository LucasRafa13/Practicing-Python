from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# Colors
color1 = "#3b3b3b"  # Dark Gray
color2 = "#333333"  # Darker Gray
color3 = "#ffffff"  # White
color4 = "#fcc058"  # Orange

window = Tk()
window.title("Age Calculator")
window.geometry("310x410")
window.configure(bg=color1)

style = ttk.Style(window)
style.theme_use("clam")

# Frames
top_frame = Frame(
    window, width=310, height=140, pady=0, padx=0, relief="flat", bg=color2
)
top_frame.grid(row=0, column=0)
bottom_frame = Frame(
    window, width=310, height=410, pady=0, padx=0, relief="flat", bg=color1
)
bottom_frame.grid(row=1, column=0, sticky=NW)

# Labels Top Frame
app_calculator = Label(
    top_frame,
    text="Age Calculator",
    width=25,
    height=1,
    padx=3,
    relief="flat",
    anchor="center",
    font=("Ivy 15 bold"),
    bg=color2,
    fg=color3,
)
app_calculator.place(x=0, y=30)


app_of_range = Label(
    top_frame,
    text="Age",
    width=11,
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Arial 35 bold"),
    bg=color2,
    fg=color4,
)
app_of_range.place(x=0, y=70)

# Labels Bottom Frame

initial_date = Label(
    bottom_frame,
    text="Current Date",
    height=1,
    padx=0,
    pady=0,
    relief="flat",
    anchor=NW,
    font=("Ivy 9"),
    bg=color1,
    fg=color3,
)
initial_date.place(x=50, y=30)

cal_initial_date = DateEntry(
    bottom_frame,
    width=10,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="dd/mm/yyyy",
    year=2025,
)
cal_initial_date.place(x=170, y=30)

birth_date = Label(
    bottom_frame,
    text="Birth Date",
    height=1,
    padx=0,
    pady=0,
    relief="flat",
    anchor=NW,
    font=("Ivy 9"),
    bg=color1,
    fg=color3,
)
birth_date.place(x=50, y=70)

cal_birth_date = DateEntry(
    bottom_frame,
    width=10,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="dd/mm/yyyy",
    year=2000,
)
cal_birth_date.place(x=170, y=70)

app_years = Label(
    bottom_frame,
    text="",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 25 bold"),
    bg=color1,
    fg=color3,
)
app_years.place(x=60, y=135)

app_label_years = Label(
    bottom_frame,
    text="Years",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_years.place(x=50, y=175)

app_months = Label(
    bottom_frame,
    text="",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 12 bold"),
    bg=color1,
    fg=color3,
)
app_months.place(x=140, y=135)

app_label_months = Label(
    bottom_frame,
    text="Months",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_months.place(x=130, y=175)

app_days = Label(
    bottom_frame,
    text="",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 12 bold"),
    bg=color1,
    fg=color3,
)
app_days.place(x=220, y=135)

app_label_days = Label(
    bottom_frame,
    text="Days",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_days.place(x=210, y=175)


# Function to calculate age
def calculate_age():
    initial_date_str = cal_initial_date.get()
    birth_date_str = cal_birth_date.get()

    day_1, month_1, year_1 = [int(f) for f in initial_date_str.split("/")]
    initial_date = date(year_1, month_1, day_1)

    day_2, month_2, year_2 = [int(f) for f in birth_date_str.split("/")]
    birth_date = date(year_2, month_2, day_2)

    years = relativedelta(initial_date, birth_date).years
    months = relativedelta(initial_date, birth_date).months
    days = relativedelta(initial_date, birth_date).days

    app_years["text"] = years
    app_months["text"] = months
    app_days["text"] = days


# Calculate Button

b_calculate_age = Button(
    bottom_frame,
    text="Calculate Age",
    width=20,
    height=1,
    bg=color1,
    fg=color3,
    font=("Ivy 10 bold"),
    relief="raised",
    overrelief="ridge",
    command=calculate_age,
)
b_calculate_age.place(x=60, y=225)

window.mainloop()
