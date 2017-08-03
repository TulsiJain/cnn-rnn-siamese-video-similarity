import numpy as np
import re
import itertools
from collections import Counter
import numpy as np
import time
import gc
import gzip
from random import random
import sys
from scipy import misc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
reload(sys)
sys.setdefaultencoding("utf-8")

class InputHelper(object):

    def getfilenames(self, line, base_filepath, mapping_dict, max_document_length):
        temp = []
        line = line.strip().split(" ")

        # Store paths of all images in the sequence
        for i in range(1, len(line), 1):
            if i < max_document_length:
                temp.append(base_filepath + mapping_dict[line[0]] + '/' + line[i] + '.png')
        
        #append-black images if the seq length is less than 20
        while len(temp) < max_document_length:
            temp.append(base_filepath + 'black_image.jpg')

        return temp


    def getTsvData(self, base_filepath, max_document_length, simplify):
        print("Loading training data from " + base_filepath)
        x1=[]
        x2=[]
        y=[]
        
        #load all the mapping dictonaries
        mapping_dict = {}
        print(base_filepath+'mapping_file')
        for line_no,line in enumerate(open(base_filepath + 'mapping_file')):
            mapping_dict['F' + str(line_no+1)] = line.strip()

        # Loading Positive sample file
        train_data=[]
        with open(base_filepath + 'positive_annotations.txt', 'r') as file1:
            for row in file1:
                temprow=row.split('/', 1)[0]
                temp=temprow.split()

                if(len(temp)>0 and temp[0][0]!='/'):
                    train_data.append(temp)
        assert(len(train_data)%7==0)

        l = []
        tags_simplify=['overlap','same']
        #simplify can only be: 'inverse','same','none'
        values_simplify=['inverse','same','none']
        assert(simplify in values_simplify)
        for exampleIter in range(0,len(train_data),7):
            if(simplify!='none'):
                if((train_data[exampleIter+4][0] in tags_simplify) and train_data[exampleIter+4][1]==simplify):
                    l.append(' '.join(train_data[exampleIter+1]))
                    l.append(' '.join(train_data[exampleIter+2]))
                else:
                    l.append(' '.join(train_data[exampleIter+1]))
                    l.append(' '.join(train_data[exampleIter+2]))


        # positive samples from file
        num_positive_samples = len(l)
        for i in range(0,num_positive_samples,2):
            if random() > 0.5:
                x1.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
            else:
                x1.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))

            y.append(1)#np.array([0,1]))


        # Loading Negative sample file
        l = []
        for line in open(base_filepath + 'negative_annotations.txt'):
            line=line.split('/', 1)[0]
            if (len(line) > 0  and  line[0] == 'F'):
                l.append(line.strip())
        
        # negative samples from file
        num_negative_samples = len(l)
        for i in range(0,num_negative_samples,2):
            if random() > 0.5:
                x1.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
            else:
                x1.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))

            y.append(0)#np.array([0,1]))
        
        return np.asarray(x1),np.asarray(x2),np.asarray(y)


    def getTsvTestData(self, base_filepath, max_document_length):
        print("Loading training data from " + base_filepath)
        x1=[]
        x2=[]
        y=[]
        
        #load all the mapping dictonaries
        mapping_dict = {}
        for line_no,line in enumerate(open(base_filepath + 'mapping_file')):
            mapping_dict['F' + str(line_no+1)] = line.strip()

        # Loading Positive sample file
        l = []
        for line in open(base_filepath + 'positive_annotations.txt'):
            line=line.split('/', 1)[0]
            if (len(line) > 0  and line[0] == 'F'):
                l.append(line.strip())

        # positive samples from file
        num_positive_samples = len(l)
        for i in range(0, num_positive_samples, 2):
            if random() > 0.5:
                x1.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
            else:
                x1.append(self.getfilenames(l[i+1], base_filepath, mapping_dict, max_document_length))
                x2.append(self.getfilenames(l[i], base_filepath, mapping_dict, max_document_length))

            y.append(1)#np.array([0,1]))

        return np.asarray(x1),np.asarray(x2),np.asarray(y)  
 
    def batch_iter(self, x1, x2, y, batch_size, num_epochs, conv_model_spec, shuffle=True):
        """
        Generates a batch iterator for a dataset.
        """
        data_size = len(y)
        temp = int(data_size/batch_size)
        num_batches_per_epoch = temp+1 if (data_size%batch_size) else temp
        
        for epoch in range(num_epochs):
            # Shuffle the data at each epoch
            if shuffle:
                shuffle_indices = np.random.permutation(np.arange(data_size))
                x1_shuffled=x1[shuffle_indices]
                x2_shuffled=x2[shuffle_indices]
                y_shuffled=y[shuffle_indices]
            else:
                x1_shuffled=x1
                x2_shuffled=x2
                y_shuffled=y
            for batch_num in range(num_batches_per_epoch):
                start_index = batch_num * batch_size
                end_index = min((batch_num + 1) * batch_size, data_size)
        if random()>0.5:
                yield(np.asarray(self.load_preprocess_images(x1_shuffled[start_index:end_index], conv_model_spec,True)),
            np.asarray(self.load_preprocess_images(x2_shuffled[start_index:end_index], conv_model_spec,True)),
                    y_shuffled[start_index:end_index])
        else:
                yield(np.asarray(self.load_preprocess_images(x1_shuffled[start_index:end_index], conv_model_spec,False)),
            np.asarray(self.load_preprocess_images(x2_shuffled[start_index:end_index], conv_model_spec,False)),
                    y_shuffled[start_index:end_index])
    
    
    def normalize_input(self, img, conv_model_spec):
        img = img.astype(dtype=np.float32)
        img = img[:, :, [2, 1, 0]] # swap channel from RGB to BGR
        img = img - conv_model_spec[0]
        return img

    def load_preprocess_images(self, seq_paths, conv_model_spec):
        batch_seq = []
        for img_paths in seq_paths:
            for img_path in img_paths:
                img_org = misc.imread(img_path)
                if(random()>0.5):
                    img_org=np.fliplr(img_org)
                    #h,w,c = img.shape
                    #noise = np.random.randint(0,30,(h, w))
                    #zitter = np.zeros_like(img)
                    #zitter[:,:,1] = noise  
                    #noise_added = cv2.add(img, zitter)
                    #img=noise_added
                img=img_org 
                img_normalized = self.normalize_input(img, conv_model_spec)
                img_resized = misc.imresize(np.asarray(img_normalized), conv_model_spec[1])
                batch_seq.append(np.asarray(img_resized))
        return batch_seq

    def dumpValidation(self,x1,x2,y,shuffled_index,dev_idx,i):
        print("dumping validation "+str(i))
        x1_shuffled=x1[shuffled_index]
        x2_shuffled=x2[shuffled_index]
        y_shuffled=y[shuffled_index]
        x1_dev=x1_shuffled[dev_idx:]
        x2_dev=x2_shuffled[dev_idx:]
        y_dev=y_shuffled[dev_idx:]
        del x1_shuffled
        del y_shuffled
        with open('validation.txt'+str(i),'w') as f:
            for text1,text2,label in zip(x1_dev,x2_dev,y_dev):
                f.write(str(label)+"\t"+text1+"\t"+text2+"\n")
            f.close()
        del x1_dev
        del y_dev
    
    # Data Preparatopn
    # ==================================================
    
    
    def getDataSets(self, training_paths, max_document_length, percent_dev, batch_size):
        simplify='same' #'inverse','none'
        x1, x2, y=self.getTsvData(training_paths, max_document_length, simplify)
        
        i1=0
        train_set=[]
        dev_set=[]

        dev_idx = -1*len(y)*percent_dev//100
        # Split train/test set
        # TODO: This is very crude, should use cross-validation
        x1_train_ordered, x1_dev_ordered = x1[:dev_idx], x1[dev_idx:]
        x2_train_ordered, x2_dev_ordered = x2[:dev_idx], x2[dev_idx:]
        y_train_ordered, y_dev_ordered = y[:dev_idx], y[dev_idx:]
        print("Train/Dev split for {}: {:d}/{:d}".format(training_paths, len(y_train_ordered), len(y_dev_ordered)))
     
        # Randomly shuffle data
        np.random.seed(131)
        shuffle_indices = np.random.permutation(np.arange(len(y_train_ordered)))
        x1_train = x1_train_ordered[shuffle_indices]
        x2_train = x2_train_ordered[shuffle_indices]
        y_train = y_train_ordered[shuffle_indices]

        # Randomly shuffle data
        np.random.seed(131)
        shuffle_indices = np.random.permutation(np.arange(len(y_dev_ordered)))
        x1_dev = x1_dev_ordered[shuffle_indices]
        x2_dev = x2_dev_ordered[shuffle_indices]
        y_dev = y_dev_ordered[shuffle_indices]

        #self.dumpValidation(x1,x2,y,shuffle_indices,dev_idx,0)
        del x1
        del x2

        temp = len(y_train)//batch_size
        sum_no_of_batches = temp + 1 if len(y_train%batch_size) else temp
        train_set=(x1_train,x2_train,y_train)
        dev_set=(x1_dev,x2_dev,y_dev)
        gc.collect()
        
        return train_set,dev_set,sum_no_of_batches
    

    def getTestDataSet(self, data_path, max_document_length):
        x1,x2,y = self.getTsvTestData(data_path, max_document_length)
        gc.collect()
        return x1,x2, y


def save_plot(val1, val2, xlabel, ylabel, title, axis, legend,path):
    pyplot.figure()
    pyplot.plot(val1, '*r--', val2, '^b-')
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.title(title)
    pyplot.axis(axis)
    pyplot.legend(legend)
    pyplot.savefig(path+'.pdf')
    pyplot.clf()

def compute_distance(distance, loss):
    d = np.copy(distance)
    if loss == "AAAI":
        d[distance>=0.5]=1
        d[distance<0.5]=0
    elif loss == "contrastive":
        d[distance>0.5]=0 
        d[distance<=0.5]=1
    else:
        raise ValueError("Unkown loss function {%s}".format(loss))
    return d
