import sys
from record import record_and_transcript

alumnos = []
entries = []


def get_alumnos():
    with open("alumnos.txt") as f:
        for linea in f:
            comps = linea.split(",")
            alumnos.append({
                "nombre": comps[1],
                "rut": comps[0],
                "num": comps[2][:-1]
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
    nota = []
    for word in words:
        if word.isalpha():
            alum += word + " "
        elif word.isdigit():
            nota.append(word)
    return alum.strip(), nota


def register(text, n=1):
    text_alum, text_nota = divide_alum_nota(text)
    enotas = []
    for i in range(n):
        if i < len(text_nota):
            enotas.append(expected_nota(text_nota[i]))
        else:
            enotas.append(-1)
    ealum = expected_alumno(text_alum)
    row = ealum["num"] + "," + ealum["rut"] + "," + ealum["nombre"] + "," + ",".join(map(str, enotas))
    print "Registro: " + row.replace(",", "\t")
    entries.append(row)


def save_to_file(n=1):
    s = raw_input("Nombre archivo: ") + ".csv"
    with open(s, "w") as f:
        f.write("N,RUT,Nombre," + ",".join(map(lambda e: "P" + str(e+1), range(n))) + "\n")
        emap = {}
        for entry in entries:
            num = entry.split(",")[0]
            emap[num] = ",".join(entry.split(",")[3:])

        for alum in alumnos:
            row = alum["num"] + "," + alum["rut"] + "," + alum["nombre"] + ","
            if alum["num"] in emap:
                row = row + emap[alum["num"]]
            f.write(row + "\n")
        f.write("\n")


if __name__ == '__main__':
    # PARAMETERS
    N = int(sys.argv[sys.argv.index("-n") + 1]) if "-n" in sys.argv else 1
    textual = "-t" in sys.argv
    verbose = "-v" in sys.argv

    # PROGRAM
    print "\t\taudioRev"
    get_alumnos()
    s = raw_input("Ingresar otra: [si]/no: ")
    while s != "no":
        if not textual:
            text = record_and_transcript(verbose=verbose)
        else:
            text = raw_input(">> ")
        register(text, n=N)
        s = raw_input("Ingresar otra: [si]/no: ")
    save_to_file(n=N)
    print "Guardado."
