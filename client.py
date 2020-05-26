from mlchain.client import Client
import cv2

image_name = '19.png' # downloaded image

def get_num(image_name):
    # tell the system to use the model currently hosting in localhost, port 5000
    model = Client(api_address='http://localhost:5000',serializer='json').model(check_status=False)

    # import our image
    img = cv2.imread(image_name)

    # get model response on image
    res = model.image_predict(img)

    # print result
    return res

if __name__ == '__main__':
    print(get_num(image_name))