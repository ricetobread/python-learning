#menghitung tinggi badan Mhs
def tinggiBadan(tinggi):
    tB=int(input("Masukkan tinggi badan="))
    while not tB==0:
        tinggi.append(tB)
        tB=int(input("masukkan tinggi badan="))
def cetakElemen(tinggi):
    for i in range(len(tinggi)):
        print(tinggi[i],end=" ")
def averageTB(tinggi):
    sums=0
    counter=0
    rata=0
    for i in range(len(tinggi)):
        counter=counter+1
        sums=sums+tinggi[i]
    rata=sums/counter
    return rata
        
def main():
    listTb=[]
    tinggiBadan(listTb)
    cetakElemen(listTb)
    print("\nrataTB=",averageTB(listTb))
main()