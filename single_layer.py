test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]
# A function that iterates over a list
# and replaces characters with nothing(remove characters)
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

# A function that leaves single years or gets the average if the date is a range                      
def process_date(string):
    if len(string) > 4:
        string = string.split("-")
        string = round((int(string[0]) + int(string[1])) / 2)
    else:
        string = int(string)
    return string

#     
processed_test_data = []   
for data in stripped_test_data:
    data = process_date(data)
    processed_test_data.append(data)
    
print(processed_test_data)

#for row in moma:
    #date = row[6]
    #date_one = strip_characters(date)
    #date_two = process_date(date_one)
    #row[6] = date_two
    
#print(moma[2][6])
   
