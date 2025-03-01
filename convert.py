# Bitdefender Password Manager to Bitwarden csv export conversion tool

# The csv structure of the Bitdefender export is "modelType, modelVersion, title, url, username, password, notes, favorite, totpKey"
# The csv structure to import into Bitwarden is "folder, favorite, type, name, notes, fields, reprompt, login_uri, login_username, login_password, login_totp"
# ^ This may change in the future, make sure to check the current structure of both platforms

# This code is only designed for accounts ("login"). If you wish to import more types of items, "modelType" (row[0]) has to change to whatever matches in the Bitwarden naming conventions

import csv

with open('b.csv', newline='') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',')
    line_count = 0

    for row in fileReader:
        with open('b_out.csv', mode='a') as outfile:
                fileWriter = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if line_count == 0:
                    title = "folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp"
                    fileWriter.writerow(title.split(','))
                else:
                    full_string = f",{row[7]},login,{row[2]},{row[6]},,,{row[3]},{row[4]},{row[5]},{row[8]}"
                    fileWriter.writerow(full_string.split(','))
        line_count += 1

    print(f"Processed {line_count} lines")