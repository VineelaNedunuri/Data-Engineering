# Exercise 0 - Bash commands

Use windows for linux (WSL), ubuntu bash, git bash or terminal in mac to solve all these exercises, **don’t use GUI**. A lot of the training in these exercises are both to search up commands and also to understand the computer science terminology.

**Tips**: work with exercise X alongside with other exercises.

---

## 0. Setup a git repository (\*)

a) Make a directory called Linux-training.

```bash
mkdir Linux-training
```

b) Create the files called

```bash
“note1.txt”, “note2.txt”, “note3.txt”, “note4"
```
```bash
touch note{1..3}.txt
touch note4
```

---

## 1. Navigating and moving (\*)

a) Make a subdirectory called cool_notes

```bash
mkdir Linux-training/cool_notes
```

b) Move all .txt files into cool_notes

```bash
mv Linux-training/*.txt Linux-training/cool_notes

```

c) Delete note4

```bash
rm Linux-training/note4
```

d) Change directory to cool_notes and list all the files there

```bash
cd Linux-training/cool_notes
ls
```

e) Move note3.txt out from cool_notes into parent directory

```bash
mv note3.txt ../note3.txt
```

f) Navigate to parent directory

```bash
cd ..

```

g) From here list all files including hidden files

```bash
ls -a

```

h) Change name on note3.txt to note_home.txt

```bash
mv note3.txt note_home.txt

```

---

## 2. Printing, variables and manipulating text (\*)

a) Print out “hello from note_home” into bash

```bash
echo "hello from note_home"

```

b) Write this text string into note_home.txt

```bash
echo "hello from note_home" > note_home.txt

```

c) Print out the “current path is: <your current directory path>” in bash

```bash
echo "current path is: $(pwd)"

```

d) Write this string into note_home in a new line so it should contain

```bash
hello from note_home
current_directory is: <your current directory path>
```

```bash
echo -e "\ncurrent path is: $(pwd)" >> note_home.txt

```
e) Print out the content of the note_home.txt

```bash
cat note_home.txt
```

f) Count the number of words in this file

```bash
wc -w note_home.txt

```

g) Count the number of lines in this file


```bash
wc -l note_home.txt

```

h) Count the number of files in cool_notes

```bash
ls -1 cool_notes | wc -l

```

i) Check the disk usage in your directory and make the format human readable

```bash
du -h
```

---

## 3. Pokeventure (\*)

a) Create a folder called data with a subfolder called pokemons

```bash
mkdir data
mkdir data/pokemons

```

b) Create a file called pokemon_list.txt

```bash
touch data/pokemon_list.txt

```

c) Type in a random list of pokemons, using echo and the bitshift operator

for example:

```bash
pikachu
voltorb
bulbasaur
mew
zapdos
mewtwo
```

```bash
echo "
pikachu
voltorb
bulbasaur
mew
zapdos
mewtwo" > data/pokemon_list.txt
```

d) Loop through your file and print out the following

```bash
pokemon: pikachu
pokemon: voltorb
pokemon: bulbasaur
pokemon: mew
pokemon: zapdos
pokemon: mewtwo
```

```bash
while read -r line; do
   echo "pokemon: $line";
done < data/pokemon_list.txt
  
```

e) Now test out the following api manually in your browser [https://pokeapi.co/api/v2/pokemon-species/voltorb](https://pokeapi.co/api/v2/pokemon-species/voltorb)


f) Now test it out using bash, and see that it prints out the same results

```bash
curl https://pokeapi.co/api/v2/pokemon-species/voltorb
 
```

g) Do a for loop on pokemon_list.txt, pick the pokemons on the file and request the api. Save each pokemon into their respective json file. Important: add a pause of 2 seconds after each iteration. Your structure should look something like this now.

```bash
└── data
    └── pokemons
        ├── bulbasaur.json
        ├── mew.json
        ├── mewtwo.json
        ├── pikachu.json
        ├── pokemon_list.txt
        ├── voltorb.json
        └── zapdos.json
```

h) Remove all files ending with .json using one command

i) Now move yourself to the same level, i.e. sibling to data directory. Create a bash script file called download_pokemons.sh. Put in bash logic for downloading the pokemons specified in data/pokemon/pokemon_list.txt file and saving it into data/pokemons/ and run it. Your file structure might look like this now. (\*\*)

```bash
├── data
│   └── pokemons
│       ├── bulbasaur.json
│       ├── mew.json
│       ├── mewtwo.json
│       ├── pikachu.json
│       ├── pokemon_list.txt
│       ├── voltorb.json
│       └── zapdos.json
└── download_pokemons.sh
```

---

## X. Commands glossary (\*)

Fill in this table. You can do this in any application, it might be too hardcore to do this with terminal only. Tips you can use man command to check documentation. Also try out the different commands to see them in action.

| Command | What does the command do | Some useful options |
| ------- | ------------------------ | ------------------- |
| cd      |                          |                     |
| ls      |                          |                     |
| touch   |                          |                     |
| wc      |                          |                     |
| grep    |                          |                     |
| mkdir   |                          |                     |
| mv      |                          |                     |
| rm      |                          |                     |
| rmdir   |                          |                     |
| ssh     |                          |                     |
| curl    |                          |                     |
| sudo    |                          |                     |
| apt-get |                          |                     |
| ps      |                          |                     |
| cp      |                          |                     |
| less    |                          |                     |
| top     |                          |                     |
| head    |                          |                     |
| echo    |                          |                     |
| cat     |                          |                     |
| chmod   |                          |                     |
| chown   |                          |                     |
| kill    |                          |                     |
| &&      |                          |                     |
| wget    |                          |                     |
| pwd     |                          |                     |
| >>      |                          |                     |
| >       |                          |                     |
| \*      |                          |                     |
| ./      |                          |                     |
| diff    |                          |                     |
| find    |                          |                     |
