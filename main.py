import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
data = pd.read_csv("sma.csv")

while True:

    print("\n===== Social Media Analytics Tool =====")
    print("1. Show Complete Data")
    print("2. Show Total Likes")
    print("3. Show Total Comments")
    print("4. Show Total Shares")
    print("5. Show Highest Likes User")
    print("6. Show Lowest Likes User")
    print("7. Show Average Likes")
    print("8. Show Bar Graph")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        print("\nComplete Data:")
        print(data)

    elif choice == 2:
        print("\nTotal Likes:", data["Likes"].sum())

    elif choice == 3:
        print("\nTotal Comments:", data["Comments"].sum())

    elif choice == 4:
        print("\nTotal Shares:", data["Shares"].sum())

    elif choice == 5:
        top_user = data.loc[data["Likes"].idxmax()]
        print("\nTop User:", top_user["User"])
        print("Highest Likes:", top_user["Likes"])

    elif choice == 6:
        low_user = data.loc[data["Likes"].idxmin()]
        print("\nUser:", low_user["User"])
        print("Lowest Likes:", low_user["Likes"])

    elif choice == 7:
        print("\nAverage Likes:", data["Likes"].mean())

    elif choice == 8:
        plt.bar(data["User"], data["Likes"])
        plt.title("Users Likes")
        plt.xlabel("Users")
        plt.ylabel("Likes")
        plt.show()

    elif choice == 9:
        print("\nThank you for using Social Media Analytics Tool!")
        break

    else:
        print("\nInvalid Choice! Please enter a number between 1 and 9.")