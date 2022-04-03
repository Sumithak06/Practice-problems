def hanoi(disks,source,auxillary,target):
    if(disks==1):
        print('move disc 1 from rod', source,'to rod',target)
        return
    hanoi(disks-1,source,target,auxillary)
    print('move disk',disks,'from rod',source,'to rod',target)
    hanoi(disks-1,auxillary,source,target)


disks=int(input('enter no of disks'))
hanoi(disks,'A','B','C')