import pandas as pd
csv_path = "Resources/election_data.csv"
election_df = pd.read_csv(csv_path)

total = election_df["Voter ID"].count()

election_result = election_df["Candidate"].value_counts()
Poll_count_list = election_result.values.tolist()
Candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
Candidate_percent_list = [Poll_count_list[0]/total,
                          Poll_count_list[1]/total,
                          Poll_count_list[2]/total,
                          Poll_count_list[3]/total]

print("Election Result")
print("------------------------")
print(f"Total Votes: {total}")
print("------------------------")
print(f"{Candidate_list[0]}: {Candidate_percent_list[0]}% ({Poll_count_list[0]})")
print(f"{Candidate_list[1]}: {Candidate_percent_list[1]}% ({Poll_count_list[1]})")
print(f"{Candidate_list[2]}: {Candidate_percent_list[2]}% ({Poll_count_list[2]})")
print(f"{Candidate_list[3]}: {Candidate_percent_list[3]}% ({Poll_count_list[3]})")
print("------------------------")
print(f"Winner: {Candidate_list[0]}")
print("------------------------")

f = open("polloutput.txt", "w")
f.write("Election Result")
f.write("------------------------")
f.write(f"Total Votes: {total}")
f.write("------------------------")
f.write(f"{Candidate_list[0]}: {Candidate_percent_list[0]}% ({Poll_count_list[0]})")
f.write(f"{Candidate_list[1]}: {Candidate_percent_list[1]}% ({Poll_count_list[1]})")
f.write(f"{Candidate_list[2]}: {Candidate_percent_list[2]}% ({Poll_count_list[2]})")
f.write(f"{Candidate_list[3]}: {Candidate_percent_list[3]}% ({Poll_count_list[3]})")
f.write("------------------------")
f.write(f"Winner: {Candidate_list[0]}")
f.write("------------------------")