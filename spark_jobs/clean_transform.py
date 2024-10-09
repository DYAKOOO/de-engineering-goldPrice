from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, coalesce, lit
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
    
    try:
        # Check if files exist
        file_df = spark.read.format("json").option("inferSchema", "true").load(input_path)
        if file_df.count() == 0:
            print(f"No files found in {input_path}")
            return
        
        # Read raw data
        df = spark.read.json(input_path, schema=schema)
        print("Input data sample:")
        df.show(5)
        print(f"Input data count: {df.count()}")
        
        cleaned_df = df.select(
            to_date(col("date"), "yyyy-MM-dd").alias("date"),
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
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()