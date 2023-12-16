import json
import csv

codes = {}
with open('codes_correct.csv', mode='r', encoding="utf8") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        codes[row[0]] = row[4]

results = []

NUTS3_name2abbrev = {
    "Hlavní město Praha": "PHA",
    "Středočeský kraj": "STC",
    "Jihomoravský kraj": "JHM",
    "Plzeňský kraj": "PLK",
    "Královéhradecký kraj": "HKK",
    "Kraj Vysočina": "VYS",
    "Karlovarský kraj": "KVK",
    "Liberecký kraj": "LBK",
    "Pardubický kraj": "PAK",
    "Moravskoslezský kraj": "MSK",
    "Olomoucký kraj": "OLK",
    "Ústecký kraj": "ULK",
    "Zlínský kraj": "ZLK",
    "Jihočeský kraj": "JHC",
}

with open('unemployment.json', 'r') as file:
    unempl = json.load(file)
    for item in unempl:
        mesic = item['month']
        rok = item['year']
        data = item['data']
        for obj in data["polozky"]:
            okres = obj['okres'].split('/')[1]
            uchazeciOZamestnaniUoZ = obj['uchazeciOZamestnaniUoZ']
            noveHlaseniUchazeci = obj['noveHlaseniUchazeci']
            noveHlasenaAUvolnenaVPM = obj['noveHlasenaAUvolnenaVPM']
            obsazenaAZrusenaVPM = obj['obsazenaAZrusenaVPM']
            absolventiSkolAMladistvi = obj['absolventiSkolAMladistvi']
            result_obj = {"kraj": NUTS3_name2abbrev[codes[okres]], "month": mesic, "year": rok,
                          'uchazeciOZamestnaniUoZ': uchazeciOZamestnaniUoZ, 'noveHlaseniUchazeci': noveHlaseniUchazeci,
                          'noveHlasenaAUvolnenaVPM': noveHlasenaAUvolnenaVPM,
                          'obsazenaAZrusenaVPM': obsazenaAZrusenaVPM,
                          'absolventiSkolAMladistvi': absolventiSkolAMladistvi}
            results.append(result_obj)

columns = ["kraj", "month", "year", 'uchazeciOZamestnaniUoZ', 'noveHlaseniUchazeci',
           'noveHlasenaAUvolnenaVPM', 'obsazenaAZrusenaVPM', 'absolventiSkolAMladistvi']
with open('unemployment.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)