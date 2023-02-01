//@version=5
strategy("SS THE ONE?", overlay=true, initial_capital=30000, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

length14 = 14
length34 = 34
length3 = 3

rsiMA1 = ta.sma(ta.rsi(close, length14), length14)
rsiMA2 = ta.sma(ta.rsi(close, length14), length3)
ema34 = ta.ema(close, length34)

longCondition = (ta.crossover(rsiMA1, 55) and (strategy.position_size < 1) and time(timeframe.period, "0930-1550"))

exitlongCondition1 = (ta.crossunder(rsiMA1, 65) and (strategy.position_size > 0) and time(timeframe.period, "0930-1600"))
exitlongCondition2 = (ta.crossunder(rsiMA1, 47) and (strategy.position_size > 0) and time(timeframe.period, "0930-1600"))
exitlongCondition3 = (ta.crossunder(ta.ema(close, 1), ta.ema(close, 12)) and (strategy.position_size > 0) and time(timeframe.period, "0930-1600"))

shortCondition = (ta.crossunder(rsiMA2, 47) and (strategy.position_size > -1) and time(timeframe.period, "0930-1550"))

exitshortCondition1 = (ta.crossover(rsiMA2, 50) and (strategy.position_size < 0) and time(timeframe.period, "0930-1600"))
exitshortCondition2 = (ta.crossover(ta.ema(close, 1), ta.ema(close, 16)) and (strategy.position_size < 0) and time(timeframe.period, "0930-1600"))

if ((longCondition) and time(timeframe.period, "0900-1550"))
strategy.entry("Long", strategy.long)

else if ((exitlongCondition1 or exitlongCondition2 or exitlongCondition3) and time(timeframe.period, "0930-1600"))
strategy.close("Long")

if ((shortCondition) and time(timeframe.period, "0930-1550"))
strategy.entry("Short", strategy.short)

else if ((exitshortCondition1 or exitshortCondition2) and time(timeframe.period, "0930-1600"))
strategy.close("Short")

buystring = "a=ACCNT b=buy q=285 t=market e=alpacapaper s=AMZN"
sellstring = "a=ACCNT c=position t=market e=alpacapaper s=AMZN"

buyshortstring = "a=ACCNT b=short q=285 t=market e=alpacapaper s=AMZN"
sellshortstring = "a=ACCNT c=position t=market e=alpacapaper s=AMZN"

if ((longCondition) and time(timeframe.period, "0930-1550"))
alert(buystring, alert.freq_once_per_bar)

if ((exitlongCondition1 or exitlongCondition2 or exitlongCondition3) and (strategy.position_size > 0) and time(timeframe.period, "0930-1600"))
alert(sellstring, alert.freq_once_per_bar)

if ((shortCondition) and time(timeframe.period, "0930-1550"))
alert(buyshortstring, alert.freq_once_per_bar)

if ((exitshortCondition1 or exitshortCondition2) and (strategy.position_size < 0) and time(timeframe.period, "0930-1600"))
alert(sellshortstring, alert.freq_once_per_bar)
