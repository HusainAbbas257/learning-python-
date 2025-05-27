import csv
# .csv files are like excel but just with a bunch of commas and confusion
# thses are opened in a similiar way as a .txt file:

data=[
    ['item','quantity','price'],
    ['chips',2,10],
    ['bitcuits',3,15]
    ]
# we can write into this by :
with open('expences.csv','w',newline='') as file:
    wr=csv.writer(file)
    wr.writerows(data)

# we can also read from it as:
with open('expences.csv','r') as file:
    rd=csv.reader(file)
    # rd is an iterable of all rows
    for rows in rd:
        print(rows)

# we can write a single rows at a time also:

with open('expences.csv','w',newline='') as file:
    wr=csv.writer(file)
    for item in data:
        wr.writerow(item)

#we can also write by dictoinaries
players = [
    {"Name": "Kumail", "Level": 16, "Power": 420},
    {"Name": "Naruto", "Level": 99, "Power": 9001},
    {"Name": "Itachi", "Level": 85, "Power": 8800}
]

with open("players.csv", "w", newline='') as file:
    fields = ["Name", "Level", "Power"]  # Header order
    writer = csv.DictWriter(file, fieldnames=fields)
    
    writer.writeheader()      # Write header row
    writer.writerows(players) # Write data rows


# we can also read them as dictionaries:
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)



# dont forget the append mode its also very usefull sometimes like adding data:
with open("players.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Level", "Power"])
    # NO writeheader() here or you'll mess up your CSV and look like an idiot
    new_player = {"Name": "Madara", "Level": 99, "Power": 9999}
    writer.writerow(new_player)