import os, sys, nltk, json
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def label_corpus(corpus, out_dir):
    for filename in os.listdir(corpus):
        print(corpus+filename)
        if filename[0] != '.':
            with open(corpus+filename, 'r') as f:
                text = f.read()
                article_text = json.loads(text)['article']
                print(article_text)
            labeled_text = label_text(article_text)
            with open(out_dir+filename, 'w') as out_f:
                [out_f.write(tup[0] + '\t' + tup[1] + '\n') for tup in labeled_text]



def label_text(text):
    labeled_text = text

    # first tokenize
    tokenized = nltk.word_tokenize(text)
    pruned_tokens = []
    print(tokenized)
    for token in tokenized:
        # check for no spaces around period
        parts = token.split('.')
        if token != '.' and len(parts) > 1:
            print("From token: " + token)
            print("Split parts: " + str(parts))
            for i, part in enumerate(parts):
                if part != '':
                    pruned_tokens.append(part)
                    if i < len(parts) - 1:
                        pruned_tokens.append('.')
                else:
                    if len(pruned_tokens) >= 1:
                        pruned_tokens[-1] += '.'
                    else:
                        pruned_tokens[0] = '.'
        else:
            pruned_tokens.append(token)
    
    # then do POS tagging
    pos_tagged = nltk.pos_tag(pruned_tokens)

    # do NER tagging in a separate list
    # st = StanfordNERTagger('/usr/local/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
    #                    '/usr/local/stanford-ner/stanford-ner.jar',
    #                    encoding='utf-8')
    # ner_tagged = st.tag(tokenized)
    st = nltk.tag.stanford.StanfordNERTagger('/usr/local/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/usr/local/stanford-ner/stanford-ner.jar',
                        encoding='utf-8')

    ner_tagged = st.tag(pruned_tokens)

    # if NER tag is present at a given index, replace POS tag with it
    labeled_text = [tag if ner_tagged[i][1] == 'O' else ner_tagged[i] for i, tag in enumerate(pos_tagged)]

    return labeled_text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        corpus = sys.argv[1]
    else:
        corpus = './RACE/train/middle/'

    if len(sys.argv) > 2:
        out_dir = sys.argv[2]
    else:
        out_dir = './story_files/'

    label_corpus(corpus, out_dir)