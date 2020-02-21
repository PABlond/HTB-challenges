import config
import pathlib

def extract_data(line, breaking_w, filename):
    data = line.split(breaking_w)[1]
    with open(filename, "a") as g:
        g.write(data)


def run():
    if pathlib.Path(config.manufacturer_filename).is_file():
        pathlib.Path(config.manufacturer_filename).unlink()
    elif pathlib.Path(config.serial_filename).is_file():
        pathlib.Path(config.serial_filename).unlink()  
        
    syslog = "syslog"
    breaking_ws = ["Manufacturer: ", "SerialNumber: "]     

    with open(syslog, "r") as f:
        for line in f:
            if breaking_ws[0] in line:
                extract_data(line=line, breaking_w=breaking_ws[0],
                             filename=config.manufacturer_filename)
            elif breaking_ws[1] in line:
                extract_data(line=line, breaking_w=breaking_ws[1],
                             filename=config.serial_filename)
