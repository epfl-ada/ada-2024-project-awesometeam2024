from os import path
import os
import pickle
import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset

class MoviesSummaryDataset(Dataset):
    """
    A dataset implements 2 functions
        - __len__  (returns the number of samples in our dataset)
        - __getitem__ (returns a sample from the dataset at the given index idx)
    """

    def __init__(self, data_dir, filename, categories):
        super().__init__()
        if not path.isdir(data_dir):
            raise ValueError(f"The directory {data_dir} does not exist.")
        if not path.isfile(path.join(data_dir, 'plain', filename)):
            raise ValueError(f"The file {filename} does not exist in the directory {data_dir}.")
        
        self.filename = filename
        self.categories = categories

        binary_file_path = path.join(data_dir, 'bin', f"{filename}.pkl")
        if path.isfile(binary_file_path):
            with open(binary_file_path, 'rb') as f:
                self.data = pickle.load(f)
        else:
            self.data = pd.read_csv(path.join(data_dir, 'plain', filename), sep='\t', header=None, names=categories)
            os.makedirs(os.path.dirname(binary_file_path), exist_ok=True)
            with open(binary_file_path, 'wb') as f:
                pickle.dump(self.data, f)

    def __len__(self):
        """Return the total number of samples."""
        return len(self.data)

    def __getitem__(self, idx):
        """
        Args:
            idx (int): Index of the data item to retrieve.
        
        Returns:
            Sample (Tensor): A single data sample, optionally transformed.
        """
        if idx < 0 or idx >= len(self.data):
            raise IndexError(f"Index {idx} is out of bounds.")
        
        sample = self.data.iloc[idx]
        return sample
    
    def save_data(self, save_dir):
        """
        Save the dataset to a specified directory either as a binary file or as a CSV file.

        Args:
            save_dir (str): The directory where the data should be saved.
        """
        if not path.isdir(save_dir):
            raise ValueError(f"The directory {save_dir} does not exist.")
        
        csv_file_path = path.join(save_dir, f'{self.filename}')
        self.data.to_csv(csv_file_path, sep='\t', index=False)


class SomeDatamodule(DataLoader):
    """
    Allows you to sample train/val/test data, to later do training with models.
        
    """
    def __init__(self):
        super().__init__()