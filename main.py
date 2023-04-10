from KoreanDrama import KoreanDrama

korean_drama_file = open("KoreanDramaList.txt", "r")

# split into each line
lines = korean_drama_file.readlines()
korean_drama_file.close()

# print(lines)

korean_dramas = [] # [][]string

# iterate through list and parse each line (kdrama) into a KoreanDrama object
for line in lines:
    line = line.rstrip()
    templine = line.split("\t")
    korean_dramas.append(KoreanDrama(templine[0], templine[1], templine[2], templine[3]))

# print(korean_dramas)

# get input from user
selected_genre = int(input("What genre of kdrama do you want to watch?\n 6 - Very dramatic\n 5 - Dramatic\n 4 - Mainly serious\n 3 - Mainly funny\n 2 - Lighthearted\n 1 - Very lighthearted\n "))
print("What year range do you prefer?")
selected_min_year = int(input(" From year: "))
selected_max_year = int(input(" To year: "))
selected_score = float(input("What minimum score do you need the recommendation to be?\n Range: 1- 10\n "))


print("Here are some korean drama recommendations: ")

# selected_kdramas = []

for kdrama in korean_dramas:
    if kdrama.genre == selected_genre and kdrama.rating >= selected_score and kdrama.releaseYear >= selected_min_year and kdrama.releaseYear <= selected_max_year:
        print(kdrama)



