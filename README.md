# Cloud Computing HW4

This project includes the mapper and reducer functions to get the number of different vehicle types involved in accidents in NYC.

To run the analysis, copy `mapper.py` and `reducer.py` to the Hadoop gate and run the command

```hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/tatavag/nyc.data -output hadoop-output```

The output can be found in the `hadoop-output` directory. My results are found in `result.json`.
