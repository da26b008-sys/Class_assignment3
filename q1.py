def printer_queue_order(pages):
    Doclist=[i for i in range(len(pages))]
    front=0
    output_list=[]
    while pages!=[]:
        if pages[front]==1:
            output_list.append(Doclist[front])
            Doclist.pop(front)
            pages.pop(front)
            if len(pages)!=0:
                front=front%len(pages)
        else:
            pages[front]-=1
            front=(front+1)%len(pages)
        
    return output_list
if __name__=='__main__':
    print(printer_queue_order([1,1,1]))