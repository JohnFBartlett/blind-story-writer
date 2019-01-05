import os, sys, json

NOUN_INTERVAL = 3
ADJ_INTERVAL = 2
VERB_INTERVAL = 4
ADV_INTERVAL = 3
# As long as INTERJ interval is 1, it's grouped with entity class
# INTERJ_INTERVAL = 1

def make_story_format(story):
    title = []
    game_text = []
    last_pos = ''
    blank = False
    with open('pos_interface_mappings.json', 'r') as mp:
        pos_map = json.load(mp)
    for i, (word, pos) in enumerate(story):
        # check POS of word
        if pos in {'PERSON', 'ORGANIZATION', 'LOCATION', 'UH'}:
            # If there are two of the same entity tag in a row,
            # it's probably the same entity
            if last_pos == pos:
                blank = True
                continue
            # if title isn't finished and we get to a blank, start it over
            if len(title) < 3:
                title = []
            game_text.append('[' + pos_map.get(pos) + ']')
            blank = True
            last_pos = pos

        elif pos in {'NN', 'NNS'}:
            if i % NOUN_INTERVAL == 0:
                # if title isn't finished and we get to a blank, start it over
                if len(title) < 3:
                    title = []
                game_text.append('[' + pos_map.get(pos) + ']')
                blank = True
            last_pos = pos

        elif pos in {'JJ', 'JJR', 'JJS'}:
            if i % ADJ_INTERVAL == 0:
                # if title isn't finished and we get to a blank, start it over
                if len(title) < 3:
                    title = []
                game_text.append('[' + pos_map.get(pos) + ']')
                blank = True
            last_pos = pos

        elif pos in {'RB', 'RBR', 'RBS'}:
            if i % ADV_INTERVAL == 0:
                # if title isn't finished and we get to a blank, start it over
                if len(title) < 3:
                    title = []
                game_text.append('[' + pos_map.get(pos) + ']')
                blank = True
            last_pos = pos

        elif pos in {'VBP', 'VBD', 'VBG'}:
            if i % VERB_INTERVAL == 0:
                # if title isn't finished and we get to a blank, start it over
                if len(title) < 3:
                    title = []
                game_text.append('[' + pos_map.get(pos) + ']')
                blank = True
            last_pos = pos
        else:
            last_pos = pos

        # If the actual word is being used
        if not blank:
            if len(title) < 3:
                title.append(word)
            game_text.append(word)

        blank = False
    return ' '.join(title) + '\t' + ' '.join(game_text)

def add_stories(story_dir, game_file):
    for filename in os.listdir(story_dir):
        if not filename.startswith('.'):
            print(story_dir+filename)
            with open(story_dir+filename, 'r') as f:
                story_text = [tuple(line.rstrip().split('\t')) for line in f]
            
            formatted_story = make_story_format(story_text)

            with open(game_file, 'a') as out_f:
                out_f.write('\n' + formatted_story)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        story_dir = sys.argv[1]
    else:
        story_dir = './story_files/'

    if len(sys.argv) > 2:
        game_file = sys.argv[2]
    else:
        game_file = './games.txt'

    add_stories(story_dir, game_file)