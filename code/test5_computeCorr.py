# -*- coding: UTF-8 -*-
from pkg.extract_modified import extract_train
from pkg.extract_modified import head_and_tails
from pkg.helper import read_data

if __name__ == "__main__":
    print("start!")
    data_lines = read_data("training_data.txt")
    
    with open("data_frame.txt", 'w') as fout1:
        for data in data_lines:
            target, feature = extract_train(data)
            fout1.write(str(target['pri_stress_position'])+'\t'+str(feature['vol_number'])+'\t'+str(feature['head'])+'\t'+str(feature['tail1'])+'\t'+str(feature['tail2'])+'\t'+str(feature['tail3'])+'\t'+str(feature['tail4'])+'\t'+str(feature['tail5'])+'\n')
            # pri_stress_position	vol_number	head	tail1	tail2	tail3	tail4


    print('Done!')