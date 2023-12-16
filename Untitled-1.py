
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLineEdit, QListWidget, QHBoxLayout, QVBoxLayout, QInputDialog, QMessageBox

import json

app = QApplication([])
window = QWidget()

text =  QTextEdit()
lineText = QLineEdit()

list = QListWidget()
tags_list = QListWidget()

main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

btn_create = QPushButton('Create')
btn_save = QPushButton('Save')
btn_delete = QPushButton('Delete')
btn_searchTag = QPushButton('Search tag')
btn_addTag = QPushButton('Create tag')
btn_deleteTag = QPushButton('Delete tag')
added_notes = {}


def show_note():
    note_name = list.currentItem().text()
    text.setText(added_notes[note_name]['text'])

    tags_list.clear()
    tags_list.addItems(added_notes[note_name]['tags'])

def write_file():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(added_notes, file, ensure_ascii=True, sort_keys=True, indent=4)


def Save_note():
    try:
        n = text.toPlainText()
        note_name = list.currentItem().text()
        
        added_notes[note_name]['text'] = n
        write_file()
        
    except:
            msg = QMessageBox(window, text ="Chose the file, please.")
            msg.show()
            msg.setStyleSheet('''background-color: #fafafa;
''')
    print(n)


def add_note():
    note_check, ok = QInputDialog.getText(window, 'Нова замітка', 'Назва замітки')
    if ok and note_check != "":
        added_notes[note_check] = {
            "text": "",
            "tags": [],
        }
        list.addItem(note_check)
def delete_note():
    current_item = list.currentItem()
    if current_item is not None:
        note_name = current_item.text()
        del added_notes[note_name]
        list.takeItem(list.row(current_item))
        write_file()

    write_file()

list.itemClicked.connect(show_note)


with open('notes.json', 'r', encoding='utf-8') as file:
    added_notes = json.load(file)
list.addItems(added_notes)

def add_tag():
    note = list.currentItem().text()
    tag = lineText.text()
    print(tag)
    added_notes[note]["tags"].append(tag)
    tags_list.addItem(tag)
    write_file()
def delete_tag():
    note = list.currentItem().text()
    tag_name = tags_list.currentItem().text()

    added_notes[note]["tags"].remove(tag_name)
    tags_list.clear()
    tags_list.addItems(added_notes[note]['tags'])

    write_file()

def search_byTag():
    tag = lineText.text()
    if(btn_searchTag.text()=="Search tag"):
        filter = {}

        for key in added_notes:
            if tag in added_notes[key]['tags']:
                filter[key] = added_notes[key]
        list.clear()
        list.addItems(filter)
        tags_list.clear()
        lineText.clear()
        btn_searchTag.setText('Cancel')

    else:
        btn_searchTag.setText('Search tag')
        list.clear()
        list.addItems(added_notes)
        tags_list.clear()

btn_searchTag.clicked.connect(search_byTag)
btn_deleteTag.clicked.connect(delete_tag)
btn_addTag.clicked.connect(add_tag)
btn_delete.clicked.connect(delete_note)

line1.addWidget(text)
line2.addWidget(list)


line2.addWidget(btn_save)


line2.addWidget(btn_addTag)
line2.addWidget(btn_searchTag)
line2.addWidget(btn_deleteTag)

H_line = QHBoxLayout()

H_line.addWidget(btn_create)
H_line.addWidget(btn_delete)

line1.addLayout(H_line)

window.setStyleSheet('''background-color: #FFC0CB;
''')

text.setStyleSheet('''background-color: #fafafa;
''')

list.setStyleSheet('''background-color: #fafafa;
''')

tags_list.setStyleSheet('''background-color: #fafafa;
''')
lineText.setStyleSheet('''background-color: #fafafa;
''')

btn_create.setStyleSheet('''background-color: 	#FFE4E1;
''')

btn_save.setStyleSheet('''background-color: 	#FFE4E1;
''')

btn_delete.setStyleSheet('''background-color: 	#FFE4E1;
''')
btn_deleteTag.setStyleSheet('''background-color: 	#FFE4E1;
''')

btn_addTag.setStyleSheet('''background-color: 	#FFE4E1;
''')

btn_searchTag.setStyleSheet('''background-color: 	#FFE4E1;
''')


line2.addWidget(tags_list)
line2.addWidget(lineText)

main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=1)

window.setLayout(main_line)

btn_create.clicked.connect(add_note)

btn_save.clicked.connect(Save_note)


window.show()
app.exec_()







