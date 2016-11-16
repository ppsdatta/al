"""
AL the guy
"""

from textblob.classifiers import NaiveBayesClassifier

class AL:
    class AL_Guy:
        "Secret inner class"
        def __init__(self):
            self.classifier = None
            self.action_map = dict()
            self.reveries = None
            self.jokes = None
            self.training_data = None
            self.converted_training_data = []

        def train(self, training_data):
            self.training_data = training_data
            for k in self.training_data.keys():
                tag = k
                tag_data = self.training_data[tag]
                self.action_map[tag] = tag_data['action']
                for d in tag_data['training_data']:
                    self.converted_training_data.append((d, tag))
            self.classifier = NaiveBayesClassifier(self.converted_training_data)

        def respond(self, data):
            action_class = self.classifier.classify(data)
            if action_class in self.action_map:
                return self.action_map[action_class](data)

            return 'Don\'t look like anything to me.... (Let me call Bernard, head of programming WW)'

    __instance = None

    def __init__(self):
        if AL.__instance is None:
            AL.__instance = AL.AL_Guy()

    def get(self):
        return AL.__instance

