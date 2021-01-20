def sum_arr(arr):
    toplam = 0
    for i in arr:
        toplam += i
    return toplam

def find_size(arr):
    if not arr:
        return 0
    arr.pop(0)
    return 1+find_size(arr)
num=390626
arr = [int(x) for x in str(num)]
print("Dizi :")
print(arr)
print("Dizi toplamı :")
toplam=sum_arr(arr)
print(toplam)
print("Dizi uzunluğu :")
length=find_size(arr)
print(length)