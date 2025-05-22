
def greeting():
    print("This is your very own perfume journal, follow instructions to personalise:)")
    name = input(" Enter your name to personalise your journal!")
    Welcome = print(f"Welcome to Your own Perfume Journal {name}") 
    print(Welcome)

greeting()

Fragrance_Notes = (" Fragrances composed of notes that smell ")
Frag_Family =["Fresh","Gourmand","Floral","Woody","Oriental"]


Scent_Names ={
    "Fr" : "refreshing effervescent scents, e.g Laundry, Musk, Citrus Aquatic.",
    "Gour" :"edible scents, e.g Vanilla, Cake,Caramel, Cacao etc",
    "Flo" : "powdery and like flowers e.g Rose, Lily of the Valley, Orange Blossom.",
    "Woody" : "earthy, aromatic e.g Sandalwood, Vertiver, Oud.",
    "Ori" : "exotic, warm and spicy, e.g Oud,Cinnamon, Mrryh,Resin."}


Fragrance_Catalogue ={
"Fresh_Descript" : f"Fresh:{Fragrance_Notes} Scent_Names[Fr]",
"Gourmand_Descript" : f"Gourmand:{Fragrance_Notes} Scent_Names[Gour]",
"Floral_Descript" : f"Floral:{Fragrance_Notes} Scent_Names[Flo]",
"Woody_Descript" : f"Woody:{Fragrance_Notes} Scent_Names[Woody]",
"Oriental_Descript" : f"Oriental{Fragrance_Notes} Scent_Names[Ori]"}

print("Here is our mini fragrance family catalog that will explain the main fragrance types based upo notes, this will help in creating a tailor Scent Profile to your taste.")
Fragrance_Catalogue() 

quiz_0 = input("Now you have a little bit more information about the types of fragrance families, are you now ready to take a mini quiz?")
print(quiz_0)

while quiz_0.lower != "yes":
    print("Please enter yes")
if quiz_0.lower() == "yes":
    exit

x ={
1 : "Absolute Fav",
2 : " Frequent Go-To",
3 : "Mood Based Choice",
4 : "Occasional Preferance",
5 : "Least Preferred"}


for var in Frag_Family:
    rank = int(input(f"Enter your ranking for each scent fanily in order of most liked to least liked, 1 = most liked & 5 = least liked:{var}"))
    

quiz ={
    "intro" : "Welcome to the mini quiz that will help personalise your profile, please answer the following questions?",
    "Username" : "Enter a username of your choice?",
    "Age" : "How old are you?",
   "Gender" : "Enter your Gender: Man,Woman, Non-Binary, Prefer not to Answer.",
    "Animal" : "Do you prefer cats or dogs?",
    "Profile Icon" : "Do you prefer bunnies or {Animal}?",
    "Scent Pref" : f"Rank the scent profiles from the Fragrance Catalog,{rank}",
    "Fav Season" : "What is your favorite season from the following: Winter,Summer,Autumn/Fall or Spring?",
    "Least Fav" : "What is your least favourite season from the following?",
    "Display Mode" : "Would you like your display to be in: Lightmode,Darkmode or Pinkmode?"}

scent_preference = { 
    x[rank]: None for rank in x}



def scent_rank():
    
    for quiz["Scent Pref"] in quiz.items():

        for var in Frag_Family:
            quiz.get("Scent Pref", {}).get(var) = rank
            scent_preference[rank][var] = rank_description
            rank_description = x.get(rank, "Unknown Ranking")

    


profile = {}

for key, quiz in quiz.items():
    q_input = quiz.format(**profile)
    profile[key] = input(q_input + "")


     

def create_profile():
    print("/n--Your Profile--")
    print(profile)
    print(scent_preference)

create_profile()