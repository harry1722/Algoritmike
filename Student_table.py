# Funksioni për të llogaritur statusin dhe mesataren sipas kritereve të dhëna
def ploteso_tabelen(studentet):
    for studenti in studentet:
        # Merr ECTS
        ects = studenti["ECTS"]

        # Vendos statusin
        if ects == 60:
            studenti["Status"] = 1
        elif 30 <= ects < 60:
            studenti["Status"] = 2
        elif ects < 30:
            studenti["Status"] = 3

        # Kalkulo mesataren vetëm nëse ECTS = 60
        if ects == 60:
            notat = [nota for nota in studenti["Marks"] if nota != "-"]  # Ignoro vlerat bosh
            mesatarja = sum(notat) / len(notat) if notat else 0
            studenti["Average"] = round(mesatarja, 2)  # Rrumbullakose në 2 shifra dhjetore
        else:
            studenti["Average"] = None  # Mesatarja është bosh nëse ECTS nuk është 60

    return studentet


# Tabela e studentëve me të dhënat përkatëse
studentet = [
    {"No": 1, "Name": "A", "Marks": [8, 6, 7], "ECTS": 60, "Status": None, "Average": None},
    {"No": 2, "Name": "B", "Marks": [10, 10, 10], "ECTS": 60, "Status": None, "Average": None},
    {"No": 3, "Name": "C", "Marks": ["-", 7, 5], "ECTS": 40, "Status": None, "Average": None},
    {"No": 4, "Name": "D", "Marks": [6, "-", "-"], "ECTS": 20, "Status": None, "Average": None},
    {"No": 5, "Name": "E", "Marks": [8, 7, 9], "ECTS": 60, "Status": None, "Average": None},
]

# Thirr funksionin për të plotësuar tabelën
studentet_e_plotesuar = ploteso_tabelen(studentet)

# Printimi i rezultatit
for studenti in studentet_e_plotesuar:
    print(f"No: {studenti['No']}, Name: {studenti['Name']}, Status: {studenti['Status']}, Average: {studenti['Average']}")
