import jinko_brain
from jinko_brain import Brain

class Jinko:
    def __init__(self, brain):
        self.ego = {}
        self.brain = brain
        self.name = brain.ego["name"]
        self.likes = brain.ego["likes"]
        self.things = brain.things
        self.dislikes = brain.ego["dislikes"]
        self.mood = brain.ego["mood"]
    
    def processMessage(self, author, message):
        known = self.likes + self.dislikes + self.brain.ego["friends"]
        #print(known)
        for word in message:
            for k in known:
                if self.brain.Compare(word, k):
                    if k in self.likes:
                        return f"I like {word}."
                    elif k in self.dislikes:
                        return f"I don't like {word}."
                    elif k in self.brain.ego["friends"]:
                        return f"I am friends with {word}!"
                    else:
                        if mood == 'curious':
                            return f"what is {word}? Please explain it to me, I don't understand..."
        
        if author not in self.brain.people:
            self.brain.people.append(author)
            self.brain.save_all()
        return ""        

    def remember(self, dict_of_message):
        self.brain.past_messages.append(dict_of_message)
        self.brain.save("past_messages")
    
    def __str__(self):
        return f"{self.name}, {self.likes}, {self.dislikes}"




if __name__ == '__main__':
    brain = Brain('ego.json', 'concepts.json', 'people.json', 'things.json', 'language.json', 'past_messages.json')

    #print(brain.concepts)

    #jinko = {"class":"Person", "name":"Jinko", "likes":["rabbit", "squirrel", "acorn", "cirno", "cas", "pizza", "likes"], "dislikes":["swears", "shadow the hedgehog", "pain", "dislikes"], "friends":["cirno", "kiyo", "snek", "lollernoob9"], "enemies":[], "mood":"waking", "isFriend":True, "discord_names":["Jinko-chan-00"]}
    #print(jinko)
    #print(brain.ego)
    jinko = Jinko(brain)
    #print(jinko)
    print(jinko.brain.Compare("rabbit", "rabbits"))
    print(jinko.likes)
    print(jinko.likes.append("spaghetti"))
    print(jinko.likes)
    print(jinko.brain.Compare("spaghet", "spaghetti"))
    print(jinko.brain.things)
    print(jinko.processMessage(["birbs"]))
    print(jinko.processMessage(["penis"]))
