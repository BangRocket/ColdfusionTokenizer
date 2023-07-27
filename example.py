import os
import torch
import torch.utils.data as data

from typing import List
from tokenizer import Tokenizer

class CFDataset(data.Dataset):

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.code = []
        self.labels = []

        for filename in os.listdir(data_dir):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r') as f:
                code = f.read()
                label = filename.split('.')[0]

                tokenizer = Tokenizer(code)
                tokens = tokenizer.get_tokens()

                self.code.append(tokens)
                self.labels.append(label)

    def __len__(self):
        return len(self.code)

    def __getitem__(self, index):
        code = self.code[index]
        label = self.labels[index]

        print(code)
        print(label)

        tokens = torch.tensor([token.to_tensor() for token in code]).reshape(1)
        return tokens, label


def main():
    dataset = CFDataset('data/')
    dataloader = data.DataLoader(dataset, batch_size=16)

    for i, (tokens, label) in enumerate(dataloader):
        print(tokens)
        print(label)


if __name__ == '__main__':
    main()
