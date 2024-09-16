import json

def load_file(filename : str, output_file):
    with open(filename, 'r', encoding="utf8") as file:
        print('loading: ' + filename)
        data = json.load(file)

    for i in data:
        lat = round(float(i['lat']),3)
        lon = round(float(i['lon']),3)
        dname = i['display_name'].replace("'", "\\'")
        prov_code = i['province']
        info_line = 'InfoBiteParameterFormValue(\'/en/location/index.html?coords=' + str(lat) + ',' + str(lon) + '\', \'' + dname + ', ' + prov_code + '\'),'
        print(info_line)
        output_file.write(info_line + "\n")


files = ['ab', 'bc', 'mb', 'nb', 'nl', 'ns', 'nt', 'nu', 'on', 'pe', 'qc', 'sk', 'yt']
msg = "Loading data"
print(msg)

output_file = open("output.txt", "w", encoding="utf8")

for prov_file_name in files:
    load_file(prov_file_name + ".json", output_file)

output_file.close()