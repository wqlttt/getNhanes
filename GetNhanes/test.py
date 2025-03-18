import getMetrics

years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014','2015-2016','2017-2018']
features = ['seqn','pfq020']
path = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
metricName = "pfq"
output_dir="E:\\NHANES_pythonpages\\getNhanes"
getMetrics.get_nhanes_data(years,features,path,metricName,output_dir)
