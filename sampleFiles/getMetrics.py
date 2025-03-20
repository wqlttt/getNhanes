import GetNhanes.getMetrics as getMetrics

years = ['1999-2000','2001-2002','2003-2004','2005-2006','2007-2008', '2009-2010', '2011-2012', '2013-2014','2015-2016','2017-2018']
# 使用小写指标
features = ['seqn','ridageyr']
path = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
metricName = "demo"
output_dir="E:\\NHANES_pythonpages\\getNhanes"
getMetrics.get_nhanes_data(years,features,path,metricName,output_dir)