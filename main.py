from db.dbConnect import connect, insert, createTable
# from optimizationScripts import optimization_script, script_optimization
from post.api import fetch_data_save
from product.combineFiles import combine_csv_json
from services import getUsers

if __name__ == '__main__':
    fetch_data_save()
    print("------------------------------------------------------------------------------------------")
    connect()
    print("------------------------------------------------------------------------------------------")
    createTable()
    print("------------------------------------------------------------------------------------------")
    insert()
    print("------------------------------------------------------------------------------------------")
    getUsers()
    print("------------------------------------------------------------------------------------------")
    combine_csv_json()
    print("------------------------------------------------------------------------------------------")
    # optimization_script()
    print("------------------------------------------------------------------------------------------")
    # script_optimization()