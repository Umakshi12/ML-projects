from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

# #left rotate of array
# arr = [1,2,3,4,5]
# temp = arr[0]
# for i in range(1,len(arr)):
#     arr[i-1]=arr[i]
# arr[len(arr)-1]=temp
# print(arr)

# d= int(input())
# temp = arr[0:d]
# for i in range(d,(len(arr))):
#     arr[d] = arr[i-d]
# for k in range(len(arr)-d,len(arr)):
#     arr[i] = temp[]
# arr[len(arr)-d] = temp[]
    