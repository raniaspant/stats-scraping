import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter


STATS = ["MP", "TS%", "eFG%", "3PAr", "FTr", "ORB%", "DRB%", "TRB%", "AST%", "STL%",
         "BLK%", "TOV%", "USG%", "ORtg", "DRtg"]
'''
workbook = xlsxwriter.Workbook('HollingerData.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
quote_page = 'http://www.espn.com/nba/hollinger/teamstats'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
for tag in soup.findAll('tr'):
    col = 0
    for s in tag.findAll('td'):
        worksheet.write(row, col, s.get_text())
        col += 1
    row += 1
'''
# month = 10
# day = 25
# year = 2016
month = 10
day = 17
year = 2017
origin = 'https://www.basketball-reference.com'
# workbook = xlsxwriter.Workbook('AdvancedStats.xlsx')
workbook = xlsxwriter.Workbook('StatsSoFar.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
statsTeam1 = [None] * len(STATS)
statsTeam2 = [None] * len(STATS)
while True:
    if month == 13:
        year += 1
        month = 1
    # if month == 6 and day == 13:
    #    break
    if month == 12 and day == 2:
        break
    quote_page = 'https://www.basketball-reference.com/boxscores/?month='+str(month)+'&day='+str(day)+'&year='+str(year)
    # print(quote_page)
    page = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    # at this point we have the new page with the box score for each match
    for tag in soup.findAll('div', class_='game_summary expanded nohover'):
        # print(tag.get_text())
        for link in tag.findAll('a', href=True, text='Box Score'):
            boxScoreLink = origin + link['href']
            pageAttributes = urllib.request.urlopen(boxScoreLink)
            soupAttributes = BeautifulSoup(pageAttributes, 'html.parser')
            team1, team2 = soupAttributes.find('h1').get_text().split(" at ")
            team2, garbage = team2.split(" Box Score")
            count = 0
            for tagAttr in soupAttributes.findAll('tfoot'):
                # print(tagAttr.get_text())
                i = 0
                for stat in tagAttr.findAll('td'):
                    if count == 1:                # fetch advanced stats only
                        statsTeam1[i] = stat.get_text()
                    if count == 3:
                        statsTeam2[i] = stat.get_text()
                    i += 1
                count += 1

            date = str(day) + "/" + str(month) + "/" + str(year)
            worksheet.write(row, 0, team1)
            worksheet.write(row, 1, team2)
            worksheet.write(row, 2, date)
            row += 1
            for j in range(0, 3):
                col = 0
                for i in range(0, len(STATS)):
                    if j == 0:
                        worksheet.write(row, col, STATS[i])
                    if j == 1:
                        worksheet.write(row, col, statsTeam1[i])
                    if j == 2:
                        worksheet.write(row, col, statsTeam2[i])
                    col += 1
                row += 1
    print(date)     # debug
    day += 1
    if day == 31:
        month += 1
        day = 1

