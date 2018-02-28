import os
from multiprocessing import Pool
from multiprocessing import Manager
import hashlib

def innerCopyFile(fileName, srcPath, desPath,q):
    # just copy the srcFile to desFile
    srcFileName = srcPath+'/'+fileName
    desFileName = desPath+'/'+fileName
    with open(srcFileName,'rb') as fr:
        with open(desFileName,'wb') as fw:
            for i in fr:
                fw.write(i)
    q.put(desFileName)
    #print("%str"%desFileName)
    #fr = open(srcFileName,'r')
    #text = fr.read()
    #fw = open(desFileName,'x')
    #fw.write(text)
    #fr.close()
    #fw.close()
    #q.put(desFileName)

def copyFile(fileName, srcPath, desPath, q):
    if (not os.path.exists(srcPath)):
        print("srcPath is not exist")
        return None

    if (not os.path.exists(desPath)):
        try:
            os.mkdir(desPath)
        except NotImplementedError:
            print("mkdir %s error"%desPath)

    innerCopyFile(fileName, srcPath, desPath, q)    

def copyFileDone(fileName, srcPath, desPath, q):
    print("%s was copied done."%fileName)
    #digSrc = hashlib.sha512()
    #digDes = hashlib.sha512()
    #srcFileName = srcPath+'/'+fileName
    #desFileName = desPath+'/'+fileName
    #with open(srcFileName,'rb') as srcF:
    #    for i in srcF:
    #        digSrc.update(i.encode('utf8'))
    #print("%s hexdig is"%(srcFileName, digSrc.hexdig()))
    #with open(desFileName,'rb') as desF:
    #    for i in desF:
    #        digDes.update(i.encode('utf8'))
    #print("%s hexdig is"%(srcFileName, digDes.hexdig()))

if __name__ == '__main__':
    srcPath = input("Please input you wanna to copy directory: ")
    desPath = srcPath+"-副本"
    while os.path.isdir(desPath):
        desPath = desPath+"-副本"
    p = Pool(4)
    q = Manager().Queue()
    allFiles = os.listdir(srcPath)
    allNum = len(allFiles)
    num = 0
    fRecord = open("record.txt", 'a+')
    fRecord.write("allNum is %d"%allNum)
    fRecord.write('\n')

    for i in allFiles:
        p.apply_async(func=copyFile, args=(i, srcPath, desPath, q))
    p.close()
    
    #fRecord = open("record.txt", 'x')
    while num < allNum:
        fileName = q.get()
        num += 1
        rate = num/allNum*100
        #print("in while... num is %d"%num)
        #fRecord.write("in while... num is %d"%num)
        #print("%s is copied done."%fileName)
        #fRecord.write("%s is copied done."%fileName)
        digSrc = hashlib.sha512()
        digDes = hashlib.sha512()
        srcFileName = srcPath+'/'+fileName.split('/')[-1]
        desFileName = desPath+'/'+fileName.split('/')[-1]
        with open(srcFileName,'rb') as srcF:
            for i in srcF:
                    digSrc.update(i)
                    #print("%s hexdig is %s"%(srcFileName, digSrc.hexdigest()))
            #fRecord.write("%s hexdig is %s"%(srcFileName, digSrc.hexdigest()))
            #fRecord.write('\n')
        with open(desFileName,'rb') as desF:
            for i in desF:
                    digDes.update(i)
                    #print("%s hexdig is %s"%(desFileName, digDes.hexdigest()))
            #fRecord.write("%s hexdig is %s"%(desFileName, digDes.hexdigest()))
            #fRecord.write('\n')
        if (digSrc.hexdigest() == digDes.hexdigest()):
            fRecord.write("%s copied right"%srcFileName)
            fRecord.write('\n')
        print("Current rate is %.1f%%"%rate)
    
    fRecord.close()
    p.join()
    print("Done")
