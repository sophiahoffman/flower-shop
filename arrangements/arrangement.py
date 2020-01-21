class Arrangement:

    def __init__(self):
        self.__flowers = []
        self.description = ""

    def enhance(self, flower):
        self.__flowers.append(flower)

    @property
    def flowers(self):
        return self.__flowers

    @flowers.setter
    def flowers(self, *args):
        self.__flowers = args
        return sel.__flowers