def run_timing():
    total_time = 0
    num_entries = 0

    while True:
        user_input = input("Enter 10 km run time: ")
        if not user_input:
            break
        total_time += float(user_input)
        num_entries += 1

    average_time = total_time / num_entries
    print(f"Average of {average_time}, over {num_entries} runs")

if __name__ == "__main__":
    run_timing()
