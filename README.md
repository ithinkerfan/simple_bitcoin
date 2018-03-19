# simple_bitcoin --python

# blockchain 由四个部分组成，分别为block(区块), chain(链), transaction(交易), node(节点)。

  1、 block的结构：
    (a) index : 区块高度；
    (b) timestamp : 时间戳；
    (c) transactions : 区块写入的交易；
    (d) proof : 当达到hash的前四位为0的时候，所进行的计算量；
    (e) previous_hash : 前一个区块的 hash 值；

  2、 chain的有效性判断：
    当前一个区块的hash值等于当前区块中 previous_hash 值时，则判断当前区块为有效的区块。

  3、 transaction 的结构：
    sender：发送者的地址；
    recipient：接收者的地址；
    amount：交易金额。

# mine(矿工)
  通过 get 方式进行挖矿，当达到 hash 的前四位为0的时候，就将区块写入链中。

# full chain(查看完整的链数据)
  通过 get 方式获取数据，进行遍历显示。

# new transaction(新交易)
  通过 post 方式获取交易数据，写入块中。

  
