from PIL import Image
import sys
import math

inputFile = sys.argv[1]
outputFile = sys.argv[2]
imageXSize = str(int(sys.argv[3]))

image = Image.open(inputFile).convert(mode="RGB")
size = width,height = image.size
PerLine = 100 / width

ModuleCode = f'local UI = Instance.new("ScreenGui",game:GetService("Players").LocalPlayer.PlayerGui)\nUI.Name = game:GetService("HttpService"):GenerateGUID(false)\nlocal ImageFrame = Instance.new("Frame",UI)\nImageFrame.Name = "ImageFrame"\nImageFrame.BorderSizePixel = 0\nImageFrame.Size = UDim2.fromOffset({width-1}*{imageXSize},{height-1}*{imageXSize})\nfunction NewPixel(self,Color,Position,Size)\n	local Pixel = Instance.new("Frame",self)\n	Pixel.Name = string.format("%dx%d",Position.X,Position.Y)\n	Pixel.Position = UDim2.fromOffset((Position.X*Size)-Size,(Position.Y*Size)-Size)\n	Pixel.Size = UDim2.fromOffset(Size,Size)\n	Pixel.BackgroundColor3 = Color\n	Pixel.BorderSizePixel = 0\nend'

if (width*height)>40000:
    print("[Error] The max size of a image is 200x200 or 40000 pixels!")
    exit()

class RobloxENV:
    def V2(x,y):
        return f"Vector2.new({x},{y})"
    def C3(r,g,b):
        return f"Color3.fromRGB({r},{g},{b})"

def loadingbarSet(num):
    newPRINT = ""
    for INDEX in range(num):
        newPRINT = newPRINT+"█"
    print("  " + str(num) + "% " + newPRINT, end="\r")

for X in range(width):
    for Y in range(height):
        XY = X,Y
        Color = image.getpixel(XY)
        Roblox_Color = RobloxENV.C3(Color[0],Color[1],Color[2])
        Roblox_Vector2 = RobloxENV.V2(X,Y)
        ModuleCode = ModuleCode + f"\nNewPixel(ImageFrame,{Roblox_Color},{Roblox_Vector2},{imageXSize})"
    loadingbarSet(math.floor(PerLine * (X+1)))
newFile = open(outputFile,"w")
newFile.write(ModuleCode)
newFile.close()
print("")
