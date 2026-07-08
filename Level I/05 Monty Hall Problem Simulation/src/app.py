import time
import pandas as pd
import streamlit as st

from src.monty_hall import simulate_game

st.title("Monty Hall Simulation :goat: :blue_car: :goat:")

num_games = st.number_input("Enter of games to simulate",
                            min_value=1, max_value=100000, value=100)


col1, col2 = st.columns(2)

wins_switch = 0
switch_history = []
col1.subheader("Win percentage with switching")
chart1 = col1.empty()


wins_no_switch = 0
no_switch_history = []
col2.subheader("Win percentage without switching")
chart2 = col2.empty()


for i in range(num_games):
    num_wins_with_switching, num_wins_without_switching = simulate_game(1)
    wins_switch += num_wins_with_switching
    wins_no_switch += num_wins_without_switching

    switch_history.append(wins_switch / (i+1))
    no_switch_history.append(wins_no_switch / (i+1))

    data1 = pd.DataFrame({
        "Trial": range(1, len(switch_history) + 1),
        "Switch": switch_history
    })
    data2 = pd.DataFrame({
        "Trial": range(1, len(no_switch_history) + 1),
        "Switch": no_switch_history
    })

    data1 = data1.set_index("Trial")
    chart1.line_chart(data1)
    data2 = data2.set_index("Trial")
    chart2.line_chart(data2)

    time.sleep(0.05)
