#排序算法

#简单选择 n^2
def select_sore(origin_item,comp=lambda x,y:x<y):
    item=origin_item[:]
    for i in range(len(item)-1):
        min_index=i
        for j in range(i+1,len(item)):
            if(comp(item[j],item[min_index])):
                min_index=j
        item[i],item[min_index]=item[min_index],item[i]
    return item

#冒泡排序
def bubble_sort(origin_item,comp=lambda x,y:x>y):
    item=origin_item[:]
    for i in range(1,len(item)):
        for j in range(len(item)-1):
            if(comp(item[j],item[j+1])):
                item[j],item[j+1]=item[j+1],item[j]
    return item

#归并
def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    print(items)
    if len(items) < 2:
        print('if')
        return items[:]
    mid = len(items) // 2
    print(mid)
    print('left')
    left = merge_sort(items[:mid], comp)
    print('right')
    right = merge_sort(items[mid:], comp)
    print("return")
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1< len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items
origin_item=[1,5,3]
print(merge_sort(origin_item))