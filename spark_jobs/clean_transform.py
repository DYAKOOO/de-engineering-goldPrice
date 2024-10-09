from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, coalesce, lit, from_json
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DateType

def main():
    spark = SparkSession.builder.appName("GoldPriceCleanTransform").getOrCreate()
    
    # Set GCS configuration
    spark._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    
    schema = StructType([
        StructField("date", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("open", FloatType(), True),
        StructField("high", FloatType(), True),
        StructField("low", FloatType(), True)
    ])
    
    input_path = "gs://gold-price-raw-data/*.json"
    output_path = "gs://gold-price-processed-data/cleaned"
    
    print(f"Reading data from: {input_path}")
    
    # Read raw data as text
    raw_df = spark.read.text(input_path)
    print("Raw data sample:")
    raw_df.show(5, truncate=False)
    
    # Try to parse JSON
    try:
        df = spark.read.json(input_path, schema=schema)
        print("Successfully parsed JSON. Input data sample:")
        df.show(5)
    except Exception as e:
        print(f"Error parsing JSON: {str(e)}")
        print("Attempting to parse JSON manually...")
        df = raw_df.select(from_json(col("value"), schema).alias("parsed")).select("parsed.*")
    
    print(f"Input data count: {df.count()}")
    
    cleaned_df = df.select(
        to_date(col("date"), "yyyyMMdd").alias("date"),
        coalesce(col("price"), lit(0.0)).alias("price"),
        coalesce(col("open"), lit(0.0)).alias("open_price"),
        coalesce(col("high"), lit(0.0)).alias("high_price"),
        coalesce(col("low"), lit(0.0)).alias("low_price")
    ).filter(col("date").isNotNull())
    
    print("Cleaned data sample:")
    cleaned_df.show(5)
    print(f"Cleaned data count: {cleaned_df.count()}")
    
    print(f"Writing cleaned data to: {output_path}")
    cleaned_df.write.partitionBy("date").parquet(output_path, mode="overwrite")
    
    print("Data cleaning and transformation completed successfully")

if __name__ == "__main__":
    main()