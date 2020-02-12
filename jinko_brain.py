import json
import datetime
import os
# Classes
class Brain:
    def __init__(self, ego, concepts, people, things, language, past_messages):
        self.version = "Alpha 1 Brain"
        self.limit = 5001
        f = open(ego, 'r')
        self.ego = json.load(f)
        f.close()
        f = open(concepts, 'r')
        self.concepts = json.load(f)
        f.close()
        f = open(people, 'r')
        self.people = json.load(f)
        f.close()
        f = open(things, 'r')
        self.things = json.load(f)
        f.close()
        f = open(language, 'r')
        self.language = json.load(f)
        f.close()
        f = open(past_messages, 'r')
        self.past_messages = json.load(f)
        f.close()
        print(self.version)

    def save_all(self):
        current_time = datetime.datetime.utcnow()
        foldername = f"data{current_time.second}-{current_time.minute}-{current_time.hour}-{current_time.day}-{current_time.month}-{current_time.year}"
        os.mkdir(foldername)
        f = open(f'{foldername}/ego.json', 'w')
        json.dump(self.ego, f, ensure_ascii=True, indent=4)
        f.close()
        f = open(f'{foldername}/concepts.json', 'w')
        json.dump(self.concepts, f, ensure_ascii=True, indent=4)
        f.close()
        f = open(f'{foldername}/people.json', 'w')
        json.dump(self.people, f, ensure_ascii=True, indent=4)
        f.close()
        f = open(f'{foldername}/things.json', 'w')
        json.dump(self.things, f, ensure_ascii=True, indent=4)
        f.close()
        f = open(f'{foldername}/language.json', 'w')
        json.dump(self.language, f, ensure_ascii=True, indent=4)
        f.close()
        f = open(f'{foldername}/past_messages.json', 'w')
        json.dump(self.past_messages, f, ensure_ascii=True, indent=4)
        f.close()
        print('saved all dicts to json files')
    
    def save(self, data_to_save):
        if data_to_save == "past_messages":
            f = open('past_messages.json', 'w')
            json.dump(self.past_messages, f, ensure_ascii=True, indent=4)
            f.close()
        elif data_to_save == "people":
            f = open('people.json', 'w')
            json.dump(self.people, ensure_ascii=True, indent=4)
            f.close()
        
    
    def Compare(self, str1, str2):
        similar = 0
        ran = 0
        if len(str1) <= len(str2):
            ran = len(str1)
        else:
            ran = len(str2)
        for i in range(0, ran):
            if str2[i] == str1[i]:
                similar += 1
        
        if similar >= 0.70 * ran:
            return True
        else:
            return False

if __name__ == '__main__':
    big = Brain('ego.json','concepts.json', 'people.json', 'things.json', 'language.json', 'past_messages.json')
    big.save_all()
    print(big.Compare("nor", "or"))