import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import Dataset
import torch.optim as optim
from sklearn.preprocessing import StandardScaler

EPOCHS = 150
BATCH_SIZE = 64
LEARNING_RATE = 0.01
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class FeatureDataset(Dataset):

    def __init__(self, file_name):
        file_out = pd.read_csv(file_name)
        x = file_out.iloc[:, 0:-1]
        y = file_out.iloc[:, -1]

        # Feature  Scaling
        sc = StandardScaler()
        x_train = sc.fit_transform(x)
        y_train = y

        self.x_train = torch.tensor(x_train, dtype=torch.float32).to(DEVICE)
        self.y_train = torch.tensor(y_train).to(DEVICE)

    def __len__(self):
        return len(self.y_train)

    def __getitem__(self, idx):
        return self.x_train[idx], self.y_train[idx]


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(2, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        logits = self.model(x)
        return logits


model = NeuralNetwork()
model.to(DEVICE)
feature_set = FeatureDataset('air_quality.csv')
train_loader = torch.utils.data.DataLoader(feature_set, batch_size=32, shuffle=True)

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)


def binary_acc(y_pred, y_test):
    y_pred_tag = torch.round(torch.sigmoid(y_pred))

    correct_results_sum = (y_pred_tag == y_test).sum().float()
    acc = correct_results_sum / y_test.shape[0]
    acc = torch.round(acc * 100)

    return acc


for e in range(1, EPOCHS + 1):
    epoch_loss = 0
    epoch_acc = 0
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()

        y_pred = model(X_batch)

        loss = criterion(y_pred, y_batch.unsqueeze(1).float())
        acc = binary_acc(y_pred, y_batch.unsqueeze(1).float())

        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
        epoch_acc += acc.item()

    print(f'Epoch {e + 0:03}: | Loss: {epoch_loss / len(train_loader):.5f} | Acc: {epoch_acc / len(train_loader):.3f}')
