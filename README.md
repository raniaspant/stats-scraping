# stats-scraping

If you want to get data from basketball-reference.com, then this is your script to go.

How it works:
* in the script there are three variables: month, day, year. Initialize them as the first day of the NBA season that actually had matches. For the 2017-2018 season, initialized as 10/17/2017
* the seemingly infinite loop breaks when you reach the date you want to stop scraping. It can be the end of the season, or a custom date.
* Opens all matches of all days you entered and puts them in an excel sheet.

Ta-dah. Good to go. Getting the Advanced Stats for each team for a different project I wanted to do, I thought it would help people who want to get data from this website
without having to check out which HTML tags they have to parse.

# Enjoy!
