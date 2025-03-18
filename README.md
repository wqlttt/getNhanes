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


### 使用示范
```python
import getMetrics

years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014','2015-2016','2017-2018']
features = ['seqn','pfq020']
path = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
metricName = "pfq"
output_dir="E:\\NHANES_pythonpages\\getNhanes"
getMetrics.get_nhanes_data(years,features,path,metricName,output_dir)

```
