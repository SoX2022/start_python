# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def StringCompressing(text):
    count = 1
    compressed_string = ''

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count +=1
        else:
            compressed_string += str(count) + text[i]
            count = 1
            
    compressed_string += str(count) + text[len(text) - 1]
    return compressed_string

def StringDecopressing(text):
    decompressed_string = ''

    for i in range(len(text)):
        for j in range(0, len(text[i].replace('\n', '')), 2):
            decompressed_string += text[i][j + 1] * int(text[i][j])
        text[i] = decompressed_string + '\n'
        decompressed_string = ''


def main():
    compressed_data = open('hw_024_compressed_data', 'w')
    w = True

    while w:
        print('Enter your new text. Enter "quit" to exit.')
        q = input()
        if q.lower() == 'quit':
            w = False
        else:
            compressed_data.writelines(StringCompressing(q) + '\n')

    compressed_data.close()

    compressed_data = open('hw_024_compressed_data', 'r')
    compressed_string = compressed_data.readlines()
    compressed_data.close()

    StringDecopressing(compressed_string)

    decompressed_data = open('hw_024_decompressed_data', 'w')
    for element in compressed_string:
        decompressed_data.writelines(element)
    decompressed_data.close()



if __name__ == "__main__":
    main()

