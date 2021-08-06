#def candle(candles):
#    amount = 0
#    tallest = candles[0]
#    for candle in candles:
#        if candle > tallest:
#            tallest = candle
#    for candle in candles:
#        if candle == tallest:
#            amount += 1
#    return amount
#
#list = [1,2,3,4,5,5,5,6,6]
#
#print(candle(list))

s = '07:05:45PM'
def timeConversion(s):
    newString = list(s.partition('PM')[0].replace(':', ' '))
    print(newString)
    

timeConversion(s)