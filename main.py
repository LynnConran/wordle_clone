# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import tkinter as tk
from tkinter import ttk
from pynput import keyboard

five_file_path = 'five_letter_words.txt'
six_file_path = "six_letter_words.txt"
guess_count = 6
word_length = 5

label_list = []
button_list = []
current_letter = 0
current_row = 0
# bottom_label = None

word = 'temp'


def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']:
        letter_pressed(k.upper())
    elif k == 'delete' or k == 'backspace':
        delete_pressed()
    elif k == 'enter':
        return_pressed()


def find_words(length):
    length_file = open(six_file_path, 'w')
    with open("all_english_words.txt") as file:
        words = file.readlines()
        for i in words:
            if len(i) == length + 1:  # Plus one for the newline
                length_file.write(i)
    length_file.close()


def read_words():
    global word
    if word_length == 5:
        with open(five_file_path) as file:
            words = file.readlines()
            for i in range(len(words)):
                words[i] = words[i].strip('\n')
    elif word_length == 6:
        with open(six_file_path) as file:
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
    if word_length == 5:
        with open(five_file_path) as file:
            words = file.readlines()
            for i in range(len(words)):
                words[i] = words[i].strip('\n')
    elif word_length == 6:
        with open(six_file_path) as file:
            words = file.readlines()
            for i in range(len(words)):
                words[i] = words[i].strip('\n')
    guess = ''
    position = current_row * word_length
    for i in range(word_length):
        guess += label_list[position + i]['text']
    guess = guess.lower()
    if guess not in words:
        bottom_label['text'] = 'Not a valid word'
        return False
    else:
        bottom_label['text'] = ''
    for i in range(len(guess)):
        if guess[i] == word[i]:
            change_label_color('green', position + i)
            change_button_color('green', guess[i].upper())
        elif guess[i] in word:
            change_label_color('yellow', position + i)
            change_button_color('yellow', guess[i].upper())
        else:
            change_label_color('grey', position + i)
            change_button_color('grey', guess[i].upper())
    if guess == word:
        game_over(True)
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
    bottom_label['text'] = ''
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


def game_over(win=False):
    global current_letter, current_row
    if win:
        bottom_label['text'] = "You Win! Word was : " + str(word).capitalize()
    else:
        bottom_label['text'] = 'Game over, word was : ' + str(word).capitalize()
    read_words()
    for i in label_list:
        i['text'] = ''
        i['background'] = 'white'
    for i in button_list:
        i['bg'] = 'SystemButtonFace'
    current_letter = 0
    current_row = 0


def change_button_color(color, letter):
    for i in button_list:
        if i['text'] == letter:
            i['bg'] = color
            return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    root = tk.Tk()
    root.title("Wordle Clone")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # window_height = int(screen_height/1.5)
    # window_width = int(window_height*(2/3))

    window_height = 800
    window_width = 533

    # print(window_height, " ", window_width)

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    label_size = int(window_width / word_length - 10)

    y_offset = int(window_height * .8)
    x_offset = int(window_width * .05)

    button_width = 5
    button_height = 26

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # root.resizable(False, False)

    q = tk.Button(root, text='Q', command=lambda: letter_pressed('Q'), width=button_width)
    button_list.append(q)
    q.place(x=button_width*0 + x_offset, y=y_offset)
    w = tk.Button(root, text='W', command=lambda: letter_pressed('W'), width=button_width)
    button_list.append(w)
    w.place(x=button_width*10 + x_offset, y=y_offset)
    e = tk.Button(root, text='E', command=lambda: letter_pressed('E'), width=button_width)
    button_list.append(e)
    e.place(x=button_width*20 + x_offset, y=y_offset)
    r = tk.Button(root, text='R', command=lambda: letter_pressed('R'), width=button_width)
    button_list.append(r)
    r.place(x=button_width*30 + x_offset, y=y_offset)
    t = tk.Button(root, text='T', command=lambda: letter_pressed('T'), width=button_width)
    button_list.append(t)
    t.place(x=button_width*40 + x_offset, y=y_offset)
    y = tk.Button(root, text='Y', command=lambda: letter_pressed('Y'), width=button_width)
    button_list.append(y)
    y.place(x=button_width*50 + x_offset, y=y_offset)
    u = tk.Button(root, text='U', command=lambda: letter_pressed('U'), width=button_width)
    button_list.append(u)
    u.place(x=button_width*60 + x_offset, y=y_offset)
    i = tk.Button(root, text='I', command=lambda: letter_pressed('I'), width=button_width)
    button_list.append(i)
    i.place(x=button_width*70 + x_offset, y=y_offset)
    o = tk.Button(root, text='O', command=lambda: letter_pressed('O'), width=button_width)
    button_list.append(o)
    o.place(x=button_width*80 + x_offset, y=y_offset)
    p = tk.Button(root, text='P', command=lambda: letter_pressed('P'), width=button_width)
    button_list.append(p)
    p.place(x=button_width*90 + x_offset, y=y_offset)

    a = tk.Button(root, text='A', command=lambda: letter_pressed('A'), width=button_width)
    button_list.append(a)
    a.place(x=button_width * 00 + x_offset*2, y=y_offset + button_height)
    s = tk.Button(root, text='S', command=lambda: letter_pressed('S'), width=button_width)
    button_list.append(s)
    s.place(x=button_width * 10 + x_offset*2, y=y_offset + button_height)
    d = tk.Button(root, text='D', command=lambda: letter_pressed('D'), width=button_width)
    button_list.append(d)
    d.place(x=button_width * 20 + x_offset*2, y=y_offset + button_height)
    f = tk.Button(root, text='F', command=lambda: letter_pressed('F'), width=button_width)
    button_list.append(f)
    f.place(x=button_width * 30 + x_offset*2, y=y_offset + button_height)
    g = tk.Button(root, text='G', command=lambda: letter_pressed('G'), width=button_width)
    button_list.append(g)
    g.place(x=button_width * 40 + x_offset*2, y=y_offset + button_height)
    h = tk.Button(root, text='H', command=lambda: letter_pressed('H'), width=button_width)
    button_list.append(h)
    h.place(x=button_width * 50 + x_offset*2, y=y_offset + button_height)
    j = tk.Button(root, text='J', command=lambda: letter_pressed('J'), width=button_width)
    button_list.append(j)
    j.place(x=button_width * 60 + x_offset*2, y=y_offset + button_height)
    k = tk.Button(root, text='K', command=lambda: letter_pressed('K'), width=button_width)
    button_list.append(k)
    k.place(x=button_width * 70 + x_offset*2, y=y_offset + button_height)
    l = tk.Button(root, text='L', command=lambda: letter_pressed('L'), width=button_width)
    button_list.append(l)
    l.place(x=button_width * 80 + x_offset*2, y=y_offset + button_height)

    z = tk.Button(root, text='Z', command=lambda: letter_pressed('Z'), width=button_width)
    button_list.append(z)
    z.place(x=button_width * 0 + x_offset*3, y=y_offset + button_height * 2)
    x = tk.Button(root, text='X', command=lambda: letter_pressed('X'), width=button_width)
    button_list.append(x)
    x.place(x=button_width * 10 + x_offset*3, y=y_offset + button_height * 2)
    c = tk.Button(root, text='C', command=lambda: letter_pressed('C'), width=button_width)
    button_list.append(c)
    c.place(x=button_width * 20 + x_offset*3, y=y_offset + button_height * 2)
    v = tk.Button(root, text='V', command=lambda: letter_pressed('V'), width=button_width)
    button_list.append(v)
    v.place(x=button_width * 30 + x_offset*3, y=y_offset + button_height * 2)
    b = tk.Button(root, text='B', command=lambda: letter_pressed('B'), width=button_width)
    button_list.append(b)
    b.place(x=button_width * 40 + x_offset*3, y=y_offset + button_height * 2)
    n = tk.Button(root, text='N', command=lambda: letter_pressed('N'), width=button_width)
    button_list.append(n)
    n.place(x=button_width * 50 + x_offset*3, y=y_offset + button_height * 2)
    m = tk.Button(root, text='M', command=lambda: letter_pressed('M'), width=button_width)
    button_list.append(m)
    m.place(x=button_width * 60 + x_offset*3, y=y_offset + button_height * 2)

    delete = tk.Button(root, text='DEL', command=delete_pressed, width=button_width * 2)
    delete.place(x=button_width * 70 + x_offset*3, y=y_offset + button_height * 2)

    enter = tk.Button(root, text='Enter', command=return_pressed, width=int(button_width*1.5))
    enter.place(x=button_width * 00 + x_offset * .5, y=y_offset + button_height * 2)

    for i in range(guess_count * word_length):
        label_list.append(ttk.Label(root, text=str(i), background="white", padding=label_size/4))

    for i in label_list:
        i.place(x=(int(i['text']) % word_length) * label_size + label_size / 2.3, y=int(int(i['text']) / word_length)
                * label_size + label_size / 4)
        i['text'] = ''

    bottom_label = tk.Label(root, width=80, background='white', height=2)
    bottom_label.place(x=0, y=int(window_height * 0.90))

    read_words()
    root.mainloop()
    # guessing_game(read_words())
