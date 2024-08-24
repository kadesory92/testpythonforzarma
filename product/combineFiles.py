import pandas as pd


def combine_csv_json():
    try:
        # Загрузка данных из файла CSV и JSON
        products_df = pd.read_csv('product/products.csv')
        sales_df = pd.read_json('product/sales.json')

        # Объединение двух фреймов данных в 'product_id'
        files_combined_df = pd.merge(products_df, sales_df, on='product_id', how='inner')

        # Агрегация продаж по продуктам
        sales_summary = files_combined_df.groupby(['product_id', 'product_name']).agg({'amount': 'sum'}).reset_index()

        # Сохранение окончательного массива в CSV-файле
        sales_summary.to_csv('product/result.csv', index=False)

        print(f"Объединенные данные были успешно сохранены в 'product/result.csv'.")
    except Exception as e:
        print(f"Произошла ошибка при объединении данных: {e}")