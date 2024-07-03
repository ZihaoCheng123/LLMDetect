import transformers
import torch
import accelerate
import pandas as pd
import json
from tqdm import tqdm

with open(r'./data/n24Guardian.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
df = pd.DataFrame(data)
df['output'] = ''
# 定义本地模型路径
model_path = "./models/Meta-Llama-3-8B-Instruct"

# 加载模型和tokenizer
pipeline = transformers.pipeline(
    "text-generation",
    model=model_path,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

system = "You are an AI assistant tasked with generating news articles. Given a news article title and its description, your task is to craft a well-structured and informative news article. Aim for a balanced and informative article that provides context and clarity to the reader. Adapt the tone and style to fit the nature of the news, whether it's business, education, or scientific to engage the target audience effectively."

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

# 使用tqdm显示进度条
for i, user_content in enumerate(tqdm(df['prompts'])):
    try:
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_content},
        ]

        outputs = pipeline(
            messages,
            max_new_tokens=1024,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )

        # 将生成的文本写入content列
        df.at[i, 'output'] = outputs[0]["generated_text"][-1]['content']

    except Exception as e:
        print(f"Error at index {i}, error: {str(e)}")
        continue

data_dict = df.to_dict('records')  # 转化为字典

with open(r'./data/result.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)