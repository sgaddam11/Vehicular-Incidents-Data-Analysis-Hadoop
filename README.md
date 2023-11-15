
UTILIZE HADOOP FOR DATA ANALYSIS <br/>
<br/>
The following commands are required to run the analysis after cloning into CS Cloud <br/>
<br/>
* Basic MapReduce Recipe (Python) cmdline:

hadoop jar  /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/nyc/nyc-traffic.csv -output /users-cloud-16fs/(your username)/output/job1-out -mapper ~/mapper.py -reducer ~/reducer.py -file ~/{mapper,reducer}.py
<br/> <br/>
* To view the output file: <br/>
hdfs dfs -cat /users-cloud-16fs/(your username)/output/job1-out/part-00000
