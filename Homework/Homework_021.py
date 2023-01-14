# Напишите программу, удаляющую из текста все слова, содержащие "абв".


def main():
    txt = 'ansабвdfk afdhiаБвauh asdhfia fisadpof adfuабвh afai iqaqfqif afhiaf fad'
    print(txt)

    txt = ' '.join(list(filter(lambda element: 'абв' not in element.lower(), txt.split())))
    print(txt)


if __name__ == "__main__":
    main()

    