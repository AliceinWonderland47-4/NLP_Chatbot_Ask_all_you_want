# 1. Import Libraries
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from simpletransformers.classification import ClassificationModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

df = pd.read_csv('Combined Data.csv')  # 总数据集
# print(df)  # 53043行，3列

# Encoding Labels
le = LabelEncoder()
df['status'] = le.fit_transform(df['status'])


def preprocess(sentence):
    # Convert to string and lowercase
    sentence = str(sentence).lower()

    # Remove hashtags
    sentence = re.sub(r'#\S+', '', sentence)

    # Remove mentions
    sentence = re.sub(r'@\S+', '', sentence)

    # Remove punctuation and numbers
    sentence = re.sub(r'[^\w\s]', '', sentence)  # Keeps alphanumeric characters and whitespace
    sentence = re.sub(r'\d+', '', sentence)  # Removes numbers

    # Normalize whitespace
    sentence = ' '.join(sentence.split())

    # Remove URLs
    sentence = re.sub(r'http\S+', '', sentence)

    return sentence


if __name__ == '__main__':
    # Apply preprocessing to the text data
    # df['statement'] = df['statement'].map(lambda s: preprocess(s))
    # %%
    # Shuffle the data and split it into 70% training and 30% development
    df = df.sample(frac=1, random_state=42).reset_index(drop=False)  # Shuffling the data
    # %%
    # Split into training (70%) and development (30%)
    train_df, dev_df = train_test_split(df, test_size=0.3, random_state=42)

    # %%
    # Save the training and development datasets into separate CSV files
    train_df.to_csv('train_data.csv', index=True)
    dev_df.to_csv('dev_data.csv', index=True)

    # 训练模型
    df_train = pd.read_csv('train_data.csv')  # 训练集
    # print(df_train)  # 37130行，3列

    # np.set_printoptions(threshold=np.inf)

    model1 = ClassificationModel('distilbert', 'distilbert-base-cased', num_labels=8, use_cuda=False, args={
        "reprocess_input_data": True,
        "use_cached_eval_features": False,
        "overwrite_output_dir": True,
        "num_train_epochs": 1}
                                 )

    model1.train_model(df_train)

    model = ClassificationModel(
        'bert', 'bert-base-uncased',  # Change the pre-trained model to BERT
        num_labels=7,  # Binary classification task
        use_cuda=False,  # Disable GPU if needed
        args={
            "reprocess_input_data": False,  # Reprocess the input data
            "use_cached_eval_features": False,  # Don't use cached eval features
            "overwrite_output_dir": False,  # Overwrite the output directory
            "num_train_epochs": 1  # Train for 1 epoch
        }
    )

    # model.train_model(df_train)

    # Define your test sentences as separate variables
    test_sentence1 = "I'm feeling very anxious today."
    test_sentence2 = "Despite the chaos around me, I feel at peace."
    test_sentence3 = "I can't help but feel overwhelmed by the weight of my responsibilities."
    test_sentence4 = "Today is a beautiful day, and I'm grateful for everything."
    test_sentence5 = "I'm excited about the future, but I worry about what could go wrong."
    test_sentence6 = "I often feel like I'm in a dark place and can't find a way out."
    test_sentence7 = "I just got a promotion at work, and I'm really proud of myself!"
    test_sentence8 = "I feel numb and detached from everything around me."
    test_sentence9 = "Even though I'm busy, I enjoy the little things in life."
    test_sentence10 = "Sometimes I feel like my anxiety is crippling, but I try to push through."

    # Preprocess the input sentence
    preprocessed_sentence1 = preprocess(test_sentence1)
    preprocessed_sentence2 = preprocess(test_sentence2)
    preprocessed_sentence3 = preprocess(test_sentence3)
    preprocessed_sentence4 = preprocess(test_sentence4)
    preprocessed_sentence5 = preprocess(test_sentence5)
    preprocessed_sentence6 = preprocess(test_sentence6)
    preprocessed_sentence7 = preprocess(test_sentence7)
    preprocessed_sentence8 = preprocess(test_sentence8)
    preprocessed_sentence9 = preprocess(test_sentence9)
    preprocessed_sentence10 = preprocess(test_sentence10)

    # %%

    # Make the prediction
    predicted_label1, raw_outputs1 = model1.predict([preprocessed_sentence1])  # Wrap the input in a list
    predicted_label2, raw_outputs2 = model1.predict([preprocessed_sentence2])  # Wrap the input in a list
    predicted_label3, raw_outputs3 = model1.predict([preprocessed_sentence3])
    predicted_label4, raw_outputs4 = model1.predict([preprocessed_sentence4])
    predicted_label5, raw_outputs5 = model1.predict([preprocessed_sentence5])
    predicted_label6, raw_outputs6 = model1.predict([preprocessed_sentence6])
    predicted_label7, raw_outputs7 = model1.predict([preprocessed_sentence7])
    predicted_label8, raw_outputs8 = model1.predict([preprocessed_sentence8])
    predicted_label9, raw_outputs9 = model1.predict([preprocessed_sentence9])
    predicted_label10, raw_outputs10 = model1.predict([preprocessed_sentence10])

    # Print the input sentences and their predicted labels
    print("Input Sentence 1:", test_sentence1)
    print("Predicted Numeric Label 1:", predicted_label1)

    print("Input Sentence 2:", test_sentence2)
    print("Predicted Numeric Label 2:", predicted_label2)

    print("Input Sentence 3:", test_sentence3)
    print("Predicted Numeric Label 3:", predicted_label3)

    print("Input Sentence 4:", test_sentence4)
    print("Predicted Numeric Label 4:", predicted_label4)

    print("Input Sentence 5:", test_sentence5)
    print("Predicted Numeric Label 5:", predicted_label5)

    print("Input Sentence 6:", test_sentence6)
    print("Predicted Numeric Label 6:", predicted_label6)

    print("Input Sentence 7:", test_sentence7)
    print("Predicted Numeric Label 7:", predicted_label7)

    print("Input Sentence 8:", test_sentence8)
    print("Predicted Numeric Label 8:", predicted_label8)

    print("Input Sentence 9:", test_sentence9)
    print("Predicted Numeric Label 9:", predicted_label9)

    print("Input Sentence 10:", test_sentence10)
    print("Predicted Numeric Label 10:", predicted_label10)
