import scipy.io


def write_txt(f,list_ids):
    f.write('\n'.join(list_ids))
    f.close()

train_test = scipy.io.loadmat("splits.mat")
train_images = tuple([int(x) for x in train_test["trainNdxs"]])
test_images = tuple([int(x) for x in train_test["testNdxs"]])
print("%d training images" % len(train_images))
print("%d test images" % len(test_images))


train_ids=[str(i-1)+'.jpg' for i in train_images]
test_ids=[str(i-1)+'.jpg' for i in test_images]

train_list_file=open('train.txt','a')
write_txt(train_list_file,train_ids)

test_list_file=open('test.txt','a')
write_txt(test_list_file,test_ids)
