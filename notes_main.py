from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

#---------------Структура для зберігання заміток в json файл--------------
notes = {
    "Ласкаво просимо!":  {
        "text": "Це найкращий додаток для заміток у світі!",
        "tag": ["добро", "інструкція"]  }
}

def writeToFile(): #функція для запису в файл
    with open("notes_data.json", "w") as file:  #записуємо структуру сортовано
        json.dump(notes, file, sort_keys = True)


# ------------------------- Вікно програми ---------------------------
app = QApplication([])
window  = QWidget()
main_width, main_height, = 800, 600
window.setWindowTitle("Smart_notes")
window.resize(main_width,main_height)
window.setStyleSheet('background-color: #7171ff; font-size: 16px; color: #000000')


# ------------------------- Ел. інтерфейсу ---------------------------
text_editor = QTextEdit()             # введення тексту замітки
text_editor.setStyleSheet('background-color: #b871ff;' )
text_editor.setPlaceholderText("Введіть текст..") # текст який буде триматись

list_widget1 = QListWidget()          # список заміток
list_widget1.setStyleSheet('background-color: #ff71ff')

list_widget2 = QListWidget()          # список тегів
list_widget2.setStyleSheet('background-color: #ff71ff;')

text_searcher = QLineEdit()           # пошук по тексту
text_searcher.setPlaceholderText("Введіть текст...")
text_searcher.setStyleSheet('background-color: #ff71b8')

tag_searcher = QLineEdit()           # пошук по тегу
tag_searcher.setPlaceholderText("Введіть тег...")
tag_searcher.setStyleSheet('background-color: #ff71b8')

# ------------------------- Кпопки ---------------------------
make_note = QPushButton()
make_note.setText("Створити замітку")
make_note.setStyleSheet('background-color: #ff7171')

delete_note = QPushButton()
delete_note.setText("Видалити замітку")
delete_note.setStyleSheet('background-color: #ff7171')

save_note = QPushButton()
save_note.setText("Зберегти замітку")
save_note.setStyleSheet('background-color: #ff7171')

add_to_note = QPushButton()
add_to_note.setText("Додати до замітки")
add_to_note.setStyleSheet('background-color: #ff7171')

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкріпити від замітки")
unpin_to_note.setStyleSheet('background-color: #ff7171')

search_for_tag = QPushButton()
search_for_tag.setText("Шукати замітку за тегом")
search_for_tag.setStyleSheet('background-color: #ff7171')

search_for_note = QPushButton()
search_for_note.setText("Шукати замітку за текстом")
search_for_note.setStyleSheet('background-color: #ff7171')

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему")
action_theme_btn.setStyleSheet('background-color: #ff7171')

# ------------------------- Розміщення на макет ---------------------------
row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток"))
col2.addWidget(list_widget1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget2)
col2.addWidget(QLabel("Ввід даних"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)
col2.addWidget(search_for_note)
col2.addWidget(search_for_tag)
col2.addWidget(action_theme_btn)

# Злиття макетів
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

#--------------------------------Функціонал програми-------------------------------

#                        ________фуннції для заміток__________
    # отримуємо текст замітки з виділеною назвою та відображаємо його в полі редагування
def show_notes():
    global key
    key = list_widget1.selectedItems() [0].text() # дізнаємось на яку записку клікнули
    list_widget2.clear()                          # очищаємо поле з тегами
    text_editor.setText(notes[key]["text"])       # відобразили текст замітки
    list_widget2.addItems(notes[key]["tag"])      # відобразили теги замтки

# додаємо нову замітку
def add_notes():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки")
    if note_name and ok:
        list_widget1.addItem(note_name)
        notes[note_name] = {"text":"","tag":[]}
    writeToFile()

#видаляємо вибрану замітку
def delete_notes():
    if list_widget1.setCurrentItem():             # якщо вибрана замітка
        if key in notes:                          # і є така в словнику notes
            notes.pop(key)                        # pop видаляє зі словника

            text_editor.clear()                   # очищаємо віджети
            list_widget1.clear() 
            list_widget2.clear()
            list_widget1.addItems(notes)          # оновлюємо віджет і список заміток
            writeToFile()                         # перезаписуємо файл

# зберігаємо замітку
def save_notes():
    if list_widget1.currentItem():                # якщо вибрана замітка
        key = list_widget1.currentItem().text()   # отримати назву вибраної замітки
        notes[key]['text'] = text_editor.toPlainText() # записати у словник notes з текстом
        writeToFile()

#             ____________________Функції для тегів_____________________ 
'''Запуск програми'''
                                                  # підключення обробки подій
list_widget1.itemClicked.connect(show_notes)


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_widget1.addItems(notes)

# макет на екран
window.setLayout(layout_note)
# ------------------------- 
window.show()
app.exec()
