from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def main():
    
    spark = SparkSession.builder.appName("GoldPriceCleanTransform").getOrCreate()
    
    # Set GCS configuration
    spark._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    

    schema = StructType([
        StructField("date", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("open_price", DoubleType(), True),
        StructField("high_price", DoubleType(), True),
        StructField("low_price", DoubleType(), True)
    ])

    input_path = "gs://gold-price-processed-data/cleaned"
    print(f"Reading data from: {input_path}")
    df = spark.read.schema(schema).parquet(input_path)

    print("Schema of input data:")
    df.printSchema()

    print("Input data sample:")
    df.show(5, truncate=False)

    print("Data types of columns:")
    df.dtypes

    # Convert date from string to date type
    df = df.withColumn("date", to_date(col("date")))

    # Ensure price columns are of DoubleType
    for column in ["price", "open_price", "high_price", "low_price"]:
        df = df.withColumn(column, col(column).cast(DoubleType()))

    print("Schema after transformations:")
    df.printSchema()

    print("Data sample after transformations:")
    df.show(5, truncate=False)

    print(f"Input data count: {df.count()}")

    output_table = "de-goldprice.gold_price_dataset.gold_prices"
    print(f"Writing data to BigQuery table: {output_table}")
    
    df.write \
        .format("bigquery") \
        .option("table", output_table) \
        .option("temporaryGcsBucket", "gold-price-temp-bucket") \
        .mode("overwrite") \
        .save()

    print("Data loaded to BigQuery successfully")

    # Verify data in BigQuery
    bq_df = spark.read.format("bigquery").option("table", output_table).load()
    print("Data in BigQuery:")
    bq_df.show(5, truncate=False)
    print(f"BigQuery data count: {bq_df.count()}")

if __name__ == "__main__":
    main()