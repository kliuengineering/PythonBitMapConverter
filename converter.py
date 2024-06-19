# Note: https://tools.withcode.uk/bitmap/

# how to use this?
# 1. go to the site and convert my image to a bit map data
# 2. run command $python3 converter.py input.txt output.txt 
# 3. i will get the final result in the output.txt file

import sys
from typing import List

class Converter:
# PUBLIC:

    def __init__(self, PATH, DEST) -> None:
        self.path = PATH
        self.data = []


    # getter
    @property
    def path(self) -> str:
        return self._path


    # setter
    @path.setter
    def path(self, path) -> None:
        self._path = path


    @property
    def dest(self) -> str:
        return self._dest
    

    @dest.setter
    def dest(self, DEST) -> None:
        self._dest = DEST


    @property
    def data(self) -> List[str]:
        return self._data
    

    @data.setter
    def data( self, data: List[str] ) -> None:
        self._data = data


    def OpenFile(self):
        with open(self.path, "r") as file:
            file_content = file.read()
            list_hex_values = file_content.split()
            self.data = list_hex_values


    # down-sampling the colour intensity here, RRGGBB to 2-digit bitmap
    def CompressRGB(self) -> None:
        compressed_data = []
        
        for colour in self.data:
            if len( colour ) == 6:
                # colour extraction here, base 16
                r = int( colour[:2],  16 )
                g = int( colour[2:4], 16 )
                b = int( colour[4:],  16 )
                colour_average = ( r // 16, g // 16, b // 16 )
                colour_compressed = f"{(colour_average[0]<<4) + colour_average[1]:02x}"
                compressed_data.append( colour_compressed )
        
        self.data = compressed_data


    def CompressBW(self) -> None:
        compressed_data = []

        for pixel in self.data:
            if pixel == "0":
                compressed_data.append("00")
            elif pixel == "1":
                compressed_data.append("FF")
        
        self.data = compressed_data


    def AppendPrefix(self) -> None:
        revised_data = []

        for hex in self.data:
            revised_data.append( "0x" + hex )

        self.data = revised_data


    def Output(self) -> None:
        counter = 0
        with open("output.txt", "w+") as file:
            for itr in self.data:
                file.write(itr + ",")
                counter += 1
                if counter > 31:
                    file.write("\n")
                    counter = 0
            

    # interface
    def ConversionRGB(self) -> List[str]:
        self.OpenFile()
        self.CompressRGB()
        self.AppendPrefix()
        self.Output()
        return self.data
    

    def ConversionBW(self) -> List[str]:
        self.OpenFile()
        self.CompressBW()
        self.AppendPrefix()
        self.Output()
        return self.data

    
    def PrintData(self):
        print(self.data)
    

def main():
    arg = sys.argv
    argc = len( sys.argv )
    print("Your input arguments are -> ", arg, "argument count ->", argc)
    converter = Converter(arg[1], arg[2])
    # converted = converter.ConversionRGB()
    converted = converter.ConversionBW()

    print(converted)


if __name__ == "__main__":
    main()



