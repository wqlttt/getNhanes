# getNhanes



## 原始数据目录
首先确保自己的数据是以这样的形式存放的
```
01_NHANES/
├── 1999-2000/
│   ├── Demographics/
│   │   ├── codebook/
│   │   ├── htm/
│   │   ├── tsv/
│   │   ├── update/
│   │   ├── varLabel/
│   │   └── xpt/
│   ├── Dietary/
│   ├── Examination/
│   ├── Laboratory/
│   ├── LimitedAccess/
│   └── Questionnaire/
├── 2001-2002/
└── 2003-2004/
└── 2005-2006/
└── 2007-2008/
```

## 模块说明
### 获取指标模块(参数介绍)
1. 确定自己需要的年份
2. 需要提取的特征列(默认为全部)
3. 你的数据的原始目录(需要遵循上述树状图)
4. 从NHANES中查看文件前缀(如需要提取DEET的数据,NHANES中的文件为DEET_I.xpt)
5. 指定输出目录(默认为当前位置,output_dir=None)
6. 是否需要合并数据(默认为不需要,merge_output=False)


```python
def get_nhanes_data(years, features, basepath, metric_prefix,
                    output_dir=None, merge_output=False):
    """
    从NHANES数据集中提取并合并指定指标数据

    :param years: 需要处理的年份列表（例如 ['2007-2008', '2009-2010']）
    :param features: 需要提取的特征列（None表示所有列，必须包含'seqn'或文件包含'seqn'）
    :param basepath: NHANES数据存储的根目录
    :param metric_prefix: 目标指标的文件名前缀（如'DEET'）
    :param output_dir: 输出目录（默认为当前目录下的nhanes_output）
    :param merge_output: 是否合并所有文件（默认False）
    """
```


#### 使用示范
```python
from GetNhanes import getMetrics

years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014','2015-2016','2017-2018']
features = ['seqn','pfq020']
path = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
metricName = "pfq"
output_dir="E:\\NHANES_pythonpages\\getNhanes"
getMetrics.get_nhanes_data(years,features,path,metricName,output_dir)

```

### phenoage 计算

公式支持:


$\begin{align*}
xb = & -19.90667 \\
& + (-0.03359355) \times \text{albumin_gL} \\
& + 0.009506491 \times \text{creat_umol} \\
& + 0.1953192 \times \text{glucose_mmol} \\
& + 0.09536762 \times \text{lncrp} \\
& + (-0.01199984) \times \text{lymph} \\
& + 0.02676401 \times \text{mcv} \\
& + 0.3306156 \times \text{rdw} \\
& + 0.001868778 \times \text{alp} \\
& + 0.05542406 \times \text{wbc} \\
& + 0.08035356 \times \text{age}
\end{align*}$

$
m = 1 - \exp\left(-\frac{1.51714 \times \exp(xb)}{0.007692696}\right)
$


$
\text{phenoage0} = \frac{\log\left(-0.0055305 \times \log(1 - m)\right)}{0.09165} + 141.50225
$

1. albumin_gL的计算:albumin_gL -> albumin*10 -> `LBXSAL`
   - 1999年使用 `LAB18`
   - 2001年使用 `L40_B`
   - 2003年使用 `L40_C`
   - 2005-2017年使用 `BIOPRO`

2. creat_umol -> creat*88.4017 -> `LBXSCR`
   - 1999年的LBXSCR =(1.013*LBXSCR+0.147)  使用 `LAB18`
   - 2001年没有LBXSCR这个指标,BioAge使用LBDSCR指标  使用 `L40_B`
   - 2003年 使用 `L40_C`
   - 2005年使用LBXSCR=(-0.016+0.978*LBXSCR) `BIOPRO`
   - 2007-2017 使用 `BIOPRO`

3. glucose_mmol -> glucose -> `LBXSGL`
   - 1999年使用 `LAB18`
   - 2001-2003年使用 `L40`
   - 2005-2017年使用 `BIOPRO`

4. lncrp -> log(1+crp)　-> `LBXCRP`
   - 1999年 使用 `LAB11`
   - 2001年 使用 `L11_B`
   - 2003年 使用 `L11_C`
   - 2005-2010年 使用 `CRP`
   - 2015-2017年 `LBXCRP`=`LBXHSCRP`/10 使用 `HSCRP`中的`LBXHSCRP`

5. lymph -> `LBXLYPCT`
   - 1999年 使用 `LAB25`
   - 2001-2003年 使用 `L25`
   - 2005-2017年 使用 `CBC`

6. mvc -> `LBXMCVSI`
   - 1999年 使用 `LAB25`
   - 2001-2003年 使用 `L25`
   - 2005-2017年 使用 `CBC`

8. rdw -> `LBXRDW`
   - 1999年 使用 `LAB25`
   - 2001-2003年 使用 `L25`
   - 2005-2017年 使用 `CBC`

9. alp -> `LBXSAPSI`
   - 1999年 使用 `LAB18`
   - 2001年没有 `LBXSAPSI` 这个指标,BioAge使用LBDSAPSI指标  使用 `L40_B`
   - 2003年 使用 `L40_C`
   - 2005-2017 使用`BIOPRO`

10. wbc -> `LBXWBCSI`
    - 1999年 使用 `LAB25`
    - 2001-2003年 使用 `L25`
    - 2005-2017年 使用 `CBC`

11. age -> `RIDAGEYR`
    - 1999到2017 使用 `DEMO`