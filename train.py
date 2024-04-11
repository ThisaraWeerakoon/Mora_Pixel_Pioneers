import keras
from src.dataloader import VIPDataset
from src.model import OpticNet
import time
import keras.backend as K
import gc
from src.utils import callback_for_training
from src.visualize import plot_loss_acc
#from tensorflow.keras.models import load_model

def train(data_dir, logdir, input_size, batch_size, epoch, snapshot_name):
    

    train_batches, test_batches = VIPDataset(batch_size, input_size, data_dir)
    num_of_classes = 3
    train_size = 14430
    test_size = 3608 
    # Clear any outstanding net or memory    
    K.clear_session()
    gc.collect()

    # Calculate the starting time
    
    start_time = time.time()

    # Callbacks for model saving, adaptive learning rate
    cb = callback_for_training(tf_log_dir_name=logdir,snapshot_name=snapshot_name)


    # Loading the model
    model = OpticNet(input_size,num_of_classes)


    # Training the model
    #history = model.fit_generator(train_batches, shuffle=True, steps_per_epoch=train_size //batch_size, validation_data=test_batches, validation_steps= test_size//batch_size, epochs=epoch, verbose=1, callbacks=cb)

    history = model.fit(train_batches, shuffle=True, steps_per_epoch=train_size //batch_size, validation_data=test_batches, validation_steps= test_size//batch_size, epochs=epoch, verbose=1, callbacks=cb)

    end_time = time.time()

    print("--- Time taken to train : %s hours ---" % ((end_time - start_time)//3600))

    # Saving the final model
    if snapshot_name == None :
        model.save('OpticNet.h5')
       
    else :    
        model.save(snapshot_name+'.h5')
    
    plot_loss_acc(history,snapshot_name)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    #parser.add_argument('--dataset', type=str, required=True, help='Choosing between 2 OCT datasets', choices=['processed_dataset','Kermany2018'])
    # parser.add_argument('--batch', type=int, default=8)
    # parser.add_argument('--input_dim', type=int, default=224)
    # parser.add_argument('--datadir', type=str, required=True, help='path/to/data_directory')
    # parser.add_argument('--epoch', type=int, default=30)
    # parser.add_argument('--logdir', type=str)
    # parser.add_argument('--weights', type=str,default=None, help='Resuming training from previous weights')
    # parser.add_argument('--model',type=str, default=None,help='Pretrained weights for transfer learning',choices=['ResNet50',
    #                              'MobileNetV2','Xception'])
    # parser.add_argument('--snapshot_name',type=str, default=None, help='Name the saved snapshot')
    # args = parser.parse_args()

    datadir='processed_dataset'
    logdir='logs'
    input_dim=224
    batch=8
    epoch=10
    snapshot_name= None
    train(datadir, logdir, input_dim, batch,epoch, snapshot_name)