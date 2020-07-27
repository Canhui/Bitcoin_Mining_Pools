# Bitcoin_Mining_Pools
Measurements and Analysis on Major Bitcoin Mining Pools

<br />

## 1. The `MiningPool()` Function

<br />

**1.1. Description**\
The `MiningPool()` function is used to obtain the mining pool label of blocks. 


<br />

**1.2. Usage**
- Input Parameters: StartBlockID, EndBlockID.
- Return: a '.csv' file named 'miningpool.csv' under the same directory of the source code. 

<br />

**1.3. Example**\
Input
```
$ python MiningPool.py 502310 543698
```



Output

| blockid | miningpool |
| ------ | ------ |
| 502310 | ViaBTC |
| ... | ... |
| 543698 | F2Pool |


<br />
<br />

## 2. The `BlockTime()` Function

<br />

**2.1. Description**

In order to solve the inconsistent problem of system clock, ba la ba la...(TO DO)

<br />

## 3. Presentation Slide
The presentation slide is available here： https://github.com/Canhui/Bitcoin_Mining_Pools/blob/master/presentation_BIGCOM2020_July_25_2020.pdf
