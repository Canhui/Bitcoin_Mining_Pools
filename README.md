### 1. Online Source Code for the Paper

## [*Measurement and Analysis of the Bitcoin Networks: A View from Mining Pools*](https://ieeexplore.ieee.org/document/9160462)

by Canhui Wang, Xiaowen Chu, Yang Qin 

Published in [*2020 6th International Conference on Big Data Computing and Communications (BIGCOM)*](https://ieeexplore.ieee.org/document/9355625), Jul 2020.

&nbsp; 


### 1. The `MiningPool()` Function

#### 1.1. Description

The `MiningPool()` function is used to obtain the mining pool label of blocks. 


#### 1.2. Usage

- Input Parameters: StartBlockID, EndBlockID.
- Return: a '.csv' file named 'miningpool.csv' under the same directory of the source code. 

#### 1.3. Example

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

&nbsp; 

### 2. The `BlockTime()` Function

#### 2.1. Description

In order to solve the inconsistent problem of system clock, ba la ba la...(TO DO)

&nbsp; 

### 3. Presentation Slide
The presentation slide is available here： https://github.com/Canhui/Bitcoin_Mining_Pools/blob/master/presentation_BIGCOM2020_July_25_2020.pdf
