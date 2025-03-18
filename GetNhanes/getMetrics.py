import os
import pandas as pd

def get_DEET(years, features, basepath,metricName):
    """

    :param years: 选择年份列表
    :param features: 选择想要的指标
    :param basepath: 基础路径
    :param metricName: 指标名称

    示例:
    # years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014']
    # basepath = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
    # features = ['seqn', "urxdee", "urxdea", "urxdhd"]
    # metricName = deet

    :return:
    """

    # 固定
    dirlist = ["Laboratory" ,"Questionnaire" ,"Examination" ,"Dietary"]

    exist_files = []
    exist_years = []

    for year in years:
        for dir in dirlist:
            each_file =  basepath + year + "\\" +dir + "\\tsv\\"
            try:
                files = [file for file in os.listdir(each_file) if
                         file.startswith(metricName) and file.endswith(".tsv")]  #数据统一从tsv中取得
                if files == []:
                    pass
                else:
                    exist_years.append(year)
                    print(f"找到的文件: {year}---{files}")

                # Add the full path of each matching file to exist_file
                for file in files:
                    full_path = os.path.join(each_file, file)
                    exist_files.append(full_path)

            except FileNotFoundError:
                print(f"找不到目录: {each_file}")
            except Exception as e:
                print(f"访问时出错 {each_file}: {e}")


    for exist_file in exist_files:
        try:
            # 读取 TSV 文件
            df = pd.read_csv(exist_file, sep="\t", low_memory=False)
            # 检查是否包含所需的列
            if all(col in df.columns for col in features):
                # 提取所需的列
                df_subset = df[features]
                year = exist_file.split('\\')[4]
                # 指定输出文件路径
                output_file_path = f"E:\\NHANES_pythonpages\\getNhanes\\{year}_{metricName}.csv"
                # 保存到 CSV 文件
                df_subset.to_csv(output_file_path, index=False, encoding='utf-8')
                print(f"{year} 数据保存成功，文件路径：{output_file_path}")
            else:
                print(f"{year} 数据中缺少所需的列：{features}")
        except Exception as e:
            print(f"{year} 数据读取失败：{e}")


if __name__ == '__main__':
    years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014', '2015-2016', '2017-2018']
    features = ['seqn', "bpq020"]
    path = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
    metricName = "bpq"
    get_DEET(years,features,path,metricName)