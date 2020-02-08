# All The APIs to get quotes 获取行情数据的接口

## SINA Finance 新浪财经

   - Common WebService API 通用webservice接口
      - WebSerivce URL: http://hq.sinajs.cn/list=
      - params: 
         - Shanghai Stock Exchange(SSE): sh + symbol, symbol here is 6 or 7 numbers as usual.
            - eg. sh000001
         - Shenzhen Stock Exchange(SZSE): sz + symbol, symbol here is 6 or 7 numbers as usual.
            - eg. sz600001
         - International Stock Index: int_ + symbol. 
            - eg. int_dji, int_nasdaq, int_sp500
         - Future: TICKER, 品种名 + 0 （数字0），代表品种连续; 如果是其他月份，使用品种名 + YYMM. 
            - 旧方法， 不再继续更新支持
            - eg. M0   
         - Future: hf_ + TICKER, 品种名 + 0 （数字0），代表品种连续; 如果是其他月份，使用品种名 + YYMM. 
            - 新方法， 支持部分数据
            - eg. hf_CHA50CFD

   - Future WebService API 新浪期货数据各品种代码（商品连续）API:
      - Minutes WebService URL: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLineXm?symbol=CODE
      - Daily WebService URL: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=CODE
      - 商品期货样例：
         - 5分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol=M0
         - 15分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine15m?symbol=M0
         - 30分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine30m?symbol=M0
         - 60分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine60m?symbol=M0
         - 日K线: http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=M1401
      - 股指期货样例
         - 5分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesMiniKLine5m?symbol=IF1306
         - 15分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesMiniKLine15m?symbol=IF1306
         - 30分钟: http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesMiniKLine30m?symbol=IF1306
         - 60分钟:http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesMiniKLine60m?symbol=IF1306
         - 日线: http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesDailyKLine?symbol=IF1306

   
   - Future Symbols
   
   | CFD Symbol | Content |
   |:-----------|:--------|
   | RB0 | 螺纹钢 |
   | AG0 | 白银 |
   | AU0 | 黄金 |
   | CU0 | 沪铜 |
   | AL0 | 沪铝 |
   | ZN0 | 沪锌 |
   | PB0 | 沪铅 |
   | RU0 | 橡胶 |
   | FU0 | 燃油 |
   | WR0 | 线材 |
   | A0 | 大豆 |
   | M0 | 豆粕 |
   | Y0 | 豆油 |
   | J0 | 焦炭 |
   | C0 | 玉米 |
   | L0 | 乙烯 |
   | P0 | 棕油 |
   | V0 | PVC |
   | RS0 | 菜籽 |
   | RM0 | 菜粕 |
   | FG0 | 玻璃 |
   | CF0 | 棉花 |
   | WS0 | 强麦 |
   | ER0 | 籼稻 |
   | ME0 | 甲醇 |
   | RO0 | 菜油 |
   | TA0 | 甲酸 |
   | CFF_RE_IF1307 | 股指期货好像没有期指连续 |

   - Future 旧方法返回值
   
   返回值为字符串，由许多数据拼接在一起，不同含义的数据用逗号隔开，顺序号从0开始。 
   
   | Index | Content |
   |:------|:--------|
   | 0 | 豆粕连续，名字  |
   | 1 | 145958，不明数字（难道是数据提供商代码？）  |
   | 2 | 3170，开盘价  |
   | 3 | 3190，最高价  |
   | 4 | 3145，最低价  |
   | 5 | 3178，昨日收盘价 （2013年6月27日）  |
   | 6 | 3153，买价，即“买一”报价  |
   | 7 | 3154，卖价，即“卖一”报价  |
   | 8 | 3154，最新价，即收盘价  |
   | 9 | 3162，结算价  |
   | 10 | 3169，昨结算  |
   | 11 | 1325，买 量  |
   | 12 | 223，卖 量  |
   | 13 | 1371608，持仓量  |
   | 14 | 1611074，成交量  |
   | 15 | 大连，大连商品交易所简称  |
   | 16 | 豆粕，品种名简称  |
   | 17 | 2013-06-28，日期 |

   - Future 新方法返回值
   
   | Index | Content |
   |:------|:--------|
   | 0 | 20号胶2003 |
   | 1 | 112959 |
   | 2 | 10780.000,开盘价 |
   | 3 | 10930.000,最高 |
   | 4 | 10710.000,最低价 |
   | 5 | 0.000,结算价 |
   | 6 | 10700.000,买价 |
   | 7 | 10715.000,卖价 |
   | 8 | 10710.000,最新价 |
   | 9 | 0.000,不明确 |
   | 10 | 10815.000,昨结价 |
   | 11 | 3,买量 |
   | 12 | 3,卖量 |
   | 13 | 17793.000,持仓量 |
   | 14 | 2718,成交量 |
   | 15 | 沪,所属市场 |
   | 16 | 20号胶,品种名称 |
   | 17 | 2020-01-02,日期 |
   | 18 | 0,不明确 |

   
## easyquotation

实时获取新浪 / 腾讯 的免费股票行情 / 集思路的分级基金行情

https://github.com/shidenggui/easyquotation
   
