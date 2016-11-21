"""
AL the guy
"""

from textblob.classifiers import DecisionTreeClassifier, NaiveBayesClassifier
from textblob import TextBlob


def cmd_extractor(document):
    blob = TextBlob(document)
    tags = blob.pos_tags
    features = {}
    if len(tags) > 0:
        first_tag = tags[0]
        if first_tag[1] == 'VB':
            if (('card', 'RB') in tags):
                features['contains(my_cards)'] = True
            elif (('joke', 'NN') in tags):
                features['contains(joke)'] = True
        else:
            features['contains(blank)'] = True
    return features


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
            self.classifier = NaiveBayesClassifier(self.converted_training_data)    #, feature_extractor=cmd_extractor)

        def respond(self, data):
            action_class = self.classifier.classify(data)
            #self.classifier.show_informative_features(5)
            if action_class in self.action_map:
                return self.action_map[action_class](data)

            return 'Don\'t look like anything to me.... (Let me call Bernard, head of programming WW)'

    __instance = None

    def __init__(self):
        if AL.__instance is None:
            AL.__instance = AL.AL_Guy()

    def get(self):
        return AL.__instance

