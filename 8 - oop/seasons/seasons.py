from datetime import date, datetime
from sys import exit
import inflect

p = inflect.engine()

def main():
    nowdate = datetime.strptime(str(date.today()), "%Y-%m-%d")
    birthdate = datetime.strptime(give_date(input("Date of Birth: ")), "%Y-%m-%d")
    delta = nowdate - birthdate
    days, x = str(delta).split(" ",1)
    totaldays = int(days) * 24 * 60
    print(add_text(totaldays))

def add_text(totaldays):
    words = p.number_to_words(totaldays).replace("and ", "").replace("and", "").replace("thous", "thousand ").replace("thousand ,","thousand,") + " minutes"
    return words.capitalize()

def give_date(date):
    try:
        x,y,z = date.split("-")
        return date
    except:
        exit(1)

if __name__ == "__main__":
    main()