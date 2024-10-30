import torch
from transformers import BartTokenizer, BartForSequenceClassification, XLNetTokenizer, XLNetForSequenceClassification
from transformers import Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset
dataset = load_dataset('J:\Source_Code（源代码）\EE 6405 Natural Language Processing_自然语言处理\Final_Project_期末项目\data')

# Initialize BART
bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large')
bart_model = BartForSequenceClassification.from_pretrained('facebook/bart-large', num_labels=2)

# Initialize XLNet
xlnet_tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
xlnet_model = XLNetForSequenceClassification.from_pretrained('xlnet-base-cased', num_labels=2)

# Tokenize dataset for BART
def tokenize_bart(examples):
    return bart_tokenizer(examples[""], padding='max_length', truncation=True)

# Tokenize dataset for XLNet
def tokenize_xlnet(examples):
    return xlnet_tokenizer(examples[""], padding='max_length', truncation=True)

# Apply tokenization
tokenized_bart = dataset.map(tokenize_bart, batched=True)
tokenized_xlnet = dataset.map(tokenize_xlnet, batched=True)

# Set format for Trainer
tokenized_bart.set_format('torch', columns=['input_ids', 'attention_mask', 'label'])
tokenized_xlnet.set_format('torch', columns=['input_ids', 'attention_mask', 'label'])

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir='./logs',
)

# Create Trainer instances
bart_trainer = Trainer(
    model=bart_model,
    args=training_args,
    train_dataset=tokenized_bart['train'],
    eval_dataset=tokenized_bart['validation']
)

xlnet_trainer = Trainer(
    model=xlnet_model,
    args=training_args,
    train_dataset=tokenized_xlnet['train'],
    eval_dataset=tokenized_xlnet['validation']
)

# Train models
bart_trainer.train()
xlnet_trainer.train()

# Evaluate models
bart_results = bart_trainer.evaluate()
xlnet_results = xlnet_trainer.evaluate()

# Print evaluation results
print("BART Evaluation Results:", bart_results)
print("XLNet Evaluation Results:", xlnet_results)
