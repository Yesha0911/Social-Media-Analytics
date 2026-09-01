import os

print(os.getcwd())
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV File
data = pd.read_csv("sma.csv")

while True:

    print("\n===== Social Media Analytics Tool =====")
    print("1. Show complete data")
    print("2. Show total likes")
    print("3. Show total comments")
    print("4. Show total shares")
    print("5. Show highest likes user")
    print("6. Show lowest likes user")
    print("7. Show average likes")
    print("8. Show bar graph individual")
    print("9. Show bar graph overall")
    print("10. Show combined bar graph")
    print("11. Search by user")
    print("12. Exit")

    choice = int(input("Enter your choice (1-12): "))

    if choice == 1:
        print("\nComplete data:")
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
        print("\nAverage Likes:", round(data["Likes"].mean(), 2))

    elif choice == 8:
        # Top 10 posts for a readable graph
        top10 = data.nlargest(10, "Likes")

        plt.figure(figsize=(10, 6))
        plt.bar(top10["User"], top10["Likes"])

        plt.title("Top 10 Posts by Likes")
        plt.xlabel("Users")
        plt.ylabel("Likes")

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    elif choice == 9:
        plt.figure(figsize=(7, 5))

        plt.bar(
            ["Likes", "Comments", "Shares"],
            [
                data["Likes"].sum(),
                data["Comments"].sum(),
                data["Shares"].sum()
            ]
        )

        plt.title("Overall Social Media Engagement")
        plt.xlabel("Category")
        plt.ylabel("Total Count")

        plt.tight_layout()
        plt.show()

    elif choice == 10:
        # Top 10 posts to avoid overlapping labels
        top10 = data.nlargest(10, "Likes")

        x = np.arange(len(top10["User"]))
        width = 0.25

        plt.figure(figsize=(12, 6))

        plt.bar(
            x - width,
            top10["Likes"],
            width,
            label="Likes"
        )

        plt.bar(
            x,
            top10["Comments"],
            width,
            label="Comments"
        )

        plt.bar(
            x + width,
            top10["Shares"],
            width,
            label="Shares"
        )

        plt.xticks(
            x,
            top10["User"],
            rotation=45,
            ha="right"
        )

        plt.title("Top 10 Posts: Likes, Comments and Shares")
        plt.xlabel("Users")
        plt.ylabel("Count")
        plt.legend()

        plt.tight_layout()
        plt.show()

    elif choice == 11:
        name = input("Enter User Name: ")

        user = data[data["User"].str.lower() == name.lower()]

        if not user.empty:
            print("\nUser Details:")
            print(user)
        else:
            print("User not found!")

    elif choice == 12:
        print("\nThank you for using Social Media Analytics Tool")
        break

    else:
        print("\nInvalid Choice! Please enter a number between 1 and 12")
