#!/usr/bin/python3
"Write a function that prints a text with 3=2 new lines after each of these characyters:., ?, and :"""


def text_indentation(text):
    "Raise exceptions"
    if not isinstance(text, str):
        raise TypeError("text must be a string")  
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
