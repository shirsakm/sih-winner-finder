from bs4 import BeautifulSoup, element
import csv

soup = BeautifulSoup(open("Smart India Hackathon.html"), "html.parser")

problem_statements = open("problemStatements.csv", "r")
ps_reader = csv.reader(problem_statements)

winning_ps = open("winningProblemStatements.csv", "w")
ps_writer = csv.writer(winning_ps)

ps_writer.writerow(["ID", "Title", "Description", "Category", "TB"])

p_ids = soup.find_all("td", {"class": "column2"})
p_ids = [p_id.text for p_id in p_ids]

for ps in ps_reader:
    if ps[0] in p_ids:
        ps_writer.writerow([ps[0], ps[1], ps[4], ps[3], ps[2]])
