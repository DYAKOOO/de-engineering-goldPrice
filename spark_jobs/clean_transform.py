from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, coalesce, lit
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DateType

def main():
    spark = SparkSession.builder.appName("GoldPriceCleanTransform").getOrCreate()

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
    df = spark.read.json(input_path, schema=schema)

    print("Input data sample:")
    df.show(5)
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