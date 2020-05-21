class EDD:  
    def __init__(self, congViec, P, D):
        self.congViec = congViec
        self.P = P
        self.D = D
    def display(self):
        print(self.congViec, end='\t\t')
        print(self.P, end='\t\t')
        print(self.D)
   
# creating list        
danhSachCongViec = list() 

n   =   int(input('Số Lượng Công Việc: '))
  
# appending instances to list  
for i in range(n):
    congViec = input(f'Công Việc {i+1} - Tên Công Việc: ')
    P = input(f'Công Việc {i+1} - P: ')
    D = input(f'Công Việc {i+1} - D: ')
    danhSachCongViec.append(EDD(congViec, P, D)) 

# danhSachCongViec.sort(key = lambda x:x.D) 
# my sort
for i in range(n):
    for j in range(i+1, n):
        if int(danhSachCongViec[i].D) > int(danhSachCongViec[j].D):
            tmp = danhSachCongViec[i] 
            danhSachCongViec[i] = danhSachCongViec[j]
            danhSachCongViec[j] = tmp
print("--------------------------EDD------------------------------------------")
print('Thứ Tự Điều Độ Công Việc Là:') 
for i in range(n): 
    # print(cv.congViec, cv.P, cv.D)
    danhSachCongViec[i].display()

print("-----------------------------------------------------------------------")
danhSach_C = []
temp = 0
for i in danhSachCongViec:
    temp += int(i.P)
    danhSach_C.append(temp)

print('Danh sach C:', danhSach_C)

danhSach_L = []
for i in range(n):
    if int(danhSachCongViec[i].D) >= danhSach_C[i]: danhSach_L.append(0)
    else: danhSach_L.append(danhSach_C[i] - int(danhSachCongViec[i].D))

print('Danh sach L:', danhSach_L)

tong_P = 0
tong_C = 0
tong_L = 0
for cv in danhSachCongViec:
    tong_P += int(cv.P)    
for i in range(len(danhSach_C)):
    tong_C += danhSach_C[i]
for i in range(len(danhSach_L)):
    tong_L += danhSach_L[i]

print("-----------------------------------------------------------------------")
print("Tổng Thời Gian Hoàn Thành: ", tong_C)
print("Độ Hữu Dụng: ", (tong_P/tong_C)*100)
print("Số Lượng Công Việc Trung Bình: ", tong_C/tong_P)
print("Tổng Thời Gian Trễ Chậm: ", tong_L/5)