import pandas as pd
csv_path = "Resources/budget_data.csv"
budget_df = pd.read_csv(csv_path)
budget_df.count()
PL1 = budget_df["Profit/Losses"].values.tolist()
PL1.insert(0, 0)
PL1.pop()

budget_df["Prior Period"] = PL1
budget_df["Change"] = budget_df["Profit/Losses"] - budget_df["Prior Period"]
max_change=budget_df["Change"].max()
min_change=budget_df["Change"].min()
IncProf = budget_df.loc[budget_df["Change"] == budget_df["Change"].max(), "Date"].values.tolist()
DecLoss = budget_df.loc[budget_df["Change"] == budget_df["Change"].min(), "Date"].values.tolist()

print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {budget_df['Date'].count()}")
print(f"Total: {budget_df['Profit/Losses'].sum()}")
print(f"Average Change: {budget_df['Change'].mean()}")
print(f"Greatest Increase in Profits: {IncProf[0]} ({max_change})")
print(f"Greatest Decrease in Profits: {DecLoss[0]} ({min_change})")
      
f = open("bankoutput.txt", "w")
f.write("Financial Analysis\n")
f.write("------------------------------------------\n")
f.write(f"Total Months: {budget_df['Date'].count()}\n")
f.write(f"Total: {budget_df['Profit/Losses'].sum()}\n")
f.write(f"Average Change: {budget_df['Change'].mean()}\n")
f.write(f"Greatest Increase in Profits: {IncProf[0]} ({max_change})\n")
f.write(f"Greatest Decrease in Profits: {DecLoss[0]} ({min_change})\n")