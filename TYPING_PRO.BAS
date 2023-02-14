   10 screen 2,0,1,1
   20 dim str w_data(3,10)={"47","ﾎｴﾎｴ","ｺﾝﾆﾁﾊ","ﾝﾀｰ","ｳﾙｳﾙ","ｵﾋｻﾃﾞｽ","ﾎﾟ","ﾋｮﾋｮ","ﾌﾟﾌﾟﾌﾟ","ﾅﾝﾀﾗｶﾀﾗ","ﾊﾟﾓﾊﾟﾓ"
   30                      ,"46","ｸﾏ","ｻﾙ","ｸｼﾞﾗ","ｱﾙﾏｼﾞﾛ","ﾅﾏｹﾓﾉ","ﾗｯｺ","ｵﾗﾝｳｰﾀﾝ","ｼﾏﾘｽ","ｴﾘﾏｷﾄｶｹﾞ","ﾗｲﾁｮｳ"
   40                      ,"59","ﾌﾙｲｹﾔ","ｶﾜｽﾞﾄﾋﾞｺﾑ","ﾐｽﾞﾉｵﾄ","ﾅﾂｸｻﾔ","ﾂﾜﾓﾉﾄﾞﾓｶﾞ","ﾕﾒﾉｱﾄ","ﾒﾆｱｵﾊﾞ","ﾔﾏ","ﾎﾄﾄｷﾞｽ","ﾊﾂｶﾞﾂｵ"}
   50 str q
   60 int i,t
   70 dim int time(3),htime(3)={0,20,30,30}
   80 while (1)
   90 print"　　　　　　　　　　　　　記録"
  100 print"１．チャッターコース",htime(1);"秒"
  110 print"２．動物さん　コース",htime(2);"秒"
  120 print"３．俳句さん　コース",htime(3);"秒"
  130 input "どのコースでいきますか？(1-3)";i
  140 if i<1 or i>3 then continue
  150    time(i)=val(right$(time$,2))+val(mid$(time$,4,2))*60
  160    for j=1 to 10
  170       print w_data(i-1,j)
  180       for t=1 to len(w_data(i-1,j))
  190          q=inkey$(0):print q;
  200          if q="" then t=t-1:continue
  210          if q<>mid$(w_data(i-1,j),t,1) then beep :t=t-1:print chr$(&H1D);:continue
  220       next
  230    print
  240    next
  250    time(i)=val(right$(time$,2))+val(mid$(time$,4,2))*60-time(i)
  260    print "所要時間";time(i);"秒"
  270    print "一文字平均時間";time(i)/val(w_data(i-1,0));"秒"
  280    if time(i)<htime(i) then print"新記録でっせ！":htime(i)=time(i)
  290 endwhile
