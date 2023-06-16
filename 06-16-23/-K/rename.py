""" 
Panuto: 

Ilagay ninyo ang code na ito sa folder ng isang class

Pagtapos ay i-run ninyo 'to depende sa pangangailangan ninyo: 
python rename.py -c="{-K, -N, C}" -t {AM, AMF, PM, PMF} -s {start_number}

Paalala na nakadepende ang pagkakasunod-sunod sa pangalan ng orihinal na file.
Ang bilang din ay magsisimula depende sa integer sa {start_number}

Halimbawa: 
Matapos kong ilagay ang code na ito sa -K na folder, 
gusto kong pangalanan ang mga files sa loob ng AMF na folder at 
nais kong magsimula sa bilang 1, kaya ang magiging itsura ng aking command ay: 
python rename.py -c="-K" -t AMF -s 1

Huwag din mag-aalala kung mayroong mga files na naka-ayos na ang pangalan, 
ang pinapalitan lamang na pangalan ng code na ito ay ang mga pangalan na
nagsisimula sa IMG

"""

import argparse
import os

parser = argparse.ArgumentParser(description='Rename Files')
parser.add_argument('-c','--class_n', type=str, required = True, help='Classes: -K, -N, C')
parser.add_argument('-t', '--type', type=str, required = True, help='Type: AM, AMF, PM, PMF')
parser.add_argument('-s', '--start', type=int, required = True, help='Start Number')
args = parser.parse_args()

if __name__ == '__main__':
    classes = ["-K", "-N", "C"]
    types = ["AM", "AMF", "PM", "PMF"]

    IMG = []

    if args.class_n not in classes or args.type not in types: raise Exception("re-check your class and type input")

    files = os.listdir(args.type) 
    for file in files: 
        if file.startswith('IMG'):
            IMG.append(file)
    IMG.sort()

    for i, file in enumerate(IMG): 
        file_path = os.path.join(args.type, file)
        renamed = args.class_n + "_" + str(args.start + i) + ".jpg"
        os.rename(file_path, os.path.join(args.type, renamed))
