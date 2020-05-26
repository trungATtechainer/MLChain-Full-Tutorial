# import mlchain workflows library
from mlchain.workflows import Parallel,Task

# import time for measurement purposes
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

# TEST 1
# start = time.time() # start time
#
# # running a for loop through all the tasks
# r = []
# for item in img_list:
#     r.append(get_num(item))
# end = time.time()
#
# # printing results and processed time
# print (r)
# print('Total time: ', end - start)


# TEST 2
start = time.time() # start time

# Using Parallel
r = Parallel(
    tasks= [Task(get_num,i) for i in img_list], # listing the tasks
    max_threads=24 # no. of threads. 24 threads for 24 images to minimize run time
).run()

end = time.time() # end time

# printing result and time
print(r)
print('Total time: ', end - start)