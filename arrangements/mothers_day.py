from arrangement import Arrangement

class Mothers_Day(Arrangement):

    def __init__(self):
        super().__init__()
        self.stem_length = 4
        self.refrigerated = False

    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added

    def enhance(self, flower):
        flower_list = ["rose", "lily", "alstroemeria"]
        if flower.getName() in flower_list.capitalize():
            self.flowers.append(flower)
        else:
            print(f"That flower is not in this bouquet. Please add a flower from {', '.join(flower_list)}.")

new_arrangement = Mothers_Day()
new_arrangement.enhance("rose")




