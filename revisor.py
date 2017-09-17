from record import record_and_transcript

alumnos = []
entries = []


def get_alumnos():
    with open("alumnos.txt") as f:
        for linea in f:
            comps = linea.split(",")
            alumnos.append({
                "nombre": comps[1][:-1],
                "rut": comps[0]
            })


def lev(s1, s2):
    if len(s1) < len(s2):
        return lev(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def expected_alumno(text):
    min_dist = 99999
    min_alum = ""
    for alumno in alumnos:
        d = lev(alumno["nombre"], text)
        if d < min_dist:
            min_dist = d
            min_alum = alumno
    return min_alum


def expected_nota(text):
    if len(text) == 0 or len(text) >= 3:
        return -1
    if len(text) == 1:
        text += "0"
    return int(text) / 10.0


def divide_alum_nota(text):
    words = text.split(" ")
    alum = ""
    nota = ""
    for word in words:
        if word.isalpha():
            alum += word + " "
        elif word.isdigit():
            nota += word
    return alum.strip(), nota


def register(text):
    text_alum, text_nota = divide_alum_nota(text)
    enota = expected_nota(text_nota)
    ealum = expected_alumno(text_alum)
    row = ealum["rut"] + "," + ealum["nombre"] + "," + str(enota)
    print "Registro:" + row.replace(",", "\t")
    entries.append(row + "\n")


def save_to_file():
    s = raw_input("Nombre archivo: ")
    with open(s, "w") as f:
        f.write("RUT,Nombre,Nota\n")
        sort_entries = sorted(entries, key=lambda x: x.split(",")[1])
        for entry in sort_entries:
            f.write(entry)


if __name__ == '__main__':
    print "\t\taudioRev"
    get_alumnos()
    s = raw_input("Ingresar otra: [si]/no: ")
    while s != "no":
        text = record_and_transcript()
        register(text)
        s = raw_input("Ingresar otra: [si]/no: ")
    save_to_file()
    print "Guardado."
