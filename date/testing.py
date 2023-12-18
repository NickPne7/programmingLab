from date import Date

data = Date(12, 3, 1988)


print(data.bisestileCheck(1988))


nuovaData = Date(12,6,1988)
nuovaData = iter(nuovaData)

print(nuovaData.ritornaMax())

anno = 1980
dataTesting = Date(1, 1, anno)
iteraData = iter(dataTesting)



while anno < 5000:
    print(str(iteraData))
    next(iteraData)
    anno += 1