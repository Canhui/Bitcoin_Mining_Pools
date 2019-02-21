# Bitcoin_Mining_Pools
Measurements and Analysis on Major Bitcoin Mining Pools

## 1. MiningPool()

**1.1. Description**
The `MiningPool()` function is used to obtain the mining pool label of blocks. 


**1.2. Usage**
- Input Parameters: StartBlockID, EndBlockID.
- Return: a '.csv' file named 'miningpool.csv' under the same directory of the source code. 

**1.3. Example**
Input
```
$ python MiningPool.py 502310 543698
```

Output
| blockid                     | miningpool |
|-----------------------------|------------|
| 502310 (i.e., StartBlockID) | ViaBTC     |
| ...                         | ...        |
| 543698                      | F2Pool     |
