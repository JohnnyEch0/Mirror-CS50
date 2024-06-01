# elif sentence_2.cells.issubset(sentence_.cells):
"""

cells = set()

for cell in sentence_.cells:
    if cell not in sentence_2.cells:
        cells.add(cell)
nu_count = sentence_.count - sentence_2.count
breakp = False
for sentence in self.knowledge:
    
    if sentence.cells == cells and sentence.count == nu_count:
        # print("AI tried to create duplicate knowledge")
        breakp = True
if breakp:
    continue

self.knowledge.append(Sentence(cells=cells, count=nu_count))
knowledge_changed = True

"""


# if sentence_.cells.issubset(sentence_2.cells):
"""

cells = set()
# every cell in sentence2 which isnt in sentence 1
for cell in sentence_2.cells:
    if cell not in sentence_.cells:
        cells.add(cell)
nu_count = sentence_2.count - sentence_.count
breakp = False
for sentence in self.knowledge:
    
    if sentence.cells == cells and sentence.count == nu_count:
        # print("AI tried to create duplicate knowledge")
        breakp = True

if breakp:
    continue
else:
    self.knowledge.append(Sentence(cells=cells, count=nu_count))
    knowledge_changed = True

"""