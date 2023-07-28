# Challenge: Make Frequency Dictionary of the Words in a File
# If the text file has these words:
# switch
# concert
# contradiction
# offset
# power
# concert
# concert
# offset
# {"switch": 1, "concert": 3, "contradiction": 1, "offset": 2, "power": 1}
file_name="words1.txt";
dict = {};
with open(file_name) as file:
    for i in file.readlines():
        temp = i.strip("\n");
        if temp not in dict:
            dict[temp] = 1;
        else:
            dict[temp] += 1;
    print(dict);

