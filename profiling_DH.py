import h5py

def explore_h5_file(file_path):
    # Open the H5 file
    with h5py.File(file_path, 'r') as f:
        # Recursively explore the file structure
        def print_structure(name, obj):
            if isinstance(obj, h5py.Dataset):
                print(f"Dataset: {name}, Shape: {obj.shape}, Data Type: {obj.dtype}")
                # Check if the dataset contains text data
                if obj.dtype == 'S':
                    print(f"Text Data: {obj[()][:10]}")  # Print first 10 elements if they are strings
                else:
                    print(f"Numeric Data: {obj[()][:1]}")  # Print first 10 elements if they are numbers
            elif isinstance(obj, h5py.Group):
                print(f"Group: {name}")
        
        # Explore the file structure
        f.visititems(print_structure)

# Example usage
# file_path = '/home/sslunder0/project/VideoQA/data/msvd/frame_feat/app_feat_train.h5'
# file_path = "/home/sslunder0/project/VideoQA/data/msvd/mot_feat/mot_feat_train.h5"
# file_path = "/home/sslunder0/project/VideoQA/data/msvd/qas_bert/bert_ft_train.h5"
file_path = "/home/sslunder0/project/VideoQA/data/msvd/region_feat_n/region_8c10b_train.h5"
explore_h5_file(file_path)
