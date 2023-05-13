#начни тут создавать приложение с умными заметками

from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QTextEdit, QListWidget, QVBoxLayout, QLineEdit, QInputDialog, QDialog
import json

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Умные заметки')

#Обработка нажатия на заметку
def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]["text"])
    list_tags.clear()
    list_tags.addItems(notes[name]["tags"])

def add_note():
    note_name, result = QInputDialog.getText(main_win, "Добавить заметку", "Название заметки:")
    if note_name != "" and result:    
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItems(note_name)

def del_note():
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        del notes[name]
        with open("notes_data.json", "w", encoding = "utf-8") as file:
            json.dump(notes, file,)
        list_notes.clear()
        list_notes.addItems(name)
        list_tags.clear()
        field_text.clear()

def save_note():
    list_notes.selectedItems()
    name = list_notes.selectedItems()[0].text()
    notes[name]["text"] = field_text.toPlainText()
    with open("notes_data.json", "w", encoding = "utf-8") as file:
        json.dump(notes, file,)

#def search_tag1():
    #tag = list_tags.text()
    #if search_tag.text() == 'Искать заметки по тегу' and tag:
        #notes_filtered = {}
        #for x in notes:
            #if tag in notes[x]['tags']
        #search_tag.setText('Сбросить поиск')
        #list_notes.clear()
        #list_tags.clear()
        #list_notes.addItems(notes_filtered)
    #elif search_tag.text() == 'Сбросить поиск':
        #write_tag.clear()
        #list_notes.clear()
        #list_tags.clear()
        #list_notes.addItems(notes)
        #search_tag.setText('Искать заметки по тегу')
    #else:
        #pass

#def add_to_tag():
    tags = write_tag.text()
    



#def unpin_tag():



#создаём словарь
notes = {
    "note_name" :{
        "text": "Добро пожаловать! Анекдот:Оказываются на необитаемом острове немец, поляк и русский. После нескольких дней прибивает к острову бутылку. Открывают они ее, а там джинн. Джинн говорит:/n За то, что вы меня выпустили исполняю по желанию./n Поляк:/n-Мешок золота и домой./n Немец:/n-Женщину, мешок золота и домой./n Русский Эх хорошая была компания./n-Ящик водки и всех обратно",
        "tags": []
}}

with open("notes_data.json", "w", encoding = "utf-8") as file:
    json.dump(notes, file, sort_keys = True)

#Создаём кнопки и линии, подключаем их
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()

create_notes = QPushButton('Создать заметку')
delete_notes= QPushButton('Удалить заметку')
save_notes = QPushButton('Сохранить заметку')
write_tag = QLineEdit()

add_notes = QPushButton('Добавить к заметке')
unpin_notes = QPushButton('Открепить от заметки')
search_tag = QPushButton('Искать заметки по тегу')

field_text = QTextEdit()
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

line2.addLayout(line3)
line2.addLayout(line4)

line1.addWidget(field_text)

line2.addWidget(list_notes, alignment = Qt.AlignCenter)

line3.addWidget(create_notes,alignment = Qt.AlignCenter)
line3.addWidget(delete_notes,alignment = Qt.AlignCenter)

line2.addWidget(save_notes,alignment = Qt.AlignCenter)
line2.addWidget(list_tags,alignment = Qt.AlignCenter)
line2.addWidget(write_tag,alignment = Qt.AlignCenter)

line4.addWidget(add_notes,alignment = Qt.AlignCenter)
line4.addWidget(unpin_notes,alignment = Qt.AlignCenter)

line2.addWidget(search_tag, alignment = Qt.AlignCenter)

line5.addLayout(line1)
line5.addLayout(line2)

#Присоединяем функцию к списку, кнопкам
list_notes.itemClicked.connect(show_note)

delete_notes.clicked.connect(del_note)

save_notes.clicked.connect(save_note)

create_notes.clicked.connect(add_note)

search_tag.clicked.connect(search_tag1)


#Добавляем линии к приложению, показываем окно, открываем его
main_win.setLayout(line5)
main_win.show()
list_notes.addItems(notes)
app.exec_()