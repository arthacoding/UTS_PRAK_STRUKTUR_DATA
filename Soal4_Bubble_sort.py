def tukar(lists, i,j):
    lists[i], lists[j] = lists[j], lists[i]


def bubble(listsku):
    perubahan = True
    sesi = len(listsku)
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listsku[j] < listsku[j - 1]:
                perubahan = True
                tukar(listsku, j, j - 1)
            j += 1
        print(listsku)

        if not perubahan:
            print("hasil akhir = %s" % str(listsku))
        sesi -= 1


print("=========== Bubble Sort ===========")
print("sebelum Bubble Sort")
mylist= [75, 90, 65, 85, 70, 95, 80]
print(mylist)
print("Setelah Bubble Sort")
bubble(mylist)