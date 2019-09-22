from PIL import Image
import sys
import math

player = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]
imageXSize = str(int(sys.argv[4]))

image = Image.open(inputFile)
size = width,height = image.size
PerLine = 100 / width

if (width*height)>40000:
    print("[Error] The max size of a image is 200x200 or 40000 pixels!")
    exit()

def loadingbarSet(num):
    newPRINT = ""
    for i in range(num):
        newPRINT = newPRINT+"█"
    print("  " + str(num) + "% " + newPRINT, end="\r")

if player == "@a":
    out = f"""function Image(player)
local ImageBY = Instance.new("ScreenGui",player:WaitForChild("PlayerGui"))
ImageBY.Name = "ImageBY"
ImageBY.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
local FrameMain = Instance.new("Frame",ImageBY)
FrameMain.BackgroundColor3 = Color3.new(0, 0, 0)
FrameMain.BorderSizePixel = 0
FrameMain.Size = UDim2.new(0, {width}, 0, {height})
function add(r,g,b,x,y,fm)
    local Frame = Instance.new("Frame",fm)
    Frame.BackgroundColor3 = Color3.new(r, g, b)
    Frame.BorderSizePixel = 0
    Frame.Position = UDim2.new(0, x*{imageXSize}, 0, y*{imageXSize})
    Frame.Size = UDim2.new(0, {imageXSize}, 0, {imageXSize})
end"""
    out = str(out)
    
    def NtoR(NValue):
        Count = 1 / 255
        RValue = Count * NValue
        return RValue

    def add(r,g,b,x,y):
        X = str(x)
        Y = str(y)
        newStr = f"""
add({r}, {g}, {b}, {X}, {Y}, FrameMain)"""
        global out
        out = out + newStr
    
    for r in range(width):
        for c in range(height):
            cor = x,y = r,c
            cRGBA = image.getpixel(cor)
            rR = str(NtoR(cRGBA[0]))
            rG = str(NtoR(cRGBA[1]))
            rB = str(NtoR(cRGBA[2]))
            add(rR,rG,rB,r,c)
        loadingbarSet(math.floor(float(str(PerLine * (r+1))[0:5])))
    newFile = open(outputFile,"w")
    out = out + str(f"""end
for i,plr in pairs(game.Players:GetPlayers()) do
    Image(plr)
    print(plr.Name)
    wait(1)
end""")
    newFile.write(out)
    newFile.close()
    print("")
else:
    out = f"""local player = game.Players['{player}']

local ImageBY = Instance.new("ScreenGui",player:WaitForChild("PlayerGui"))
ImageBY.Name = "ImageBY"
ImageBY.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

local FrameMain = Instance.new("Frame",ImageBY)
FrameMain.BackgroundColor3 = Color3.new(0, 0, 0)
FrameMain.BorderSizePixel = 0
FrameMain.Size = UDim2.new(0, {width}, 0, {height})
function add(r,g,b,x,y,fm)
    local Frame = Instance.new("Frame",fm)
    Frame.BackgroundColor3 = Color3.new(r, g, b)
    Frame.BorderSizePixel = 0
    Frame.Position = UDim2.new(0, x*{imageXSize}, 0, y*{imageXSize})
    Frame.Size = UDim2.new(0, {imageXSize}, 0, {imageXSize})
end"""
    out = str(out)
    
    def NtoR(NValue):
        Count = 1 / 255
        RValue = Count * NValue
        return RValue

    def add(r,g,b,x,y):
        X = str(x)
        Y = str(y)
        newStr = f"""
add({r}, {g}, {b}, {X}, {Y}, FrameMain)"""
        global out
        out = out + newStr
    
    for r in range(width):
        for c in range(height):
            cor = x,y = r,c
            cRGBA = image.getpixel(cor)
            rR = str(NtoR(cRGBA[0]))
            rG = str(NtoR(cRGBA[1]))
            rB = str(NtoR(cRGBA[2]))
            add(rR,rG,rB,r,c)
        loadingbarSet(math.floor(float(str(PerLine * (r+1))[0:5])))
    newFile = open(outputFile,"w")
    newFile.write(out)
    newFile.close()
    print("")
