# mlchain Pipeline
from mlchain.workflows.pipeline import Pipeline,Step

# time for measurement purposes
import time

# import get_num function from client.py
from client import get_num

# create list of images
img_list = ['17.png', '18.png', '30.png', '31.png', '32.png', '41.png',
            '44.png', '46.png', '51.png', '55.png', '63.png', '68.png',
            '76.png', '85.png', '87.png', '90.png', '93.png', '94.png',
            '97.png', '112.png', '125.png', '137.png', '144.png',
            '146.png'] # contains 24 images

for i in range(len(img_list)):
    img_list[i] = 'data/' + img_list[i] # specify PATH toward images

def get_square(x):
    time.sleep(1)
    return x**2

# TEST 1
# # traditional approach
# start = time.time() #start time
#
# # run a for loop through both function and return result
# r = []
# for item in img_list:
#     number = get_num(item) # get number from image (~2s)
#     square_num = get_square(number) # get square (~1s)
#     r.append(square_num)
#
# end = time.time() # end time
#
# print(r) # print results
# print('Total time: ', end - start)

# TEST 2
start = time.time() # start time

# pipeline architecture
pipeline = Pipeline(
    Step(get_num, max_thread = 24),
    Step(get_square, max_thread = 12)
)

#print results
r = pipeline(*img_list) # get results (* since input has to be multiple values)
end = time.time() # end time

print(r)
print('Total time: ', end - start)
