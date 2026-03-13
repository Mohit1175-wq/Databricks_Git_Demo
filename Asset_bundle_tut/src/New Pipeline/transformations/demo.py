import dlt

@dlt.table
def demo_table():
  return spark.range(100)