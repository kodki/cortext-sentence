import cortext_sentence.parser
import cortext_sentence.visualizer


def visualize(sentence):
    tagged = cortext_sentence.parser.parse(sentence)
    visualizer = cortext_sentence.visualizer.Visualizer(tagged)
    return visualizer.visualize()
