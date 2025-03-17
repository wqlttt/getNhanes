import getMetrics

years = ['2007-2008', '2009-2010', '2011-2012', '2013-2014']
features = ['seqn', "diq010"]
x = "E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES\\"
metricName = "diq"
getMetrics.get_DEET(years,features,x,metricName)