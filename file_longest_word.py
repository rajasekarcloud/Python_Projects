# Challenge: Find the Longest Word in a File
file_name="words.txt";
temp=0;
with open(file_name) as file:
    for i in file.readlines():
        if len(i.rstrip("\n")) > temp:
            temp = len(i.rstrip("\n"));
            long_word = i.rstrip("\n");
    print(f'Longest Word is {long_word} and it has {temp} letters.');
