# blind-story-writer
NLP mad libs implementation with tkinter GUI written in Python3

This application lets you play a madlibs-like game by filling in blanks from essays taken the [Cornell RACE corpus](https://arxiv.org/abs/1704.04683). Blanks are created and labeled using the POS Tagger and StanfordNERTagger from nltk.

# Implementation
Tokens in the essays are tagged with the following tagset, then blanks of each kind of tag are inserted into the story at varying intervals.
Story titles are automatically created by taking the first three non-blank words with semantically significant tags.

# Running the Project
As it is, you can run the game with the provided story templates with the following command:
```
python3 story_interface.py
```

### If you want to create your own story templates, follow these steps:
1. Extract and tag stories from the corpus: `python3 story_labeler.py [CORPUS_PATH] [LABELED_STORY_DIR]`
2. If you want, modify blank intervals by POS at the top of `python3 add_stories.py`
3. Add stories to game file (currently games.txt): `python3 add_stories.py [LABELED_STORY_DIR] [GAMES_FILE]`
4. Run game with your new templates: `python3 story_interface.py`
