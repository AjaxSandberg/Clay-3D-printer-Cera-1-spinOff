import re

def round_gcode_line(line, precision=3):
    def replacer(match):
        num = float(match.group(0))
        return "{0:.{1}f}".format(num, precision)
    
    return re.sub(r"(?<=[XYZEFxyzef])(-?\d+\.?\d*)", replacer, line)

if write:
    try:
        cleaned_lines = [round_gcode_line(line) for line in lines]
        with open(path, 'w') as f:
            for line in cleaned_lines:
                f.write(line.strip() + '\n')
        print("✅ G-code written to: {}".format(path))
    except Exception as e:
        print("⚠️ Error writing file: {}".format(e))
else:
    print("️ Waiting for button press...")
