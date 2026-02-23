import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import csv
def create_dataset(data, look_back=1):
    X, Y = [], []
    for i in range(len(data) - look_back):
        a = data[i:(i + look_back)]
        X.append(a)
        Y.append(data[i + look_back])
    return np.array(X), np.array(Y)

data = pd.read_csv('../Rinse/total_csv/Download_total_astro-ph.csv')
paper_num = data['Paper_Num'].values.astype(float).reshape(-1, 1)
#归一化处理,缩小到[0,1]
scaler = MinMaxScaler()
paper_num_scaled = scaler.fit_transform(paper_num)

#滑动窗口size = 3
look_back = 3
#转换为时序数据集
X, Y = create_dataset(paper_num_scaled, look_back)

split_ratio = int(len(X) * 0.75)
#分为训练集和测试集
train_X, test_X = X[:split_ratio], X[split_ratio:]
train_Y, test_Y = Y[:split_ratio], Y[split_ratio:]

train_X = torch.tensor(train_X, dtype=torch.float)
test_X = torch.tensor(test_X, dtype=torch.float)
train_Y = torch.tensor(train_Y, dtype=torch.float)
test_Y = torch.tensor(test_Y, dtype=torch.float)

class PaperPredictionLSTM(nn.Module):
    def __init__(self):
        super(PaperPredictionLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=20, num_layers=2, batch_first=True)
        #input_size:输入数据的维度
        #hidden_size:隐藏层中神经元数量
        #num_layers:网络层数
        self.linear = nn.Linear(20, 1)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x[:, -1, :])
        return x

model = PaperPredictionLSTM()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


epochs = 200
loss_history = []

def train_model():
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(train_X)
        loss = criterion(outputs, train_Y)
        loss.backward()
        optimizer.step()
        #关闭梯度追踪,测试性能
        with torch.no_grad():
            model.eval()
            test_outputs = model(test_X)
            test_loss = criterion(test_outputs, test_Y)

        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch + 1}/{epochs}, Train Loss: {loss.item():.6f}, Test Loss: {test_loss.item():.6f}")
        loss_history.append((loss.item(), test_loss.item()))

    train_losses, test_losses = zip(*loss_history)

    plt.plot(train_losses, label='Train Loss')
    plt.plot(test_losses, label='Test Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def predict_future(model, num_predictions, init_seq):
    model.eval()
    predictions = []
    for _ in range(num_predictions):
        with torch.no_grad():
            pred = model(init_seq)
            predictions.append(pred.item())
            #预测结果用于下一次预测
            init_seq = torch.cat((init_seq[:, 1:, :], pred.view(1, 1, 1)), dim=1)

    return np.array(predictions)


train_model()
num_future_months = 6
#输入数据
last_known_data = paper_num_scaled[-look_back:]
last_known_data = torch.tensor(last_known_data, dtype=torch.float).unsqueeze(0)

#预测
future_preds = predict_future(model, num_future_months, last_known_data)
future_preds_unscaled = scaler.inverse_transform(future_preds.reshape(-1, 1))

print("以下是预测结果:"+"\n")
for idx, prediction in enumerate(future_preds_unscaled):
    print(f"{idx+7}月: {prediction[0]:.2f}")

csv_file = "Forecast_paperNum/Forecast_astro-ph.csv"
# 将数据写入CSV文件
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(["月份", "预测科目发表量"])
    # 循环遍历预测结果并写入CSV文件
    for idx, prediction in enumerate(future_preds_unscaled):
        month = idx + 7
        value = int(prediction[0])
        writer.writerow([f"{month}月", f"{value}"])
