import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
word = input("Enter the word: ").lower()
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression LIKE '%{}%'".format(word[1:3]))
    patterns = cursor.fetchall()
    newres = []
    
    if patterns:
        for pattern in patterns:
            newres.append(pattern[0].lower())
        results = get_close_matches(word, newres, n=1)

    if len(results) > 0:
        yn = input("Did you mean '%s' instead? Y for yes, N for No: " % results[0])
        if yn in ("YES", "Yes", "yes", "yES", "Y", "y"):
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}'".format(results[0]))
            results = cursor.fetchall()
            for result in results:
                print(result[0])
        elif yn in ("NO", "No", "no", "nO", "N", "n"):
            print("The word \"%s\" doesn't exist in the dictionary" % word)
        else:
            print("Entry is not understood :(")
    else:
        print("The word \"%s\" doesn't exist in the dictionary" % word)


    


