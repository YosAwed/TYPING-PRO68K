import x68k
import machine
import uctypes
import time
from struct import pack

w_data =[
  ["47","ﾎｴﾎｴ","ｺﾝﾆﾁﾊ","ﾝﾀｰ","ｳﾙｳﾙ","ｵﾋｻﾃﾞｽ","ﾎﾟ","ﾋｮﾋｮ","ﾌﾟﾌﾟﾌﾟ","ﾅﾝﾀﾗｶﾀﾗ","ﾊﾟﾓﾊﾟﾓ"],
  ["46","ｸﾏ","ｻﾙ","ｸｼﾞﾗ","ｱﾙﾏｼﾞﾛ","ﾅﾏｹﾓﾉ","ﾗｯｺ","ｵﾗﾝｳｰﾀﾝ","ｼﾏﾘｽ","ｴﾘﾏｷﾄｶｹﾞ","ﾗｲﾁｮｳ"],
  ["59","ﾌﾙｲｹﾔ","ｶﾜｽﾞﾄﾋﾞｺﾑ","ﾐｽﾞﾉｵﾄ","ﾅﾂｸｻﾔ","ﾂﾜﾓﾉﾄﾞﾓｶﾞ","ﾕﾒﾉｱﾄ","ﾒﾆｱｵﾊﾞ","ﾔﾏ","ﾎﾄﾄｷﾞｽ","ﾊﾂｶﾞﾂｵ"]
]

htime =[0,20,30,30]
ptime =[0,0,0,0]

# main
def main():
  # initialize screen
  x68k.crtmod(12,True)
  x68k.curoff()
  x68k.iocs(x68k.i.TXFILL,a1=pack('6h',0,0,0,1024,1024,0))
  x68k.iocs(x68k.i.TXFILL,a1=pack('6h',1,0,0,1024,1024,0))
  x68k.iocs(x68k.i.BOX,a1=pack('6h',0,0,511,511,0xffff,0xffff))

  while True:

    print("　    　　　　　  　　記録")
    print("１．チャッターコース  " + str(htime[1]) + "秒")
    print("２．動物さん　コース  " + str(htime[2]) + "秒")
    print("３．俳句さん　コース  " + str(htime[3]) + "秒")

    course = input("どのコースでいきますか？(1-3)")
    i = int(course)
    if i < 1 or i > 3:
        continue

    ptime[i] = time.time()

   for j in range(10):
        print(w_data[i-1][j+1])
        t = 1
        wlen = len(w_data[i-1][j+1])
        #for t in range(len(w_data[i-1][j+1])):
        while (t < wlen):
            #print("t" + str(t) ,end="")
            #q = inkey$(0)
            q = x68k.iocs(x68k.i.B_KEYINP) & 0xff
            #if q == 0:
            #    continue
            print(chr(q) ,end="")
            #if q != mid$(w_data[i-1][j],t,1)
            w = w_data[i-1][j+1]
            #print(w[t])
            if chr(q) != w[t]:
                #beep
                print("\a")
                #print( chr$(&H1D), end="")
                print("\033[1D" ,end="")
                print(chr(0x08), end="")
                continue
            t = t + 1
    print()

    ptime[i]= time.time() - ptime[i]
    print("所要時間" + str(ptime[i]) + "秒")
    print("一文字平均時間" + str(ptime[i]/int(w_data[i-1][0])) + "秒")

    if ptime[i] < htime [i]:
        print("新記録でっせ！")
        htime[i]=ptime[i]

  # cursor on
  x68k.curon()

if __name__ == "__main__":
  main()
