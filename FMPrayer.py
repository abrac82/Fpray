#-*-coding:utf-8

import time
import datetime
now = time.localtime()

#각 날짜별로 베이스를 백업하는 시스템 만들기(전체 공용으로 사용 가능)
dtime = datetime.date.today()
dhour = datetime.time.hour
dt = dtime.isoformat()
dtt = dt[2:4] + dt[5:7] + dt[8:10] #dtt 는 현재 시각을 160101로 나타내줌
dm = dtime.month

# 각 달별 구역 입력 하여, 카운팅 할 준비

mcount = {2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}


print(">김해교회 월삭기도회 출석 정리 프로그램")

print(">베이스 파일을 로딩 합니다...")


#Fpray라는 뜻은 새벽기도라는 뜻

# 한 사람당 한 클래스를 쓰기로 결정하여, 속성을 '이름', '구역', '출석 월' 로 준다.

class Fpray:
    def __init__ (self, a_name, a_parish=[], a_month=[]):
        self.name = a_name
        self.parish = a_parish
        self.month = a_month

    def add_month(self,month_value):   #달 리스트에 추가하는 정의
        self.month.append(month_value)
        self.month = sorted(list(set(self.month)))




#이름과 교구를 불러서 클래스 안에 넣어주는 코드

open_names = open("TBase.txt", 'r') #베이스 파일을 지정하는 곳

#먼저 클래스에 집어 넣기 전에 정리를 좀 해야 겠다.

names_before1 = []

#Tbase에서 names_plus로 한 줄씩 읽어서 여기에 리스트로 기록한다.
#그리고 나면, TbaseClean에다가 중복을 제거하고 순서대로 정렬하여 리스트로 만든다.

while 1 :
    names_plus = open_names.readline().rstrip()
    if not names_plus: break
    names_before1.append(names_plus)
    #print(names_before1)

TbaseClean = sorted(list(set(names_before1))) #네임즈 비포의 역할은 여기까지

print("비교전: ",TbaseClean)
a = 0
while 1:
    if a +1 >= len(TbaseClean):
        break
    f = TbaseClean[a]

    print("a",a)
    #print("첫번째 대상",f)

    g = TbaseClean[a+1]
    #print("두번째 대상 %s \n" % g)

    print("첫째:",f[0:4])
    print("둘째:",g[0:4])
    r = f[0:4]
    f = g[0:4]

    #print("렝스",len(f))



    if r != f:
        print("첫째:",f[0:4])
        print("둘쨰:",g[0:4])
        print(">>>>>걸린대상: %s \n"% f)
        #i = TbaseClean.index(f[0:4])
        #print("삭제됨",i)
        #TbaseClean.pop(i)



    elif a >= len(TbaseClean):
        print("이걸 들어갔나?")
        break

    else:
        print("패스함")
        pass
    a = a + 1
print("비교후: ",TbaseClean)





#print(">>>>>>>티베이스 클린:",TbaseClean) # 깔끔하게 정리된 티베이스 클린 변수가 생겨남

open_names.close()



#티베이스 클린에다가 TXT 파일로 새로 생성

#TbaseClean2 = open("TbaseClean.txt", 'w') #티베이스클린2라는 변수를 이용해서, 티베이스 클린TXT를 생성한다.

#for x in range(0,len(TbaseClean)): #티베이스클린1 을 이용해서 다시 내려 쓰기 해야 한다.
    #TbaseClean2.write(TbaseClean[x]+"\n")

#TbaseClean2.close()
#내려 쓰기 완료


#>>>>>>>>>>>>> 아래 부터는 클래스를 입력한다.
names_before = [] #임시 이름 파일, 클래스 단계의 이름을 만들기 전의 리스트

prayers = [] #클래스 단계의 이름 보관 리스트
exlist = 0 #구역이 안적힌 리스트 숫자
exname = [] #구역이 안적힌 성도의 명단


#백업을 날짜별로 실시

bh = now.tm_hour
bm = now.tm_min

ba = 'backupbase%s_%s_%s.txt' % (dtt, bh, bm)
backuptxt = open(ba, 'w') #베이스 백업용

open_names2 = open("TbaseClean.txt", 'r') #정리했던 티베이스클린 베이스 txt 에서 읽는다.
names_before2 = [] #네임즈 비포어1과 구분하기 위해서 사용. 1은 정리할 때 사용했다.

#베이스 파일을 로딩 하는 코드
print(">>>>>>>>>>>>>>>>>>>>>>>>>> 여기하는 중")
#print("베이스파일 재차 로딩")
while 1:
    #print("베이스 파일 프레이어로 쓰는 루프 시작")
    names_plus = open_names2.readline().rstrip()  #rstrip() 을 붙여줘야, \n 같은 문자가 사라짐
    #names_plus는 리스트에서 이름과 구역을 받은 뒤에, 분리 하기 전에, 임의로 설정한 변수
    if not names_plus: break
    names_before2.append(names_plus)
    forclass = names_plus.split() #클래스를 만들기 위한 변수

    try:
        #print("포클래스",forclass[0])
        namef = forclass[0]
        parish = forclass[1]
        prayer = Fpray(namef, parish)
       # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>구역함께 프레이어에 들어가는 이름 확인",prayer)

        backuptxt.write(namef) #백업에 기록하는 코드
        backuptxt.write(parish +'\n') #백업에 기록하는 코드

    except:
        namef = forclass[0]
        parish = []
        prayer = Fpray(namef, parish)
        exlist = exlist + 1
        #print("구역 없이 프레이어에 들어가는 이름 확인",prayer)
        exname.append(namef) #구역이 안적힌 이름을 기록하는 코드
        backuptxt.write(namef +'\n')
    prayers.append(prayer)



    # 클래스로 불러와서, 그 클래스는 prayer 라는 리스트에 저장을 시켜 놓는다.


    #print(namef)
    #print(parish)
backuptxt.close() #Tbase 백업 마무리

print("")
print(">>>베이스 파일 로딩 및 백업 완료<<<")

for x in range(0,len(prayers)):
    print(prayers[x].name,end=" ")
    print(prayers[x].parish)

#print("네임즈 비포어2",names_before2)


#names = sorted(list(set(names_before)))

#print("이름을 정리=",names)


# >>>>>>>>>>>>>>>>클래스 로딩 후 결과 정리를 보여주기 위함

classnamebefore = []
#print("프레이어 클래스 출력",prayers)
for x in range(0, len(prayers)):
    #print(">>>>>>>>>>>프레이어 클래스의 이름을 출력하는지 확인 중 ",prayers[x].name)
    classnamebefore.append(prayers[x].name)

classname = sorted(classnamebefore)
numname = len(classname)

print("베이스에 로딩 된 명단",classname, '총 %d 명' % numname)
print("명단 중에 구역이 안 적힌 성도 = ",exname, "총", exlist, "명")


#매달별 파일의 이름을 가져 와서 클래스와 이름을 비교하고 같으면, 해당 월을 추가하는 코드

print(">>>달 별 명단을 로딩 합니다.")


names_before3 = []
errmonth = []
fattendname = []
fattendmonth = []
fattend = [] #새로운 달에 새로 추가된 이름
fmonth = 2 #현재 달을 나타내는 변수
last_month = None


for x in range(2,13): #매 달별로, TXT를 읽어서 이름을 비교하여 클래스에 월을 추가하기 시작

    try:
        addmonth = 'T%d월.txt' % fmonth #백업하는 내용 아님, 실행 코드
        open_names = open(addmonth, 'r')
        print(">%d월 명단을 출력합니다" % fmonth)
        last_month = fmonth

        while True : #해당 월의 이름을 모두 불러 들이는 루프
            names_plus = open_names.readline().rstrip() #rstrip() 을 붙여줘야, \n 같은 문자가 사라짐
            if not names_plus:
                print("네임 플러스로 정지")
                break
            names_before3.append(names_plus)




            print(names_plus,end=" ") #그냥 보여 주는 출력

            for x in range(0,len(prayers)): #클래스 길이만큼 반복

                #print("함보자",len(prayers))
                a = prayers[x].name
                print("비교이름",names_plus)
                print(a)
                if  a == names_plus: #클래스의 이름과 비교하여 같은지를 밝힘
                    print(">>>>>>>>>>>>>비교하는 이름",prayers[x].name)

                    prayers[x].add_month(fmonth) #이름이 같을 경우, 클래스에 month에 달 숫자를 추가
                    if prayers[x].parish != []: #빈 리스트를 month에 안넣으려고 하는 코드
                        mcount[fmonth].append(prayers[x].parish) #mcount2~12에 출석한 구역을 기록해 넣는 코드
                        print(prayers[x].name + "성도님은 구역이 기록 되었습니다.")
                        print("확인",mcount)
                        print(prayers[x])

                        print(names_before3.pop(),':',fmonth,'월 출석 기록됨') # 등록된 이름을 제거하는 코드
                        break






        while 2: #새로 등록된 이름을 클래스 '월'에 추가하는 코드
            if not names_before3: break
            print(names_before3[-1],":", fmonth,"월 추가된 새이름", )
            prayer = Fpray(names_before3.pop())
            prayers.append(prayer)



        print()




        fmonth = fmonth + 1
    except:
        errmonth.append(fmonth)
        fmonth = fmonth + 1
        print("열외되었음")




print(">>>베이스 업데이트")



#addbase = "newbase%s.txt" % dtt
#print(addbase)
#여기가 기존의 Tbase 파일을 덮는 코드

newbase = []
newbasetxt = open("Tbase1.txt", 'w')

for x in range(0,len(prayers)):
    namef = prayers[x].name
    parish = prayers[x].parish
    print(namef,parish, end="")
    newbasetxt.write("%s " % namef)
    try:
        newbasetxt.write(parish + '\n')
        print('')

    except:
        print(" = 구역이 입력되어 있지 않습니다")
        newbasetxt.write('\n')


newbasetxt.close()


print(">>>베이스 기록된 최종 인원: ",len(prayers),"명")


print(">>>월별 명단을 출력 완료했습니다.\n")

print(">>>다음과 같은 달은 입력되지 않았습니다 - ",errmonth, "<<총 %d 달>>" % len(errmonth),"\n")


#레포트 기록하는 코드를 시작합니다.

report = open("report%s.txt" % dtt, 'w')

re = report.write

report.write("<%s월 월삭기도회 출석 리포트> \n \n" % dm)

re("최근 기록 중 가장 많은 인원이 출석한 구역 TOP3 (최근 입력: %s월까지) \n" % last_month)

m = last_month - 1

pcount = mcount[m] #달과 함께 구역 리스트
report1 = []
report3 = []
report4 = []

print(">>>>>>>>>>>>>>>>>>>>>>>여기 하는 중 >>>>>>>>>>>>>>>>>>>>>>")

print("계산하는 달",m)
print("엠카운트 확인",mcount)
print("피카운트 확인",pcount)

for mm in range(0,len(pcount)):
    a = pcount[mm] #구역 이름 번호를 나타냄
    report1.append(str(a) + "구역 출석인원: " + str(pcount.count(a)) +"명") #레포트용으로 사용, 구역과 출석 인원
    report3.append(a) #계산하는 달의 구역만 나열
    #set 사용하기 위하여 리스트화 시킴



report2 = sorted(list(set(report1)))
print("리포트1", report1)
print("리포트2", report2) #중복 내용을 제거하고, 순서대로 나열
print("리포트3", report3)
try:#만약에 리포트3에 [] 있으면 제거
    report3.remove([])
    print("리포트 3 괄호를 제거함",report3)

except:
    pass

try:# 할 수 있으면 정리
    report4 = sorted(report3)
    print("리포트 4정리 중",report4)

except:
    pass
print("리포트4의 결과", report4)

#차례로 보여주기 위하여 set화 시켰음 다시 출력물 만들어야 함


print(">>>>>>>>>>>>>>>>>>>>>>>> 이제 통계 쪽 하고 있음")

parishrank = []
parishrank2 = []

b = 1
c = 1
d = 0

#print(report4[0])
#print(report4[1])
st = 1 #큰 루프 횟수
ac = 0
fdel = 0
pc = 0 # 큰 수들을 비교 함
cp = 0 # 큰 수가 몇개인지 카운트

#for aa in range(0,3):
while x:
    print(">>>>>>>%s 큰 루프 시작합니다 \n" % st)# % aa)
    st = st + 1


    for m1 in range(0,len(report4)):



        print(">>>>>>>>>>>>>>>>>>>>>%s 작은 루프시작할때" % m1,report4)
        a = report4[m1] #구역 이름 번호를 나타냄
        #ac2 = ac + 1
        #print("ac2",ac2)
        #print("report4[ac2]",len(report4))

        #print("뭐때문이고?",ac2)
        m2 = m1+1
        if m2 == len(report4): #이걸 안하면 out of range가 뜸
            break


        a1 = report4[m2]
        print("순서가 맞는지 확인",a)


        print("구역1 확인", a)
        print("구역2 확인", a1)
        print("b 확인",b)
        print("c확인",c)
        print("cp확인",cp)

        #if len(report4) == 1:
        #    print("길이로 스탑합니다")
        #    break

        #이제 비교 시작!!
        if a1 != a: #다르면 비교하여 순위 명단에 보내든지 말든지 결정
            if c < b : #c는 전 단계에서 차출 될 때 가졌던 갯수, b는 현재 루프 중에 쌓인 갯수
                print("1번바퀴")


               # if b >= c:
                parishrank.insert(0, b) #순위 명단 리스트
                parishrank.insert(0, a)
                c = b
                print(">>>입력되는 현황 파악",parishrank,"\n")
                #del report4[0:b]
                # ac = ac - b

                b = 1
                cp = cp + 1
                print("cp확인",cp)
                break

            elif c == b:
                if cp >= 3:
                    parishrank.insert(0, b)
                    parishrank.insert(0, a)
                    cp = cp
                    print("2번바퀴")
                    print(parishrank)
                    break

                elif cp < 3:
                    parishrank.insert(0, b)
                    parishrank.insert(0, a)
                    cp = cp + 1
                    print("3번바퀴")
                    print(parishrank)
                    break

            else:
                print("4번 바퀴")
                b = 1


        elif a == report4[m1]:
            b = b +1
            ac = ac + 1
            print(">>계속 갑니다. 고 합니다")



        #elif len(parishrank) == 2:
           # del report4[0:b]
           # print("두개 남았을때",parishrank)
            #print(report4)
            #st = st - b + 1
           # break


        else:
            print("문제 있습니다.")

    if len(report4) <= 0:
        print("길이로 스탑합니다.")
        break

    del report4[0:c]

    ac = ac -b +1

    #if c < pc: #pc는 바로 전의 뽑힌 구역의 숫자
    #    if cp >= 3: #cp 는 카운팅 하는 수
     #       break
#
    pc = c

    c = 1




#print(parishrank.pop())

print("구역 랭킹", parishrank)

#>>>>>>>>>>>>>>>>>>>이제 구역 랭킹을 순서대로 정리

od = 0

while x :

    print("od갯수",od)
    print("렝스길이",len(parishrank))
    if od >= len(parishrank)/2:

        break
    if b >= len(parishrank):
        break

    print("비의 길이",b)

    a = parishrank[od] #첫번째 구역 이름
    b = parishrank[od+2] #두번째 구역 이름
    c = parishrank[od+1] #첫번째 출석 수
    d = parishrank[od+3] #두번째 출석 수

    print("구역이름1",a)
    print("출석수1",c)
    print("구역이름2",b)
    print("출석수2 %s \n " % d)

    if c < d:
        del parishrank[od:od+4]
        print("지운 상태 확인",parishrank)
        parishrank.insert(od,b)
        parishrank.insert(od+1,d)

        parishrank.insert(od+2,a)
        parishrank.insert(od+3,c)
        print("바꿈처리1",parishrank)




    elif c == d :
        if a < b:
            del parishrank[od:od+4]

            parishrank.insert(od,b)
            parishrank.insert(od+1,d)

            parishrank.insert(od+2,a)
            parishrank.insert(od+3,c)
            print("바꿈처리2",parishrank)



    else:
        od = od + 2

print("순서 바뀌었나 확인",parishrank)

# 여기까지 완성 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 구역 랭킹 3위까지 골라 주는 코드
od = 1 #리스트에서 2칸씩 넘어 다니면서 출석 수만 체크하도록
count = 0

while x :
    if b >= len(parishrank):
        break

    a = parishrank[od]
    b = parishrank[od+2]

    if a != b:
        od = od + 2
        count = count + 1
        if count >= 3:
            break

    elif a == b:
        count = count + 1
        od = od + 2
        if od >= len(parishrank)/2:
            break

print("%s 월 구역별 출석 순위" % m)

sunwi = 1

# 출석 순위를 출력하는 코드

od = 1 #리스트에서 2칸씩 넘어 다니면서 출석 수만 체크하도록
count = 0

while x :
    if b >= len(parishrank):
        break

    a = parishrank[od]
    b = parishrank[od+2]

    if a != b:
        print("%s등 : %s 구역, 출석인원 %s명" % (count+1, parishrank[od-1], parishrank[od]))
        od = od + 2
        count = count + 1
        if count >= 3:
            print("1번으로 정지")
            break


    elif a == b:
        print("%s등 : %s 구역, 출석인원 %s명" % (count+1, parishrank[od-1], parishrank[od]))
        count = count + 1
        od = od + 2
        if od >= len(parishrank)/2:
            print("2번으로 정지")
            break






