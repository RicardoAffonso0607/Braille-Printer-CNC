import serial

import time

INPUT = "input.txt"
OUTPUT = "output.txt"

brai = [
    "⠁", "⠃", "⠉", "⠙", "⠑", "⠋", "⠛", "⠓", "⠊", "⠚",
    "⠅", "⠇", "⠍", "⠝", "⠕", "⠏", "⠟", "⠗", "⠎", "⠞",
    "⠥", "⠧", "⠭", "⠽", "⠵", "⠺"
]

specials = [
    "⠯",  # Ç
    "⠿",  # é
    "⠜",  # ã
    "⠂",  # ,
    "⠖",  # !
    "⠢",  # ?
    "⠄",  # .
    "⠬",  # ó
    "⠷",  # á
    "⠌",  # í
    "⠾",  # ú
    "⠫",  # à
    "⠡",  # â
    "⠹",  # ô
    "⠪",  # õ
    "⠣"   # ê
]

# Opens the file and reads the chracters
with open(INPUT, 'r', encoding='utf-8') as input_file, open(OUTPUT, 'w', encoding='utf-8') as output_file:
    letter = input_file.read(1)
    while letter:
        if not (65 <= ord(letter) <= 90) and not (97 <= ord(letter) <= 122) :
            if letter == ' ':
                output_file.write(" ")
            elif letter == 'ç':
                output_file.write(specials[0])
            elif letter == 'é':
                output_file.write(specials[1])
            elif letter == 'ã':
                output_file.write(specials[2])
            elif letter == ',':
                output_file.write(specials[3])
            elif letter == '!':
                output_file.write(specials[4])
            elif letter == '?':
                output_file.write(specials[5])
            elif letter == '.':
                output_file.write(specials[6])
            elif letter == 'ó':
                output_file.write(specials[7])
            elif letter == 'á':
                output_file.write(specials[8])
            elif letter == 'í':
                output_file.write(specials[9])
            elif letter == 'ú':
                output_file.write(specials[10])
            elif letter == 'à':
                output_file.write(specials[11])
            elif letter == 'â':
                output_file.write(specials[12])
            elif letter == 'ô':
                output_file.write(specials[13])
            elif letter == 'õ':
                output_file.write(specials[14])
            elif letter == 'ê':
                output_file.write(specials[15])
        else:
            if letter.isupper():
                output_file.write("⠨" + brai[ord(letter) - ord('A')])
            elif letter.islower():
                output_file.write(brai[ord(letter) - ord('a')])
            

        letter = input_file.read(1)

# Change this port to where your Arduino is connected
porta_serial = 'COM9'
baud_rate = 9600

# Connect to the Arduino
try:
    arduino = serial.Serial(porta_serial, baud_rate)
    print("Arduíno connected")
except:
    print("Fail to connect")

conteudo = input("Press to start the printing:")

with open(INPUT, 'r') as arquivo:
    conteudo = arquivo.read()

arduino.write(conteudo.encode('latin-1'))


try:
    while True:
        time.sleep(5)
        resposta = arduino.read_all().decode('latin-1')
        print(resposta)


except KeyboardInterrupt:
    arduino.close()
