# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import tkinter as tk
from tkinter import ttk

five_file_path = 'five_letter_words.txt'
guess_count = 6
word_length = 5

button_width = 6
button_height = 30

label_list = []
current_letter = 0
current_row = 0

word = 'temp'


def read_words():
    global word
    with open(five_file_path) as file:
        words = file.readlines()
        for i in range(len(words)):
            words[i] = words[i].strip('\n')
    word_count = len(words)
    random_int = random.randint(0, word_count)
    word = words[random_int]


# def guessing_game(word):
#     guess_number = 0
#     while guess_number < guess_count:
#         guess = prompt_guess(len(word))
#         if check_guess(word, guess):
#             print("You win!")
#             continue
#         else:
#             provide_feedback(word, guess)
#         guess_number += 1
#     print('game over, word was ' + word)


def prompt_guess(length):
    guess = input("Guess a word: ")
    while len(guess) != length:
        guess = input("invalid word length, try again ")
    return guess


def change_label_color(color, position):
    label_list[position]['background'] = color

def provide_feedback():
    with open(five_file_path) as file:
        words = file.readlines()
        for i in range(len(words)):
            words[i] = words[i].strip('\n')
    guess = ''
    position = current_row * word_length
    for i in range(word_length):
        guess += label_list[position + i]['text']
    guess = guess.lower()
    if guess not in words:
        print("Not a valid word")
        return False
    for i in range(len(guess)):
        if guess[i] == word[i]:
            change_label_color('green', position + i)
        elif guess[i] in word:
            change_label_color('yellow', position + i)
        else:
            change_label_color('grey', position + i)
    return True


def letter_pressed(letter):
    global current_letter
    if current_letter > -1:
        position = current_letter + (current_row * word_length)
        label_list[position]['text'] = letter
        if current_letter < word_length - 1:
            current_letter += 1
        else:
            current_letter = -1


def delete_pressed():
    global current_letter
    if current_letter == 0:
        position = current_letter + (current_row * word_length)
    elif current_letter == -1:
        position = current_row * word_length + word_length - 1
        label_list[position]['text'] = ''
        current_letter = word_length - 1
        return
    else:
        position = current_letter + (current_row * word_length) - 1
    label_list[position]['text'] = ''
    if current_letter > 0:
        current_letter -= 1


def return_pressed():
    global current_letter, current_row
    if provide_feedback():
        if current_letter == -1:
            if current_row != guess_count - 1:
                current_row += 1
                current_letter = 0
            else:
                game_over()


def game_over():
    global current_letter, current_row
    print("Game over, word was : " + word)
    read_words()
    for i in label_list:
        i['text'] = ''
        i['background'] = 'white'
    current_letter = 0
    current_row = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Wordle Clone")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_height = int(screen_height/1.5)
    window_width = int(window_height*(2/3))

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    label_size = int(window_width / word_length - 10)

    y_offset = int(window_height * .8)
    x_offset = int(window_width * .05)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    q = ttk.Button(root, text='Q', command=lambda: letter_pressed('Q'), width=button_width)
    q.place(x=button_width*0 + x_offset, y=y_offset)
    w = ttk.Button(root, text='W', command=lambda: letter_pressed('W'), width=button_width)
    w.place(x=button_width*10 + x_offset, y=y_offset)
    e = ttk.Button(root, text='E', command=lambda: letter_pressed('E'), width=button_width)
    e.place(x=button_width*20 + x_offset, y=y_offset)
    r = ttk.Button(root, text='R', command=lambda: letter_pressed('R'), width=button_width)
    r.place(x=button_width*30 + x_offset, y=y_offset)
    t = ttk.Button(root, text='T', command=lambda: letter_pressed('T'), width=button_width)
    t.place(x=button_width*40 + x_offset, y=y_offset)
    y = ttk.Button(root, text='Y', command=lambda: letter_pressed('Y'), width=button_width)
    y.place(x=button_width*50 + x_offset, y=y_offset)
    u = ttk.Button(root, text='U', command=lambda: letter_pressed('U'), width=button_width)
    u.place(x=button_width*60 + x_offset, y=y_offset)
    i = ttk.Button(root, text='I', command=lambda: letter_pressed('I'), width=button_width)
    i.place(x=button_width*70 + x_offset, y=y_offset)
    o = ttk.Button(root, text='O', command=lambda: letter_pressed('O'), width=button_width)
    o.place(x=button_width*80 + x_offset, y=y_offset)
    p = ttk.Button(root, text='P', command=lambda: letter_pressed('P'), width=button_width)
    p.place(x=button_width*90 + x_offset, y=y_offset)

    a = ttk.Button(root, text='A', command=lambda: letter_pressed('A'), width=button_width)
    a.place(x=button_width * 00 + x_offset*2, y=y_offset + button_height)
    s = ttk.Button(root, text='S', command=lambda: letter_pressed('S'), width=button_width)
    s.place(x=button_width * 10 + x_offset*2, y=y_offset + button_height)
    d = ttk.Button(root, text='D', command=lambda: letter_pressed('D'), width=button_width)
    d.place(x=button_width * 20 + x_offset*2, y=y_offset + button_height)
    f = ttk.Button(root, text='F', command=lambda: letter_pressed('F'), width=button_width)
    f.place(x=button_width * 30 + x_offset*2, y=y_offset + button_height)
    g = ttk.Button(root, text='G', command=lambda: letter_pressed('G'), width=button_width)
    g.place(x=button_width * 40 + x_offset*2, y=y_offset + button_height)
    h = ttk.Button(root, text='H', command=lambda: letter_pressed('H'), width=button_width)
    h.place(x=button_width * 50 + x_offset*2, y=y_offset + button_height)
    j = ttk.Button(root, text='J', command=lambda: letter_pressed('J'), width=button_width)
    j.place(x=button_width * 60 + x_offset*2, y=y_offset + button_height)
    k = ttk.Button(root, text='K', command=lambda: letter_pressed('K'), width=button_width)
    k.place(x=button_width * 70 + x_offset*2, y=y_offset + button_height)
    l = ttk.Button(root, text='L', command=lambda: letter_pressed('L'), width=button_width)
    l.place(x=button_width * 80 + x_offset*2, y=y_offset + button_height)

    z = ttk.Button(root, text='Z', command=lambda: letter_pressed('Z'), width=button_width)
    z.place(x=button_width * 0 + x_offset*3, y=y_offset + button_height * 2)
    x = ttk.Button(root, text='X', command=lambda: letter_pressed('X'), width=button_width)
    x.place(x=button_width * 10 + x_offset*3, y=y_offset + button_height * 2)
    c = ttk.Button(root, text='C', command=lambda: letter_pressed('C'), width=button_width)
    c.place(x=button_width * 20 + x_offset*3, y=y_offset + button_height * 2)
    v = ttk.Button(root, text='V', command=lambda: letter_pressed('V'), width=button_width)
    v.place(x=button_width * 30 + x_offset*3, y=y_offset + button_height * 2)
    b = ttk.Button(root, text='B', command=lambda: letter_pressed('B'), width=button_width)
    b.place(x=button_width * 40 + x_offset*3, y=y_offset + button_height * 2)
    n = ttk.Button(root, text='N', command=lambda: letter_pressed('N'), width=button_width)
    n.place(x=button_width * 50 + x_offset*3, y=y_offset + button_height * 2)
    m = ttk.Button(root, text='M', command=lambda: letter_pressed('M'), width=button_width)
    m.place(x=button_width * 60 + x_offset*3, y=y_offset + button_height * 2)

    delete = ttk.Button(root, text='DEL', command=delete_pressed, width=button_width * 2)
    delete.place(x=button_width * 70 + x_offset*3, y=y_offset + button_height * 2)

    enter = ttk.Button(root, text='Enter', command=return_pressed, width=int(button_width*1.5))
    enter.place(x=button_width * 00 + x_offset, y=y_offset + button_height * 2)

    for i in range(guess_count * word_length):
        label_list.append(ttk.Label(root, text=str(i), background="white", padding=label_size/4))

    for i in label_list:
        i.place(x=(int(i['text']) % word_length) * label_size + label_size / 2.3, y=int(int(i['text']) / word_length)
                * label_size + label_size / 4)
        i['text'] = ''

    read_words()
    root.mainloop()
    # guessing_game(read_words())
