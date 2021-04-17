import os
import codecs

decode_hex = codecs.getdecoder("hex_codec")

data = b"\x4d\x54\x48\x53\x00\x01"
count = 0
print("Reading and converting media files...")
for filename in os.listdir("m"):
    if filename != "index.mth":
        data += decode_hex(filename)[0]
        count += 1

print("Writing to file...")
file = open("m/index.mth", "wb")
file.write(data)
file.close()
print("Wrote " + str(count) + " medias to file.")
