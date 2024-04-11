import os
import random
import shutil

def dataset_process(data_dir='raw_dataset', base_dir='processed_dataset'):
    # Original dataset
    folder_names = os.listdir(data_dir)

    # Create train and test directories
    list_of_set = ['Train', 'Test']
    list_of_dir = ['0', '1', '2']
    for setlist in list_of_set:
        more_extended = os.path.join(base_dir, setlist)
        os.makedirs(more_extended, exist_ok=True)  # Use os.makedirs to create nested directories

    for folder_name in folder_names:
        if folder_name != '.DS_Store':
            class_dir = os.path.join(data_dir, folder_name)
            sample_names = os.listdir(class_dir)

            # Calculate 80% of images count
            total_images = sum(len(os.listdir(os.path.join(class_dir, sample))) for sample in sample_names if sample!='.DS_Store')
            print(total_images)
            train_count = int(0.8 * total_images)
            print('train_count',train_count)
            test_count = total_images - train_count
            print('test_count',test_count)

            # Create directories in train and test
            for setlist in list_of_set:
                for directory in list_of_dir:
                    os.makedirs(os.path.join(base_dir, setlist, directory), exist_ok=True)

            # Move images to train and test directories
            moved_train = 0
            moved_test = 0

            #subset of whole dataset
            subset_train_count = int(0.01*train_count)
            subset_test_count = int(0.01*test_count)
            
            for sample_name in sample_names:
                if sample_name != '.DS_Store':
                    sample_dir = os.path.join(class_dir, sample_name)
                    img_names = os.listdir(sample_dir)
                    for img_name in img_names:
                        if img_name != '.DS_Store':
                            img_path = os.path.join(sample_dir, img_name)
                            #for subset of dataset.If you want total dataset replace subset_train_count from train_count
                            if moved_train < subset_train_count:
                                # Move to train directory
                                shutil.copy2(img_path, os.path.join(base_dir, 'Train', folder_name, img_name))
                                moved_train += 1
                            elif moved_test < subset_train_count:
                                # Move to test directory
                                shutil.copy2(img_path, os.path.join(base_dir, 'Test', folder_name, img_name))
                                moved_test += 1
                            else:
                                break
            print('moved_train',moved_train)
            print('moved_test',moved_test)

dataset_process()
